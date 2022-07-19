"""Post gen hook to ensure that the generated project
has only one package management, either pipenv or pip."""
import sys
from pathlib import Path
from typing import Union, List


def remove_folder(folder_path: Union[Path, str], missing_ok=True):
    if isinstance(folder_path, str):
        folder_path = Path(folder_path)
    if not folder_path.exists():
        print(f"目标删除文件夹{folder_path}不存在")
        if not missing_ok:
            raise FileNotFoundError(f"[WinError 3] 系统找不到指定的路径。: '{folder_path}'")

    file_folder_num = 0
    for f in folder_path.iterdir():
        if f.is_dir():
            # 递归删除
            remove_folder(f)
        elif f.is_file():
            print(f"删除文件: {f}")
            f.unlink()
        else:
            raise Exception("unknown")
        file_folder_num += 1

    print(f"删除文件夹: {folder_path}")
    folder_path.rmdir()


# 根目录
PROJECT_DIRECTORY = Path(".").cwd().resolve()


def clean_files():
    """Removes either requirements files and folder or the Pipfile."""
    db_name = "{{cookiecutter.db_name}}"
    use_docker = "{{cookiecutter.use_docker}}"
    use_pipenv = "{{cookiecutter.use_pipenv}}"
    save_login = "{{cookiecutter.save_login}}"

    to_delete: List[Path] = []

    # 删除False选项文件
    if db_name == "False":
        to_delete = to_delete + [PROJECT_DIRECTORY.joinpath("base").joinpath("models").joinpath("dbs.py"),
                                 PROJECT_DIRECTORY.joinpath("base").joinpath("models").joinpath("create.sql"),
                                 PROJECT_DIRECTORY.joinpath("base").joinpath("helper").joinpath("saver.py")
                                 ]

    if use_docker == "False":
        to_delete = to_delete + [PROJECT_DIRECTORY.joinpath("Dockerfile"),
                                 PROJECT_DIRECTORY.joinpath("docker-entrypoint.sh"),
                                 PROJECT_DIRECTORY.joinpath(".dockerignore"),
                                 ]
    if use_pipenv == "False":
        to_delete = to_delete + [PROJECT_DIRECTORY.joinpath("Pipfile")]


    if save_login == "False":
        to_delete = to_delete + [PROJECT_DIRECTORY.joinpath("base").joinpath("helper").joinpath("login.py"),]

    try:
        for file_or_dir in to_delete:
            if file_or_dir.is_file():
                file_or_dir.unlink(missing_ok=True)
            elif file_or_dir.is_dir():
                remove_folder(file_or_dir)
    except OSError as e:
        print("While attempting to remove file(s) an error occurred")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    clean_files()
