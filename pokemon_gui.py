#josh was not here
try:
    import random
    from tkinter import *
    
    # u need to initiate a function that let you input pokemon
    # into slots, and then when you press a button they appear on the gui

    #create the widget
    my_s = Tk()
    my_s.minsize(height=300, width=100)
    my_s.config(padx=20, pady=20, bg="#b2eded")
    cool_icon = random.choice(["\u042F", "\u041F"])
    my_s.title(f"{cool_icon} redmans pokemon tool v0 {cool_icon}")


    #give widget labels, text inputs && buttons

    opening_label = Label(text=f"{cool_icon} redmans poketool v0 {cool_icon}")
    opening_label.config(padx=15, pady=15, font=("halvetica", 24, "italic"), bg="#b2eded")
    opening_label.pack()

    #pokemon one
    label_one = Label(bg="#e0115f", text=".pokemon one ..")
    label_one.config(padx=15,pady=15)
    label_one.pack()
    #Entry for this label
    #create entry
    entry_one = Entry(width=50)
    entry_one.config(bg="#fffffa")
    entry_one.insert(END, string=".enter pokemon one...")
    entry_one.pack(padx=14,pady=14)

    #pokemon two
    label_two = Label(bg="#e0115f", text=".pokemon two ..")
    label_two.config(padx=15,pady=15)
    label_two.pack()
    #Entry for this label
    #create entry
    entry_two = Entry(width=50)
    entry_two.config(bg="#fffffa")
    entry_two.insert(END, string="enter pokemon two...")
    entry_two.pack(padx=14,pady=14)
    

    #pokemon three
    label_three = Label(bg="#e0115f", text=".pokemon three ..")
    label_three.config(padx=15,pady=15)
    label_three.pack()
    #Entry for this label
    #create entry
    entry_three = Entry(width=50)
    entry_three.config(bg="#fffffa")
    entry_three.insert(END, string="enter pokemon three...")
    entry_three.pack(padx=14,pady=14)

    #pokemon four
    label_four = Label(bg="#e0115f", text=".pokemon four ..")
    label_four.config(padx=15,pady=15)
    label_four.pack()
    #Entry for this label
    #create entry
    entry_four = Entry(width=50)
    entry_four.config(bg="#fffffa")
    entry_four.insert(END, string="enter pokemon four...")
    entry_four.pack(padx=14,pady=14)

    #pokemon five
    label_five = Label(bg="#e0115f", text=".pokemon five ..")
    label_five.config(padx=15,pady=15)
    label_five.pack()
    #Entry for this label
    #create entry
    entry_five = Entry(width=50)
    entry_five.config(bg="#fffffa")
    entry_five.insert(END, string="enter pokemon five...")
    entry_five.pack(padx=14,pady=14)
    #pokemon six
    label_six = Label(bg="#e0115f", text=".pokemon six ..")
    label_six.config(padx=15,pady=15)
    label_six.pack()
    #Entry for this label
    #create entry
    entry_six = Entry(width=50)
    entry_six.config(bg="#fffffa")
    entry_six.insert(END, string="enter pokemon six...")
    entry_six.pack(padx=14,pady=14)


    #create listener
    def button_press():
        print("u just clicke a virus")
        if label_one:
            label_one.config(text=entry_one.get())
        if label_two:
            label_two.config(text=entry_two.get())
        if label_three:
            label_three.config(text=entry_three.get())
        if label_four:
            label_four.config(text=entry_four.get())
        
        if label_five:
            label_five.config(text=entry_five.get())
        if label_six:
            label_six.config(text=entry_six.get())
        else:
            opening_label.config(text=f"{cool_icon} import your six pokemon {cool_icon}")

    #give widget button
    button = Button(text="submit", command=button_press)
    button.config(padx=13,pady=13)
    button.pack()

    my_s.mainloop()
    #initiate mainloop
except KeyboardInterrupt:
    print(f"{cool_icon} bye {cool_icon}")
    quit()