import customtkinter as ctk
from ui.splash import SplashScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Trading Tracker")
        self.geometry("1200x800")
        self.splash = SplashScreen(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()