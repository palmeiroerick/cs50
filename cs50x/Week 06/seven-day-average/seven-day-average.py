import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# Create a dictionary to store 14 most recent days of new cases by state
def calculate(covid_data):
    new_cases = dict()
    previous_cases = dict()

    for row in covid_data:
        state, cases = row["state"], int(row["cases"])

        if state not in new_cases:
            new_cases[state] = []
            previous_cases[state] = cases

        daily_new = cases - previous_cases[state]
        previous_cases[state] = cases

        new_cases[state].append(daily_new)

        if len(new_cases[state]) >= 14:
            new_cases[state].pop(0)

    return new_cases


# Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        this_week = round(sum(new_cases[state][7:]) / 7)
        last_week = round(sum(new_cases[state][:7]) / 7)

        diff = this_week - last_week

        change = "an increase" if diff > 0 else "a decrease"
        percent = abs(round(diff / last_week * 100, 2))

        print(f"{state} had a 7-day average of {this_week} and {change} of {percent}%")


if __name__ == "__main__":
    main()
