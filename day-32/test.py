import smtplib

my_email = "martintestmailone@gmail.com"
password = "kvuwvgnbiexbwmet" #from google

# connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="kamenov.martin@yahoo.com",
#     msg="Subject: Test Email\n\nThis is the body of the email."
# )
# connection.close()

#The above is equivalent to the following:
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="kamenov.martin@yahoo.com",
#         msg="Subject: Test Email\n\nThis is the body of the email."
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(now)
print(year)
print(month)
print(day_of_week)

date_of_birth = dt.datetime(year=1992, month=1, day=11)
print(date_of_birth)