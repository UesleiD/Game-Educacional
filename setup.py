import cx_Freeze

executables = [cx_Freeze.Executable (script="game.py", icon="assets/iconeapp.ico")]

cx_Freeze.setup(
    name="It's Raining Garbage",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files":["assets"]
        }},
    executables=executables
)