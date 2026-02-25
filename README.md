Monday.com Business Intelligence Agent
🚀 Overview

This project is a Conversational Business Intelligence Agent that generates executive-level insights from monday.com sales and work-order data.

Leadership can ask natural language questions like:

How is our pipeline looking?

What risks do we have?

How is the Mining sector performing?

Prepare a weekly leadership update

The agent converts company data into clear executive summaries using an LLM.

🌐 Live Demo

Hosted Prototype:
👉 https://monday-bi-agent-hayu.onrender.com

API Docs (Swagger UI):
👉 https://monday-bi-agent-hayu.onrender.com/docs

Example Endpoint

POST /chat?q=How is our pipeline looking?
🎯 Assignment Goal

Build a conversational AI agent that:

Connects to monday.com data

Generates leadership-ready business insights

Handles ambiguity and incomplete data gracefully

Produces weekly executive updates

🏗️ Architecture

User → Streamlit UI → FastAPI Backend → Data Pipeline → LLM (OpenRouter) → Executive Insights

Components

FastAPI Backend

REST API endpoint /chat

Handles conversation logic

Connects data + LLM

Streamlit Frontend

Chat interface for business users

Data Pipeline

Loads and cleans monday.com exports

Creates structured summaries

LLM Layer

OpenRouter (Llama 3.1)

Generates executive-level insights

🛠️ Tech Stack
Layer	Technology	Reason
Backend API	FastAPI	Fast & production-ready
Frontend	Streamlit	Quick conversational UI
LLM Provider	OpenRouter (Llama 3.1)	Cost-effective LLM access
Data Processing	Pandas	Data summarisation
Deployment	Render	Public hosted prototype
💡 Key Features
Conversational BI

Leadership can ask questions in natural language.

Executive-Level Insights

Responses include:

Pipeline health

Sector analysis

Risks & recommendations

Weekly Leadership Updates

Agent can automatically generate structured executive reports.

Handles Imperfect Data

The agent explicitly calls out:

Missing fields

Data quality issues

Ambiguities

⚙️ Local Setup (Optional)

Clone repo:

git clone https://github.com/dharmes18/monday-bi-agent.git
cd monday-bi-agent

Install dependencies:

pip install -r requirements.txt

Create .env file:

OPENROUTER_API_KEY=your_key_here
MONDAY_API_KEY=your_key_here

Run backend:

uvicorn main:app --reload

Open Swagger docs:

http://127.0.0.1:8000/docs

Run Streamlit UI:

streamlit run app.py
🔐 Environment Variables

Required for deployment:

OPENROUTER_API_KEY

MONDAY_API_KEY

🧠 Design Decisions (Summary)

Used FastAPI for production-ready API hosting

Used OpenRouter to avoid vendor lock-in

Focused on executive summaries instead of dashboards

Prioritised conversational UX for leadership teams

👤 Author

Dharmeswaran M
B.Tech AIML — Final Year