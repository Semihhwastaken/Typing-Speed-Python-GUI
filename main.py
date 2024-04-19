from tkinter import *
class TypingSpeed(Tk):
  def __init__(self):
    super().__init__()
    self.title = "Typing Speed"
    self.geometry("500x500")
    self.canvas = Canvas(master=self,width=500,height=500)
    self.canvas.pack()
    self.user_interface()
  def take_letters(self):
    with open("wordlist.10000.txt") as file:
      words = file.readlines()
    
    clean_words = [word.replace("\n"," ") for word in words]
    
    return clean_words

  def user_interface(self):
    self.canvas.create_text(250,30,text="Enter the words",fill="black",font=("Arial 30 bold"))
    self.canvas.pack()
  
  def update(self):
    
    




def main():
  ts = TypingSpeed()
  ts.mainloop()

if __name__ == "__main__":
  main()