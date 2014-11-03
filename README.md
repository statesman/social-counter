# Social counter
This is a simple Python script to check the follow/like counts for Facebook, Twitter, Instagram, Google+, YouTube and Tumblr account and store them in a Google Spreadsheet.

It's a quick and dirty solution (no error handling, etc.) that was put together in an afternoon for our social media editor so buyers beware.

## Setup
1. Copy the [Google Spreadsheet template](https://docs.google.com/spreadsheets/d/1lj6B1i7oxgvbXN5Fzob2Rl7NlKfFBuOh1bzEfiRJxTE/) and add a column for each account you'd like to track.
2. Copy [`config.cfg.sample`](config.cfg.sample) to `config.cfg`
3. Generate Twitter API credentials at https://apps.twitter.com/app/new and paste them into your `config.cfg` file
4. Generate Instagram API credentials at http://instagram.com/developer/clients/register/ and paste them into your `config.cfg` file
5. In the Google API console, setup a new project https://console.developers.google.com/, enable the Google+ API and create a new browser access key. Add the key to `config.cfg`.
6. Register a new Tumblr application at https://www.tumblr.com/oauth/register and add the Oauth consumer key to `config.cfg`
7. Add the title for the spreadsheet you filled out in step one to the `[google_docs]` section with credentials for the account that owns it.
8. Install dependencies with `pip`
9. Setup a cron job to run `counter.py` at least once day (the script won't record stats more often than that)
