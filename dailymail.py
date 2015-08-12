import datetime
import smtplib
import requests
import simplejson as json
from email.mime.text import MIMEText
from settings import settings, mails

cur_date = datetime.date.today().strftime("%B") +\
    ' ' + datetime.date.today().strftime("%d") +\
    ', ' + datetime.date.today().strftime("%Y")
subject = 'Family forecast for ' + cur_date

# get the weather
mail_url = 'http://api.wunderground.com/api/79041d492b3219b3/forecast/q/VA/Leesburg.json'
r = requests.get(mail_url)
j = json.loads(r.text)

html_open = """\
<html>
  <head></head>
  <body>
"""

html_close = """\
  </body>
</html>
"""

wxdate = j['forecast']['txt_forecast']['date']

mail_text = '<p><b>Hello, DeBarros family!</b></p><p>Here is the Leesburg, Va., weather forecast as of ' + wxdate + '</p>'
forecast_length = len(j['forecast']['txt_forecast']['forecastday']) - 1

for i in range(0, forecast_length):
    cast = '<p><b>' + j['forecast']['txt_forecast']['forecastday'][i]['title'] + '</b>: ' +\
           j['forecast']['txt_forecast']['forecastday'][i]['fcttext'] + '</p>'
    mail_text += cast

mail_text = html_open + mail_text + html_close

# mail stuff
COMMASPACE = ', '

msg = MIMEText(mail_text, 'html')
msg['Subject'] = subject
msg['From'] = 'DeBarros Family Hackr Bot2 ' + settings['address']
msg['To'] = COMMASPACE.join(mails)

server = smtplib.SMTP(settings['smtp'], 25)
server.login(settings['address'], settings['p'])
server.set_debuglevel(1)
server.sendmail(settings['address'], mails, msg.as_string())
server.quit()
