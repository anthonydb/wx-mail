# wx-mail

I'm a weather nerd. I also own a Raspberry Pi. So, what better coding project than a short Python script that lets the Pi email me the weather forecast every day? Because: Lazy. Also, I wanted to learn more about using Python to send emails.

## Usage

* Sign up for a free API key from [Dark Sky](https://darksky.net/dev). You won't be hitting the API much, so the free plan will work just fine.
* Find the latitude and longitude of the place you want for your forecast.
* Add those coordinates, your API key and your email information to `settings.py`. In there, you can also specify a list of the email addresses to send your forecast to.
* You'll probably want to edit the email HTML to suit your needs.
* Set this to run on a cron job and enjoy a fresh forecast in your inbox.

## Requirements

You'll need two Python libraries:

```
pip install requests darkskylib
```
