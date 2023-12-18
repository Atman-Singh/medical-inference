import requests
import json
import tkinter as tk
import customtkinter as ctk
from config import url
import colors


def main():

    win = tk.Tk()
    win.state('zoomed')

    title_label = ctk.CTkLabel(master=win, text='Ask a Medically Related Question', text_color=colors.text, font=("Lato", 70))
    title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    entry = ctk.CTkEntry(master=win, width=1000, height=50, corner_radius=10, fg_color=colors.hover, text_color=colors.entry_text, font=("Lato", 20))
    entry.place(relx=0.5, rely=0.28, anchor=tk.CENTER)

    response_label = ctk.CTkLabel(master=win, text='', text_color=colors.text, font=("Lato", 45), wraplength=1000)
    response_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    get_response_button = create_button(win, "Get Response", 100, 60, command=lambda: display_response(response_label, entry))
    get_response_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    win.mainloop()


def create_button(self, text, width, height, command):
    return ctk.CTkButton(
        master=self,
        text=text,
        width=width,
        height=height,
        corner_radius=10,
        command=command,
        fg_color=colors.button_fg,
        hover_color=colors.hover,
        text_color=colors.text,
        font=("Lato", height / 2 + 5))


def display_response(label, entry):
    label.configure(text=get_response(entry.get()), justify='center')


def get_response(question):
    data = {"inputs": question}
    data_json = json.dumps(data)
    output = requests.post(url, data=data_json)
    for output in output.json():
        return output['generated_text'][len(question) + 1:]


def remove_question(question, output):
    return output[len(question)+1:]


if __name__ == '__main__':
    main()
