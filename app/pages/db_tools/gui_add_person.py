from person_tools import *
from family_tools import *
from location_tools import *
from relationship_tools import *
from terminus_tools import *
from gui_input_validation import *

def add_person():
    first  = required_value("First name: ")
    middle = optional_value("Middle name: ")
    last = required_value("Last name: ")

    gender = valid_entry("Gender [M/F]: ","TEXT",['M','F'])

    family_data = ['[{0}] {1}'.format(i['id'],i['name']) for i in list_families()]
    family_ids = [i['id'] for i in list_families()]
    test_str = ''
    for each in family_data:
        test_str += '\n'+each

    os.system('clear')
    family  = valid_entry("Family id: ","NUMBER",family_ids,test_str)

    dob = valid_date("Date of birth [YYYY-MM-DD]: ")
    dod = valid_date("Date of death [YYYY-MM-DD]: ")

    os.system('clear')

    print('''
        First: {0}
        Middle: {1}
        Last: {2}
        Gender: {3}
        Family: {4}
        Birth: {5}
        Death: {6}
        '''.format(first,middle,last,gender,[i['name'] for i in list_families() if i['id'] == family][0],dob,dod))

    cont = raw_input("\nCorrect? [Y/N]: ")
    if cont.upper() == 'Y':
        pass
    else:
        add_person()
