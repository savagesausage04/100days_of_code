from bs4 import BeautifulSoup
import requests

print("Welcome to the all-time stats analyzer!")

category = input("Which category would you like to analyze: ")

URL = f"https://www.basketball-reference.com/leaders/{category}.html"
# header = {
#     "SeasonType": "Regular%20Season",
#     "StatCategory": f"{category}",
#
# }
response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

rankings = soup.find_all(name="a")
player_list = []
for player in rankings:
    player_name = player.getText()
    player_list.append(player_name)


updated = player_list[90:]
print(updated)