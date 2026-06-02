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

        self.topbar = ctk.CTkFrame(
            self.main,
            fg_color=self.colors["sidebar"],
            height=48
        )
        self.topbar.pack(fill="x", side="top")
        self.topbar.pack_propagate(False)

        self.page_title = ctk.CTkLabel(
            self.topbar,
            text="DASHBOARD",
            font=("Consolas", 13, "bold"),
            text_color=self.colors["text"]
        )
        self.page_title.pack(side="left", padx=16, pady=12)

        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="PULSE OS",
            font=("Consolas", 16, "bold"),
            text_color=self.colors["accent2"]
        )
        self.logo_label.pack(pady=(20, 4), padx=12, anchor="w")

        self.logo_sub = ctk.CTkLabel(
            self.sidebar,
            text="MARKET TERMINAL",
            font=("Consolas", 10, "normal"),
            text_color=self.colors["muted"]
        )
        self.logo_sub.pack(padx=12, anchor="w", pady=(0, 16))

        self.add_nav_item("Dashboard", active=True)
        self.add_nav_item("Watchlist")
        self.add_nav_item("Portfolio")
        self.add_nav_item("Crypto")
        self.add_nav_item("Stocks")
        self.add_nav_item("Favourites")
        self.add_nav_item("Settings")

    def add_nav_item(self, text, active=False):
        color = self.colors["accent2"] if active else self.colors["muted"]
        btn = ctk.CTkButton(
            self.sidebar,
            text=text,
            fg_color="transparent",
            text_color=color,
            hover_color=self.colors["surface"],
            anchor="w",
            font=("Consolas", 12),
            height=36
        )
        btn.pack(fill="x", padx=8, pady=2)
        return btn