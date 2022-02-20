import subprocess
import platform

from shared.Enums.os_type import OsType


class OpenDesktopAppService:
    def execute(self,app_path):
        if platform.system() == OsType.WINDOWS.name:
            subprocess.Popen(["start",app_path])
        if platform.system() == OsType.DARWIN.name:
            subprocess.Popen(["open",app_path])
        if platform.system() == OsType.LINUX.name:
            subprocess.Popen(["see",app_path])