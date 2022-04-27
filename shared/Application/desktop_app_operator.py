import subprocess

import platform
from shared.Enums.os_type import OsType


class DesktopAppOperator:
    def run(self, app_path):
        # 非同期処理
        # subprocess.Popen(app_path)
        # 同期処理(前の処理を待ってから次の処理へ)
        subprocess.run(app_path)

        # if platform.system() == "Windows":
        #     os = OsType.WINDOWS
        # elif platform.system() == "Darwin":
        #     os = OsType.WINDOWS
        # else:
        #     os = OsType.LINUX

        # match os:
        #     case OsType.WINDOWS:
        #         subprocess.Popen(["start",app_path])
        #     case OsType.DARWIN:
        #         subprocess.Popen(["open", app_path])
        #     case OsType.LINUX:
        #         subprocess.Popen(["see", app_path])
        #     case _:
        #         pass
