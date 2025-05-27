from fastapi import FastAPI
from agents.api_agent import get_asia_tech_data
from agents.analytics_agent import analyze_exposure, analyze_earnings
from agents.language_agent import generate_market_brief
from agents.voice_agent import text_to_speech

app = FastAPI()

@app.get("/market_brief")
def market_brief():
    market_data = get_asia_tech_data()
    exposure = analyze_exposure(market_data)
    earnings = analyze_earnings(market_data)
    brief = generate_market_brief(exposure, earnings)
    text_to_speech(brief)
    return {"brief": brief}