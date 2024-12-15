from tkinter import *
from gtts import gTTS
import os
saved_text = ""

def set_text():
    global saved_text
    saved_text = entry.get("1.0", "end-1c")
    if saved_text.strip():
        status_label.config(text="Text saved successfully!")
    else:
        status_label.config(text="Please enter some text.")

def text_to_speech():
    global saved_text
    if saved_text.strip():
        tts = gTTS(text=saved_text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3") 
        status_label.config(text="Playing the saved text...")
    else:
        status_label.config(text="No text has been set. Please use 'Set'.")

def exit_program():
    root.destroy()

root = Tk()
root.title("Text to Speech")
root.geometry("500x400") 
root.config(bg="#e8f0f2")  # خلفية بلون أزرق فاتح مائل للرمادي

title_label = Label(root, text="Text to Speech", font=("Arial", 18, "bold"), bg="#e8f0f2", fg="#2d6187")  # نص بلون أزرق غامق
title_label.pack(pady=10)

entry_frame = Frame(root, bg="#e8f0f2")
entry_frame.pack(pady=10)
entry_label = Label(entry_frame, text="Enter your text:", font=("Arial", 16), bg="#e8f0f2", fg="#2d6187")  # لون مشابه للعنوان
entry_label.pack(side=LEFT, padx=5)
entry = Text(entry_frame, height=5, width=40, font=("Arial", 12), bg="#ffffff", fg="#333333", insertbackground="#2d6187")  # خلفية بيضاء للنص ولون رمادي للنص
entry.pack(side=LEFT)

button_frame = Frame(root, bg="#e8f0f2")
button_frame.pack(pady=20)

set_button = Button(button_frame, text="Set", command=set_text, font=("Arial", 12, "bold"), bg="#4caf50", fg="white", width=10, height=2)  # أخضر للأزرار
set_button.grid(row=0, column=0, padx=10)

play_button = Button(button_frame, text="Play", command=text_to_speech, font=("Arial", 12, "bold"), bg="#2196f3", fg="white", width=10, height=2)  # أزرق ساطع
play_button.grid(row=0, column=1, padx=10)

exit_button = Button(button_frame, text="Exit", command=exit_program, font=("Arial", 12, "bold"), bg="#f44336", fg="white", width=10, height=2)  # أحمر للخروج
exit_button.grid(row=0, column=2, padx=10)

status_label = Label(root, text="", font=("Arial", 10), fg="#2d6187", bg="#e8f0f2")  # لون متناسق مع العنوان
status_label.pack(pady=10)

root.mainloop()
