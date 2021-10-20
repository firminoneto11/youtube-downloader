from .base import Tkinter
from .home import Home
from tkinter import messagebox


class Run:

    def __init__(self) -> None:
        
        try:
            # Initial settings for the app
            root_window = Tkinter()
            root_window.title("Youtube Downloader!")
            root_window.resizable(False, False)
            root_window.center(width=600, height=400)

            # Initializing the widgets for the app
            Home(root=root_window)

            # Mainloop
            root_window.mainloop()
        
        except Exception as error:
            # Handling errors
            messagebox.showerror(title="A problem occurred.", message=f"A problem occurred while executing the program. More details about it:\n\n{error}")
