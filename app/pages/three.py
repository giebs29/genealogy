from Tkinter import *
import ttk
from db_tools import family_tools
from db_tools import person_tools
from db_tools import input_validation
from db_tools import terminus_tools
from db_tools import location_tools
from db_tools import relationship_tools

class MarriagePage():
    def __init__(self,notebook,height,width):
        self.nb = notebook
        self.page_height = height
        self.page_width = width
        self.config_page()
        self.config_widgets()

    def config_page(self):
        self.page = ttk.Frame(self.nb,width=self.page_width,height=self.page_height)
        self.nb.add(self.page, text='Add Marriage')

    def config_widgets(self):
        # Husband
        husband_label = Label(self.page)
        husband_label['text'] = 'Husband'
        husband_label.grid(row=0, column=0, sticky=E)

        males = relationship_tools.list_males()
        self.male_list = self.build_name_list(males)

        self.husband_combo = ttk.Combobox(self.page)
        self.husband_combo['values'] = [i[0] for i in self.male_list]
        self.husband_combo['width'] = 30
        self.husband_combo.grid(row=0,column=1,columnspan=4, sticky=W)

        # Wife
        wife_label = Label(self.page)
        wife_label['text'] = 'Wife'
        wife_label.grid(row=1, column=0, sticky=E)

        females = relationship_tools.list_females()
        self.female_list = self.build_name_list(females)

        self.wife_combo = ttk.Combobox(self.page)
        self.wife_combo['values'] = [i[0] for i in self.female_list]
        self.wife_combo['width'] = 30
        self.wife_combo.grid(row=1,column=1,columnspan=4, sticky=W)

        # Marriage location
        loc_label = Label(self.page)
        loc_label['text'] = 'Location'
        loc_label.grid(row=5, column=0, sticky=E)

        locations_dict = location_tools.list_locations()
        self.locations = self.build_location_list(locations_dict)

        self.loc_combo = ttk.Combobox(self.page)
        self.loc_combo['values'] = [i[0] for i in self.locations]
        self.loc_combo['width'] = 50
        self.loc_combo.grid(row=5,column=1,columnspan=4, sticky=W)

        # Marriage start
        start_label = Label(self.page)
        start_label['text'] = 'Start Date'
        start_label.grid(row=6, column=0, sticky=E)

        self.start_entry = Entry(self.page)
        self.start_entry['width'] = 10
        self.start_entry.grid(row=6,column=1, sticky=W)

        # Marrigae end
        end_label = Label(self.page)
        end_label['text'] = 'End Date'
        end_label.grid(row=7, column=0, sticky=E)

        self.end_entry = Entry(self.page)
        self.end_entry['width'] = 10
        self.end_entry.grid(row=7,column=1, sticky=W)

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

            locations.append([temp_str, loc['id']])
        locations.sort(key=lambda loc: loc[0])
        return locations

    def build_name_list(self,person_dict):
        people = []
        for person in person_dict:
            if person['middle']:
                name = '{0} {1} {2}'.format(person['first'],person['middle'], person['last'])
            else:
                name = '{0} {1}'.format(person['first'],person['last'])
            people.append([name,person['id']])
        people.sort(key=lambda i: i[0])
        return people


    def clear_values(self):
        self.wife_combo.set('')
        self.husband_combo.set('')
        self.loc_combo.set('')
        self.start_entry.delete(0, 'end')
        self.end_entry.delete(0, 'end')

    def submit_values(self):
        husband_id = self.male_list[self.husband_combo.current()][1]
        wife_id = self.female_list[self.wife_combo.current()][1]
        loc_id = self.locations[self.loc_combo.current()][1]
        start_date = self.start_entry.get()
        end_date = self.end_entry.get()

        if husband_id and wife_id:
            relationship_tools.add_marriage(husband_id,wife_id,start_date,end_date,loc_id)
