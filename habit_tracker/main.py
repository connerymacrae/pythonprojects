import requests
from datetime import date, datetime

USERNAME = "connery"
TOKEN = "fgFG64!!absolutE88"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : "fgFG64!!absolutE88",
    "username" : "connery",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Daily Music Practice",
    "unit": "minute",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_info = {
    "date": date.today().strftime("%Y%m%d"),
    "quantity": "38",
}

# response = requests.post(url=add_pixel_endpoint, json=pixel_info, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{add_pixel_endpoint}/20250105"

update_info = {
    "quantity": "43"
}

# response = requests.put(url=update_pixel_endpoint, json=update_info, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{add_pixel_endpoint}/20250105"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)