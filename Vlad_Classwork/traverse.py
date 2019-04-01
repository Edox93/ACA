import os


def traverse_path(path: str, level: int = 0):
    for name in os.listdir(path):
        sys_path = os.path.join(path, name)
        if os.path.isdir(sys_path):
            print(level * ' ', 'Dir:', name)
            traverse_path(sys_path, level + 1)
            continue
        print(level * ' ', 'File:', name)

    for entry in os.scandir(path):
        if entry.is_dir():
            print(level * ' ', 'Dir:', entry.name)
            traverse_path(entry.path, level + 1)
            continue
        print(level * ' ', 'File:', entry.name)


traverse_path('temp')
