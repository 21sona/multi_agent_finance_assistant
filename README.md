# multi_agent_finance_assistant
Deliver spoken market briefs with a modular, multi-agent system that combines real-time financial data, earnings analysis, natural language generation, and voice synthesis. This assistant answers:

🗣️ “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

## 🏗️ Architecture Overview

```
[User Voice Input]
       ↓
 [STT (Whisper)]
       ↓
 [FastAPI Orchestrator]
       ↓
 [Agents Layer]
 ┌────────────┬─────────────┬──────────────┐
 │  API Agent │ Scraping    │ Analytics    │
 │  (Yahoo)   │ Agent       │ Agent        │
 └────────────┴─────────────┴──────────────┘
       ↓
 [Retriever Agent (FAISS)]
       ↓
 [Language Agent (LLM)]
       ↓
 [TTS (pyttsx3)]
       ↓
[Voice/Text Output to Streamlit]
```

---

## 🧱 Frameworks & Toolkits Used

| Agent Type        | Toolkits / Libraries                           |
|------------------|-------------------------------------------------|
| API Agent         | `yfinance`, `AlphaVantage`, `polygon.io`       |
| Scraping Agent    | `unstructured`, `playwright`, `bs4`, `requests-html` |
| Retriever Agent   | `FAISS`, `OpenAIEmbeddings`, `InstructorEmbedding` |
| Analytics Agent   | `pandas`, `numpy`                              |
| Language Agent    | `LangChain`, `OpenAI GPT-4`, `CrewAI`          |
| Voice Agent       | `Whisper`, `pyttsx3`, `EdgeTTS`                |
| UI & Routing      | `Streamlit`, `FastAPI`, `Docker`               |

---

## 🛠️ Setup Instructions (Local)

### 1. Clone & Setup Environment
```bash
git clone <your_repo_url>
cd multi_agent_finance_assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run FastAPI Backend
```bash
uvicorn orchestrator.main:app --reload --port 8000
```

### 3. Run Streamlit UI
```bash
cd streamlit_app
streamlit run app.py
```

---

## ☁️ Deployment

### A. Streamlit Cloud (Frontend)
- Link repo to [Streamlit Cloud](https://streamlit.io/cloud)
- Set app path: `streamlit_app/app.py`

### B. Render (Backend)
- Host FastAPI via [https://render.com](https://render.com)
- Start command: `uvicorn orchestrator.main:app --host 0.0.0.0 --port 8000`

### Update Streamlit to Use Remote FastAPI
```python
response = requests.get("https://your-fastapi-service.onrender.com/market_brief")
```

---

## 🚀 Performance Benchmarks

| Feature                  | Time/Latency | Notes                          |
|--------------------------|--------------|--------------------------------|
| API Data Fetching        | ~1.2s        | From Yahoo Finance             |
| Whisper STT              | ~2s          | On 5s audio clip               |
| LLM Response (GPT-4)     | ~2.5s        | Short prompt + single turn     |
| Retrieval Query (FAISS)  | <500ms       | Local vector DB                |
| TTS Playback             | ~1s          | With `pyttsx3`                 |

---

## 📁 Project Structure
```
📦 multi_agent_finance_assistant
├── agents/                # Specialized agents
├── orchestrator/          # FastAPI microservice logic
├── data_ingestion/        # APIs, scrapers
├── vector_store/          # FAISS interface
├── streamlit_app/         # Frontend UI
├── docs/                  # Logs & architecture
├── Dockerfile             # Container setup
├── requirements.txt       # Dependencies
└── README.md
```

---

## 📚 Future Enhancements
- Plug-in calendar scheduler for auto-trigger at 8AM
- Add WebRTC for 2-way live voice
- Integrate LangGraph or CrewAI for more robust agent collaboration

---


