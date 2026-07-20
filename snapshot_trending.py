import requests
import csv
import os
from datetime import datetime

URL = "https://api.evoevo.ai/v1/square/feed?limit=100&type=agent&chain_id=16661"

data = requests.get(URL).json()

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

csv_file = "trending_agents.csv"

file_exists = os.path.isfile(csv_file)

with open(csv_file, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow([
            "timestamp",
            "rank",
            "agent_id",
            "name",
            "points",
            "win_rate",
            "streak"
        ])

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
