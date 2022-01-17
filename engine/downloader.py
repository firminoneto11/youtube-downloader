from pytube import YouTube
from os.path import exists
from os import mkdir


class Downloader:

    filters = {
        "min_res": "720p",
        "max_res": "1080p",
        "min_fps": 25,
        "medium_fps": 30,
        "max_fps": 60,
        "mime_type": "video/mp4",
        "type": "video"
    }

    save_dir = r".\outputs"

    @classmethod
    def check_output(cls) -> None:
        if not exists(cls.save_dir):
            mkdir(cls.save_dir)

    @classmethod
    def download(cls, url: str, resolve, reject) -> str:
        try:
            # Checking id the directory exists
            cls.check_output()

            # Connecting to youtube
            youtube = YouTube(url=url)

            # Selectting the videos with audio
            videos = youtube.streams.filter(progressive=True)
            videos = list(filter(lambda el: True if el.mime_type == cls.filters.get("mime_type") and el.type == cls.filters.get("type") else False, videos))

            # Checking the filtered results and downloading the video
            if len(videos) == 0:
                # Returning a generic message in case the quality of the videos found aren't that great
                return resolve("Unfortunately the desired video is not available within the ideal settings...")
            # Downloading and outputting the path
            elif len(videos) == 1:
                return resolve(videos[0].download(output_path=cls.save_dir))
            # Filtering the videos returned by the previous query
            elif len(videos) > 1:
                best_available = None
                for video in videos:
                    if video.resolution == cls.filters.get("max_res") and video.fps >= cls.filters.get("max_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("max_res") and video.fps >= cls.filters.get("medium_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("max_res") and video.fps >= cls.filters.get("min_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("min_res") and video.fps >= cls.filters.get("max_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("min_res") and video.fps >= cls.filters.get("medium_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("min_res") and video.fps >= cls.filters.get("min_fps"):
                        best_available = video
                        break
                # Downloading and outputting the path
                return resolve(best_available.download(output_path=cls.save_dir))
        except Exception as error:
            # TODO: Way too broad exception. See if we can narrow it down
            return reject(error)
