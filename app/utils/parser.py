import json

def load_config():
    """Load API key from a configuration file."""
    with open('config.json', 'r') as file:
        config = json.load(file)
        return config

def get_api_key():
    """Retrieve the OpenAI API key from the config."""
    config = load_config()
    return config.get('openai_api_key', 'No API key found')
