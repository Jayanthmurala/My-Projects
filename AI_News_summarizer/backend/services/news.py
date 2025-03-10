import requests

def fetch_news(api_key: str, category: str = "general"):
    url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["articles"]