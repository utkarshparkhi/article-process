from transformers import pipeline
import torch


def get_sentiment(texts):
    classifier = pipeline("sentiment-analysis")
    res = classifier(texts)
    return res