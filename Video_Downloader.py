import yt_dlp
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):   
        super().__init__()
        WIDTH = 500
        HEIGHT = 500
        # Sets screen width and height, and places it in centre of the screen
        self.geometry(f"{WIDTH}x{HEIGHT}+{int(self.winfo_screenwidth()/2 - WIDTH/2)}+{int(self.winfo_screenheight()/2 - HEIGHT/2)}")
        self.title('Video Downloader')
        self.resizable (False, False)

        self.create_widgets()
        
    def create_widgets(self):
        self.urlEntry = ctk.CTkEntry(self, width = 200, justify = "center")
        self.urlEntry.bind("<Return>", (lambda event: self.update_url()))
        self.urlEntry.pack()

    def update_url(self):
        url = self.urlEntry.get()
        if not "https://" in url:
            print('Url must start with "https://"')
            return;
        if not ("youtube.com/watch?v=" in url or "youtu.be/" in url):
            print("Invalid video url")
            return;
    
        urlType = "Video"
        print(f"{urlType}: {url}")
            
if __name__ == "__main__":
    app = App()
    app.mainloop()