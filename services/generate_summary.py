from transformers import pipeline

summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text: str) -> str:
    summary = summarizer(text, max_length=len(text.split(' ')), min_length=1, do_sample=False)
    
    return summary[0]['summary_text']

