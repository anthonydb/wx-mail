import smtplib
import datetime
import requests
from darksky import forecast
from email.mime.text import MIMEText
from local_settings import mail_settings, send_to_addresses, api_key, latitude, longitude


def fetch_forecast(api_key, latitude, longitude):
    f = forecast(api_key, latitude, longitude)
    return f

def build_html(today_weather):
    # build some HTML snippets to open and close this email
    html_open = """\
    <html>
      <head></head>
      <body>
    """
    html_close = """\
      </body>
    </html>
    """

    # let's now build the HTML body contents
    wxdate = datetime.datetime.fromtimestamp(today_weather.time).strftime('%B %e, %Y, at %l:%M %p')
    mail_text = '<h3>Hello!</h3><p>Here\'s the ' +\
                'weather forecast as of ' + wxdate + '</p>'

    # This is the summary line
    summary = '<p><b>Today\'s Look Ahead</b></p>' + today_weather.daily.summary.encode('UTF-8')
    mail_text += summary

    # The forecast line
    cast_head = '<p><b>Your Big Weekly Forecast</b></p>'
    mail_text += cast_head

    # Iterate through each day's forecast and build HTML
    for item in today_weather.daily:
        date = datetime.datetime.fromtimestamp(item['time']).strftime('%A, %-m/%e')
        summary = item['summary']
        min_temp = item['temperatureMin']
        max_temp = item['temperatureMax']
        sunrise = datetime.datetime.fromtimestamp(item['sunriseTime']).strftime('%l:%M %p')
        sunset = datetime.datetime.fromtimestamp(item['sunsetTime']).strftime('%l:%M %p')
        
        cast = '<p><b>' +\
               date + '</b><br/> ' + summary + '<br/>* High ' + str(int(round(max_temp))) + '; low ' + str(int(round(min_temp))) +\
                   '. <br/>* Sunrise ' + sunrise.lower() + '; set ' + sunset.lower() + '.</p>'
        mail_text += cast.encode('UTF-8')

    # put it all together
    html_body = html_open + mail_text + html_close
    return html_body


def send_email(mail_text):
    # Set the current time and add that to the message subject
    cur_date = datetime.date.today().strftime("%B") +\
        ' ' + datetime.date.today().strftime("%d") +\
        ', ' + datetime.date.today().strftime("%Y")
    subject = 'Family forecast for ' + cur_date

    # Set up the message subject, etc. Then send it.
    COMMASPACE = ', '

    msg = MIMEText(mail_text, 'html')
    msg['Subject'] = subject
    msg['From'] = mail_settings['from']
    msg['To'] = COMMASPACE.join(send_to_addresses)

    server = smtplib.SMTP(mail_settings['smtp'], 25)
    server.login(mail_settings['address'], mail_settings['pw'])
    server.set_debuglevel(1)
    server.sendmail(mail_settings['address'], send_to_addresses,
                    msg.as_string())
    server.quit()


if __name__ == "__main__":
    today_weather = fetch_forecast(api_key, latitude, longitude)
    mail_text = build_html(today_weather)
    send_email(mail_text)
