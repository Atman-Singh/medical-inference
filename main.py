import requests
import json
import tkinter as tk
import customtkinter as ctk
from config import url
import colors

# displays user interface and connects it to API
def main():
    # create user interface window, open maximized by default
    win = tk.Tk()
    win.state('zoomed')

    # title text
    title_label = ctk.CTkLabel(master=win, text='Ask a Medically Related Question', text_color=colors.text, font=("Lato", 70))
    title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    # user input box for user to ask question
    entry = ctk.CTkEntry(master=win, width=1000, height=50, corner_radius=10, fg_color=colors.hover, text_color=colors.entry_text, font=("Lato", 20))
    entry.place(relx=0.5, rely=0.28, anchor=tk.CENTER)

    # text box that displays the model's answer when receieved
    response_label = ctk.CTkLabel(master=win, text='', text_color=colors.text, font=("Lato", 25), wraplength=700)
    response_label.place(relx=0.5, rely=0.4, anchor=tk.N)

    # button that user can press to prompt a response
    get_response_button = create_button(win, "Get Response", 100, 60, command=lambda: display_response(response_label, entry))
    get_response_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    win.mainloop()


# creates button according to project's styling rules
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


# prints model's response to console and updates response_label to display response
def display_response(label, entry):
    response = get_response(entry.get())
    print(response)
    label.configure(text=response, justify='center')


# posts json data to api to invoke a response
def get_response(question):
    # this prompt ensures that the model responds in english and does not overflow the screen with text
    prompt = "Answer the following question in English and in a 100 word paragraph. " + question

    # parameters tuned to recieve accurate and concise result
    data = {
        "inputs": prompt,
        "parameters": {
            "do_sample": True,
            "top_p": 0.6,
            "temperature": 0.9,
            "top_k": 50,
            "max_new_tokens": 512,
            "stop": ["</s>"]
        }
    }

    # post json to api and return response without the original question
    data_json = json.dumps(data)
    output = requests.post(url, data=data_json)
    return output.json()[0]['generated_text'][len(prompt)+1:]


if __name__ == '__main__':
    main()
