# Configuration settings for the application

# Web scraping settings
SCRAPING_TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Model settings
SUMMARIZATION_MODEL = "t5-small"  # Small, fast model
SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"

# API settings
API_TITLE = "Web Content Summarizer API"
API_DESCRIPTION = "An API that scrapes, summarizes, and analyzes sentiment of web content"
API_VERSION = "0.1.0" 