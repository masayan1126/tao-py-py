import platform
from shared.Enums.os_type import OsType
from shared.judgement import Judgement


class OsTypeJudgement(Judgement):
    def judge(self):
        if platform.system() == "Windows":
            return OsType.WINDOWS
        elif platform.system() == "Darwin":
            return OsType.DARWIN
        else:
            return OsType.LINUX
