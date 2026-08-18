import requests

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

players = data["elements"]

print("Number of players found:", len(players))

print("\nFirst 5 players:")

for player in players[:5]:
    print(
        player["first_name"],
        player["second_name"],
        "- £" + str(player["now_cost"] / 10),
        "-", player["total_points"], "points"
    )