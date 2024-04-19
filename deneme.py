from tkinter import *
import random
from PIL import Image, ImageTk


class TypingSpeed:
  def __init__(self):
      self.window = Tk()
      self.window.title("Typing Speed")
      self.window.config(pady=40, padx=30, bg="#B1DDC6")
      self.canvas = Canvas(width=800, height=526)
      self.button = Button(text="Start Game")
      self.canvas.config(bg="#B1DDC6", highlightthickness=0)
      self.canvas.grid(row=0, column=0, columnspan=2)
      button_image = Image.open('./images/images.png')
      new_img = ImageTk.PhotoImage(button_image)
      self.label = self.canvas.create_text(400,50,text="Welcome to the Typing Speed Test",font=("Arial",30))
      self.button = Button(
        image=new_img,text="Start Game",
        command=lambda:[self.start_typing(),self.button.destroy(),self.canvas.delete(self.label)],
        highlightthickness=0,
        borderwidth=2,
        bg="#B1DDC6")
      self.button.grid(row=0,column=0,columnspan=2)
      self.window.mainloop()

  def start_typing(self):
      self.total_word = 1
      self.true_words = 0
      self.false_words = 0
      with open("wordlist.10000.txt") as file:
        words = file.readlines()
        self.clean_words = [word.replace("\n", " ") for word in words]
      self.word = self.canvas.create_text(400, 150, text="", font=("Arial", 40, "bold"))
      self.score_text = self.canvas.create_text(700, 30, text="Score: 0", font=("Arial", 30))
      self.take_word()
      self.enter_word()
      self.window.after(ms=1000,func=self.countdown(60))
      
  
  def countdown(self, remaining):
    if remaining <= 0:
        self.canvas.delete("timer_text")
        self.canvas.delete("all")
        self.entry.grid_forget()
        image = Image.open("images/10.jpeg")
        new_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(400, 263, image=new_image)
        self.canvas.create_text(100, 60, text="Time's up!", font=("Arial", 13,"bold"), tag="timer_text",fill="white")
        self.canvas.create_text(700, 60, text=f"Total word: {self.total_word}",font=("Arial",13,"bold"),fill="white")
        self.canvas.create_text(700, 80, text=f"True words: {self.true_words}", font=("Arial", 13,"bold"),fill="white")
        self.canvas.create_text(700, 100, text=f"False words: {self.false_words}", font=("Arial", 13,"bold"),fill="white")
        self.canvas.create_text(400,400,text=f"You knew %{self.true_words/self.total_word*100:.2f} of words", font=("Arial", 13,"bold"),fill="white")
        self.button = Button("")
    else:
        self.canvas.delete("timer_text")
        self.canvas.create_text(400, 40, text=remaining, font=("Arial", 30), tag="timer_text")
        self.window.after(1000, lambda: self.countdown(remaining-1))
      
  def take_word(self):
    self.random_word = random.choice(self.clean_words)
    self.canvas.itemconfig(self.word, text=self.random_word, fill="black")

  def enter_word(self):
    self.entry = Entry(width=50,font=("Arial",17))
    self.entry.grid(row=0, column=0, columnspan=2)
    self.entry.bind("<Return>", self.check_word)

  def check_word(self, event):
    entered_word = event.widget.get()
    if entered_word.strip() == self.random_word.strip():
        self.update_score(True)
    else:
        self.update_score(False)
    self.take_word()
    self.entry.delete(0, END)
    self.total_word += 1
      

  def update_score(self, situation):
    current_score = int(self.canvas.itemcget(self.score_text, "text").split(":")[-1].strip())
    if situation:
      new_score = current_score + 1
      self.true_words += 1
    else:
      new_score = current_score - 1
      self.false_words += 1
    self.canvas.itemconfig(self.score_text, text=f"Score: {new_score}")


typingspeed = TypingSpeed()
