import Tkinter
import ttk
from pages import one, two, three

class App():

    schedGraphics = Tkinter
    root = schedGraphics.Tk()

    def __init__(self):
        # Execute core methods
        self.config_app()
        self.add_pages()
        self.run_app()

    def config_app(self):
        self.root.title("Genealogy Tool")
        self.nb = ttk.Notebook(self.root)
        self.page_width = 600
        self.page_height = 600

    def add_pages(self):
        one.PersonPage(
            notebook=self.nb,
            height=self.page_height,
            width=self.page_width)

        two.ChildPage(
            notebook=self.nb,
            height=self.page_height,
            width=self.page_width)

        three.MarriagePage(
            notebook=self.nb,
            height=self.page_height,
            width=self.page_width)

    def config_widgets(self):
        pass

    def run_app(self):
        # Run the mainloop
        self.root.mainloop()

if __name__ == "__main__":
    new_window = App()
