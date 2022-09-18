import requests
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Age Calculator")
        self.geometry("310x400")
        self.resizable(False, False)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AgeCalc, Customizer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # Image
        self.image = Image.open("transparency.png")
        
        self.resized = self.image.resize((310,400))
        self.bg = ImageTk.PhotoImage(self.resized)
        self.label = ttk.Label(self, image = self.bg)

        self.label.image = self.bg


        self.label.place(x=0,y=0)

        # Cat Image
        self.image = Image.open("mmmmeow.png")

        self.resized = self.image.resize((250,200))

        self.img = ImageTk.PhotoImage(self.resized)
        self.label = ttk.Label(self, image = self.img)
        self.label.image = self.img

        self.label.pack(pady = 10)

        self.pack()

        # Buttons
        button = ttk.Button(self, text="Go",
                            command=lambda: controller.show_frame("AgeCalc"))
        button2 = ttk.Button(self, text="Customizer",
                            command=lambda: controller.show_frame("Customizer"))
        button3 = ttk.Button(self, text="Exit",
                            command=self.quit)


        button.pack(ipadx = 5, ipady = 10)
        button2.pack(ipadx = 5, ipady = 10)
        button3.pack(ipadx = 5, ipady = 10)


class AgeCalc(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        AgeCalc.columnconfigure(self, 0, weight=2)

        # Image
        self.image = Image.open("transparency.png")

        self.resized = self.image.resize((310,400))
        self.bg = ImageTk.PhotoImage(self.resized)
        self.label = ttk.Label(self, image = self.bg)

        self.label.image = self.bg


        self.label.place(x=0,y=0)


        # Family Image
        self.image = Image.open("fam.png")

        self.resized = self.image.resize((150,150))

        self.img = ImageTk.PhotoImage(self.resized)
        self.label = ttk.Label(self, image = self.img)
        self.label.image = self.img

        self.label.grid(column = 0, row = 0, pady = 10, columnspan=3)


        # Buttons (Go to Start Page, Customizer or Exit)
        button = ttk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = ttk.Button(self, text="Customizer",
                    command=lambda: controller.show_frame("Customizer"))
        button3 = ttk.Button(self, text="Exit",
                    command=self.quit)

        button.grid(column = 0, row = 7, padx = 15, pady = 17)
        button2.grid(column = 1, row = 7, padx = 10, pady = 17)
        button3.grid(column = 2, row = 7, padx = 15, pady = 17)

        self.result = ttk.Label(self)
        self.result.grid(column = 0, row = 6, columnspan = 3)


        # YEARS
        a = []
        for i in range(1940, 2023):
            a.append(i)
        self.years = (a)
        self.create_years()

        # MONTHS
        self.months = ('January', 'February', 'March',
                        'April', 'May', 'June', 'July', 'August',
                        'September', 'October', 'November', 'December')
        self.create_months()

        # DAYS
        c = []
        for i in range(1,32):
            c.append(i)
        self.days = (c)
        self.create_days()

        # TIMEZONE
        self.time = ('Asia', 'Australia', 'Europe', 'United Kingdom', 'United States')
        self.create_timezone()


    def create_timezone(self):

        # label
        label = ttk.Label(self, text='Select your place of living:')
        label.grid(column = 0, row = 1, columnspan = 3, sticky = 'w', padx = 15, pady = 1)

        self.option_varo = tk.StringVar(self)

        # option menu
        option_menus = ttk.OptionMenu(
            self,
            self.option_varo,
            self.time[0],
            *self.time,
            )

        option_menus.grid(column = 1, row = 1, pady = 1, columnspan=2)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid()


    def create_years(self):

        # label
        label = ttk.Label(self, text='Select your birth year:')
        label.grid(column = 0, row = 2, columnspan = 3, sticky = 'w', padx = 15, pady = 1)

        self.option_vari = tk.IntVar(self)

        # option menu
        option_menuy = ttk.OptionMenu(
            self,
            self.option_vari,
            self.years[-1],
            *self.years,
            )

        option_menuy.grid(column = 1, row = 2, sticky = 'e', pady = 1)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid()
    


    def create_months(self):

        # label
        label = ttk.Label(self, text='Select your birth month:')
        label.grid(column = 0, row = 3, columnspan = 3, sticky = 'w', padx = 15, pady = 1)

        self.option_var = StringVar(self)

        # option menu
        option_menum = ttk.OptionMenu(
            self,
            self.option_var,
            self.months[0],
            *self.months,
            )

        option_menum.grid(column = 1, row = 3, pady = 1, columnspan = 2)

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid()


    def create_days(self):

        # label
        label = ttk.Label(self, text='Select your birth day:')
        label.grid(column = 0, row = 4, columnspan = 3, sticky = 'w', padx = 15, pady = 1)

        self.option_varb = tk.StringVar(self)

        # option menu
        option_menud = ttk.OptionMenu(
            self,
            self.option_varb,
            self.days[0],
            *self.days,
            )

        option_menud.grid(column = 1, row = 4, sticky = 'e', pady = 1)


        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid()



        # Calculate button
        calculate = ttk.Button(self, text = "Calculate", command = self.clicked)
        calculate.grid(column = 0, row = 5, pady = 15, columnspan = 3)

    def clicked(self):

        # Getting current time from API
        timezone = self.option_varo.get()
        shit = f"https://timezone.abstractapi.com/v1/current_time/?api_key=8601ce1ce2d14147b53ace01de9a0675&location=Oxford, {timezone}"
        response = requests.get(shit)
        dictresponse = response.json()
        
        date_time = dictresponse["datetime"]

        # Current time
        years_now = date_time[:4]
        months_now = date_time[5:7] # if months_now[0] == 0: months_now[0].remove() so it strips/removes the first index 0 as we don't need it
        days_now = date_time[8:10]

        hours_now = date_time[11:13] # i need another fucking frame that switches between years, months, days and years, months, days, hours, minutes, seconds
        minutes_now = date_time[14:16]
        seconds_now = date_time[17:19]

        # User birthday
        birth_year = self.option_vari.get()
        birth_month = self.months.index(self.option_var.get())+1
        birth_day = self.option_varb.get()

        indexes = []
        for i,j in enumerate(self.months):
            #print(i) #index
            #print(j) #month
            indexes.append(i+1)

        if birth_month in self.months:
            return


        # Getting rid of unnecessary 0's at months and days
        if str(months_now[0]) == "0":
            months_now = months_now[1]
        else:
            pass

        if str(days_now[0]) == "0":
            days_now = days_now[1]
        else:
            pass

        # The calculating.
        # User year
        user_year = int(years_now) - int(birth_year)

        # User month

        user_month = []
        if int(birth_month) > int(months_now):
            for i in range(int(birth_month) - int(months_now)):
                user_month.append(birth_month)
                birth_month += 1
        else:
            for i in range(int(months_now) - int(birth_month)):
                user_month.append(birth_month)
                birth_month += 1
            
        # Years to days
        user_year_days = user_year * 365

        liven_years = []

        for i in range(int(years_now) - int(birth_year)):
            birth_year += 1
            if birth_year % 4 == 0:
                liven_years.append(birth_year)

        for i in range(len(liven_years)):
            user_year_days += 1

        user_month_days = 0
        # Months to days
        if 1 in user_month:
            user_month_days += 31
        if 2 in user_month:
            user_month_days += 28
        if 3 in user_month:
            user_month_days += 31
        if 4 in user_month:
            user_month_days += 30
        if 5 in user_month:
            user_month_days += 31
        if 6 in user_month:
            user_month_days += 30
        if 7 in user_month:
            user_month_days += 31
        if 8 in user_month:
            user_month_days += 31
        if 9 in user_month:
            user_month_days += 30
        if 10 in user_month:
            user_month_days += 31
        if 11 in user_month:
            user_month_days += 30
        if 12 in user_month:
            user_month_days += 31
        
        # User days
        if int(birth_day) > int(days_now):
            user_day = int(birth_day) - int(days_now)
            users_days = user_year_days + user_month_days - user_day
        else:
            user_day = int(days_now) - int(birth_day)
            users_days = user_year_days + user_month_days + user_day

        numbers = "{:,}".format(users_days)

        # Result output label

        self.result['text'] = f"You are {numbers} days old."



class Customizer(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller

        Customizer.columnconfigure(self, 0, weight = 2)

        # Image
        self.image = Image.open("sprinkles.png")
        self.images = Image.open("donuts.png")
        self.imagez = Image.open("Metal_gear_rising_revengeance_raiden.png")
        self.imagey = Image.open("transparency.png")

        self.resizeds = self.images.resize((310,400))
        self.resized = self.image.resize((310,400))
        self.resizezz = self.imagez.resize((310,400))
        self.resizedg = self.imagey.resize((310,400))

        self.sprinkles = ImageTk.PhotoImage(self.resized)
        self.donuts = ImageTk.PhotoImage(self.resizeds)
        self.raiden = ImageTk.PhotoImage(self.resizezz)
        self.bg = ImageTk.PhotoImage(self.resizedg)
        self.label = ttk.Label(self, image=self.bg)
        self.label.image = self.sprinkles
        self.label.image = self.donuts
        self.label.image = self.raiden
        self.label.image = self.bg

        self.label.place(x=0,y=0)


        label = ttk.Label(self, text="Styles", font = 50)
        label.grid(column = 0, row = 1, columnspan = 3, pady = 55, sticky='s', rowspan = 3)
        
        # Buttons
        button = ttk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button3 = ttk.Button(self, text="Exit",
                    command=self.quit)

        button.grid(column = 0, row = 20, padx = 15, pady = 197, sticky ='w')
        button3.grid(column = 2, row = 20, padx = 15, pady = 197, sticky='e')


        # Styling
        self.stylings = ("Default", "Sprinkles", "Donuts", "Raiden MGRR")
        self.create_widgets()

        # Dark Mode
        self.create_darkmode()


    # Creating option menu for the different stylings
    def create_widgets(self):

        self.option_var = tk.StringVar(self)

        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.stylings[0],
            *self.stylings,
            command=self.option_changed,
            style = 'Bigger.TMenubutton')

        option_menu.grid(column=0, row=3, columnspan = 3, rowspan = 4, sticky = 'n', pady = 10)


    def option_changed(self, *args):
        if self.option_var.get() == "Sprinkles":
            self.label['image'] = self.sprinkles
        elif self.option_var.get() == "Donuts":
            self.label['image'] = self.donuts
        elif self.option_var.get() == "Default":
            self.label['image'] = self.bg
        elif self.option_var.get() == "Raiden MGRR":
            self.label['image'] = self.raiden


    def dark_mode(self):
        if self.dark.get() == "dark_mode":
            self.style.configure('TLabel', background='black', foreground='white')
            self.style.configure('TMenubutton', background='black', foreground='white')
            self.style.configure('TButton', background='black', foreground='black')
            self.style.configure('Bigger.TCheckbutton', background='black', foreground='white')
            self.style.configure('Bigger.TMenubutton', background='black', foreground='white')
        else:
            self.style.configure('TLabel', background='#F0F0F0', foreground='black')
            self.style.configure('TMenubutton', background='#F0F0F0', foreground='black')
            self.style.configure('TButton', background='#F0F0F0', foreground='black')
            self.style.configure('Bigger.TCheckbutton', background='#F0F0F0', foreground='black')
            self.style.configure('Bigger.TMenubutton', background='#F0F0F0', foreground='black')


    # Creating checkbutton for dark mode
    def create_darkmode(self):
        
        self.dark = tk.StringVar(self)

        dark = ttk.Checkbutton(
                self,
                text='Dark Mode',
                command = self.dark_mode,
                variable = self.dark,
                onvalue='dark_mode',
                offvalue='light_mode',
                style = 'Bigger.TCheckbutton')

        dark.grid(column = 0, row = 4, columnspan = 3, rowspan = 4, pady = 2, sticky = 'n')


        # Styling checkbox
        self.style = ttk.Style(self)
        
        self.style.configure('Bigger.TCheckbutton', font = 1)
        self.style.configure('Bigger.TMenubutton', font = 1)


if __name__ == "__main__":
    app = App()
    app.mainloop()