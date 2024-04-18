from datetime import datetime


def get_days_from_today(date):
    DATE_FORMAT = "%Y-%m-%d"
    input_date = None
    try:
        input_date = datetime.strptime(date, DATE_FORMAT)
    except TypeError:
        print(f"Input paramentr {date} has \'{type(date).__name__}\' type, "
              "but should be a string, date format is \"YYYY-MM-DD\" e.g \"2021-11-23\"")
    except ValueError:
        print(f"Input paramentr {date} has wrong date format."
              " Date format should be \"YYYY-MM-DD\" e.g \"2021-11-23\"")
    return datetime.now().toordinal()-input_date.toordinal()


print(get_days_from_today("2024-04-17"))
