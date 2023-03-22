import requests                                                         # we will be using API calls
import smtplib
import time

MY_EMAIL = "shruti24ai057@satiengg.in"
MY_PASSWORD = "Hidden_due_to_privacy"

# PANNA (M.P) INDIA , lattitude and longitude - my hometown
MY_LAT = 24.704599
MY_LONG = 80.179802


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
#----------------------------------------------------------------------------------------------------------------