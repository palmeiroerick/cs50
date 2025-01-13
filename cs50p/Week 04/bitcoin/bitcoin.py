import requests
import sys

if len(sys.argv) == 2:
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    pass
else:
    print(f"${response["bpi"]["USD"]["rate_float"] * bitcoins:,.4f}")
