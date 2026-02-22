from dotenv import load_dotenv
from agents import Agent, Runner, function_tool
import requests
from pydantic import BaseModel
from typing import List

load_dotenv()

class Crypto(BaseModel):
    """coin_ids: full name string to represent the crypto currency. """
    coin_ids: List[str]

@function_tool
def get_price_of_bitcoin(crypto:Crypto) -> str:
    """ 
    Get the current prices of a list of cryptocurrencies.

    Args:
        Crypto: An object with list of coin_ids.(e.g. ["bitcoin", "ethereum", "ripple"])
    """
    ids = ",".join(crypto.coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data



crypto_agent = Agent(
    name="CryptoTracker",
    instructions="You are a crypto tracking assistant. Use tools to get the real-time data. When getting the crypto prices, call the tool only once for all request.",
    tools=[get_price_of_bitcoin],
)

result = Runner.run_sync(crypto_agent, "What is the price of bitcoin, ethereum, and ripple?")
print(result.final_output)


