import requests

class CoinGeckoAPI:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def fetch_price(self, coin_ids: list, currencies: list):
        ids_string = ",".join(coin_ids)
        currencies_string = ",".join(currencies)
        url = f"{self.base_url}/simple/price?ids={ids_string}&vs_currencies={currencies_string}&include_24hr_change=true"
        try:
            response = requests.get(url)
            return response.json()
        except Exception as e:
            print(f"Fehler beim API-Call: {e}")
            return None
        


