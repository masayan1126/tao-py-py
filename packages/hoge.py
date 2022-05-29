import ffmpeg
from shared.Domain.FileSystem.x_file_system_path import XFileSystemPath
from shared.Domain.String.xstr import XStr


stream = ffmpeg.input(
    XFileSystemPath(XStr("packages/clipping_yt/videos/【プロ野球 開幕戦】3_25 阪神タイガース VS 東京ヤクルトスワローズを一緒に観戦するライブ。【開幕戦2022】-V2SSVEmWGs8.mp4")).of_text(),
    ss=9227.07,
    t=6.64,
)

audio_stream = stream.audio

stream.filter("fps", fps=15, round="up").output(
    stream,
    audio_stream,
    XFileSystemPath(XStr("packages/clipping_yt/videos/cliped/output.mp4")).of_text(),
    crf=30,
).run(overwrite_output=True)


print("debug")
