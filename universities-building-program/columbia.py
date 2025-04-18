import requests

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif message.startswith("bitcoin"):
            url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'enter CoinMarketCapAPI Key'
    }
    params = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        for coin in data['data']:
            if coin['symbol'] == 'BTC':
                price = coin['quote']['USD']['price']
                return f"BTC price: ${price:,.2f}"
        return "BTC not found in the response."
    else:
        return f"Error: {response.status_code} - {response.text}"


if __name__ == "__main__":
   user_input = input("Search real-time price of : ")
   print(handle_message(user_input))
