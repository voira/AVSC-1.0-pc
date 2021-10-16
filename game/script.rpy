# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vena")

default preferences.text_cps = 30

init python:
    your_new_encyclopaedia = Encyclopaedia()


# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    stop music fadeout 1.0

    call prologue from _call_prologue

    scene blackscreen with fade

    pause 3.0


    menu:
        "Choose a character."

        "Vena":
            jump venaprologue

        "Haru":
            jump haruprologue



    # These display lines of dialogue.


    # This ends the game.

    return
