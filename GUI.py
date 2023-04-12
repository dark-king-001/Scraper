import tkinter as tk
import Worker as wk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.website_input = tk.Entry(self)
        self.website_input.pack()

        self.load_button = tk.Button(self, text="Load Sitemap", command=self.load_sitemap)
        self.load_button.pack()

        self.links_input = tk.Entry(self)
        self.links_input.pack()

        self.menu_options = ["json", "txt"]
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(self.menu_options[0])
        self.menu = tk.OptionMenu(self, self.selected_option, *self.menu_options)
        self.menu.pack()

        self.load_button = tk.Button(self, text="Load Links", command=self.link_extract)
        self.load_button.pack()

        self.output_window = tk.Text(self)
        self.output_window.pack()

        self.after(1000, self.update_output)

    def load_sitemap(self):
        website = self.website_input.get()
        wk.Worker("python3 sitemap_loader.py {}".format(website))
    def link_extract(self):
        file_path = self.links_input.get()
        option = self.selected_option.get()
        wk.Worker("python3 link_extract.py {} {}".format(file_path,option))
    def update_output(self):
        with open("WorkerLog/Output_log.txt", "r") as f:
            new_lines = f.readlines()
        for line in new_lines:
            self.output_window.insert("end", line)
        self.output_window.see("end")
        self.after(1000, self.update_output)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
