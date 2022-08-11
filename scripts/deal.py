import os


CATEGORIES = {
    "司法解释": "A-司法解释",
    "行政法规": "B-行政法规",
    "地方性法规": "C-地方性法规",
    "部门规章": "D-部门规章",
    "案例": "E-案例",
    "其他": "F-其他",
}


def rename_file(folder_path, old, new):
    for path, _, files in os.walk(folder_path):
        for name in files:
            if old in name:
                file_path = os.path.join(path, name)
                new_name = os.path.join(path, name.replace(old, new))
                os.rename(file_path, new_name)


def rename_dir(folder_path):
    for path, subdirs, _ in os.walk(folder_path):
        for name in subdirs:
            for k, v in CATEGORIES.items():
                if k in name:
                    os.rename(os.path.join(path, name), os.path.join(path, v))
                    break


def remove_file(folder_path):
    for path, _, files in os.walk(folder_path):
        for name in files:
            if name == "_index.md":
                os.remove(os.path.join(path, name))


def main():
    os.chdir(os.getcwd() + "/src")
    rename_file(".", "(", "（")
    rename_file(".", ")", "）")
    rename_file(".", " ", "、")
    rename_dir(".")
    remove_file(".")


if __name__ == "__main__":
    main()
