# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Union


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
