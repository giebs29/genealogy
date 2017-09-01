from Tkinter import *
import ttk
from db_tools import family_tools
from db_tools import person_tools
from db_tools import input_validation
from db_tools import terminus_tools
from db_tools import location_tools
from db_tools import relationship_tools

class ChildPage():
    def __init__(self,notebook,height,width):
        self.nb = notebook
        self.page_height = height
        self.page_width = width
        self.config_page()
        self.config_widgets()

    def config_page(self):
        self.page = ttk.Frame(self.nb,width=self.page_width,height=self.page_height)
        self.nb.add(self.page, text='Add Child')

    def config_widgets(self):
        # Child
        child_label = Label(self.page)
        child_label['text'] = 'Child'
        child_label.grid(row=0, column=0, sticky=E)

        orphans = relationship_tools.list_orphans()
        self.orphan_list = self.build_name_list(orphans)

        self.child_list = ttk.Combobox(self.page)
        self.child_list['values'] = [i[0] for i in self.orphan_list]
        self.child_list['width'] = 30
        self.child_list.grid(row=0,column=1,columnspan=4, sticky=W)

        # Mother
        mother_label = Label(self.page)
        mother_label['text'] = 'Mother'
        mother_label.grid(row=1, column=0, sticky=E)

        females = relationship_tools.list_females()
        self.female_list = self.build_name_list(females)

        self.mother_list = ttk.Combobox(self.page)
        self.mother_list['values'] = [i[0] for i in self.female_list]
        self.mother_list['width'] = 30
        self.mother_list.grid(row=1,column=1,columnspan=4, sticky=W)

        # Father
        father_label = Label(self.page)
        father_label['text'] = 'Father'
        father_label.grid(row=2, column=0, sticky=E)

        males = relationship_tools.list_males()
        self.male_list = self.build_name_list(males)

        self.father_list = ttk.Combobox(self.page)
        self.father_list['values'] = [i[0] for i in self.male_list]
        self.father_list['width'] = 30
        self.father_list.grid(row=2,column=1,columnspan=4, sticky=W)

        clear_button = Button(self.page)
        clear_button['text'] = 'Clear'
        clear_button['command'] = self.clear_values
        clear_button.grid(row=10, column=1,sticky=E)

        submit_button = Button(self.page)
        submit_button['text'] = 'Submit'
        submit_button['command'] = self.submit_values
        submit_button.grid(row=10, column=2,sticky=E)

        self.nb.grid(column=0)

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
        self.child_list.set('')
        self.mother_list.set('')
        self.father_list.set('')

    def submit_values(self):
        child_id = self.orphan_list[self.child_list.current()][1]
        mother_id = self.female_list[self.mother_list.current()][1]
        father_id = self.male_list[self.father_list.current()][1]

        if child_id and mother_id:
            relationship_tools.add_child(child_id,mother_id)
        if child_id and father_id:
            relationship_tools.add_child(child_id,father_id)
