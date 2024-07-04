import customtkinter
from datetime import datetime


time = str(datetime.now())


def click_handler():
    text_get = f"{textbox.get('0.0', 'end')}"
    print(f"text has been received as: {text_get}")
    with open(r'save_log.txt', 'a') as f:
        f.write(f"\n {time}, {text_get}")
    with open(r'last_save_log.txt', 'w') as f:
        f.write(text_get)

def load_last_save_file():
    with open(r'last_save_log.txt', 'r') as f:
        a= f.read()
        print(a)
        textbox.insert('end',text=a)

def load_log_file():
    with open(r'save_log.txt', 'r') as f:
        a= f.read()
        print(a)
        textbox.insert('end',text=a)

app = customtkinter.CTk()
app.geometry("350x400")

customtkinter.set_appearance_mode("system")

dictionary = customtkinter.CTkLabel(app, text="Small Wish-/Todolist", font=("Arial",15))
dictionary.pack(padx=20, pady=0)

textbox = customtkinter.CTkTextbox(app, scrollbar_button_color="#e6e6fa", corner_radius=16, width=300, border_color="#872657", border_width=2)
textbox.pack(padx=20, pady=5)



write_button = customtkinter.CTkButton(app, text="Save list", font=("Arial",12), command=click_handler, fg_color="#872657")
write_button.pack(padx=20, pady=5)

read_last_list_button = customtkinter.CTkButton(app, text="Read last List", font=("Arial",12), command=load_last_save_file, fg_color="#872657")
read_last_list_button.pack(padx=20, pady=5)

read_everything_button = customtkinter.CTkButton(app, text="Read everything", font=("Arial", 12), command=load_log_file, fg_color="#872657")
read_everything_button.pack(padx=20, pady=5)

app.mainloop()