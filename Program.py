from engine.downloader import Downloader


class Main:

    @staticmethod
    def run():
        downloader = Downloader()
        downloader.download(url="https://www.youtube.com/watch?v=Wg7EuMtk7FE&ab_channel=Rocketseat")


if __name__ == '__main__':
    Main.run()
