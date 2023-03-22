# SMTP is the protocol for sending mails through internet
import smtplib   # a python library for accessing smtp
import datetime as dt
import pandas

my_mail = 'shruti24ai057@satiengg.in'
pss = 'Hidden_due_to_privacy_reason'                    # generated through security for one particular action

# today = dt.datetime.now()            #now returns the exact/current date and time
# today_tuple = (today.month, today.day)
today = dt.datetime(year=2023,month=11,day=29)
today_tuple = (today.month, today.day)
# accessing birth dates from csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = 'letter_template.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com') as connection:      #the parameter passed is specially for @gmail extensions
        connection.starttls()                 #Puts the connection to the SMTP server into TLS(Transport layer security) mode.
        connection.login(user=my_mail,password=pss)
        connection.sendmail(from_addr=my_mail,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{contents}")
        # email without subject is prime suspect of spam mail
        connection.close()                      #Close the connection to the SMTP server.


#-------------------------------------------------------------------------------------------------------------