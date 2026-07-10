import zipfile
import pathlib

def make_archive(filepaths_arg, dest_dir_arg):
    dest_path = pathlib.Path(dest_dir_arg, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths_arg:
            filepath = pathlib.Path(filepath) #biến thành class Path cho dễ xử lý
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths_arg=["cli.py", "gui.py"], dest_dir_arg="Bonus/filezip")