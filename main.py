import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Trading Tracker")
        self.geometry("800x600")
        self.sidebar = ctk.CTkFrame(master=self, width=150)
        self.sidebar.pack(side="left", fill="y")
        self.btn_dashboard = ctk.CTkButton(master=self.sidebar, text="Dashboard", command=self.show_dashboard)
        self.btn_dashboard.pack(pady=10)
        self.btn_portfolio = ctk.CTkButton(master=self.sidebar, text="Portfolio", command=self.show_portfolio)
        self.btn_portfolio.pack(pady=10)
        self.btn_settings = ctk.CTkButton(master=self.sidebar, text="Settings", command=self.show_settings)
        self.btn_settings.pack(pady=10)
        self.content = ctk.CTkFrame(master=self)
        self.content.pack(side="right", fill="both", expand=True)
        self.frame_dashboard = ctk.CTkFrame(master=self.content)
        self.frame_portfolio = ctk.CTkFrame(master=self.content)
        self.frame_settings = ctk.CTkFrame(master=self.content)
        ctk.CTkLabel(master=self.frame_dashboard, text="Dashboard View").pack()
        self.show_dashboard()

    def show_dashboard(self):
        self.show_frame(self.frame_dashboard)
        
    def show_portfolio(self):
        self.show_frame(self.frame_portfolio)

    def show_settings(self):
        self.show_frame(self.frame_settings)

    def show_frame(self, frame):
        self.frame_dashboard.pack_forget()
        self.frame_portfolio.pack_forget()
        self.frame_settings.pack_forget()
        frame.pack(fill="both", expand=True)

app = App()
app.mainloop()