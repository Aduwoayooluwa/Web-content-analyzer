# Web Content Summarizer API

A FastAPI-based service that scrapes web content, generates summaries, and performs sentiment analysis to provide actionable recommendations.

## Features

- Web scraping of text content from URLs
- Text summarization using T5-Small (a compact, efficient summarization model)
- Sentiment analysis using DistilBERT
- Automated recommendations based on content analysis
- RESTful API endpoints

## Installation

1. Clone the repository
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install dependencies:    

```bash
pip install -r requirements.txt
```

4. Run the FastAPI application:

```bash
uvicorn api:app --reload
```

## API Endpoints

### Summarize Web Content

```bash
curl -X POST "http://localhost:8000/summarize" -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}'
```

### Get Recommendations

```bash
curl -X POST "http://localhost:8000/recommendations" -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}'
```

## Configuration

The application uses the following configuration settings:

- `SCRAPING_TIMEOUT`: Timeout for web scraping (default: 10 seconds)
- `USER_AGENT`: User agent string for web scraping (default: Chrome browser)
- `SUMMARIZATION_MODEL`: Model for text summarization (default: T5-Small)
- `SENTIMENT_MODEL`: Model for sentiment analysis (default: DistilBERT)
