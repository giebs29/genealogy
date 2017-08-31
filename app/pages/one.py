from Tkinter import *
import ttk
from db_tools import family_tools
from db_tools import person_tools
from db_tools import input_validation
from db_tools import terminus_tools
from db_tools import location_tools

class PersonPage():
    def __init__(self,notebook,height,width):
        self.nb = notebook
        self.page_height = height
        self.page_width = width
        self.config_page()
        self.config_widgets()

    def config_page(self):
        self.page = ttk.Frame(self.nb,width=self.page_width,height=self.page_height)
        self.nb.add(self.page, text='Add Person')

    def config_widgets(self):
        # First name
        first_label = Label(self.page)
        first_label['text'] = 'First'
        first_label.grid(row=0, column=0, sticky=E)

        self.first_entry = Entry(self.page)
        self.first_entry['width'] = 30
        self.first_entry.grid(row=0,column=1,columnspan=4, sticky=W)

        # Middle name
        middle_label = Label(self.page)
        middle_label['text'] = 'Middle'
        middle_label.grid(row=1, column=0, sticky=E)

        self.middle_entry = Entry(self.page)
        self.middle_entry['width'] = 30
        self.middle_entry.grid(row=1,column=1,columnspan=4, sticky=W)

        # Last name
        last_label = Label(self.page)
        last_label['text'] = 'Last'
        last_label.grid(row=2, column=0, sticky=E)

        self.last_entry = Entry(self.page)
        self.last_entry['width'] = 30
        self.last_entry.grid(row=2,column=1,columnspan=4, sticky=W)

        # Gender
        gender_label = Label(self.page)
        gender_label['text'] = 'Gender'
        gender_label.grid(row=3, column=0, sticky=E)

        self.gender = StringVar()
        male = ttk.Radiobutton(self.page, text='Male', variable=self.gender, value='M')
        female = ttk.Radiobutton(self.page, text='Female', variable=self.gender, value='F')
        male.grid(row=3,column=1,sticky=W)
        female.grid(row=4,column=1,sticky=W)

        # Family
        family_label = Label(self.page)
        family_label['text'] = 'Family'
        family_label.grid(row=5, column=0, sticky=E)

        self.family_list = ttk.Combobox(self.page)
        families = family_tools.list_families()
        self.family_list['values'] = [i['name'] for i in families]
        self.family_list.grid(row=5,column=1,sticky=W,columnspan=4)

        # Birth
        birth_label = Label(self.page)
        birth_label['text'] = 'Birth'
        birth_label.grid(row=6, column=0, sticky=E)

        self.birth_entry = Entry(self.page)
        self.birth_entry['width'] = 10
        self.birth_entry.grid(row=6,column=1)

        locations_dict = location_tools.list_locations()
        locations = self.build_location_list(locations_dict)

        self.birth_loc = ttk.Combobox(self.page)
        self.birth_loc['values'] = locations
        self.birth_loc['width'] = 50
        self.birth_loc.grid(row=6,column=2,columnspan=4)

        # Death
        death_label = Label(self.page)
        death_label['text'] = 'Death'
        death_label.grid(row=7, column=0, sticky=E)

        self.death_entry = Entry(self.page)
        self.death_entry['width'] = 10
        self.death_entry.grid(row=7,column=1)

        self.death_loc = ttk.Combobox(self.page)
        self.death_loc['values'] = locations
        self.death_loc['width'] = 50
        self.death_loc.grid(row=7,column=2,columnspan=4)

        clear_button = Button(self.page)
        clear_button['text'] = 'Clear'
        clear_button['command'] = self.clear_values
        clear_button.grid(row=10, column=1,sticky=E)

        submit_button = Button(self.page)
        submit_button['text'] = 'Submit'
        submit_button['command'] = self.submit_values
        submit_button.grid(row=10, column=2,sticky=E)

        self.nb.grid(column=0)

    def build_location_list(self,locations_dict):
        locations = []
        for loc in locations_dict:
            temp_str = ''
            if loc['name']:
                keys = ['name','city','state','country']
            else:
                keys = ['name','addr1','addr2','addr3','addr4','city','state',
                    'zip','country','x','y']
            for key in keys:
                if loc[key]:
                    if temp_str:
                        temp_str += ', {0}'.format(loc[key])
                    else:
                        temp_str += loc[key]

            locations.append(temp_str)
        return locations


    def clear_values(self):
        self.first_entry.delete(0, 'end')
        self.middle_entry.delete(0, 'end')
        self.last_entry.delete(0, 'end')
        self.family_list.set('')
        self.birth_entry.delete(0, 'end')
        self.death_entry.delete(0, 'end')

    def submit_values(self):
        first = self.first_entry.get()
        middle = self.middle_entry.get()
        last = self.last_entry.get()
        gender = self.gender.get()
        family = self.family_list.current()+1
        birth = self.birth_entry.get()
        birth_loc = self.birth_loc.current()+1
        death =self.death_entry.get()
        death_loc = self.death_loc.current()+1

        if first and last and gender and family > 0:
            if not person_tools.person_exists(first,middle,last,gender,family):
                person_tools.add_person(first,middle,last,gender,family)

                person_id = person_tools.person_search(first,middle,last,gender,family)[0]['id']

                if birth and input_validation.valid_date(birth):
                    if birth_loc > 0:
                        terminus_tools.add_birth(person_id,birth,birth_loc)
                    else:
                        terminus_tools.add_birth(person_id,birth,'')

                if death and input_validation.valid_date(death):
                    if death_loc > 0:
                        terminus_tools.add_death(person_id,death,death_loc)
                    else:
                        terminus_tools.add_death(person_id,death,'')
