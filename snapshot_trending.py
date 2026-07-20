import requests
import csv
from datetime import datetime

url = "https://api.evoevo.ai/v1/square/feed?limit=100&type=agent&chain_id=16661"

print("Fetching:", url)

r = requests.get(url)

print("Status:", r.status_code)

data = r.json()

print("Keys:", data.keys())

print("Items found:", len(data.get("items", [])))

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

with open("trending_agents.csv", "a", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    count = 0

    for item in data.get("items", []):

        profile = item.get("agent_profile", {})

        writer.writerow([
            timestamp,
            item.get("rank"),
            profile.get("agent_id"),
            profile.get("display_name"),
            profile.get("source_power_pts"),
            profile.get("win_rate_pct"),
            profile.get("current_win_streak")
        ])

        count += 1

print("Rows written:", count)
