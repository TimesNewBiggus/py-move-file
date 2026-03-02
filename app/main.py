import os
from pathlib import Path


def move_file(command: str) -> None:
    command_log = command.split(" ")

    if len(command_log) == 3 and command.startswith("mv"):
        command_name, origin_file, created_path = command_log
        (dir_part,
         new_filename) = (os.path.dirname(created_path),
                          os.path.basename(created_path))
        directories = list(Path(dir_part).parts)

        if new_filename == "":
            os.rename(origin_file, created_path + origin_file)

        elif dir_part == ".":
            os.rename(origin_file, os.getcwd() + origin_file)

        elif dir_part == "":
            os.rename(origin_file, new_filename)

        elif len(directories) >= 1:
            if dir_part:
                os.makedirs(name=dir_part, exist_ok=True)
            os.rename(origin_file, created_path)
