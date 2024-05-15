import openai
import json
import pandas as pd
import numpy as np
import json
from functools import lru_cache
from .parser import get_api_key


def open_ai_response():
    openai.api_key = get_api_key()  

    file_path = 'Dataset/news.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
    article_text = data[0]['Article']
    prompt="Analyze the sentiment of this text: '{}'. Is it positive, negative, or neutral?".format(article_text),


    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Or use "gpt-4o" or the latest available model
        prompt=prompt,
        max_tokens=60
    )

    sentiment = response.choices[0].text.strip()
    print(f"Sentiment: {sentiment}")



@lru_cache(maxsize=None) 
def generate_sentiment_data():
    """Generate dummy sentiment data."""
    np.random.seed(0)
    data = np.random.normal(loc=-0.5, scale=0.25, size=50).clip(-1, 1)
    df = pd.DataFrame(data, columns=['Sentiment Score'])
    return df
