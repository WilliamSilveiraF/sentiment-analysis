from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

tokenizer = AutoTokenizer.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')

def sentiment_score(text: str) -> int:
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    return { 'negative': scores[0], 'neutral': scores[1], 'positive': scores[2] }
