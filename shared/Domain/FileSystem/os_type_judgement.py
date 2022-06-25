import platform
from shared.Enums.os_type import OsType
from shared.i_judgement import IJudgement


class OsTypeJudgement(IJudgement):
    def judge(self):
        if platform.system() == "Windows":
            return OsType.WINDOWS
        elif platform.system() == "Darwin":
            return OsType.DARWIN
        else:
            return OsType.LINUX
