import os
def valid_date(message):
    valid = False
    while not valid:
        os.system('clear')
        date_str = raw_input("\n{0}".format(message))
        try:
            if date_str:
                # YYYY-MM-DD
                year,month,day = date_str.split('-')
                if len(year) == 4:
                    if int(month) <= 12:
                        if int(day) <= 31:
                            valid = True
            else:
                valid = True
        except:
            os.system('clear')
            raw_input("\nInvalid date!")
    return date_str

def required_value(message):
    entry = ''
    while not entry:
        os.system('clear')
        entry = raw_input("\n{0}".format(message))
    return entry

def optional_value(message):
    os.system('clear')
    return raw_input("\n{0}".format(message))

def valid_entry(message,data_type,valid_list,choices=None):
    valid = False
    while not valid:
        os.system('clear')
        if choices:
            print choices
        if data_type == 'TEXT':
            entry = raw_input("\n{0}".format(message)).upper()
        else:
            entry = input("\n{0}".format(message))
        if entry not in valid_list:
            os.system('clear')
            raw_input('\nEntry not valid!')
        else:
            return entry
