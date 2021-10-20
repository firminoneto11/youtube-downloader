from pytube import YouTube
from os.path import exists
from os import mkdir


class Downloader:

    filters = {
        "min_res": "720p",
        "max_res": "1080p",
        "min_fps": 30,
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
    def download(cls, url: str) -> None:
        # Checking id the directory exists
        cls.check_output()

        # Connecting to youtube
        youtube = YouTube(url=url)

        # Selectting the videos with audio
        videos = youtube.streams.filter(progressive=True)

        # TODO: Some videos are comming with 25fps only. Need to apply more filters to the search.
        print(videos)

        # Filtering the videos returned by the previous query
        filtered_videos = []
        for video in videos:
            if video.mime_type == cls.filters.get("mime_type") and video.type == cls.filters.get("type"):
                if video.resolution == cls.filters.get("max_res") or video.resolution == cls.filters.get("min_res"):
                    if video.fps == cls.filters.get("max_fps") or video.fps == cls.filters.get("min_fps"):
                        filtered_videos.append(video)
        # Checking the filtered results and downloading the video
        if len(filtered_videos) == 1:
            # Downloading and outputting the path
            return filtered_videos[0].download(output_path=cls.save_dir)
        elif len(filtered_videos) > 1:
            best_available = None
            for video in filtered_videos:
                if video.mime_type == cls.filters.get("mime_type") and video.type == cls.filters.get("type"):
                    if video.resolution == cls.filters.get("max_res") and video.fps == cls.filters.get("max_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("max_res") and video.fps == cls.filters.get("min_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("min_res") and video.fps == cls.filters.get("max_fps"):
                        best_available = video
                        break
                    elif video.resolution == cls.filters.get("min_res") and video.fps == cls.filters.get("min_fps"):
                        best_available = video
                        break
            # Downloading and outputting the path
            return best_available.download(output_path=cls.save_dir)
        else:
            # Returning a generic message in case the quality of the videos found aren't that great
            return "Unfortunately the desired video is not available within the ideal conditions..."
