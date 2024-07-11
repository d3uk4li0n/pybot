# w13 as1
import requests, json

api_key = "" # insert your API key here
base_url = "http://api.openweathermap.org/data/2.5/forecast?q="
city_name = 'Georgia'
# URL
complete_url = base_url + city_name + "&appid=" + api_key
# send request and get response
response = requests.get(complete_url)
# to json format
x = response.json()

weather = ''  # weather information
# check if valid request, response
if x["cod"] != "404":

    for data_dict in x['list']:
        weather += 'Datetime: ' + data_dict['dt_txt'] + '\n'
        weather += 'Temperature: ' + str(data_dict['main']['temp']) + '\n'
        weather += 'Pressure: ' + str(data_dict['main']['pressure']) + '\n'
        weather += 'Humidity: ' + str(data_dict['main']['humidity']) + '\n'
        weather += 'Wind: ' + str(data_dict['wind']['speed']) + '\n'
        weather += 'Description:'
        for des in data_dict['weather']:
            weather += ' ' + des['description']
        weather += '\n\n'

print(weather)

state_name = 'ga'
complete_url = "https://api.covidtracking.com/v1/states/" + state_name + "/current.json"

# send request and get response
response = requests.get(complete_url)
# to json format
x = response.json()

covid_info = ''
covid_info += 'Date Checked: ' + x['dateChecked'] + '\n'
covid_info += 'State: ' + x['state'] + '\n'
covid_info += 'Death Confirmed: ' + str(x['deathConfirmed']) + '\n'
covid_info += 'Death Probable: ' + str(x['deathProbable']) + '\n'
covid_info += 'Positive: ' + str(x['positive']) + '\n'
covid_info += 'Death Increase: ' + str(x['deathIncrease']) + '\n'
covid_info += 'Hospitalized Increase: ' + str(x['hospitalizedIncrease']) + '\n'

print(covid_info)

#weather = 'test a'
#covid_info = 'test b'

# generate automatic email that provides weather and covid at that position
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address --> ANY EMAIL
password = ''
subject = 'Weather and Covid 19 Update'

message = 'Weather Information'
message += '\n----------------\n'
message += weather
message += '\n----------------\n'
message += 'Covid-19 Information\n'
message += covid_info

sending_message = 'Subject: {}\n\n{}'.format(subject, message)

import smtplib
# creates SMTP session
s = smtplib.SMTP(smtp_server, 587)
s.starttls()

# authentication
s.login(sender_email, password)

# sending the mail
s.sendmail(sender_email, receiver_email, sending_message)
# terminating the session
s.quit()

print('Email has been sent successfully')

# use bot
