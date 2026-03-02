import os


def move_file(command: str) -> None:
    command_log = command.split(" ")
    exact_com, origin_file, created_path = command_log
    *directories, new_filename = created_path.split("/")

    if len(command_log) == 3 and exact_com == "mv":
        if len(directories) == 0:
            os.rename(origin_file, new_filename)

        elif len(directories) >= 1:

            for i in range(1, len(directories) + 1):
                dire = os.path.join(*directories[:i])
                if not os.path.exists(dire):
                    os.makedirs(dire)
                continue

            with (open(origin_file, "r") as o_file,
                  open(created_path, "w") as n_file):
                n_file.write(o_file.read())

            os.remove(origin_file)
