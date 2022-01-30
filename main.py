import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("Environment Variables/env.txt")

STOCK = "YOUR STOCK"
COMPANY_NAME = "YOUR STOCK COMPANY"

# Alpha Vantage API
PRICE_API_ENDPOINT = "https://www.alphavantage.co/query"
PRICE_API_KEY = os.getenv("PRICE_API_KEY")
PRICE_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": PRICE_API_KEY
}

# News API
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_PARAMETERS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# Twilio Messaging API
SMS_ACCOUNT_SID = os.getenv("SMS_ACCOUNT_SID")
SMS_AUTH_TOKEN = os.getenv("SMS_AUTH_TOKEN")
sms_auth_token = SMS_AUTH_TOKEN
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
NUMBER_TO_SEND = os.getenv("NUMBER_TO_SEND")

price_response = requests.get(url=PRICE_API_ENDPOINT, params=PRICE_PARAMETERS)
price_response.raise_for_status()
price_data = price_response.json()
daily = price_data["Time Series (Daily)"]
daily_list = [value for (key, value) in daily.items()]
# get the stock prices
yesterday_price = float(daily_list[0]["4. close"])
day_before_yest = float(daily_list[1]["4. close"])

# compare the stock prices between yesterday and the day before yesterday
if yesterday_price - day_before_yest > 0:
    symbol = "🔺"
else:
    symbol = "🔻"
price_diff = abs(yesterday_price - day_before_yest)
percentage_change = price_diff / day_before_yest * 100
# if the percentage difference is greater than 5%,
if percentage_change > 0.05:
    news_response = requests.get(url=NEWS_API_ENDPOINT, params=NEWS_PARAMETERS)
    news_response.raise_for_status()
    news_data = news_response.json()
    # get the first 3 news pieces for YOUR STOCK COMPANY
    first_three_news = news_data["articles"][:3]

    # Send a separate message with the percentage change,
    # and each article's title and description to your phone number.
    for each_news in first_three_news:
        headline = each_news["title"]
        brief = each_news["description"]

        account_sid = SMS_ACCOUNT_SID
        auth_token = SMS_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"{STOCK}: {symbol}{int(percentage_change)}%\nHeadline: {headline}.\nBrief: {brief}.",
            from_=PHONE_NUMBER,
            to=NUMBER_TO_SEND
        )
