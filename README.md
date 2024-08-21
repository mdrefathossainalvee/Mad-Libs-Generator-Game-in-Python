# Python Mad Libs Generator Game

Welcome to the **Python Mad Libs Generator Game**! This project is a fun way to generate and play Mad Libs using Python and Tkinter. Dive into the world of creative storytelling and enjoy filling in the blanks to create hilarious and memorable stories.

## About the Project

Mad Libs is a popular word game where players fill in blanks with random words to complete a story. Without knowing the context, you add words, and the story comes to life with a humorous twist. This project allows you to play Mad Libs with a simple graphical user interface (GUI) built using Tkinter.

## Project Prerequisites

To successfully run this project, you need to have:

- Basic knowledge of Python functions
- Basic understanding of Tkinter for creating GUIs

### Installation

To get started, you need to install the Tkinter module. You can install it using pip:

```bash
pip install tk
```

## Project Structure

The project consists of the following steps:

1. **Installing Tkinter**: Ensure Tkinter is installed to create the GUI.
2. **Initializing the Window**: Set up the main window for the game.
3. **Creating Functions**: Develop functions to generate different Mad Libs stories.
4. **Creating Buttons**: Add buttons to the GUI for users to select and generate stories.

### Step 1: Installing Tkinter

Tkinter is a GUI toolkit in Python. It's simple and fast to create graphical applications. Install Tkinter with the following command:

```bash
pip install tk
```

### Step 2: Initializing the Window

Create the main window for the game:

```python
from tkinter import *

Screen = Tk()
Screen.title("Mad Libs Generator")
Screen.geometry('400x400')
Screen.config(bg="pink")

Label(Screen, text='Mad Libs Generator', font=("Times New Roman", 16)).place(x=100, y=20)

# Creating buttons
Story1Button = Button(Screen, text='A Memorable Day', font=("Times New Roman", 13), command=lambda: Story1(Screen), bg='Blue')
Story1Button.place(x=140, y=90)

Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13), command=lambda: Story2(Screen), bg='Blue')
Story2Button.place(x=150, y=150)

Screen.mainloop()
```

### Step 3: Creating Functions

**Function for the First Story**:

```python
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
```

**Function for the Second Story**:

```python
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
```

## Project Output

Once the code is run, a window will pop up where you can choose between two stories: "A Memorable Day" and "Ambitions". After filling in the blanks, your personalized story will be displayed.
