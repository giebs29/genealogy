import npyscreen

class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)
        print self.myDate

    def create(self):
       self.myName        = self.add(npyscreen.TitleText, name='Name')
       self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
       self.myDate        = self.add(npyscreen.TitleCombo, name='Date Employed', values=['1','2'])

class mainOptionsForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(myEmployeeForm)

    def create(self):
        options = [
            'Add Person',
            'Add Relationship',
            'Add Marriage']
        self.optionChoice = self.add(npyscreen.TitleSelectOne, scroll_exit=True,
            max_height=3, name='Options',values = options)
        print self.optionChoice

class MyApplication(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', mainOptionsForm, name='Main Menu')
       # A real application might define more forms here.......

TestApp = MyApplication().run()
