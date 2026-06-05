import customtkinter as ctk
from api.coingecko import CoinGeckoAPI
from api.yfinance_api import YFinance

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

        self.cg_api = CoinGeckoAPI()
        self.yf_api = YFinance()
        self.card_labels = {}
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

        self.content = ctk.CTkFrame(
            self.main,
            fg_color=self.colors["bg"]
        )
        self.content.pack(fill="both", expand=True, padx=16, pady=16)

        self.cards_row = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        self.cards_row.pack(fill="x", pady=(0, 8))

        self.add_metric_card(self.cards_row, "BTC", "$70,114", "+2.4%")
        self.add_metric_card(self.cards_row, "ETH", "$1,984", "+1.1%")
        self.add_metric_card(self.cards_row, "AAPL", "$306.31", "-1.8%")
        self.add_metric_card(self.cards_row, "MSFT", "$460.52", "+2.3%")

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
        self.update_cards()

    def fetch_data(self):
        crypto = self.cg_api.fetch_price(
            ["bitcoin", "ethereum"],
            ["usd"]
        )
        stocks = self.yf_api.fetch_stocks(
            ["AAPL", "MSFT"],
            ["usd"]
        )
        return crypto, stocks

    def update_cards(self):
        crypto, stocks = self.fetch_data()

        if crypto:
            btc = crypto.get("bitcoin", {})
            eth = crypto.get("ethereum", {})

            if "BTC" in self.card_labels:
                price = f"${btc.get('usd', 0):,.2f}"
                self.card_labels["BTC"]["price"].configure(text=price)
                change_value = btc.get('usd_24h_change', 0)
                color = self.colors["green"] if change_value >= 0 else self.colors["red"]
                change = f"{change_value:.2f}%"
                self.card_labels["BTC"]["change"].configure(text=change, text_color=color)

            if "ETH" in self.card_labels:
                price = f"${eth.get('usd', 0):,.2f}"
                self.card_labels["ETH"]["price"].configure(text=price)
                change_value = eth.get('usd_24h_change', 0)
                color = self.colors["green"] if change_value >= 0 else self.colors["red"]
                change = f"{change_value:.2f}%"
                self.card_labels["ETH"]["change"].configure(text=change, text_color=color)

        if stocks:
            for symbol in ["AAPL", "MSFT"]:
                if symbol in self.card_labels and symbol in stocks:
                    price = f"${stocks[symbol].get('currentPrice', 0):,.2f}"
                    self.card_labels[symbol]["price"].configure(text=price)
                    change_value = stocks[symbol].get('regularMarketChangePercent', 0)
                    color = self.colors["green"] if change_value >= 0 else self.colors["red"]
                    change = f"{change_value:.2f}%"
                    self.card_labels[symbol]["change"].configure(text=change, text_color=color)

        self.after(60000, self.update_cards)

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

    def add_metric_card(self, parent, symbol, price, change):
        card = ctk.CTkFrame(
            parent,
            fg_color=self.colors["surface"],
            corner_radius=8
        )
        card.pack(side="left", padx=8, pady=8, ipadx=16, ipady=12)

        ctk.CTkLabel(
            card,
            text=symbol,
            font=("Consolas", 11),
            text_color=self.colors["muted"]
        ).pack(anchor="w", padx=12, pady=(10, 0))

        price_label = ctk.CTkLabel(
            card,
            text=price,
            font=("Consolas", 20, "bold"),
            text_color=self.colors["text"]
        )
        price_label.pack(anchor="w", padx=12)

        change_color = self.colors["green"] if "+" in change else self.colors["red"]
        change_label = ctk.CTkLabel(
            card,
            text=change,
            font=("Consolas", 11),
            text_color=change_color
        )
        change_label.pack(anchor="w", padx=12, pady=(0, 10))

        self.card_labels[symbol] = {
            "price": price_label,
            "change": change_label
        }

        return card