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

## Results

The email text ends up looking like this:



**Hello!**

Here's the weather forecast as of March 16, 2019, at 8:00 PM

**Today's Look Ahead**

Snow (< 1 in.) on Monday, with high temperatures bottoming out at 47°F on Monday.

**Your Big Weekly Forecast**

**Saturday, 3/16**
Partly cloudy until afternoon.
* High 57; low 39. 
* Sunrise 7:21 am; set 7:19 pm.

**Sunday, 3/17**
Mostly cloudy starting in the evening.
* High 51; low 32. 
* Sunrise 7:20 am; set 7:20 pm.

**Monday, 3/18**
Light snow (< 1 in.) in the morning.
* High 47; low 33. 
* Sunrise 7:18 am; set 7:21 pm.

*etc. ...*