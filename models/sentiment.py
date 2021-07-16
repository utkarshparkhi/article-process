from transformers import pipeline


def get_sentiment(texts):
    print("getting sentiment")
    classifier = pipeline("sentiment-analysis")
    res = classifier(texts)
    return res
