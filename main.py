import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, pipeline


_summarizer = None
_sentiment_analyzer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline('summarization', model="t5-small")
    return _summarizer

def get_sentiment_analyzer():
    global _sentiment_analyzer
    if _sentiment_analyzer is None:
        _sentiment_analyzer = pipeline('sentiment-analysis', 
                                      model="distilbert-base-uncased-finetuned-sst-2-english")
    return _sentiment_analyzer

def web_scraper(url): 
    try:
        response = requests.get(url, timeout=10) 
        response.raise_for_status()  
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraphs = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "div"])
        text_content = ' '.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        return text_content
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        raise

def summarizer(text):
    # Use cached models
    summarizer_pipeline = get_summarizer()
    sentiment_pipeline = get_sentiment_analyzer()
    
    if not text.strip():
        return "No content to summarize", [{"label": "NEUTRAL", "score": 1.0}]

  
    tokenizer = AutoTokenizer.from_pretrained(sentiment_pipeline.model.config._name_or_path)
    encoded_text = tokenizer(text, truncation=True, max_length=512, return_tensors="pt")
    truncated_text = tokenizer.decode(encoded_text["input_ids"][0], skip_special_tokens=True)
    
    # Process with pipelines
    summary = summarizer_pipeline(text, max_length=150, min_length=30, do_sample=False)
    sentiment = sentiment_pipeline(truncated_text)
    
    return summary[0]['summary_text'], sentiment

def generate_recommendations(summary, sentiment):
    recommendations = []
    sentiment_label = sentiment[0]['label']
    sentiment_score = sentiment[0]['score']
    
    if sentiment_label == 'NEGATIVE' and sentiment_score > 0.75:
        recommendations.append("Critical: Investigate potential serious issues with the website content")
    elif sentiment_label == 'NEGATIVE':
        recommendations.append("Investigate potential issues with the website content")
    elif sentiment_label == 'POSITIVE' and sentiment_score > 0.75:
        recommendations.append("The website content is very positive. Leverage this for marketing campaigns.")
    elif sentiment_label == 'POSITIVE':
        recommendations.append("The website content is positive. Consider highlighting these aspects.")
    else:
        recommendations.append("The website content is neutral. Consider adding more engaging content.")
 
    if len(summary) < 50:
        recommendations.append("The website may lack sufficient content. Consider adding more detailed information.")
    
    return recommendations

if __name__ == "__main__":
    # Example usage
    url = 'https://www.alphadesigns.com.ng'
    text_contents = web_scraper(url)
    summary, sentiment = summarizer(text_contents)
    recommendations = generate_recommendations(summary, sentiment)
    print("Summary: ", summary)
    print("Sentiment: ", sentiment)  
    print("Recommendations: ", recommendations)

