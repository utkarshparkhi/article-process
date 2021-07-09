from models import facebook_large_cnn


def summarize(texts):
    summary = []
    batch_size = 2
    for i in range(0, len(texts), batch_size):
        summary.extend(facebook_large_cnn.get_summary(texts[i:i + batch_size]))
    return summary
