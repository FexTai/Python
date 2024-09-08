import openai
import customtkinter
import time

openai.api_key = "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"
assistant_id = "asst_UykKnPSqB5PuDnHoZNPU1rbO"
resp = ""

# chatbot

# Fenstereinstellungen
main = customtkinter.CTk()
main.geometry("800x600")
main.resizable(False, False)

font_cosmica = ("Cosmica", 20, "bold")
customtkinter.set_default_color_theme("Blue.json")


def answer():
    chat_box.delete("0.0", "end")
    global resp
    def create_thread(ass_id, prompt):
        thread = openai.beta.threads.create()
        my_thread_id = thread.id
        #create a message
        message = openai.beta.threads.messages.create(
            thread_id=my_thread_id,
            role="user",
            content=prompt
        )
        #run
        run = openai.beta.threads.runs.create(
            thread_id=my_thread_id,
            assistant_id=ass_id,
        )
        return run.id, thread.id


    def check_status(run_id, thread_id):
        run = openai.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id,
        )
        return run.status

    user_input = chat_entry.get()
    my_run_id, my_thread_id = create_thread(assistant_id, f"[topic]: {user_input}")
    status = check_status(my_run_id, my_thread_id)
    while (status != "completed"):
        status = check_status(my_run_id, my_thread_id)
        time.sleep(2)
    response = openai.beta.threads.messages.list(
    thread_id=my_thread_id
    )
    if response.data:
        resp = str(response.data[0].content[0].text.value)
        chat_box.insert("0.0", resp)
        chat_box.configure(state="disabled")
        chat_box.pack()




# Tabs
textbot = customtkinter.CTkTabview(master=main,
                                   width=740, height=570,
                                   #segmented_button_fg_color="#e74c3c",
                                   #segmented_button_selected_color="white",
                                   #segmented_button_unselected_color="white",
                                   #text_color="black"
                                   )
textbot.pack(padx=5, pady=5)
textbot.add("Textbot")
textbot.add("Imagebot")


# Entryboxes
chat_entry = customtkinter.CTkEntry(textbot.tab("Textbot"), width=400, height=45,
                                    font=font_cosmica)
chat_entry.pack(pady=30, side="bottom")


# Buttons
send_button = customtkinter.CTkButton(textbot.tab("Textbot"), text="🡑", width=45, height=45,
                                      font=font_cosmica,
                                      command=answer
                                      )
send_button.place(x=570, y=447)


# Label
chat_box = customtkinter.CTkTextbox(textbot.tab("Textbot"), width=400, height=500)

main.mainloop()
