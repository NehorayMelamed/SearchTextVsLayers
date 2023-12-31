import time

import requests
import json

# Base URL of your Flask application
# Base URL of your Flask application
BASE_URL = "http://127.0.0.1:8001"


def test_search():
    url = f"{BASE_URL}/search"
    data = {
  "sentences": [
    "קאנטרי קלאב",
    "hamlet",
    "Art Design",
"بعد دوار الشيخ ايد شمالا (بيت لاهيا)",
      "الله أكبر والنصر للاسلام"
  ]
}

    headers = {'Content-Type': 'application/json'}
    s = time.time()
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(time.time() - s)
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
