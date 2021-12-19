import yagmail
import pandas as pd
from news import NewsFeed  # for news feed object

import apikey  # it contains my email address and password

import datetime

today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() -
             datetime.timedelta(days=2)).strftime('%Y-%m-%d')

df = pd.read_excel('people.xlsx')

for i, row in df.iterrows():
    interest = row['interest']
    news_feed = NewsFeed(intrest=interest, from_date=today, to_date=yesterday)

    email = yagmail.SMTP(user=apikey.email_id, password=apikey.email_password)
    receiver_email = row['email']
    receiver_name = row['name']
    email.send(
        to=receiver_email,
        subject=f'Hello {receiver_name}, here is your news for today',
        contents=f"Hi {receiver_name}, see what's on about {interest} for today,\n{news_feed.get10()}"
    )
