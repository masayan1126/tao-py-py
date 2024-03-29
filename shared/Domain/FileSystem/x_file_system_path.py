import pathlib

from shared.Domain.String.xstr import XStr


class XFileSystemPath:
    def __init__(self, path_str: XStr):
        # 引数で受け取ったパス文字列(絶対・相対どちらでもOK)からパスオブジェクトを生成
        self._path = pathlib.Path(path_str.value())

    def path(self) -> pathlib.Path:
        return self._path

    def to_text(self) -> str:
        return str(self.path())

    # 相対パス(cwdを起点とする相対パス)
    # Ex) #'tests\\x_file_system_path.py'
    def to_relative(self, base_path=None):
        if base_path is None:
            base_path = self.path().cwd()

        try:
            return XFileSystemPath(
                XStr(str(self.to_absolute().path().relative_to(base_path)))
            )
        except Exception:
            # 相対パスに変換しようとしたパスに、起点となるcwdが含まれていない場合例外(つまり、もとの絶対パスに起点となるcwdが含まれている必要がある)
            raise ValueError

    # 絶対パス(cwd + self.path())
    # Ex) #'C:\\Users\\・・・\\tests\\x_file_system_path.py'
    def to_absolute(self):
        return XFileSystemPath(XStr(str(self.path().resolve())))

    # 現在の作業ディレクトリ(カレントワーキングディレクトリ)の絶対パス
    @staticmethod
    def cwd():
        return XFileSystemPath(XStr(str(pathlib.Path.cwd())))

    # ユーザーのホームディレクトリの絶対パス
    # Ex) 'C:\\Users\\nishigaki'
    @staticmethod
    def home_dir():
        return XFileSystemPath(XStr(str(pathlib.Path.home())))

    def exsits(self):
        return self.path().exists()

    # 相対パスかを判定するメソッドはpathilibにはなし
    def is_absolute(self) -> bool:
        return self.path().is_absolute()

    # ディレクトリかどうかを返します
    # 存在しないパスは強制的にFalse
    def is_file(self) -> bool:
        return self.path().is_file()

    # ファイルかどうかを返します
    # 存在しないパスは強制的にFalse
    def is_dir(self) -> bool:
        return self.path().is_dir()

    # パス文字列を追加して返します
    def join(self, *more_path_strs: str):
        self._path = self._path.joinpath(*more_path_strs)
        return XFileSystemPath(XStr(str(self.path())))

    def delete(self):
        if self.is_file():
            self.path().unlink()
        else:
            self.path().rmdir()

    # TODO: 拡張子の取得(suffix), ディレクトリ・ファイル名の取得(name)
    # TODO: あるディレクトリのファイルの一覧
    # ※再帰的に取得する場合は、globを使う必要あり。
    # path = Path(”hoge/foo”)
    # genelator = path.iterdir()
    # path_list = list(genelator)
