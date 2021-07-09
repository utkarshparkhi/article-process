from models import facebook_xsum


def oneliners(texts):
    oneliners = []
    batch_size = 2
    for i in range(0, len(texts), batch_size):
        oneliners.extend(facebook_xsum.get_onel(texts[i:i + batch_size]))
    return oneliners
