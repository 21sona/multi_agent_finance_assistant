# AI Tool Usage Log: Multi-Agent Finance Assistant

This document provides a detailed breakdown of AI tool usage, code generation steps, and model configurations for the Multi-Agent Finance Assistant project.

---

## 🧠 Whisper (STT - Speech-to-Text)

* **Toolkit**: `openai/whisper`
* **Model Used**: `base.en`
* **Purpose**: Converts spoken queries into text for processing.
* **Parameters**:

  * `language`: 'en'
  * `fp16`: False
* **Notes**: Integrated locally for latency; converts audio to intermediate transcript used by Orchestrator.

---

## 📊 LangChain + LLM (GPT-4)

* **Toolkit**: `LangChain`, `openai`
* **Model Used**: `gpt-4` (via OpenAI API)
* **Prompt Template**:

```
You are a financial assistant. Based on the data: {retrieved_docs}, summarize the risk exposure and earnings surprises.
```

* **Temperature**: `0.3`
* **Max Tokens**: `300`
* **Use Case**: Narrative generation for daily market briefings.
* **Retrieval Confidence Threshold**: 0.75
* **Fallback Handling**: Asks for clarification if retrieval score falls below threshold.

---

## 🔍 Retrieval Agent

* **Toolkit**: `FAISS`, `InstructorEmbedding`
* **Embedding Model**: `hkunlp/instructor-large`
* **Vector Dimension**: 768
* **Index Type**: `FlatL2`
* **Chunking Method**: `RecursiveCharacterTextSplitter`
* **Chunk Size**: 500 chars
* **Top-k**: 4

---

## 📈 Data Ingestion & Analysis

### API Agent

* **Toolkit**: `yfinance`
* **Tickers Tracked**: `TSM`, `SSNLF`, `ASML`, etc.
* **Data Points**: price, volume, earnings date, surprise %
* **Sample Code**:

```python
ts_data = yf.Ticker("TSM").history(period="2d")
```

### Scraping Agent

* **Toolkit**: `unstructured`, `requests-html`, `bs4`
* **Target Sources**: SEC Filings, MarketWatch, Yahoo Finance News
* **Simplification**: Used `unstructured.partition` to avoid full browser automation
* **Chunk Storage**: Appended to `faiss_index.json`

---

## 🔊 Voice Agent

* **STT**: Whisper (`base.en`)
* **TTS**:

  * `pyttsx3` for offline
  * `EdgeTTS` for web voice synthesis
* **Audio Format**: WAV (Mono, 16kHz)
* **Pipeline**:

  1. STT (Whisper)
  2. Orchestrator → LLM
  3. TTS (response → voice)

---

## 🧠 CrewAI & LangGraph (Optional)

* **Agent Orchestration Frameworks**:

  * `CrewAI`: for persistent task memory and multi-agent workflows
  * `LangGraph`: for graph-style LLM orchestration (planned)
* **Use Case**: Future upgrade for complex task routing and fallback chains

---

## 📓 Code Generation Log (Key Interactions)

* Prompt: "Generate a FastAPI microservice that accepts a query, runs a retrieval pipeline, and responds with GPT-generated text"

* Output: Auto-generated `/market_brief` endpoint with chained agents

* Prompt: "Create a Streamlit frontend that records audio, sends it to backend, and plays TTS response"

* Output: Full audio interaction loop integrated with `streamlit.runtime.scriptrunner`

---

## 📘 Model Usage Summary

| Component  | Model / Tool        | Purpose                      |
| ---------- | ------------------- | ---------------------------- |
| STT        | Whisper (base.en)   | Voice to text                |
| LLM        | GPT-4 (OpenAI)      | Market summary generation    |
| Retriever  | FAISS + Instructor  | Top-k document retrieval     |
| TTS        | pyttsx3 / EdgeTTS   | Text to speech output        |
| Embeddings | InstructorEmbedding | Vectorization of text chunks |

---

## 🔒 Ethics & Transparency

All prompts, retrieval mechanisms, and agent logic are logged to support transparency. No sensitive data is stored.

---

## 🏁 Next Steps

* Track token usage for cost awareness.
* Compare Whisper vs Vosk STT.
* Try open-source LLMs like Mistral or LLaMA for offline deployments.
