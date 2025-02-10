from tkinter import *
import pandas as pd
from random import *

from packaging.utils import canonicalize_version

#-----------------------------------CONSTANTS---------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"

#-------------------------------------FILE HANDLING-----------------------------------
try:
    df1 = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("../flash-card-project-start/data/french_words.csv")
    words_dictionary = df.to_dict(orient="records")
except pd.errors.EmptyDataError:
    print("Error >> No data present in CSV File.....")
except Exception as e:
    print(f"Error: {e}")
else:
    words_dictionary = df1.to_dict(orient="records")
#----------------------------------NEXT FRENCH CARD GENERATOR MECHANISM----------------------

def french_card_generator():
    global random_dict, card_change
    windows.after_cancel(card_change)
    random_dict = choice(words_dictionary)
    word = random_dict.get("French")
    canvas.itemconfig(card_front, image = card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=word, fill="black")

    card_change = windows.after(3000,english_card_generator)




#------------------------ENGLISH CARD SWITCH FUNCTION-------------------------------------------
def english_card_generator():
    eng_word = random_dict.get("English")
    canvas.itemconfig(card_front, image= card_back_image)
    canvas.itemconfig(card_title, text = "English", fill= "white")
    canvas.itemconfig(card_word, text=eng_word, fill= "white")


#------------------------SAVING YOUR PROGRESS----------------------------------------------------
def saving_progress():
    """Function to remove words from deck that the user already knows"""
    words_dictionary.remove(random_dict)
    df2 = pd.DataFrame(words_dictionary)
    df2.to_csv("words-to_learn.csv", index= False)




#----------------------------------------UI SETUP------------------------------------------------
windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg = BACKGROUND_COLOR)
card_change = windows.after(3000,english_card_generator)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg =BACKGROUND_COLOR)
card_front_image = PhotoImage(file="../flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="../flash-card-project-start/images/card_back.png")


card_front = canvas.create_image(400, 263,image= card_front_image)
card_title = canvas.create_text(400,150, text="title", fill="black", font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263, text ="word", fill = "black", font = ("Arial",60,"bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

#-----------------------------------BUTTONS----------------------------------------------
right_image = PhotoImage(file="../flash-card-project-start/images/right.png")
checkmark_button = Button(image=right_image, highlightthickness=0, command= lambda:[saving_progress(), french_card_generator()])
checkmark_button.grid(row=1, column = 1)

wrong_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
cross_button = Button(image=wrong_image, highlightthickness=0, command=french_card_generator)
cross_button.grid(row=1, column = 0)


french_card_generator()




























windows.mainloop()
