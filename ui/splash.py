import customtkinter as ctk 

class SplashScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.colors = {
            "bg": "#13111c",
            "surface": "#1d1927",
            "accent": "#8b5cf6",
            "accent2": "#c4b5fd",
            "text": "#ede9fe",
            "muted": "#6d6483",
            "green": "#4ade80",
            "red": "#f87171"
            }
        self.configure(fg_color=self.colors["bg"])
        self.pack(fill="both", expand=True)
        self.build_ui()

    def build_ui(self):
        self.logo = ctk.CTkLabel(
            self,
            text="PULSE OS",
            font=("Courier", 48, "bold"),
            text_color=self.colors["accent2"]
        )
        self.logo.pack(pady=(200, 0))

        self.subtitle = ctk.CTkLabel(
            self,
            text="MARKET TERMINAL v1.0",
            font=("Courier", 25, "normal"),
            text_color=self.colors["muted"]
        )
        self.subtitle.pack(pady=(8, 0))

        self.progress = ctk.CTkProgressBar(
            self,
            width=400,
            progress_color=self.colors["accent2"],
            fg_color=self.colors["surface"]
        )
        self.progress.set(0)
        self.progress.pack(pady=(40,0))

        self.status = ctk.CTkLabel(
            self,
            text="Booting...",
            font=("Courier", 14),
            text_color=self.colors["muted"]
        )
        self.status.pack(pady=(10,0))
        self.animate()

    def animate(self):
        self.boot_messages = [
            "Initializing PulseOS...",
            "Loading market data...",
            "Connecting to APIs...",
            "Fetching prices...",
            "Ready."
        ]
        self.boot_step = 0
        self._run_animation()

    def _run_animation(self):
        if self.boot_step < len(self.boot_messages):
            msg = self.boot_messages[self.boot_step]
            progress = self.boot_step / len(self.boot_messages)
            self.status.configure(text=msg)
            self.progress.set(progress)
            self.boot_step += 1
            self.after(800, self._run_animation)