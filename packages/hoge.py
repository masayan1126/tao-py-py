from youtube_transcript_api import YouTubeTranscriptApi
import ffmpeg
import youtube_dl

transcript_list = YouTubeTranscriptApi.list_transcripts("V2SSVEmWGs8")

all_translations = []


for transcript in transcript_list:
    for tr in transcript.fetch():
        all_translations.append(tr)

# 対象の動画をダウンロード
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=V2SSVEmWGs8"])

# {'text': '糸井の2ラン', 'start': 9227.07, 'duration': 7.64}

# ffmpeg.input("input.mp4", ss=5, t=10).filter("fps", fps=15, round="up").output(
#     "output.mp4", crf=30
# ).run(overwrite_output=True)

print("debug")
