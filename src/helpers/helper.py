from datetime import datetime


def format_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return None
