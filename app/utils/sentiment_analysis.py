import plotly.express as px
from functools import lru_cache
from .sentiment import generate_sentiment_data

def create_sentiment_plot():
    """Create an interactive Plotly histogram of sentiment scores with dark theme."""

    df = generate_sentiment_data()

    fig = px.histogram(df, x='Sentiment Score', nbins=30, marginal='violin',
                       title='Sentiment Scores',
                       template='plotly_dark', color_discrete_sequence=['darkblue'])  # Using dark theme
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#FFF",
        title={'x': 0.5},
        width=600,  # Adjust width to make plot smaller
        height=400  # Adjust height
    )
    fig.update_traces(opacity=0.75)
    return fig

@lru_cache(maxsize=None) 
def save_sentiment_data(df):
    """Save sentiment data to a JSON file."""
    df.to_json('Dataset/sentiment_data.json', orient='records', lines=True)

if __name__ == '__main__':
    df = generate_sentiment_data()
    create_sentiment_plot(df)
    save_sentiment_data(df)
