import requests
import smtplib
import time
from datetime import datetime


MY_LAT = 43.1915198
MY_LONG = 23.6541707
MY_EMAIL = "martintestmailone@gmail.com"
MY_PASSWORD = "kvuwvgnbiexbwmet"


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    sunrise_sunset_data = response.json()
    sunrise = int(sunrise_sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunrise_sunset_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now > sunset or time_now < sunrise:
            return True


def send_email():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="mar7in.kamenov@gmail.com",
            msg="Subject:ISS Passing By\n\nHey, go outside look up and find ISS as it's passing by over your head."
        )


while True:
    time.sleep(10)

    if is_night() and is_iss_overhead():
        send_email()
        print("Success!")