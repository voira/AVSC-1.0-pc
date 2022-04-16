
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vena")

init:
    $ n = Character(None, ctc = anim.Blink("gui/heart.png"))

default preferences.text_cps = 30

init python:
    your_new_encyclopaedia = Encyclopaedia()


define Silver_Hollow = EncEntry(
    parent=your_new_encyclopaedia,
    name="Silver Hollow",
    text=[
    "{size=+25}The site where witches lived before the Black Massacre.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Waceera_Entry = EncEntry(
    parent=your_new_encyclopaedia,
    name="Waceera",
    text=[
    "{size=+25}The first and the last Night Mother of the Silver Hollow. She’s been lost ever since the Black Massacre, and there’s no information on if she’s alive, or not.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Black_Massacre = EncEntry(
    parent=your_new_encyclopaedia,
    name="Black Massacre",
    text=[
    "{size=+25}The event that caused the death of many Silver Hallow residents. An unknown power suddenly wiped out more than half of the population, forcing the survivors to seek shelter in the Outer World.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Almasi_Entry = EncEntry(
    parent=your_new_encyclopaedia,
    name="Almasi",
    text=[
    "{size=+25}One of the most influential, respected and old figures of the Silver Hollow.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Void_Crawler = EncEntry(
    parent=your_new_encyclopaedia,
    name="Void Crawler",
    text=[
    "{size=+25}The name given to the creatures of Abyss.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Night_Mother = EncEntry(
    parent=your_new_encyclopaedia,
    name="Night Mother",
    text=[
    "{size=+25}The leader of the people in the Silver Hollow. The first leader that had been elected was Waceera, and she held that title till the day of the Black Massacre. Today, the seat belonging to the Night Mother is empty.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Mana_Meditation = EncEntry(
    parent=your_new_encyclopaedia,
    name="Mana Meditation",
    text=[
    "{size=+25}A method can be used to recover, or flow one’s mana.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Whemond = EncEntry(
    parent=your_new_encyclopaedia,
    name="Whemond",
    text=[
    "{size=+25}The capital city of the Sun Kingdom of Aelthians, or Aelthus as most may prefer to call.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Royal_Academy = EncEntry(
    parent=your_new_encyclopaedia,
    name="Royal Academy",
    text=[
    "{size=+20}Full name goes as “Royal Magic Academy of the Sun Kingdom of Aelthians.” This institute is the source of all blueprints of the magical tools that the Kingdom uses, giving lessons on magic to young academicians, and providing a research laboratory whenever it is needed, meaning almost every day. The Academy is also notably famous, beyond the borders of the Kingdom, for how the entire structure floats in the air.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Shore = EncEntry(
    parent=your_new_encyclopaedia,
    name="Shore",
    text=[
    "{size=+25}An alternative name for the Land of the Dead.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Rune_Cards = EncEntry(
    parent=your_new_encyclopaedia,
    name="Rune Card",
    text=[
    "{size=+25}A simple card enchanted with a personal rune, made for the purpose of fortune reading. Different from the common runes, these cards are very personal; as readings and runes varies from one person to another. Those cards shall never be touched other than the owner, or their enchantment would wear off.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Light_Bearer = EncEntry(
    parent=your_new_encyclopaedia,
    name="Light Bearer",
    text=[
    "{size=+25}The leader of a circle. The Light Bearers are chosen by the Night Mother. The title is a reference to the Star Gems that are only handed to them.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Ashas_Prophecy = EncEntry(
    parent=your_new_encyclopaedia,
    name="Asha's Prophecy",
    text=[
    "{size=+25}The Black Massacre Prophecy that Asha foresaw through her rune cards. The cards brought the news of the end of the “world”, and said doomsday would arrive when a Priest of Death would walk upon this land.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Kiokos_Confession = EncEntry(
    parent=your_new_encyclopaedia,
    name="Kioko's Confession",
    text=[
    "{size=+25}Right afterwards the events of the Black Massacre, Kioko confessed that she might have seen the perpetrator but couldn’t remember it clearly.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
define Crimson_Bay = EncEntry(
    parent=your_new_encyclopaedia,
    name="Crimson Bay",
    text=[
    "{size=+25}The name of the gulf which Aelthian Kingdom surrounded. There’s no other country’s border in the region.{/size}"
    ],
    viewed_persistent=True,
    locked=True,
    locked_persistent=True
)
label start:
    stop music fadeout 1.0

    show screen menu_button()

    call prologue from _call_prologue

    show screen ctc()

    scene blackscreen with fade

    pause 1.0

    "Choose a character."

    pause 3.0

    call screen character_select()
label end:
    return
