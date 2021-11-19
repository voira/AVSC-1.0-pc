# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vena")

default preferences.text_cps = 30

init python:
    your_new_encyclopaedia = Encyclopaedia()


# The game starts here.

label start:
    stop music fadeout 1.0
    #call screen ctc()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    call prologue from _call_prologue

    #call screen ctc()

    scene blackscreen with fade

    pause 3.0

    "Choose a character."


    call screen character_select


    # These display lines of dialogue.


    # This ends the game.
label end:
    return

screen character_select:

    add Image("gui/overlay/game_menu.png")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.75
        ypos 0.5
        idle "images/vena_choice_idle.png"
        hover "images/vena_choice_hover.png"
        action [Hide("displayTextScreenV"), Jump("venaprologue")]

        # hovered Show("displayTextScreenV", displayText = "Vena")
        # unhovered Hide("displayTextScreenV")

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.5
        idle "images/haru_choice_idle.png"
        hover "images/haru_choice_hover.png"
        action [Hide("displayTextScreenH"), Jump("haruprologue")]

        # hovered Show("displayTextScreenH", displayText = "Haru")
        # unhovered Hide("displayTextScreenH")

screen displayTextScreenH:
    default displayText = ""
    vbox:
        xalign 0.25
        yalign 0.1
        frame:
                text displayText
screen displayTextScreenV:
    default displayText = ""
    vbox:
        xalign 0.75
        yalign 0.1
        frame:
                text displayText
