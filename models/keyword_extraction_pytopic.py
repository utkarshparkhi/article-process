from topicrankpy import extractinformation as t


def get_keywords(text, no_of_phrases):

    keywords = t.top_phrases_extraction(text, no_of_phrases)
    return [k[0] for k in keywords]
