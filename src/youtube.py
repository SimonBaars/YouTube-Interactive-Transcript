import yt_dlp

def download_audio(youtube_url):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'outtmpl': 'output.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.download([youtube_url]) == 0
