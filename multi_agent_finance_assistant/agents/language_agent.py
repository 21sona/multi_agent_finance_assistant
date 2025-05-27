from openai import OpenAI
openai = OpenAI()

def generate_market_brief(exposure, earnings):
    prompt = f"""
    Provide a financial morning brief:
    Exposure: {exposure['asia_tech_aum']*100:.0f}% of AUM, previous {exposure['prev_aum']*100:.0f}%.
    Earnings: TSMC surprise {earnings['TSMC']['surprise']*100:.0f}%, Samsung {earnings['Samsung']['surprise']*100:.0f}%.
    """
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content