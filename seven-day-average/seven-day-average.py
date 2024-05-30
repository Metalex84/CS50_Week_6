import csv
import requests

# NEED TO GO BACK HERE IN THE FUTURE. Too complex for me now :-(

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


def calculate(reader):
    # Init 2 dicts: one for the previous, one for the new dataset
    new_cases = dict()
    prev_cases = dict()

    # Each row is composed by 3 fields.
    for row in reader:
        state = row["state"]
        date = row["date"]
        cases = int(row["cases"])
        # Maybe, there are not previous cases of COVID in this state
        if state not in prev_cases:
            prev_cases[state] = cases
            new_cases[state] = []
        else:
            new_case = cases - prev_cases[state]
            prev_cases[state] = cases
            if state not in new_cases:
                new_cases[state] = []
            if len(new_cases[state]) >= 14:
                new_cases[state].pop(0)
            new_cases[state].append(new_case)

    return new_cases


def comparative_averages(new_cases, states):
    for state in states:
        recent_cases = new_cases[state][7:]
        last_week_cases = new_cases[state][:7]
        avg_recent = round(sum(recent_cases) / 7)
        avg_last_week = round(sum(last_week_cases) / 7)

        diff = avg_recent - avg_last_week

        msg = "an increase" if diff > 0 else "a decrease"

        try:
            p = round((diff / avg_last_week) * 100, 2)
        except ZeroDivisionError:
            raise ZeroDivisionError

        print(f"{state} had a 7-day average of {avg_recent} and {msg} of {p}%")


main()
