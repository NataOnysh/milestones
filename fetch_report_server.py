import calendar
import csv
from flask import Flask, jsonify, request


app = Flask(__name__)


def read_csv():
    with open('database.csv', mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


@app.route("/birthdays", methods=["GET"])
def fetch_birthdays():
    data = read_csv()
    month = request.args.get('month')
    department = request.args.get('department')
    employees = []
    for id, employee in enumerate(data):
        if calendar.month_name[int(employee["Birthday"].split("-")[1])] == month.capitalize() and department.lower() == employee["Department"].lower():
            info = {
                "Occasion": "Birthday",
                "Department": employee["Department"],
                "Date": f"{calendar.month_name[int(employee["Birthday"].split("-")[1])]} {employee["Birthday"].split("-")[2]}",
                "Name": employee["Name"],
                "ID": id,
                }
            employees.append(info)
    response = {
        "Total": len(employees),
        "Employees": employees
    }
    return jsonify(response)


@app.route("/anniversaries", methods=["GET"])
def fetch_anniversaries():
    data = read_csv()
    month = request.args.get('month')
    department = request.args.get('department')
    employees = []
    for id, employee in enumerate(data):
        if calendar.month_name[int(employee["Hiring Date"].split("-")[1])] == month.capitalize() and department.lower() == employee["Department"].lower():
            info = {
                "Occasion": "Anniversary",
                "Department": employee["Department"],
                "Date": f"{calendar.month_name[int(employee["Hiring Date"].split("-")[1])]} {employee["Hiring Date"].split("-")[2]}",
                "Name": employee["Name"],
                "ID": id
                }
            employees.append(info)
    response = {
        "Total": len(employees),
        "Employees": employees
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
