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


    "Choose a character."


    call screen character_select


    # These display lines of dialogue.


    # This ends the game.
label end:
    return

screen character_select:
    #background
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.5
        idle "images/vena_choice_idle.png"
        hover "images/vena_choice_hover.png"
        action [Hide("displayTextScreen"), Jump("venaprologue")]

        hovered Show("displayTextScreen", displayText = "Vena")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.6
        ypos 0.5
        idle "images/haru_choice_idle.png"
        hover "images/haru_choice_hover.png"
        action [Hide("displayTextScreen"), Jump("haruprologue")]

        hovered Show("displayTextScreen", displayText = "Haru")
        unhovered Hide("displayTextScreen")

screen displayTextScreen:
    default displayText = ""
    vbox:
        xalign 0.01
        yalign 0.5
        frame:
                text displayText
