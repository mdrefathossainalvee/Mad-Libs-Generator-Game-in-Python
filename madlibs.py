from tkinter import *

# Initialize the main window
Screen = Tk()
Screen.title("Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="pink")

Label(Screen, text='Mad Libs Generator', font=("Times New Roman", 16)).place(x=100, y=20)

# Function for the first story
def Story1(win):
    def final(tl, name, game, city, player, drink, snack):
        text = f'''
        One day, my friend {name} and I decided to play {game} in {city}.
        We watched our favorite player, {player}, while enjoying {drink} and {snack}.
        It was an amazing day, and we can't wait to do it again!
        '''
        tl.geometry('500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='yellow')
    NewScreen.title("A Memorable Day")
    NewScreen.geometry('500x500')

    Label(NewScreen, text='Memorable Day').place(x=100, y=0)
    Label(NewScreen, text='Name:').place(x=0, y=35)
    Label(NewScreen, text='Enter a game:').place(x=0, y=70)
    Label(NewScreen, text='Enter a city:').place(x=0, y=110)
    Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
    Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
    Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)

    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    game = Entry(NewScreen, width=17)
    game.place(x=250, y=70)
    city = Entry(NewScreen, width=17)
    city.place(x=250, y=110)
    player = Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = Entry(NewScreen, width=17)
    snack.place(x=250, y=230)

    SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda: final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)

    NewScreen.mainloop()

# Function for the second story
def Story2(win):
    def final(tl, profession, noun, feeling, emotion, verb):
        text = f'''
        I dream of becoming a {profession}. 
        Sometimes, I imagine holding a {noun} while feeling {feeling}.
        It's an emotion that makes me want to {verb} every day.
        '''
        tl.geometry('500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width()).place(x=160, y=310)
        Label(tl, text=text, wraplength=tl.winfo_width()).place(x=0, y=330)

    NewScreen = Toplevel(win, bg='red')
    NewScreen.title("Ambitions")
    NewScreen.geometry('500x500')

    Label(NewScreen, text='Ambitions').place(x=150, y=0)
    Label(NewScreen, text='Enter a profession:').place(x=0, y=35)
    Label(NewScreen, text='Enter a noun:').place(x=0, y=70)
    Label(NewScreen, text='Enter a feeling:').place(x=0, y=110)
    Label(NewScreen, text='Enter an emotion:').place(x=0, y=150)
    Label(NewScreen, text='Enter a verb:').place(x=0, y=190)

    profession = Entry(NewScreen, width=17)
    profession.place(x=250, y=35)
    noun = Entry(NewScreen, width=17)
    noun.place(x=250, y=70)
    feeling = Entry(NewScreen, width=17)
    feeling.place(x=250, y=110)
    emotion = Entry(NewScreen, width=17)
    emotion.place(x=250, y=150)
    verb = Entry(NewScreen, width=17)
    verb.place(x=250, y=190)

    SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda: final(NewScreen, profession.get(), noun.get(), feeling.get(), emotion.get(), verb.get()))
    SubmitButton.place(x=150, y=270)

    NewScreen.mainloop()

# Creating buttons for stories
Story1Button = Button(Screen, text='A Memorable Day', font=("Times New Roman", 13), command=lambda: Story1(Screen), bg='Blue')
Story1Button.place(x=140, y=90)

Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13), command=lambda: Story2(Screen), bg='Blue')
Story2Button.place(x=150, y=150)

Screen.mainloop()
