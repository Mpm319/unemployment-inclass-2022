
# this is the "app/unemployment_report.py" file...

import json
from pprint import pprint
from statistics import mean

import requests
from plotly.express import line

from app.alpha import API_KEY



request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
#print(type(parsed_response))
#pprint(parsed_response)

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

#breakpoint()

latest = parsed_response["data"][0]
print(latest)
