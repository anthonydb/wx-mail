import datetime
import smtplib
import requests
import simplejson as json
from email.mime.text import MIMEText
from settings import mail_settings, outgoing_mails, api_key

def fetch_forecast(api_key):
    mail_url = 'http://api.wunderground.com/api/' + api_key + '/forecast/q/VA/Leesburg.json'
    r = requests.get(mail_url)
    j = json.loads(r.text)
    return j

json = fetch_forecast(api_key)


# Set the current time and add that to the message subject
cur_date = datetime.date.today().strftime("%B") +\
    ' ' + datetime.date.today().strftime("%d") +\
    ', ' + datetime.date.today().strftime("%Y")
subject = 'Family forecast for ' + cur_date


html_open = """\
<html>
  <head></head>
  <body>
"""

html_close = """\
  </body>
</html>
"""

wxdate = json['forecast']['txt_forecast']['date']

mail_text = '<p><b>Hello, DeBarros family!</b></p><p>Here is the Leesburg, Va., weather forecast as of ' + wxdate + '</p>'
forecast_length = len(json['forecast']['txt_forecast']['forecastday']) - 1

for i in range(0, forecast_length):
    cast = '<p><b>' + json['forecast']['txt_forecast']['forecastday'][i]['title'] + '</b>: ' +\
           json['forecast']['txt_forecast']['forecastday'][i]['fcttext'] + '</p>'
    mail_text += cast

mail_text = html_open + mail_text + html_close

# mail stuff
COMMASPACE = ', '

msg = MIMEText(mail_text, 'html')
msg['Subject'] = subject
msg['From'] = 'DeBarros Family Hackr Bot'
msg['To'] = COMMASPACE.join(outgoing_mails)

server = smtplib.SMTP(mail_settings['smtp'], 25)
server.login(mail_settings['address'], mail_settings['pw'])
server.set_debuglevel(1)
server.sendmail(mail_settings['address'], outgoing_mails, msg.as_string())
server.quit()
