import openai
import customtkinter as ctk

openai.api_key = "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"
assistant_id = "asst_UykKnPSqB5PuDnHoZNPU1rbO"

# GUI-Setup
main = ctk.CTk()
main.geometry("800x600")
main.resizable(False, False)

font_cosmica = ("Cosmica", 20, "bold")
ctk.set_default_color_theme("Blue.json")

# Chat-Funktion
def answer():
    chat_box.configure(state="normal")  # Setze den Zustand auf normal, um den Text hinzuzufügen
    chat_box.delete("1.0", "end")
    user_input = chat_entry.get()
    my_run_id, my_thread_id = create_thread(assistant_id, f"[topic]: {user_input}")
    check_status_periodically(my_run_id, my_thread_id)

# Thread erstellen
def create_thread(ass_id, prompt):
    thread = openai.beta.threads.create()
    my_thread_id = thread.id
    message = openai.beta.threads.messages.create(
        thread_id=my_thread_id,
        role="user",
        content=prompt
    )
    run = openai.beta.threads.runs.create(
        thread_id=my_thread_id,
        assistant_id=ass_id,
    )
    return run.id, my_thread_id

# Status periodisch überprüfen
def check_status_periodically(run_id, thread_id):
    status = check_status(run_id, thread_id)
    if status != "completed":
        main.after(1000, check_status_periodically, run_id, thread_id)  # Nach 1 Sekunde erneut überprüfen
    else:
        response = openai.beta.threads.messages.list(thread_id=thread_id)
        if response.data:
            resp = str(response.data[0].content[0].text.value)
            chat_box.insert("1.0", resp)
            chat_box.configure(state="disabled")  # Setze den Zustand wieder auf deaktiviert

# Status überprüfen
def check_status(run_id, thread_id):
    run = openai.beta.threads.runs.retrieve(
        thread_id=thread_id,
        run_id=run_id,
    )
    return run.status

# Tabs
textbot = ctk.CTkTabview(master=main, width=740, height=570)
textbot.pack(padx=5, pady=5)
textbot.add("Textbot")

# Entryboxes
chat_entry = ctk.CTkEntry(textbot.tab("Textbot"), width=400, height=45, font=font_cosmica)
chat_entry.pack(pady=30, side="bottom")

# Buttons
send_button = ctk.CTkButton(textbot.tab("Textbot"), text="🡑", width=45, height=45, font=font_cosmica, command=answer)
send_button.place(x=570, y=447)

# Label
chat_box = ctk.CTkTextbox(textbot.tab("Textbot"), width=400, height=500)
chat_box.pack()

main.mainloop()