import json
import requests 
from datetime import date
from business_days import business_days

def compile_report() -> list[json]| None:
    start_date = date(2021, 3, 1)
    end_date = date(2021, 5, 6)
    report = []
    for business_day in business_days(start_date, end_date):
        response = requests.get(f'http://127.0.0.1:8080/api/{business_day}?base=USD&symbols=EUR')
        if response.status_code == 200:
            report.append(response.json())
    

    return report

def print_report(report: list[json]| None = None) -> None:
    if report is None:
        return
    for item in report:
        print(item)




if __name__ == "__main__":
    print_report(compile_report())