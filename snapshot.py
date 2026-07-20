import requests
import pandas as pd
from datetime import datetime

CHAINS = {
    "0G": 16661,
    "BSC": 56
}

rows = []

for chain_name, chain_id in CHAINS.items():

    url = f"https://api.evoevo.ai/v1/platform/home/overview?chain_id={chain_id}"

    try:

        data = requests.get(url).json()

        overview = data["overview"]

        rows.append({
            "timestamp": datetime.utcnow().isoformat(),
            "chain": chain_name,
            "chain_id": chain_id,
            "agents": overview["total_agents"],
            "opinions": overview["agent_opinions"],
            "memories": overview["memory_count"],
            "markets": overview["total_markets"],
            "tokens": overview["llm_total_tokens"]
        })

    except Exception as e:

        print(f"Failed: {chain_name}")
        print(e)

file = "history.csv"

df_old = pd.read_csv(file)

df_new = pd.concat(
    [df_old, pd.DataFrame(rows)],
    ignore_index=True
)

df_new.to_csv(file, index=False)

print("Snapshots Saved")
