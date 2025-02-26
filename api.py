from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, HttpUrl
from main import generate_recommendations, summarizer, web_scraper
import requests

app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'Hello World'
    }


class SummarizeRequest(BaseModel):
    url: HttpUrl 


@app.post('/summarize')
async def summarize(request: SummarizeRequest):
    url = str(request.url) 
    
    try:
        text_contents = web_scraper(url)
        if not text_contents.strip():
            raise HTTPException(status_code=400, detail="Could not extract meaningful text from the provided URL")
            
        summary, sentiment = summarizer(text_contents)
        recommendations = generate_recommendations(summary, sentiment)

        return {
            'summary': summary,
            'sentiment': sentiment,
            'recommendations': recommendations
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error accessing URL: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")
