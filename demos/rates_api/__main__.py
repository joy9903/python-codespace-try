# default module for that package 
from rates_api.api_server import api_server
from rates_api.rates_app import start_rates_api
import requests

def main() -> None:
    health_check_url = "http://localhost:8080/check"

    with api_server(health_check_url, start_rates_api):
        resp = requests.get("http://localhost:8080/api/2021-04-08?base=INR&symbols=USD,EUR")
        print(resp.json())
if __name__ == "__main__":
    main()