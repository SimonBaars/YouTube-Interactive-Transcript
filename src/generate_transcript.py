import click

from youtube import download_audio

@click.command()
@click.argument('youtube_url', type=str)
def generate_transcript(youtube_url):
    print(f'Generating transcript for {youtube_url}')
    if not download_audio(youtube_url):
        print('Failed to download audio')
        return
    print('Downloaded audio')

if __name__ == '__main__':
    generate_transcript()
