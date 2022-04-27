from shared.Domain.Text.text_file_operator import TextFileOperator
from shared.Domain.Text.x_text import XText
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr

filepath = XFileSystemPath(XStr("packages/sample.txt")).to_absolute()

# 読み取り
content = TextFileOperator(x_text=XText(filepath)).readline(encoding="UTF-8")
print(content)
print(content[0])
