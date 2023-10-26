from services.sentiment_calculator import sentiment_score

def test_sentiment_scores_1():
    text = "I really like this project"
    scores = sentiment_score(text)
    assert scores['positive_score'] > scores['neutral_score'] > scores['negative_score']

def test_sentiment_scores_2():
    text = "I don't like lettuce"
    scores = sentiment_score(text)
    assert scores['positive_score'] < scores['neutral_score'] < scores['negative_score']

def test_sentiment_scores_3():
    text = "The temperature today is 20 degrees Celsius."
    scores = sentiment_score(text)
    assert scores['positive_score'] < scores['neutral_score'] > scores['negative_score']