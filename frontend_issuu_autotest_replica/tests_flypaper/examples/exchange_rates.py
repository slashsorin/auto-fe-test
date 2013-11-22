"""
In the script below we present how Helium can be used to automatically
read data from websites and make it available for further processing.
"""
from helium.api import *

def get_current_exchange_rate(base_currency, counter_currency):
	currency_pair = base_currency + counter_currency
	ff = start_firefox(
		"http://finance.yahoo.com/q?s={0}=X".format(currency_pair)
	)
	spot_rate = Text(below=Text(
		"{0}/{1} ({2}=X)".format(
			base_currency, counter_currency, currency_pair)
		)).value
	kill(ff)
	return spot_rate

print get_current_exchange_rate("EUR", "USD")
print get_current_exchange_rate("USD", "JPY")
