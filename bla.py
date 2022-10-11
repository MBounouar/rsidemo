import requests
import json

URL = "http://localhost:8000"

response = requests.post(
    f"{URL}/trendsignal/rsi",
    """{
    "startDate": "2020-09-01",
    "endDate": "2020-10-01",
    "priceCol": "close",
    "freq": "Min"
    }""",
    verify=False,
)

print(response)
records = json.loads(response.content.decode("utf8"))
print(records)
