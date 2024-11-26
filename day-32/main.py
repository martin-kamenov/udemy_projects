import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "martintestmailone@gmail.com"
MY_PASSWORD = "kvuwvgnbiexbwmet"

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 3:
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        random_quote = choice(quotes[:-1])

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="kamenov.martin@yahoo.com",
            msg=f"Subject: Motivational quote\n\n{random_quote}"
        )