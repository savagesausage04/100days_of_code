import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
username = "kylehan"
token = "Sangjun04!"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "savagesausage04",
    "name": "Coding Habit Tracker",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": token
}

pixel_endpoint = "https://pixe.la/v1/users/kylehan/graphs/savagesausage04"

today = datetime(year=2022, month=int(input("month: ")), day=int(input("day: ")))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did u code today? "),
}


response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# put_endpoint = "https://pixe.la/v1/users/kylehan/graphs/savagesausage04/20220629"
#
# put_config = {
#     "quantity": "260",
# }
#
# # response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# # print(response.text)
#
# delete_endpoint = "https://pixe.la/v1/users/kylehan/graphs/savagesausage04/20220629"
# #
# # response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)