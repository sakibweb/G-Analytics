import tkinter as tk
from tkinter import messagebox
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import socket
import os
import time
import requests
from io import BytesIO
from PIL import Image, ImageTk
import datetime as dt

class UpdateLabel():
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("G-Analytics | Easy Way To Monetize Your GIG")
        self.win.iconbitmap('favicon.ico')
        self.win.resizable(False, False)
        self.win.resizable(0,0)
        self.win.overrideredirect(0)
        self.win.attributes('-toolwindow', False)
        self.win.geometry('900x600')
        back = "gray25"
        opt = "HotPink1"
        self.win.configure(background=back)
        self.ctr = 1
        self.tk_var = tk.StringVar()
        # self.tk_var.set("0")
        self.tk_tm = tk.StringVar()
        self.tk_dt = tk.StringVar()
        self.tk_ip = tk.StringVar()
        self.tk_ping = tk.StringVar()
        self.tk_us = tk.StringVar()
        self.tk_keyw = tk.StringVar()
        self.tk_us_on = tk.StringVar()
        self.froms = tk.StringVar()
        self.since = tk.StringVar()
        self.rating = tk.StringVar()
        self.review = tk.StringVar()
        self.response = tk.StringVar()
        self.last = tk.StringVar()
        self.tk_op1 = tk.StringVar()
        self.tk_op2 = tk.StringVar()
        self.tk_op3 = tk.StringVar()
        self.tk_op4 = tk.StringVar()
        self.tk_op5 = tk.StringVar()
        self.tk_op6 = tk.StringVar()

        lbl1 = tk.Label(text="G-Analytics", background=back, foreground="alice blue", font=("Comic Sans MS", 35))
        lbl1.place(x=450, y=30, anchor="center")
        lbl11 = tk.Label(text="Easy Way To Monetize Your GIG", background=back, foreground="cornsilk2",
                      font=("Arial Bold", 12))
        lbl11.place(x=450, y=70, anchor="center")
        lbl111 = tk.Label(
            text="------------------------------------------------------------------------ Script : V4 | Develop By : Sakibur Rahman ------------------------------------------------------------------------",
            background=back, foreground="cornsilk2", font=("", 10))
        lbl111.place(x=450, y=90, anchor="center")

        ########Clock########
        tme = tk.Label(self.win, textvariable=self.tk_tm, background=back, foreground="mint cream", font=("Burford", 10))
        tme.place(x=30, y=30, anchor="w")
        dte = tk.Label(textvariable=self.tk_dt, background=back, foreground="mint cream", font=("Burford", 10))
        dte.place(x=30, y=50, anchor="w")
        ########Clock########



        ########Ping########
        ipp = tk.Label(self.win, textvariable=self.tk_ip, background=back, foreground="mint cream", font=("Burford", 10))
        ipp.place(x=865, y=30, anchor="e")
        pngg = tk.Label(self.win, textvariable=self.tk_ping, background=back, foreground="mint cream", font=("Burford", 10))
        pngg.place(x=865, y=50, anchor="e")
        ########Ping########



        foreground = "SpringGreen2"

        result_json = open("data.json", "r")
        result = json.load(result_json)
        response = requests.get(result["us_img"])
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        panel = tk.Label(self.win, image=img)
        panel.place(x=110, y=190, bordermode="outside" , anchor="w")

        us = tk.Label(self.win, textvariable=self.tk_us, background=back, foreground=foreground, font=("Arial Bold", 30))
        us.place(x=190, y=186, anchor="w")


        line = tk.Label(self.win, textvariable=self.tk_us_on, background=back, foreground=foreground, font=("Segoe UI Emoji", 10))
        line.place(x=105, y=148, anchor="w")

        def hello():
            # from logging import root
            # from urllib.request import Request, urlopen
            # from bs4 import BeautifulSoup
            # import json
            # from tkinter import *
            # from tkinter import messagebox
            root = tk.Tk()
            root.geometry("400x200")
            root.resizable(False, False)
            root.resizable(0, 0)
            root.iconbitmap('favicon.ico')
            root.title("G-Analytics | Update Info")
            root.configure(background="black")

            def top():
                if entry1.get() == "":
                    messagebox.showerror("User Name", "User Name Not Found !")
                else:
                    if entry2.get() == "":
                        messagebox.showerror("Keyword", "Keyword  Not Found !")
                    else:
                        uuss = entry1.get()
                        url = "https://www.fiverr.com/" + uuss
                        req = Request(url, headers={
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                        webpage = urlopen(req).read()
                        html = webpage.decode("utf-8")
                        soup = BeautifulSoup(html, 'html.parser')

                        if uuss in html:
                            a_file = open("data.json", "r")
                            json_object = json.load(a_file)
                            a_file.close()

                            json_object["username"] = entry1.get()
                            json_object["keyword"] = entry2.get()

                            a_file = open("data.json", "w")
                            json.dump(json_object, a_file)
                            a_file.close()
                            root.destroy()
                        else:
                            messagebox.showerror("User Name",
                                                 '''User Name Not Found On Fiverr !
            Use Correct User Name.''')

            label1 = tk.Label(root, text="User Name : ", background="black", foreground="SpringGreen2",
                           font=("Arial Bold", 15))
            entry1 = tk.Entry(root, background="gray25", foreground="alice blue", font=("Arial Bold", 15))
            label2 = tk.Label(root, background="black", foreground="SpringGreen2", font=("Arial Bold", 15),
                           text="Keyword : ")
            entry2 = tk.Entry(root, background="gray25", foreground="alice blue", font=("Arial Bold", 15))
            button1 = tk.Button(root, background="gray25", foreground="HotPink1", text="Save", font=("Arial Bold", 15),
                             command=top)

            label1.place(x=10, y=50, anchor="w")
            entry1.place(x=390, y=50, anchor="e")
            label2.place(x=10, y=100, anchor="w")
            entry2.place(x=390, y=100, anchor="e")
            button1.place(x=200, y=150, anchor="center")

            root.mainloop()

        btntxt = '''Update
Info'''
        b = tk.Button(text=btntxt, fg="alice blue", bg=foreground, font=("Arial Bold" , 10), height=3, width=6,
                   command=hello)
        b.place(x=110, y=290, anchor="w")

        clk = tk.Label(self.win, text = "ↆ Click To", background=back, foreground=opt, font=("Segoe UI Emoji", 10))
        clk.place(x=105, y=248, anchor="w")

        key = tk.Label(self.win, textvariable=self.tk_keyw, background=back, foreground=foreground, font=("Arial Bold", 30))
        key.place(x=190, y=288, anchor="w")



        loc = tk.Label(self.win, textvariable=self.froms, background=back, foreground=foreground,
                       font=("Arial Bold", 12))
        loc.place(x=800, y=150, anchor="e")

        sins = tk.Label(self.win, textvariable=self.since, background=back, foreground=foreground,
                       font=("Arial Bold", 12))
        sins.place(x=800, y=180, anchor="e")


        rat = tk.Label(self.win, textvariable=self.rating, background=back, foreground=foreground,
                       font=("Arial Bold", 12))
        rat.place(x=800, y=210, anchor="e")


        rew = tk.Label(self.win, textvariable=self.review, background=back, foreground=foreground,
                       font=("Arial Bold", 12))
        rew.place(x=800, y=240, anchor="e")


        res = tk.Label(self.win, textvariable=self.response, background=back, foreground=foreground,
                       font=("Arial Bold", 12))
        res.place(x=800, y=270, anchor="e")


        lst = tk.Label(self.win, textvariable=self.last, background=back, foreground=foreground,
                       font=("Arial Bold", 12))
        lst.place(x=800, y=300, anchor="e")




        lbb = tk.Label(
            text="----------------------------------------------------------------------------          .          ----------------------------------------------------------------------------",
            background=back, foreground=foreground, font=("", 10))
        lbb.place(x=450, y=340, anchor="center")


        lab=tk.Label(self.win, textvariable=self.tk_var,
                       background=back, foreground=opt)
        lab.place(x=450, y=340, anchor="center")


        font_size = "Arial Bold", 20

        op1 = tk.Label(text="Best Selling - ", background=back, foreground=opt, font=(font_size))
        op1.place(x=100, y=370, anchor="w")
        op11 = tk.Label(self.win, textvariable=self.tk_op1, background=back, foreground=opt, font=(font_size))
        op11.place(x=800, y=370, anchor="e")

        op2 = tk.Label(text="Best Selling Online - ", background=back, foreground=opt, font=(font_size))
        op2.place(x=100, y=410, anchor="w")
        op22 = tk.Label(self.win, textvariable=self.tk_op2, background=back, foreground=opt, font=(font_size))
        op22.place(x=800, y=410, anchor="e")

        op3 = tk.Label(text="Relevance - ", background=back, foreground=opt, font=(font_size))
        op3.place(x=100, y=450, anchor="w")
        op3 = tk.Label(self.win, textvariable=self.tk_op3, background=back, foreground=opt, font=(font_size))
        op3.place(x=800, y=450, anchor="e")

        op4 = tk.Label(text="Relevance Online - ", background=back, foreground=opt, font=(font_size))
        op4.place(x=100, y=490, anchor="w")
        op4 = tk.Label(self.win, textvariable=self.tk_op4, background=back, foreground=opt, font=(font_size))
        op4.place(x=800, y=490, anchor="e")

        op5 = tk.Label(text="Newest Arrivals - ", background=back, foreground=opt, font=(font_size))
        op5.place(x=100, y=530, anchor="w")
        op55 = tk.Label(self.win, textvariable=self.tk_op5, background=back, foreground=opt, font=(font_size))
        op55.place(x=800, y=530, anchor="e")

        op6 = tk.Label(text="Newest Arrivals Online - ", background=back, foreground=opt, font=(font_size))
        op6.place(x=100, y=570, anchor="w")
        op66 = tk.Label(self.win, textvariable=self.tk_op6, background=back, foreground=opt, font=(font_size))
        op66.place(x=800, y=570, anchor="e")


        self.updater()
        self.win.mainloop()
#################################################################











    def updater(self):
        self.ctr +=1

        result_json = open("data.json", "r")
        result = json.load(result_json)

        self.tm = f"{dt.datetime.now():%I:%M %p %A}"
        self.tk_tm.set(str(self.tm))

        self.dt = f"{dt.datetime.now():%d %B(%m) %Y}"
        self.tk_dt.set(str(self.dt))


        self.ip = result["ip"] + " : IP"
        self.tk_ip.set(str(self.ip))

        self.ping = result["ping"] + " : Ping"
        self.tk_ping.set(str(self.ping))



        self.us = result["username"]
        self.tk_us.set(str(self.us))

        self.key = result["keyword"]
        self.tk_keyw.set(str(self.key))

        self.line = result["us_line"]
        self.tk_us_on.set(str(self.line))



        self.fromss = "From " + result["from"] + " ✈"
        self.froms.set(str(self.fromss))

        self.sincee = "Since " + result["since"] + " ⌛"
        self.since.set(str(self.sincee))

        self.ratingg = "Rating " + result["rating"] + " ★"
        self.rating.set(str(self.ratingg))

        self.revieww = "Review " + result["review"] + " 👍"
        self.review.set(str(self.revieww))

        self.responsee = "Response Time " + result["response"] + " ✉"
        self.response.set(str(self.responsee))

        self.lastt = "Last Delivery " + result["last"] + " 🎁"
        self.last.set(str(self.lastt))


        self.op1 = result["option1"]
        self.tk_op1.set(str(self.op1))

        self.op2 = result["option2"]
        self.tk_op2.set(str(self.op2))

        self.op3 = result["option3"]
        self.tk_op3.set(str(self.op3))

        self.op4 = result["option4"]
        self.tk_op4.set(str(self.op4))

        self.op5 = result["option5"]
        self.tk_op5.set(str(self.op5))

        self.op6 = result["option6"]
        self.tk_op6.set(str(self.op6))


        # self.new_st = "y65"
        # self.tk_var.set(str(self.new_st))

        self.ldigit = self.ctr%10

        if self.ldigit == 0:
            self.new_st = "⚫UPDATING⚪"
        if self.ldigit == 1:
            self.new_st = "⚪uPDATING⚪"
        if self.ldigit == 2:
            self.new_st = "⚪UpDATING⚪"
        if self.ldigit == 3:
            self.new_st = "⚪UPdATING⚪"
        if self.ldigit == 4:
            self.new_st = "⚪UPDaTING⚪"
        if self.ldigit == 5:
            self.new_st = "⚪UPDAtING⚪"
        if self.ldigit == 6:
            self.new_st = "⚪UPDATiNG⚪"
        if self.ldigit == 7:
            self.new_st = "⚪UPDATInG⚪"
        if self.ldigit == 8:
            self.new_st = "⚪UPDATINg⚪"
        if self.ldigit == 9:
            self.new_st = "⚪UPDATING⚫"

        self.tk_var.set(str(self.new_st))




        result_json.close()


##############################PING#############################
        if self.ctr == 5:
            result_json = open("data.json", "r")
            result = json.load(result_json)
            # result.close()

            ping = os.popen('ping ' + result["base"] + ' -n 5')
            result = ping.readlines()
            msLine = result[-1].strip()
            # print(msLine)
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            new1 = msLine.split()
            new2 = new1[-1]

            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            # print(json_object)

            json_object["ip"] = local_ip
            json_object["ping"] = new2

            a_file = open("data.json", "w")
            json.dump(json_object, a_file)
            a_file.close()


################################HADER##############################

        if self.ctr == 10:
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()

            username = json_object["username"].lower()
            url = "https://www.fiverr.com/" + username
            req = Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
            webpage = urlopen(req).read()
            html = webpage.decode("utf-8")
            soup = BeautifulSoup(html, 'html.parser')

            filter1 = soup.find('span', class_='seller-image')


            filter2 = filter1.find_all('img')
            for image in filter2:
                imsg = image['src']
                # print(image['alt'])

            online = filter1.find('span', class_='is-online')
            if online == None:
                active = "✖Offline"
            else:
                active = "✔Online"


            filter = soup.find('div', class_='grid-12')

            f_r = filter.find('b', class_="rating-score rating-num").contents[0:1]
            rating = str(f_r).split("'")[1]

            if "ratings-wrapper" in html:
                f_r = filter.find('b', class_="rating-score rating-num").contents[0:1]
                rating = str(f_r).split("'")[1]
                # print("Rating : " + rating)
                ###
                f_k = filter.find('span', class_="ratings-count rating-count").contents[2:3]
                review = str(f_k).split("'")[1]
                reviews = review.replace('reviews', '')
                # print("Reviews : " + reviews)
                ###
            else:
                reviews = "0"
                rating = "0"

            f_c = filter.find('li', class_="location")

            loc = (f_c.find('b').get_text())
            # print(loc)

            f_cc = filter.find('li', class_="member-since")

            sc = (f_cc.find('b').get_text())
            # print(sc)

            f_ccc = filter.find('li', class_="recent-delivery")

            scc = (f_ccc.find('strong').get_text())
            # print(scc)

            f_res = filter.find('li', class_="response-time")
            resp = (f_res.find('b').get_text())
            # print(resp)



            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            # print(json_object)

            json_object["us_img"] = imsg
            json_object["us_line"] = active
            json_object["from"] = loc
            json_object["since"] = sc
            json_object["review"] = reviews
            json_object["rating"] = rating
            json_object["response"] = resp
            json_object["last"] = scc

            a_file = open("data.json", "w")
            json.dump(json_object, a_file)
            a_file.close()




###########################OPTION1###################################

        if self.ctr == 20:
            base = "www.fiverr.com"
            host = "https://" + base + "/"
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            username = json_object["username"].lower()
            keyword = json_object["keyword"].lower().replace(' ', '%20')
            page = 1
            task = 1
            result = ""
            page_name = ""
            makeurl = host + "search/gigs?query=" + keyword + "&source=pagination&acmpl=1&search_in=everywhere&search-autocomplete-original-term=" + keyword + "&search-autocomplete-available=true&search-autocomplete-type=suggest&search-autocomplete-position=1&filter=rating&offset=-2&page="
            while task > 0:
                url = makeurl + str(page)
                req = Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                webpage = urlopen(req).read()
                html = webpage.decode("utf-8")
                soup = BeautifulSoup(html, 'html.parser')
                if username in html:
                    result = "page: " + str(page) + " found"
                    task = 0
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option1"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                else:
                    result = "page: " + str(page) + " not found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option1"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    time.sleep(2)
                    if page == 20:
                        task = 0
                    else:
                        page += 1


        ###########################OPTION2##################################
        if self.ctr == 30:

            base = "www.fiverr.com"
            host = "https://" + base + "/"
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            username = json_object["username"].lower()
            keyword = json_object["keyword"].lower().replace(' ', '%20')
            page = 1
            task = 1
            result = ""
            page_name = ""
            makeurl = host + "search/gigs?query=" + keyword + "&source=pagination&acmpl=1&search_in=everywhere&search-autocomplete-original-term=" + keyword + "&search-autocomplete-available=true&search-autocomplete-type=suggest&search-autocomplete-position=1&filter=rating&ref=is_seller_online%3Atrue&page="
            while task > 0:
                url = makeurl + str(page)
                req = Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                webpage = urlopen(req).read()
                html = webpage.decode("utf-8")
                soup = BeautifulSoup(html, 'html.parser')
                if username in html:
                    result = "page: " + str(page) + " found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option2"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    task = 0
                else:
                    result = "page: " + str(page) + " not found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option2"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    time.sleep(2)
                    if page == 20:
                        task = 0
                    else:
                        page += 1


        ###########################OPTION3##################################

        if self.ctr == 40:
            base = "www.fiverr.com"
            host = "https://" + base + "/"
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            username = json_object["username"].lower()
            keyword = json_object["keyword"].lower().replace(' ', '%20')
            page = 1
            task = 1
            result = ""
            page_name = ""
            makeurl = host + "search/gigs?query=" + keyword + "&source=pagination&acmpl=1&search_in=everywhere&search-autocomplete-original-term=" + keyword + "&search-autocomplete-available=true&search-autocomplete-type=suggest&search-autocomplete-position=1&filter=auto&page="
            while task > 0:
                url = makeurl + str(page)
                req = Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                webpage = urlopen(req).read()
                html = webpage.decode("utf-8")
                soup = BeautifulSoup(html, 'html.parser')
                if username in html:
                    result = "page: " + str(page) + " found"
                    task = 0
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option3"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()

                else:
                    result = "page: " + str(page) + " not found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option3"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    time.sleep(2)
                    if page == 20:
                        task = 0
                    else:
                        page += 1



        ###########################OPTION4##################################

        if self.ctr == 50:
            base = "www.fiverr.com"
            host = "https://" + base + "/"
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            username = json_object["username"].lower()
            keyword = json_object["keyword"].lower().replace(' ', '%20')
            page = 1
            task = 1
            result = ""
            page_name = "https://www.fiverr.com/search/gigs?query=photo%20retouch&source=toggle_filters&search_in=everywhere&search-autocomplete-original-term=photo%20retouch&filter=auto&offset=-7&ref=is_seller_online%3Atrue"
            makeurl = host + "search/gigs?query=" + keyword + "&source=toggle_filters&search_in=everywhere&search-autocomplete-original-term=" + keyword + "&filter=auto&offset=-7&ref=is_seller_online%3Atrue&page="
            while task > 0:
                url = makeurl + str(page)
                req = Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                webpage = urlopen(req).read()
                html = webpage.decode("utf-8")
                soup = BeautifulSoup(html, 'html.parser')
                if username in html:
                    result = "page: " + str(page) + " found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option4"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    task = 0

                else:
                    result = "page: " + str(page) + " not found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option4"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    time.sleep(2)
                    if page == 20:
                        task = 0
                    else:
                        page += 1


        ###########################OPTION5##################################

        if self.ctr == 60:

            base = "www.fiverr.com"
            host = "https://" + base + "/"
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            username = json_object["username"].lower()
            keyword = json_object["keyword"].lower().replace(' ', '%20')
            page = 1
            task = 1
            result = ""
            page_name = ""
            makeurl = host + "search/gigs?query=" + keyword + "&source=pagination&acmpl=1&search_in=everywhere&search-autocomplete-original-term=" + keyword + "&search-autocomplete-available=true&search-autocomplete-type=suggest&search-autocomplete-position=1&filter=new&offset=-2&page="
            while task > 0:
                url = makeurl + str(page)
                req = Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                webpage = urlopen(req).read()
                html = webpage.decode("utf-8")
                soup = BeautifulSoup(html, 'html.parser')
                if username in html:
                    result = "page: " + str(page) + " found"
                    task = 0
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option5"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                else:
                    result = "page: " + str(page) + " not found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option5"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    time.sleep(2)
                    if page == 20:
                        task = 0
                    else:
                        page += 1

        ###########################OPTION6##################################

        if self.ctr == 70:

            base = "www.fiverr.com"
            host = "https://" + base + "/"
            a_file = open("data.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            username = json_object["username"].lower()
            keyword = json_object["keyword"].lower().replace(' ', '%20')
            page = 1
            task = 1
            result = ""
            page_name = ""
            makeurl = host + "search/gigs?query=" + keyword + "&source=pagination&acmpl=1&search_in=everywhere&search-autocomplete-original-term=" + keyword + "&search-autocomplete-available=true&search-autocomplete-type=suggest&search-autocomplete-position=1&filter=new&offset=-2&ref=is_seller_online%3Atrue&page="
            while task > 0:
                url = makeurl + str(page)
                req = Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'})
                webpage = urlopen(req).read()
                html = webpage.decode("utf-8")
                soup = BeautifulSoup(html, 'html.parser')
                if username in html:
                    result = "page: " + str(page) + " found"
                    task = 0
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option6"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                else:
                    result = "page: " + str(page) + " not found"
                    a_file = open("data.json", "r")
                    json_object = json.load(a_file)
                    a_file.close()
                    json_object["option6"] = result
                    a_file = open("data.json", "w")
                    json.dump(json_object, a_file)
                    a_file.close()
                    time.sleep(2)
                    if page == 20:
                        task = 0
                    else:
                        page += 1

        ###########################OP##################################

        if self.ctr == 75:
            self.ctr = 1


        if self.ctr < 100:
            self.win.after(1234, self.updater)
        else:
            self.win.quit()
            exit()

UL=UpdateLabel()
exit()