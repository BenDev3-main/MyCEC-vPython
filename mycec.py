import cmd2
import os
import sys

class MyCEC(cmd2.Cmd):
    intro="DataGuard verified.\nMyCEC (basic).\n"
    prompt = "mycec(complete)> "
    def do_PrintMsg(self,arg):
        print(arg)
    def do_CreateFile(self, args):
        "Create an empty file inside the current WorkDir."
        filename = args.strip()

        if not filename:
            self.poutput("Usage: CreateFile <filename>")
            return

    # Ruta final adentro de WorkDir
        full_path = os.path.join(self.wdir, filename)

        try:
        # Crear el archivo vacío
            with open(full_path, "w", encoding="utf-8") as f:
                pass

            self.poutput(f"Created: {filename}  (#in {self.wdir})")

        except Exception as e:
            self.poutput(f"Error creating file: {e}")
    def do_DeleteItem(self,arg):
        blocked = ('.dll','.fish','.exe','.ps1','.bat')
        if not arg.endswith(blocked):
            os.remove(arg)
        else:
            pass
    def do_WriteFile(self, args):
        parts = args.split(" ", 1)

        if len(parts) < 2:
            self.poutput("Usage: WriteFile <filename> <text>")
            return

        filename, text = parts[0], parts[1]

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
            self.poutput(f"Written to {filename}")
        except Exception as e:
            self.poutput(f"Error: {e}")
    def do_CreateDir(self,arg):
        arg = arg.split("$", 1)[0].strip()
        if not arg:
            print("missing folder name.")
            return
        target = os.path.join(self.wdir, arg)
        try:
            if os.path.exists(target):
                print(f"Dir already exists: {arg}")
            else:
                os.makedirs(target)
                print(f"Dir created: {arg}")
        except Exception as e:
            print(f"CreateDir Error: {e}")
    def do_ListWDir(self,arg):
        arg = self.wdir()
        print(os.listdir(arg))
    def do_ChangeWDir(self, arg):
        path = arg.strip()
        if not path:
            print("You must specify a directory.")
            return

        '''# Convertir a ruta absoluta'''
        full = os.path.abspath(path)

        if os.path.isdir(full):
            self.wdir = full
            print(f"Working Dir changed to: #{self.wdir}")
        else:
            print("Invalid directory.")
    def do_ChangeVDir(self, arg):
        path = arg.strip()

        if not path:
            print("You must specify a directory.")
            return

        full = os.path.abspath(path)

        if os.path.isdir(full):
            self.vdir = full
            print(f"Vision Dir changed to: #{self.vdir}")
        else:
            print("Invalid directory.")
    def do_ShowPaths(self,arg):
        print(f"WorkDir: {self.wdir}\nVisualDir: {self.vdir}")
    def do_Version(self,arg):
        if arg.lower() == "mycec":
            print("MyCEC vPython (complete) v1.0.4")
        elif arg.lower() == "dataguard":
            f=open("MyProg\\DataGuard\\info.toml")
            print(f"DataGuard (info.json): {f.read()}")
            f.close()
        else:
            print(f"Producto '{arg}' no reconocido.")
    def do_Exit(self, arg):
        print(f"Exiting...")
        return True


if __name__ == "__main__":
    print("Select your working directory (leave empty to use current folder):")
    path = input("> ").strip()

    if path == "":
        path = os.getcwd()


    if not os.path.isdir(path):
        print("Invalid directory. Using current folder instead.")
        path = os.getcwd()
    print(f"Working directory set to: {path}")

    app = MyCEC()
    app.wdir = path
    app.vdir = path
    
    app.cmdloop()