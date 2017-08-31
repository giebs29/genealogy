def valid_date(date_str):
    try:
        # YYYY-MM-DD
        year,month,day = date_str.split('-')
        if len(year) == 4:
            if int(month) <= 12:
                if int(day) <= 31:
                    return True

    except:
        return False
