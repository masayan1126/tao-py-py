import subprocess
from time import sleep

from shared.Domain.FileSystem.os_type_judgement import OsTypeJudgement
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.FileSystem.os_type import OsType


class SoftWareProcessOperator:
    def open(self, software_path: XFileSystemPath, wait_time: float):
        judgement = OsTypeJudgement()
        os_type = judgement.judge()

        if os_type == OsType.WINDOWS:
            subprocess.call(["start", software_path.of_text()])
        elif os_type == OsType.DARWIN:
            p = subprocess.Popen(["open", software_path.of_text()])
            p.wait()
        else:
            subprocess.call(["see", software_path.of_text()])

        if wait_time:
            self.wait(wait_time)

    def wait(self, wait_time: float) -> None:
        sleep(wait_time)
