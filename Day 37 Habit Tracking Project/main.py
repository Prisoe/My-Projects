import requests
from datetime import datetime


# API pixela for creating graph schedules
pixela_endpoint = "https://pixe.la/v1/users"
username = "prosper"
token = "Rasengan2@2612000"

parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# post requests use json format as parameters
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)


# Graph endpoint
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "graph1"

graph_params = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "kuro"

}
# Http headers to hide ApiKEy, token etc
headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# strftime method for editing time objects to strings
today = datetime.now()
year = (today.strftime("%Y"))
month = (today.strftime("%m"))
day = (today.strftime("%d"))
date = today.strftime("%Y%m%d")
# print(date)


#Post a pixel to the graph
pixel_params = {
    "date": "20220725",
    "quantity": "4"
}
pixels_endpoint = f"{graph_endpoint}/{graph_id}"
# response = requests.post(url=pixels_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# Put Request update a pixel

update_params = {
    "quantity": "1"
}

update_endpoint = f"{pixels_endpoint}/{date}"
response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)

f"/v1/users/{username}/graphs/{graph_id}/20220725"