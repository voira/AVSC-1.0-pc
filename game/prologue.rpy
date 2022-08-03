define sin = Character("???", ctc= "ctc_blink" , ctc_position="nestled")
define sak = Character("???", ctc= "ctc_blink" , ctc_position="nestled")
define ea = Character("Ealdwine", ctc= "ctc_blink" , ctc_position="nestled")
define ma = Character("Marley", ctc= "ctc_blink" , ctc_position="nestled")
define wa = Character("Wilbur Asquith", ctc= "ctc_blink" , ctc_position="nestled")
define li = Character("Lionel", ctc= "ctc_blink" , ctc_position="nestled")
define narrator = Character(None, ctc= "ctc_blink" , ctc_position="nestled")

define fastdissolve = Dissolve(0.1)
define slowdissolve = Dissolve(1.5)

init python:
    your_new_encyclopaedia = Encyclopaedia()


label prologue:

    scene blackscreen with fade
    pause 1.5

    show text 'No matter where I am,'
    with dissolve
    pause 1.0
    hide text
    with dissolve
    show text 'And no matter what time it is,'
    with dissolve
    pause 1.0
    hide text
    with dissolve
    show text 'I will be there when you desire,'
    with dissolve
    pause 1.0
    hide text
    with dissolve
    show text 'I will wake upon your {b}call{/b}.'
    with dissolve
    pause 1.0
    hide text
    with dissolve


    pause 1.5
    scene hqin with fade
    pause 1.5
    sin "“Fool…”"
    sin "“She ruined my work! Everything! All of it!”"
    sak "“Is there any trace of her?”"

    sin "“No! I can’t feel her mana any longer. It’s almost as if she disappeared into thin air.”"
    sin "“I don’t even know who she is.”"
    sin "“Fool! Fool! That wench probably brought death upon herself too with this kind of clumsiness.”"
    sin "“...”"
    sin "“Ealdwine.”"

    ea "“I am listening.”"

    sin "“Keep your eyes open, and inform Vivian. If that woman is alive we have to find her no matter what.”"
    sin "“Before she spills it all.”"
    pause 1.5
    # Text box will disappear slowly here.

    scene hallbg with fade

    "My patience… was at its very end."
    "The emotions I had been hiding excellently thus far were now leaking through the cracks of my mask right before the King."
    "And there was nothing else I could do to calm myself down other than pace in the throne room in an anxious way."

    ma "“There have been numerous sightings of fatalities in the city. What I will say might sound atrocious, but I would have been happy if the responsible for those were just one man.”"
    ma "“Alas, one would see there were two different perpetrators, if they investigated the cases.”"

    "I came to a halt and glanced over the room. How pitiful it was to see that these serious matters merited so little reaction."

    ma "“One of them steals their victims’ mana out of their bodies. And the other commits cruel monstrosities I dare not speak of.”"
    ma "“So much so that I cannot even fathom if those actions were done by a person who dares to call themselves a man, or a ravenous beast.”"

    "The King and I made eye contact after those words. There was a dull expression on his face, as if what I said went over his head."
    scene hallbg with vpunch
    "With three long steps, I closed the distance between us and knelt."

    ma "“My lord, I beg of you. Think this through.”"
    ma "“Do not let them come here. There will be nothing but commotion upon their arrival-”"

    wa "“That’s enough, Marley.”"

    "No, it wasn’t. It could not be. No matter how unbecoming of a king he was, I was not going to let him drag Aelthus to the grave he dug."
    "I began to talk through my gritted teeth."

    ma "“People are talking about Khaunet’s return. Rumours are flying around the commoners about the incompetence of Dawn Knights.”"
    ma "“As if that weren’t enough, there are some gadabouts, which prefer to call themselves ‘hunters’, roaming in the streets with their crossbows, scaring people off.”"
    ma "“And for some unknown reason, all of this is happening right before the arrival of these women.”"

    wa "“Marley, since I liked your father I tend to turn a blind eye to your tone. In this matter however, you overstep yourself too much, young man.”"
    wa "“As a society, we needed a magical revolution and the opportunity has finally come.”"
    wa "“We can learn the fundamentals of the ancient magic.”"
    wa "“No one would ever suffer from disease, death-”"

    ma "“You still cannot get past your late wife! You are speaking, with her in your mind. That was long ago, please, I beg you to let her go.”"

    "Unfortunately I could only realize how harsh my words were after they left my mouth."
    "The eyes that had been frozen for so long were now ablaze with fury."

    wa "“Never speak to me in that way again. I would have you regret it.”"

    "The tone of his voice almost brought the chill of winter into the otherwise warm room."

    "His sons Xerxes and Cyril flinched, whereas Lionel grinned slyly. I grimaced."

    wa "“We will not have any more arguments on this subject again.”"
    wa "“The witches are to come to Whemond, and this is my last word.”"
    wa "“And you… Instead of keeping your head busy with what is already decided, you can revert your attention to the Knights of the Dawn that are under your care. Or I will pass their command to Lionel.”"

    show Lionel Smiling with dissolve:
        xpos 0.3 ypos 0.2 zoom 0.85

    li "“You can trust me, father.”"

    "(Sneaky brat…)"
    "Slowly, I got up while trying to make up my mind."

    ma "“Very well, I am at your disposal, as always. Even when we differ in opinion.”"
    ma "“My voice shall be raised on this matter no more, but I have a condition for you to hear of.”"
    ma "“I too, would like to be a supervisor of the witches. Just like Lionel.”"

    "With this way I could keep an eye on both Lionel and the witches at the same time."

    show Lionel Frown with dissolve

    wa "“You never give up, do you? Like father like son…”"
    wa "“In any case, do whatever you like and do not trouble me any longer.”"


return
