import requests
import pandas as pd
from datetime import datetime
import os

url = "https://api.evoevo.ai/v1/platform/home/overview?chain_id=16661"

data = requests.get(url).json()

overview = data["overview"]

row = {
    "timestamp": datetime.utcnow().isoformat(),
    "agents": overview["total_agents"],
    "opinions": overview["agent_opinions"],
    "memories": overview["memory_count"],
    "markets": overview["total_markets"],
    "tokens": overview["llm_total_tokens"]
}

file = "history.csv"

df_old = pd.read_csv(file)

df_new = pd.concat(
    [df_old, pd.DataFrame([row])],
    ignore_index=True
)

df_new.to_csv(file, index=False)

print("Snapshot Saved")
