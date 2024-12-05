##################### Extra Hard Starting Project ######################

import pandas
import smtplib
import random
import datetime as dt


MY_EMAIL = "martintestmailone@gmail.com"
MY_PASSWORD = "kvuwvgnbiexbwmet"

today = dt.datetime.now()

# 1. Update the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
birthday = birthday_data[(birthday_data.month == today.month) & (birthday_data.day == today.day)]

name = birthday.name.to_list()
email = birthday.email.to_list()

friends_with_birthdays_today = []

for index in range(len(name)):
    friends_with_birthdays_today.append(
        {
            "name": name[index],
            "email": email[index]
        }
    )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if friends_with_birthdays_today:
    num = random.randint(1, 3)

    for friend in friends_with_birthdays_today:
        with open(f"letter_templates/letter_{num}.txt") as letter:
            content = letter.read()
            content = content.replace("[NAME]", friend["name"])
            message = f"Subject:Happy Birthday\n\n{content}"

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=friend["email"],
                msg=message
            )
