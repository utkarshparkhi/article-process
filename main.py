import datetime

import models
from utils import summarize, oneliners
from utils.dump_data import dump_data
from utils.load_data import load_data
from constant.metrics import rating_metric, date_metric


# texts = [data['text']]


def process(reviews):
    texts = [r['text'] for r in reviews]
    summary = summarize.summarize(texts)
    onel = oneliners.oneliners(texts)
    processed_data = []
    for d, s1, o1 in zip(reviews, summary, onel):
        d.update({'suma1': s1})
        d.update({'onel1': o1})
        # d.update({'suma2': s2})
        # d.update({'onel2': o2})
        processed_data.append(d)
    processed_data = reviews
    for data in processed_data:
        if 'rating' in data.keys() and 'domain' in data.keys():
            data['rating'] = float(data['rating']) / rating_metric[data['domain']]
        if 'comments' in data.keys():
            data['comments'] = int(data['comments'])
        if 'pub_date' in data.keys() and 'domain' in data.keys():
            data['pub_date'] = datetime.datetime.strptime(data['pub_date'], date_metric[data['domain']])
        if 'suma1' in data.keys():
            data.update({"sentiment": models.sentiment.get_sentiment(data['suma1'])[0]})
    dump_data(processed_data)


data = load_data()
process(data)
