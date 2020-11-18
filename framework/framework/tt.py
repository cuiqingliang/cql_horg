import yaml


def load_date():
    with open('date.yaml',encoding='utf-8') as f:
        date=yaml.safe_load(f)
        date1=date['date']
        date2=date['steps'][0]['find_element'][1]
        print(date1,date2)
        return date
load_date()