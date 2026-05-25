import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url , headers=headers) 
simpsons = pd.read_html(StringIO(response.text))
print(simpsons[1])
