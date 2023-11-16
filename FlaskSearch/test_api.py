import time

import requests
import json

# Base URL of your Flask application
# Base URL of your Flask application
BASE_URL = "http://0.0.0.0:8000"


def test_search():
    url = f"{BASE_URL}/search"
    data = {
  "sentences": [
    "منطقة ال الحناوي الكرام",
    "Greenhouse",
     "منزل مصطفى يوسف ابو مجدي",
    "Third sentence to search"
  ]
}
    headers = {'Content-Type': 'application/json'}
    # s = time.time()
    response = requests.post(url, data=json.dumps(data), headers=headers)
    # print(time.time() - s)
    print("Search Endpoint Response:")
    print(response.status_code, response.json())


def test_is_service_alive():
    url = f"{BASE_URL}/is_service_alive"

    response = requests.get(url)
    print("\nIs Service Alive Endpoint Response:")
    print(response.status_code, response.json())


if __name__ == "__main__":
    test_search()
    test_is_service_alive()
