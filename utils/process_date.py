from datetime import datetime

from constant.metrics import date_metric


def process_date(data):
    if 'pub_date' in data.keys() and 'domain' in data.keys():
        if isinstance(data['pub_date'], str):
            if data['domain'] == 'GSM':
                if data['pub_date'].split()[1] == "Sept":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "September"
                    data['pub_date'] = " ".join(data["pub_date"])

                elif data['pub_date'].split()[1] == "Oct":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "October"
                    data['pub_date'] = " ".join(data["pub_date"])

                elif data['pub_date'].split()[1] == "Feb":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "February"
                    data['pub_date'] = " ".join(data["pub_date"])

                elif data['pub_date'].split()[1] == "Jan":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "January"
                    data['pub_date'] = " ".join(data["pub_date"])

                elif data['pub_date'].split()[1] == "Nov":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "November"
                    data['pub_date'] = " ".join(data["pub_date"])

                elif data['pub_date'].split()[1] == "Dec":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "December"
                    data['pub_date'] = " ".join(data["pub_date"])

                elif data['pub_date'].split()[1] == "Mar":
                    data['pub_date'] = data['pub_date'].split()
                    data['pub_date'][1] = "March"
                    data['pub_date'] = " ".join(data["pub_date"])
            for format in date_metric[data['domain']]:
                try:
                    return datetime.strptime(data['pub_date'], format)
                except:
                    pass
    return data['pub_date']
