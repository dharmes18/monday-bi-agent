import os
import requests
from dotenv import load_dotenv
from data_pipeline import load_data

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# ⭐ NEW — cleans weird LLM garbage text
def clean_llm_output(text):
    stop_words = [
        "Assessment(",
        "ACTION assess",
        "Limited Information:",
        '"""'
    ]

    for word in stop_words:
        if word in text:
            text = text.split(word)[0]

    return text.strip()


# ⭐ UPDATED — now includes error handling + cleaning
def ask_llm(prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/llama-3.1-8b-instruct",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )

        data = response.json()
        answer = data["choices"][0]["message"]["content"]

        # ⭐ Clean output before returning
        answer = clean_llm_output(answer)

        return answer

    except Exception as e:
        return f"⚠️ Error contacting AI service: {str(e)}"


def dataframe_summary(deals, work):
    return f"""
DEALS OVERVIEW:
Total Deals: {len(deals)}
Total Pipeline Value: {deals['Masked Deal value'].sum()}

Top Sectors:
{deals['Sector/service'].value_counts().to_string()}

WORK ORDERS OVERVIEW:
Total Work Orders: {len(work)}
Status Breakdown:
{work['WO Status (billed)'].value_counts().to_string()}
"""


def analyse(question):
    deals, work = load_data()
    summary = dataframe_summary(deals, work)

    # ⭐ Better prompt = better answers
    if "leadership" in question.lower() or "weekly" in question.lower() or "update" in question.lower():
        prompt = f"""
You are a senior business analyst.

Create a WEEKLY LEADERSHIP UPDATE for executives.
Be concise, structured, and professional.

Include:
• Executive Summary
• Pipeline value
• Top sectors
• Operational risks
• Key observations
• Recommendations

Company Data:
{summary}
"""
    else:
        prompt = f"""
You are a BUSINESS INTELLIGENCE assistant for founders.

Provide executive-level insights.
Highlight risks if data is incomplete.
Be clear and structured.

User Question:
{question}

Company Data:
{summary}
"""

    return ask_llm(prompt)