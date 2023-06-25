from tkinter import messagebox
print("Hello, welcome to my message box creator!")
while True:
    print("What would your message box like to be today?")
    print("------Information message box------")
    print("1. Information message box")
    print("------Warning message boxes------")
    print("2. Warning message box")
    print("3. Error message box")
    print("------Question message boxes------")
    print("4. Question message box")
    print("5. An 'ok|cancel' messagebox")
    print("6. A 'retry|cancel' messagebox")
    print("7. A 'yes|no|cancel' messagebox")
    print("(Remember, the messageboxes don't have any actions.)")
    try:
        question = int(input("Choose one of them: "))
        if question == 1:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.showinfo(title, message)
        elif question == 2:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.showwarning(title, message)
        elif question == 3:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.showerror(title, message)
        elif question == 4:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.askquestion(title, message)
        elif question == 5:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.askokcancel(title, message)
        elif question == 6:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.askretrycancel(title, message)
        elif question == 7:
            title = input("What will be the title be? ")
            message = input("What will the message be? ")
            messagebox.askyesnocancel(title, message)
    except:
        print("Invalid number.")
    
    next_one = input("Next one? (y/n) ")
    if next_one == "y":
        continue
    elif next_one == "n":
        break
    else:
        print("Don't press other keys (make sure 'y' or 'n' are lowercase).")