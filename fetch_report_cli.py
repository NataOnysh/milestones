import requests
import sys


def fetch_report(occasion, month, department):
    url = f"http://127.0.0.1:5000/{occasion}?month={month}&department={department}"
    response = requests.get(url)
    data = response.json()
    return data


def print_report(data):
    occasion = data["Employees"][0]["Occasion"]
    department = data["Employees"][0]["Department"]
    date = data["Employees"][0]["Date"].split(" ")[0]
    print(f"{occasion} report for {department} department for {date} fetched.")
    print(f"Total: {data['Total']}")
    print("Employees:")
    for employee in data["Employees"]:
        print(f"- {employee['Date']}, {employee['Name']}")


def main():
    if len(sys.argv) != 4:
        print("Provide 3 arguments: anniversaries/birthdays month department")
        sys.exit()
    occasion = sys.argv[1]
    month = sys.argv[2]
    department = sys.argv[3]

    data = fetch_report(occasion, month, department)
    print_report(data)


if __name__ == "__main__":
    main()
