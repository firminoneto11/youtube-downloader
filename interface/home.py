from tkinter import Label, messagebox
from tkinter.constants import ACTIVE, DISABLED
from tkinter.ttk import Entry, Button, Style
from .base import Tkinter
from engine.downloader import Downloader
import webbrowser
from os.path import join


class Home:

    title_label = {
        "text": "Insert the url of a youtube video that\nyou wish to download on the box bellow!",
        "font": ("helvetica", 18),
    }

    input_field = {
        "font": ("helvetica", 14),
        "width": 50,
    }

    button_config = {
        "text": "Download",
        "width": 50,
    }

    def __init__(self, root: Tkinter) -> None:
        style = Style()
        style.configure('TButton', font=("helvetica", 12))
        
        # Inserting some widgets onto the screen
        Label(root, **self.title_label).pack(pady=15)
        self.input = Entry(root, **self.input_field)
        self.download = Button(root, **self.button_config, command=lambda: self._download())

        self.input.pack(pady=10)
        self.download.pack(pady=40, ipady=10, ipadx=10)
    
    def _download(self):
        # Changing the state of the download button
        self.download.config(state=DISABLED, text="Downloading...")
        self.download.update()

        # Getting the user input and checking if is a valid url
        url = self.input.get()
        if not url.startswith("https://www.youtube.com"):
            messagebox.showwarning(title="Link invalid", message="Please enter valid youtube url!")
            self.download.configure(state=ACTIVE, text="Download!")
            return None
        try:
            path = Downloader.download(url=url)
        except Exception as error:
            # Handling errors
            messagebox.showerror(title="A problem occurred", message=f"A problem occurred while downloading the requested video. More details about it:\n\n{error}")
        else:
            # Displaying a message informing the user that the download is finished and opening the directory
            response = messagebox.showinfo(title="Download completed", message="Download completed successfully!")
            if response:
                print(path)
                # path = path.split('\\')
                # path.pop()
                # webbrowser.open(join(*path))
        finally:
            # Reseting the state of the download button
            self.download.config(state=ACTIVE, text="Download!")
            self.download.update()
