'''App 3 Finished'''

from Tkinter import *
import tkFileDialog


class App():

    '''
    This is a basic Tkinter app
    '''

    # class-level attributes

    master = Tk() # Create Tk instance

    def __init__(self):

        # Assign additional class-level attributes

        # Execute core methods
        self.config_app()
        self.config_widgets()
        self.run_app()

    def config_app(self):

        # Configure app
        self.master.title('SAMPLE')

    def config_widgets(self):

        # Insert widgets

        input_label = Label(self.master)
        input_label['text'] = 'Input File'
        input_label.grid(row=0, column=0)

        self.input_entry_box = input_entry_box = Entry(self.master)
        input_entry_box['width'] = 50
        input_entry_box.grid(row=0,column=1)

        input_button = Button(self.master)
        input_button['text'] = 'Add Person'
        input_button['command'] = self.execute_tool
        input_button.grid(row=0, column=2)

        output_label = Label(self.master)
        output_label['text'] = 'Output File'
        output_label.grid(row=1, column=0)

        self.output_entry_box = output_entry_box = Entry(self.master)
        output_entry_box['width'] = 50
        output_entry_box.grid(row=1,column=1)

        output_button = Button(self.master)
        output_button['text'] = 'BROWSE'
        output_button['command'] = self.execute_tool
        output_button.grid(row=1, column=2)

        exec_button = Button(self.master)
        exec_button['text'] = 'EXECUTE'
        exec_button['command'] = self.execute_tool
        exec_button.grid(row=2,column=1)

    def run_app(self):

        # Run the mainloop
        self.master.mainloop()


    def execute_tool(self):

        # Retrieve input parameters
        input_file_path = self.input_entry_box.get()
        output_file_path = self.output_entry_box.get()

        # Print input parameters
        print(input_file_path)
        print(output_file_path)

if __name__ == '__main__':
    new_window = App()
