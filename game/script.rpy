
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vena")

default preferences.text_cps = 30

init python:
    your_new_encyclopaedia = Encyclopaedia()

label start:
    stop music fadeout 1.0

    call prologue from _call_prologue

    show screen ctc()

    scene blackscreen with fade

    pause 3.0

    "Choose a character."

    # hide(ctc)

    call screen character_select
label end:
    return
