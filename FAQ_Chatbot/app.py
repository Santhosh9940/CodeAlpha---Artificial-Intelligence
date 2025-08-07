import tkinter as tk
from tkinter import scrolledtext
import json
import os
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load FAQ data
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "faq.json")

with open(file_path, "r", encoding="utf-8") as f:
    faq_data = json.load(f)
# Preprocess questions
faq_questions = [nlp(faq["question"]) for faq in faq_data]

def get_answer(user_input):
    user_doc = nlp(user_input)
    similarities = [user_doc.similarity(faq_q) for faq_q in faq_questions]
    best_match_index = similarities.index(max(similarities))
    return faq_data[best_match_index]["answer"]

# GUI setup
def send_message():
    user_input = user_entry.get()
    if not user_input.strip():
        return
    chat_window.config(state='normal')
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = get_answer(user_input)
    chat_window.insert(tk.END, "Bot: " + response + "\n\n")
    chat_window.config(state='disabled')
    user_entry.delete(0, tk.END)

app = tk.Tk()
app.title("FAQ Chatbot using spaCy")

chat_window = scrolledtext.ScrolledText(app, wrap=tk.WORD, state='disabled', width=60, height=20)
chat_window.pack(padx=10, pady=10)

user_entry = tk.Entry(app, width=50)
user_entry.pack(padx=10, pady=(0, 10), side=tk.LEFT)

send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(padx=(0,10), pady=(0, 10), side=tk.LEFT)

app.mainloop()
