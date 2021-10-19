from pytube import YouTube
from os.path import exists
from os import mkdir


class Downloader:

    def __init__(self) -> None:
        self.save_dir = r".\outputs"

    def check_output(self) -> None:
        if not exists(self.save_dir):
            mkdir(self.save_dir)

    def download(self, url: str) -> None:
        # Checking id the directory exists
        self.check_output()

        # Connecting to youtube
        youtube = YouTube(url=url)

        # Picking the extension
        video_to_download = youtube.streams.filter(file_extension='mp4')

        # Picking the full-hd resolution and 60fps
        for attribute in video_to_download:
            if attribute.resolution == "1080p" and attribute.fps == 60:
                video_to_download = youtube.streams.get_by_itag(attribute.itag)
        
        # Downloading and outputting the path
        print('Downloading...')
        path_to_video = video_to_download.download(output_path=self.save_dir)
        print(f'Downloaded!\nSaved on {path_to_video}')
