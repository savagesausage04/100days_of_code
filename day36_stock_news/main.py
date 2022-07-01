import requests
from twilio.rest import Client
account_sid = "AC47cefb54da23e053f6131749d8e567ae"
auth_token = "764edbf047cafd5a70adf53756b8be77"


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "GM6CDR5GLJEH1NGZ"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
y_data = data_list[0]
y_price = float(y_data["4. close"])

dby_data = data_list[1]
dby_price = float(dby_data["4. close"])
up_down = None
difference = (y_price - dby_price)
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_dif = round((difference / y_price) * 100, 2)


news_api_key = "625d4dd39fa24a66869e1c19cb5e626a"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,

}

if abs(percentage_dif) > 1:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    three_articles = news_data["articles"][:3]
    articles_updated = [f'{STOCK_NAME}: {up_down}{percentage_dif}%\nHeadline: {article["title"]}.\nBrief Description: {article["description"]}' for article in three_articles]


    client = Client(account_sid, auth_token)
    for article in articles_updated:
        message = client.messages.create(
            to='+19494008938',
            from_="+18456608440",
            body=article
    )

    print(message.sid)



