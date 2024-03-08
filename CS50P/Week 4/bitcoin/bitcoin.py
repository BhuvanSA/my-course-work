import requests
import sys
import json

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"


def get_input():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        try:
            no = float(sys.argv[1].strip())
        except:
            sys.exit("Command-line argument is not a number")
        else:
            return no


try:
    ...
    no = get_input()
    response = requests.get(URL)
    if response.status_code == 200:
        price = (response.json()["bpi"]["USD"]
                 ["rate_float"])*float(sys.argv[1])
        print(f"${price:,.4f}")
except requests.RequestException:
    sys.exit("Something went wrong while making a request to coindesk server")
