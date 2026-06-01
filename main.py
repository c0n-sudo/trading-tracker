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
        self.btn_portfolio = ctk.CTkButton(master=self.sidebar, text="Portfolio")
        self.btn_portfolio.pack(pady=10)
        self.btn_settings = ctk.CTkButton(master=self.sidebar, text="Settings")
        self.btn_settings.pack(pady=10)
        self.content = ctk.CTkFrame(master=self)
        self.content.pack(side="right", fill="both", expand=True)

    def show_dashboard(self):
        print("Dashboard")

app = App()
app.mainloop()