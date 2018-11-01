from cx_Freeze import setup, Executable

setup(
    name="Gerador de Bearer",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("Gerador_ JWT.py")])

