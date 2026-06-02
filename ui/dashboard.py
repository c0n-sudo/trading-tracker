import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#13111c")
        self.pack(fill="both", expand=True)
        self.colors = {
            "bg": "#13111c",
            "surface": "#1d1927",
            "accent": "#8b5cf6",
            "accent2": "#c4b5fd",
            "text": "#ede9fe",
            "muted": "#6d6483",
            "green": "#4ade80",
            "red": "#f87171",
            "sidebar": "#0d0b14",
            "border": "#2a2040"
        }
        self.build_ui()

    def build_ui(self):
        self.sidebar = ctk.CTkFrame(
            self,
            fg_color=self.colors["sidebar"],
            width=180
        )
        self.sidebar.pack(side="left", fill="y")
        self.main = ctk.CTkFrame(
            self,
            fg_color=self.colors["bg"]
        )
        self.main.pack(side="left", fill="both", expand=True)
        self.logo_label = ctk.CTkLabel(
        self.sidebar,
        text="PULSE OS",
        font=("Courier", 14, "bold"),
        text_color=self.colors["accent2"]
        )
        self.logo_label.pack(pady=(20, 4), padx=12, anchor="w")

        self.logo_sub = ctk.CTkLabel(
            self.sidebar,
            text="MARKET TERMINAL",
            font=("Courier", 9, "normal"),
            text_color=self.colors["muted"]
        )
        self.logo_sub.pack(padx=12, anchor="w")