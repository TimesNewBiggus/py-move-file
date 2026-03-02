import os
from pathlib import Path


def move_file(command: str) -> None:
    command_log = command.split(" ")

    if len(command_log) == 3 and command.startswith("mv"):
        exact_com, origin_file, created_path = command_log
        (dir_part,
         new_filename) = (os.path.dirname(created_path),
                          os.path.basename(created_path))
        directories = list(Path(dir_part).parts)

        if new_filename is None:
            os.rename(origin_file, created_path + origin_file)

        elif len(directories) == 0:
            os.rename(origin_file, new_filename)

        elif len(directories) >= 1:
            for i in range(1, len(directories) + 1):
                dire = os.path.join(*directories[:i])
                if not os.path.exists(dire):
                    os.makedirs(dire)
                continue

            os.rename(origin_file, created_path)
