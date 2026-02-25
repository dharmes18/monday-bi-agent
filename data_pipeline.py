import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MONDAY_API_KEY")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORK_BOARD_ID = os.getenv("WORK_BOARD_ID")

def run_query(query):
    url = "https://api.monday.com/v2"
    headers = {"Authorization": API_KEY}
    response = requests.post(url, json={"query": query}, headers=headers)
    return response.json()

def fetch_board(board_id):
    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            name
            column_values {{
              text
              column {{ title }}
            }}
          }}
        }}
      }}
    }}
    """
    data = run_query(query)
    items = data["data"]["boards"][0]["items_page"]["items"]

    rows = []
    for item in items:
        row = {"Item Name": item["name"]}
        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]
        rows.append(row)

    df = pd.DataFrame(rows)
    return df

def clean_dataframe(df):
    # Convert numbers safely
    for col in df.columns:
        df[col] = df[col].replace("", None)

    # Convert deal value to number if exists
    if "Masked Deal value" in df.columns:
        df["Masked Deal value"] = pd.to_numeric(
            df["Masked Deal value"], errors="coerce"
        )

    # Convert dates if present
    date_cols = ["Close Date (A)", "Tentative Close Date", "Created Date"]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df

def load_data():
    deals = fetch_board(DEALS_BOARD_ID)
    work = fetch_board(WORK_BOARD_ID)

    deals = clean_dataframe(deals)
    work = clean_dataframe(work)

    return deals, work