import getters as get
from ConfigParser import ConfigParser
from gspread import Client
import datetime
from dateutil.parser import parse

"""
print get.facebook('statesman')
print get.twitter('statesman')
print get.insta('statesman')
print get.youtube('AmericanStatesman')
print get.googleplus('Statesman')
print get.tumblr('austinstatesman')
"""

# Get Google Docs info from the config
cfg = ConfigParser()
cfg.readfp(open('config.cfg'))
user = cfg.get('google_docs', 'user_name')
pw = cfg.get('google_docs', 'password')
sheet_title = cfg.get('google_docs', 'spreadsheet_title')

# Login to Google
c = Client(auth=(user, pw))
c.login()

# Get the spreadsheet
s = c.open(sheet_title)


def get_latest_update(network):
    """
    @network: str
    """
    w = s.worksheet(network)
    cell_val = w.acell('A' + str(w.row_count)).value
    return str(parse(cell_val).date())


def save_stats(network, getter):
    """
    @network: str
    @getter: function
    """
    todays_date = str(datetime.date.today())
    # Only pull stats if we haven't yet pulled them for today
    if get_latest_update(network) != todays_date:
        print "Saving stats for " + network
        w = s.worksheet(network)
        counts = [todays_date]
        for account in w.row_values(1)[1:]:
            counts.append(str(getter(account)))
            w.append_row(counts)
    else:
        print "Today's stats already gathered for " + network


# Get the stats for each network and save them to GDocs
save_stats('Facebook', get.facebook)
save_stats('Twitter', get.twitter)
save_stats('Instagram', get.insta)
save_stats('YouTube', get.youtube)
save_stats('Google+', get.googleplus)
save_stats('Tumblr', get.tumblr)
