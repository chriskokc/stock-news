# stock-news
# This program serves as your stock monitoring system. It helps you check the recent price changes and fetch you relevant company news to assist you to make an investment decision.

Are you a professional stock trader? Or do you want to learn how to invest as a beginner? No matter how expereinced you are in stock investing, this application helps you monitor your stock 
and gives you some updates on the company. This program is inspired by the professional computer software Bloomberg Terminal, which 
enables traders to monitor and analyze real-time financial market data. 

This application is a simple version of Bloomberg Terminal. It gets the updated stock prices from Alpha Vantage API. By comparing the price difference between yesterday and the day before yesterday,
it checks if there is a significant change its trend. If it is greater than 5%, the app will fetch you the top three related company news from the News API. With the Twilio Messaging API service, those news will be
sent to your phone as separare SMS message. So next time you won't have to be busy checking your stock performance, as this app can help you do the work!
