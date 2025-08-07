import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3

engine = pyttsx3.init()

language_dict = GoogleTranslator(source='auto', target='english').get_supported_languages(as_dict=True)
language_list = list(language_dict.values())

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x400")
root.resizable(False, False)

def translate_text():
    try:
        src_lang = source_lang_combo.get().lower()
        dest_lang = target_lang_combo.get().lower()
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def speak_text():
    try:
        text = output_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Speak Error", "No text to speak.")
            return
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("TTS Error", str(e))

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

tk.Label(root, text="Enter text:", font=("Arial", 12)).pack()
input_text = tk.Text(root, height=5, width=70)
input_text.pack(pady=5)

lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

tk.Label(lang_frame, text="From:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
source_lang_combo = ttk.Combobox(lang_frame, values=language_list, width=25)
source_lang_combo.set("english")
source_lang_combo.grid(row=0, column=1)

tk.Label(lang_frame, text="To:", font=("Arial", 10)).grid(row=0, column=2, padx=5)
target_lang_combo = ttk.Combobox(lang_frame, values=language_list, width=25)
target_lang_combo.set("tamil")
target_lang_combo.grid(row=0, column=3)

translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="green", fg="white", font=("Arial", 12))
translate_btn.pack(pady=10)

tk.Label(root, text="Translated text:", font=("Arial", 12)).pack()
output_text = tk.Text(root, height=5, width=70)
output_text.pack(pady=5)

opt_frame = tk.Frame(root)
opt_frame.pack(pady=10)

tk.Button(opt_frame, text="🔊 Speak", command=speak_text).grid(row=0, column=0, padx=10)
tk.Button(opt_frame, text="📋 Copy", command=copy_text).grid(row=0, column=1, padx=10)

# Run GUI loop
root.mainloop()

