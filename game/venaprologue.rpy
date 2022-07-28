define v = Character("Vena", ctc= "ctc_blink" , ctc_position="nestled")
define h = Character("Haru", ctc= "ctc_blink" , ctc_position="nestled")
define k = Character("Kioko", ctc= "ctc_blink" , ctc_position="nestled")
define a = Character("Asha", ctc= "ctc_blink" , ctc_position="nestled")
define al = Character("Almasi", ctc= "ctc_blink" , ctc_position="nestled")
define bbg = Character("A Silver Hollow Resident", ctc= "ctc_blink" , ctc_position="nestled")
define obg = Character("Another Person", ctc= "ctc_blink" , ctc_position="nestled")
define dbg = Character("Another Silver Hollow Resident", ctc= "ctc_blink" , ctc_position="nestled")
define gr = Character("Grand Duke", ctc= "ctc_blink" , ctc_position="nestled")
define m = Character("Marley", ctc= "ctc_blink" , ctc_position="nestled")
define c = Character("Cyril", ctc= "ctc_blink" , ctc_position="nestled")
define l = Character("Lionel", ctc= "ctc_blink" , ctc_position="nestled")
define u = Character("???", ctc= "ctc_blink" , ctc_position="nestled")
define narrator = Character(None, ctc= "ctc_blink" , ctc_position="nestled")


init:
    $ flash = Fade(.25, 0, .75, color="#fff")

##Grimoire Entries

##--------------GRIMOIRE ENTRIES END HERE ----------


label venaprologue:

    stop music fadeout 1.0

    scene blackscreen with fade
    pause 1.5
    "(Oh, how I wish I could see you for one last time…)"
    "(And confess those feelings that I piled up in my heart.)"
    pause 1.5
    scene traincomp with fade
    pause 1.5

    show Haru Default with dissolve:
        yalign 1 zoom 1.8

    h "“It’s surprising to see she can sleep.”"

    hide Haru Default with dissolve

    "I glanced at Kioko out of the corner of my eye."

    show Haru Default at right with dissolve:
        xalign 0.5 yalign 1 zoom 1.5
        linear 0.5 xalign 0.9


    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    pause 1.5
    "She was consumed by her worry, and fears."
    "Unlike a certain someone…"
    hide kiokoeye with dissolve

    v "“And it’s surprising to see how you can be this joyous after all that happened.”"

    show Haru Mischievous with dissolve:
        yalign 1 zoom 1.8

    "In response, Haru puffed her cheeks."

    $Silver_Hollow.locked = False
    $Silver_Hollow.locked_persistent = False

    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    h "“We don’t get the chance to leave {color=#ab1529}Silver Hollow{/color} every day. This is a first-”"


    "I interrupted her quickly."

    v "“And the last.”"

    show Haru Concerned with dissolve:
        xalign 0.5 yalign 1 zoom 1.5
        linear 0.5 xalign 0.9

    "It would be healthier for her if she didn’t get carried away by this ordeal. There was a possibility that we might not be able to see this place again for hundreds, or thousands of years after we returned to our home."
    "Which I believed to be the best for everyone."
    "It seemed unlikely for us to live in harmony with the people from the outside world, even if it was written in the stars."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    pause 1.0

    v "“She couldn’t sleep a wink these past few days because of the stress.”"

    show Haru Default with dissolve

    "Though I couldn’t say that this was a peaceful rest either."
    "Beads of sweat were rolling down her temples. Sometimes she shook vehemently, and sometimes stiffened as if she was bare in winter."
    "(Is she seeing “that day”?)"
    "Whatever it was I wished to take a look at that myself; however Haru might not take this well."

    hide kiokoeye with dissolve

    h "“I think everyone here suffers from a similar problem.”"

    v "“Everyone except you.”"

    hide Haru with dissolve

    "She glared at me for a while, but that was fine."
    "Many of our people had lost their lives, Silver Hollow was in ruins, and our leader was missing. I would not feel remorse because I got angry at a child who acted like she was going on a vacation in a dire situation such as this."

    show Haru Sideway at center with dissolve:
        yalign 1 zoom 1.8

    h "“I will get some air.”"

    "(The chance I’ve been waiting for…)"
    "Still, I didn’t wish to raise suspicion by seeming eager."
    "Although Haru wasn’t good at reading people, sometimes she could be uncharacteristically sharp."

    v "“Where are you going?”"

    show Haru Default with dissolve:
        yalign 1 zoom 1.8

    h "“Just taking a walk in the aisle. My legs have gone numb.”"

    v "“Alright. Just don’t get yourself in trouble.”"

    hide Haru with dissolve

    "She nodded curtly in response before leaving the compartment."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    pause 1.0

    "Quickly I turned to Kioko. There was no time to waste."
    "Before awakening my powers, I shut my eyes and took her hand between mine."
    "(Sorry Kioko. This is for the greater good.)"

    scene fogforest with fade

    "The nightmare of my sister took me to the place I’d been missing so dearly."
    "I knew every single tree here. Every branch, every single Hollow on them was familiar to me."
    "But I hadn’t cast this spell to find peace in the Silver Hollow that now lived only in memories."


    $Black_Massacre.locked = False
    $Black_Massacre.locked_persistent = False

    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    "Somewhere around here, Kioko must be witnessing an important event regarding the {color=#f00}Black Massacre.{/color}"


    play sound walking

    "With heavy steps I walked towards the village, I kept to the shadows of the trees, while hiding myself from the eyes of my sister."

    stop sound

    "My presence in the dream was urging it to become more vivid and dragging its owner’s consciousness here as well."
    "So I didn’t want to be caught by the “real” Kioko."
    "The forest which once bathed in the light of the stars was now covered in a thick fog as the result of a dark power."
    "Even though my body was determined to go forward, a voice in my mind was begging me to get out of here."
    "I dismissed those fearful thoughts at once. It was nothing but a dream anyway, and whatever had happened in reality could not be undone. Living in the past would only bring despair."
    "And this was not the time to be afraid."
    "Kioko’s nightmare must had been encouraged by my bravado, however…"

    scene blackscreen with fade
    # Buraya Dead Bodies CG'si eklenecek!

    "Since it felt the need to show me these."
    "(I’ve almost stepped on them.)"
    "Narrowing my eyes, I carefully gazed at the girls’ faces for a while."
    "Most of them were alive, sitting and chatting somewhere in the “train”. But here, in this dream, they were looking at me with glassy eyes, like the dead people had that day."
    "Not a single wound or scar could be found on their body; but it was understood that they were dead by the silence of their pulse, the lungs would not fill with air, and eyes that swore not to shut."
    "Struggling to contain my emotions, I leaned down and closed one of the girl’s eyes before moving."

    scene fogforest with fade

    "If my guess was right, the dream should have taken place amidst the forest, which was also the heart of our residency."
    "I was not certain how much this dream reflected reality, given that the dead bodies I’d just seen that belonged to people who were actually alive."
    "However, any information was crucial. Kioko’s faded memories had to be brought to light, no matter what."

    play sound walking

    pause 4.0

    scene shd with fade
    stop sound

    "Finally, I found myself in the village center. And there was the person I was looking for, crouched down next to the fountain, crying in agony while clasping a dead body."

    show Kioko Crying with dissolve:
        yalign 1 zoom 1.3

    "Resisting the temptation to console her was hard; to wrap her up in my arms, and rub her shoulder in a comforting way."
    "But I hadn’t come here to console anyone."
    "Finding the perpetrator was my main goal."

    hide Kioko with dissolve

    scene forest with flash  

    show Kioko Concerned with dissolve:
        yalign 1 zoom 1.3

    k "“Vena I… Think I saw the person that was responsible for what… Happened.”"

    show Kioko Concerned with dissolve:
        yalign 1 zoom 1.3

    k "“But I can’t remember. I just can’t.”"

    hide Kioko with dissolve

    scene shd with flash

    show Kioko Crying with dissolve:
        yalign 1 zoom 1.3

    "(Where are you… Where are you? Come now, don’t be shy-)"

    show Kioko Shocked with dissolve:
        xpos 0.55

    pause 2.0

    hide Kioko with dissolve

    scene fogforest with fade

    scene fogforest with vpunch

    "Too caught up in my thoughts, for a while I didn’t realize Kioko’s eyes were actually fixated on me. Immediately, I hid behind the tree I’d been leaning on."
    "A moment later though, my heart still thudding in my chest by the sudden contact of our eyes, I realized that panicking was totally unnecessary."
    "It was not a problem to be seen by the “dream” Kioko."
    "What mattered was to not get caught by the “real” one, and she was probably looking for me everywhere since her consciousness would be on high alert due to a stranger’s presence in the dream."
    "(No time to waste.)"
    "I peeked from around the tree."

    scene shd with fade

    "Voices were raised in the old Coven, causing the great oak it sat on to tremble."
    "If I remembered correctly, this was also the last place Kioko visited before losing her memories."
    "Her memories might actually be shrouded by some spell, given the possibility of the perpetrator being one of our own people."
    "Or, she’d simply lost them naturally by the shock and trauma she’d gone through."
    "We had no evidence or information on what or whom she may have seen. I could not discount the chance of her meeting with the culprit."
    "How much this dream reflected the truth was a mystery, however. Still-"

    scene shd with vpunch

    "…!"
    "A sudden, familiar scream made me lose all composure. And before I realized what I was doing, I’d yelled back at the top of my lungs."

    v "“Waceera!”"

    "I sprang into action at once."
    "Looking back now, how embarrassing that must have seemed; being ready to try my hardest to save a person who was not even real."
    scene shd with vpunch
    "However, before I could disgrace myself further, someone grabbed my arm."
    "I sharply turned to the person behind me, gasping, momentarily disoriented."

    scene fogforest with fade

    show Kioko Gasping with dissolve:
        zoom 1.6

    k "“Vena? Are you… The real Vena?”"

    "{i}Nice.{/i}. I got caught. But this was no time to waste with pointless questions."
    "I grabbed Kioko by the shoulders."
    v "“Kiki, listen to me. We should move immediately. There's something going on in the old Coven-”"

    hide Kioko with dissolve

    scene fogforest with vpunch

    "A loud bang interrupted my words, then the ground began to shake."
    "I and Kioko barely held on to the nearest tree as the world churned and quaked around us."
    "Quickly I raised my head to see the source of the sound."

    scene shd with fade

    show VoidCrawler with dissolve

    "(No, no…)"
    "A huge void vortex appeared in the ruins of the cabin which used to be our old Coven."
    "We were too late. This meant my chance of taking a peek at whatever had happened was lost."

    $Void_Crawler.locked = False
    $Void_Crawler.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    "There was nothing I could do at this point other than running my fingers through my hair restlessly, powerless to stop the {color=#f00}Void Crawlers{/color} attacking everyone in the grove."
    "Except by waking up…"

    scene traincomp with fade

    "I was back to square one."
    "Loud voices, almost like yelling, could be heard outside. And the compartment was still one person short. Rubbing my eyes, I wondered where Haru could be."

    show Kioko Confused with dissolve:
        yalign 1 zoom 1.5

    k "“Vena… Why didn’t you ask me beforehand?”"
    "(Oh…)"
    "I wetted my lips before taking a deep breath. There was no anger in her features, but she clearly felt uncomfortable."

    v "“Since you were having a nightmare, I thought it would be good to check if those blocked memories could be reached.”"

    show Kioko Melancholic with dissolve:
        yalign 1 zoom 1.5

    k "“You are suspicious of me, aren’t you?”"

    k "“Just like everyone else.”"

    "Her words caught me off guard."
    "What was most shocking was the nugget of truth buried inside them. No matter how small..."

    v "“Kioko-”"

    "My words were interrupted by the sound of the door."

    hide Kioko with dissolve

    show Haru Concerned with dissolve

    "I turned to look at Haru."

    v "“Did something happen? I heard someone yelling.”"

    show Haru Smiling with dissolve

    h "“The usual arguments, you know. Nothing else.”"

    "…What kind of “usual arguments” was she talking about?"


    $Mana_Meditation.locked = False
    $Mana_Meditation.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    "Whatever… Because that I hadn’t done {color=#f00}mana meditation{/color} for a long time this experience had left me weary, so there was no energy left in me to pursue it."
    "I shrugged before closing my eyes."


    $Whemond.locked = False
    $Whemond.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    "And I had no intention of opening them before we arrived in {color=#f00}Whemond.{/color}"

    scene blackscreen with fade

    "Tall buildings that were made from cold concrete… People who were famishing in the alleyways, and the viscous humidity which made you feel suffocated…"
    "These weren’t things that a person, who had spent their life in the middle of a forest and kissed goodnight by the stars before falling asleep every night, could get used to in a single day."
    "And I felt achingly lonely despite being surrounded by my sisters."
    "(Like a shunned wretch who dared to call herself a “nomad”.)"

    scene academylivingroom with fade

    $Royal_Academy.locked = False
    $Royal_Academy.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    "Finally we were in the famous {color=#f00}Royal Academy.{/color}"
    "I was busy organizing the jars that I had filled with herbs from the village we’d stayed in after the Massacre."
    "My body was begging for rest, but I desired at least to get one thing done before truly relaxing."
    "Meanwhile Haru, Kioko and Asha had gathered before the window and were watching the hell beneath which had been given a fancy name such as “city”."
    "My attention was focused solely on the task at hand since I was not sure if I could refrain from dampening their joyful mood with my distasteful comments."
    "However it was also impossible to ignore what was being said."

    show Asha Grinning at left with dissolve

    a "“Ladies, if you’re this impressed already, I can’t imagine your reactions over the sunset! It always looks like the sun bleeds right into the sea.”"
    a "“And in the dawn, it is gloriously reborn from the blood coloured tides to light the sky once more.”"
    a "“Alas, I have to admit… Almost everything has changed since I was here the last time.”"

    "I began to mutter through my gritted teeth."

    v "“A disgrace is what this place is. There’s no single thing to be impressed about.”"

    show Asha Default with dissolve

    v "“Not once did I think that the light magic could be used in such useless way.”"

    "Thanks to the overwhelming light pollution from the streets and buildings, the stars that had guided me through my whole life hadn’t shown themselves for even a second since we’d arrived."
    "And the situation was worse in Whemond."
    "It almost seemed like a harbinger of misfortune."

    show Kioko Shy with dissolve:
        xpos 0.8 ypos 0.18

    k "“Well, I… I think the lights look pretty.”"

    "(…You too, Kioko?)"

    show Asha Smiling with dissolve

    a "“Don’t worry, you will have the opportunity to go on a trip into the city after things have settled more I think.”"

    "Before I had time to recover from what Kioko had said, another outrageous claim was raised from Asha."

    play sound loudthud



    hide Asha with dissolve

    show Asha Gasping

    show Kioko Gasping with vpunch:
        ypos 0.18 xpos 0.83

    show Haru Gasping at left with dissolve
    show ex with hpunch:
        ypos 0.15 xpos 0.6

    "My anger made me slam the jar on the counter with much more force, while trying to place it."
    hide ex with dissolve
    "Now all of the eyes in the room were upon me."
    "Going on a trip, having fun… How could they make such laid-back plans when we couldn’t have held a ritual for our dead?"
    "Our leader was missing; friends, sisters we cherished so dear had lost their lives and we were not even capable of bringing their lifeless bodies back to cremate."
    "How could they act this nonchalantly? Especially Asha, of all people!"

    v "“Asha, I beg you to not to put such atrocious thoughts into anyone’s mind.”"
    v "“Not Haru’s, nor Kioko’s, nor anyone else’s.”"

    show Asha Default
    show Kioko Neutral:
        xpos 0.83 ypos 0.18
    with dissolve

    show Haru Default at left with dissolve

    a "“What’s the problem? We can arrange a one-day trip.”"

    v "“Absolutely not.”"
    v "“We are in a very difficult time that requires extra care. The reason why all this happened in the first place is still a mystery.”"
    v "“Unless they have a death wish then our people should never leave this Academy.”"
    v "“In fact, even if it’s exactly what they wish for, you still shouldn’t let them. As a leader it’s one of your priorities to seek everyone’s safety, Asha.”"
    v "“Let alone we are not here to amuse ourselves, we have casualties.”"

    "As our acting leader- no, setting that aside, as a person who walked the world several thousands of years, I expected Asha to be more cautious, sharper."
    "Particularly while treading upon the cracks that had begun to form among us."

    hide Kioko
    hide Haru
    with dissolve
    show Asha Grinning with zoomin

    a "“You’re just like Waceera.”"

    "At this point, it was hard to figure out if she’d said that to criticize me, or to praise me. But it didn’t matter."

    v "“How nice it is to see that you can laugh. You shouldn’t dismiss the importance of this situation. Especially with Almasi being on your tail like this, looking for any possible mistake you might make.”"

    show Asha Smiling with dissolve

    a "“It seems you don’t see me worthy as of your trust as Waceera.”"

    "I shut my eyes for a moment."
    "Even a stranger could understand that what she said was true. There was no point in lying."

    v "“I am speaking up for your own good, please don’t turn it into a competition.”"

    a "“That I won’t, let’s just say I’m stating a fact.”"
    a "“Oh Vena… There’s no reason for you to worry. We will find Waceera, and get back to Silver Hollow. I can assure you.”"

    "She stood, making ready to leave."

    show Asha Default:
        xalign 0.5
        linear 0.8 xpos 0.2

    a "“I shouldn’t bother you three anymore. It is time for you to sleep.”"

    show Kioko Laughing at right with dissolve

    k "“You still act like we are little kids, Asha.”"

    show Asha Default:
        xalign 0.2
        linear 1 xpos 0.6

    pause 1.5
    "Asha ruffled Kioko’s hair gently."

    a "“That is because you are little children on my perspective. And you will always remain as such for me.”"

    hide Asha
    hide Kioko
    with dissolve
    play sound doorclose
    pause 2.0

    scene shd with flash

    show Waceera Smiling with dissolve

    u "“You’ll always stay as a kid in my eyes, Vena.”"

    scene academylivingroom with flash

    "(…)"
    "Just when I was about to get lost in my memories, Haru’s voice shook me back to reality."

    show Haru Default:
        xpos 0.8 ypos 0.18
    show Kioko Default:
        xpos 0.3 ypos 0.18
    with dissolve

    h "“So… We are returning to our rooms?”"
    v "“You two can leave. I still have work to do.”"
    k "“Please don’t tire yourself out.”"

    show Haru Concerned with dissolve

    h "“I agree with Kioko, Vena. Also, well… Good night.”"

    v "“Good night.”"

    hide Haru
    hide Kioko
    with dissolve

    "Once the two of them left, I buried my face in my hands, and tried to take a deep breath."

    scene blackscreen with fade

    "There was still so much work to do."
    "And no matter how tired I was, I knew that it was impossible for me to sleep when I had this much on my mind."

    scene academylivingroom with fade

    "I reached to the shelves behind me to take down an ointment I’d made with rosemary."
    "Never in my life had I spent a day sitting still on a seat as much as I’d done today. Why people preferred to torture themselves with that big mess they called a “train”, while they could simply teleport with magic was a mystery for me."
    "(All of my muscles are sore. Great…)"
    "Shaking my head with despair, I began to rub the ointment on my thighs. To think that we have to take that journey again…"
    "(Only if we can go back to Silver Hollow…)"
    "I dismissed those ominous thoughts before they started to take root in my mind. Whatever it took, we were going to find a way to return."
    "Standing up, I got closer to the window. Since the Academy floated in the air, the whole city could be viewed from up here."

    scene whemond with fade

    "Whemond…"
    "That was what they called this place."
    "The structures had been dressed up in a pathetic attempt to make them seem majestic instead of daunting, but no matter how much plaster they tried to use, hiding the filth beneath was impossible."
    "Even with the magical barrier which surrounded the Academy, I could sense how people felt down below: Their nervousness, sorrow, and distress."
    "Seeing such intense emotions gathering in one place was another first in my life. And it was quite unnerving, to be frank."
    "I wanted my peaceful, vibrant days back, not to stagnate and rot just like everything else did here."
    "And doing whatever was needed to avoid such a miserable end was my intention."

    scene blackscreen with fade

    pause 2.0

    # Buraya sonraki gün ibaresi eklenecek!

    scene academyclass with fade

    "A busy day was ahead."
    "Today marked our first council meeting after the Black Massacre."
    "(I don’t know how solution oriented this will be. More like the mood’s suggesting that there will be further disputes between us.)"
    "(And Almasi is the main reason of that.)"

    scene academyclass with zoomin

    play sound crowdtalking loop

    "I took a seat with Haru in the classroom which the Academy had handed us."

    play sound sitting
    queue sound crowdtalking volume 0.6 loop

    "Placing the Memory Stone on the desk, I thought of Kioko, who wasn’t able to attend this meeting due to her fatigue."
    "I didn’t want her to miss what would be said. Recording the memories for her was the best option I had."

    play sound doorclose
    queue sound crowdtalking volume 0.3 loop
    show Asha Default at right with dissolve
    show Zuri Default at left with dissolve

    "Before long, Asha and Zuri came to the classroom as well."
    "As I’d guessed she might, Zuri left Asha alone at the podium, and instead took a seat in the front row."

    hide Asha with dissolve
    hide Zuri with dissolve

    "(So she doesn’t want to take the blame again. Could Kioko’s shyness be inherited from her?)"

    show Asha Default with dissolve

    a "“Nice… You’re all here- oh, except one person.”"

    "Kioko…"

    show Asha Sideways with dissolve

    a "“Which is okay.”"
    a "“I promised you that once we arrived to Whemond, I would try to answer whatever questions you may have.”"

    show Asha Default with dissolve

    a "“And today, I am here to keep my word-”"

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    al "“You can start with explaining why you think your sister might be alive.”"

    "(Stars guide our way.)"

    hide kiokoeye
    hide Asha
    with dissolve

    "I turned and looked at the woman who was so determined to light a fire even when the hearing had yet to start."

    show Almasi Angry with dissolve

    "Her intent to cause chaos could be read in every detail of her face."

    hide Almasi with dissolve

    show Asha Default with dissolve

    a "“There’s no point in lying.”"
    a "“The circle which I, Waceera and Zuri shared was looser than the others.”"

    play sound whispering

    hide Asha with dissolve

    "(…)"
    "I’d had doubts on this matter. Saying I hadn’t expected them to be true would be a lie, rather I simply didn’t want them to be confirmed."
    "Things not being ethic didn’t concern me anymore. I just wished there was a way to guarantee Waceera’s safety."
    stop sound
    pause 3.0
    "Upon our birth we were placed to circles, which was decided by our star maps."

    scene constellation with fade

    "The magic that bonded us together helped the members of the circle to sense each other like they were of the same body, made them much, much more powerful, extended their lives, and granted other such benefits."
    "But as for the give-and-take rule, the tighter the bond between the members was, the higher the risk and the more negative effects there were."
    "For example, since the circle pushed us to be “one”, we lacked truly individual emotions."
    "And if one of us got hurt, others would suffer from the same condition. Moreover, if one of us died, then the others died as well."

    scene academyclass with fade

    "This aspect alone had given us a huge disadvantage during the Black Massacre, had thinned our numbers much too quickly."
    "Because of that, the first thing we had done upon arriving in the Outer World was loosening the circles."

    al "“So you admit the fact that you made us live like puppets while benefitting from the system this whole time, right?”"

    show Asha ClosedEye with zoomin

    a "“…”"

    show Asha Default with zoomin

    a "“I wouldn’t call it benefitting.”"
    a "“This was Waceera’s decision. To provide us longer lives…”"
    al "“Nonsense!”"

    show Asha ClosedEye with zoomin

    a "“My only responsibility at this meeting, is telling you the truth.”"

    show Asha Default with zoomin

    a "“The reasons behind Waceera’s actions are things that you can only learn from her.”"
    a "“I know this might get you irritated, but I have no other answer than this to give.”"
    a "“Therefore, I would suggest you to keep your provocations for her return.”"

    play sound commotion loop
    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    al "“How nice, how nice! You really found yourself an escape route, didn’t you?”"
    stop sound

    "I gritted my teeth. Surely Asha’s leadership was lacking, but must we fight over it between us?"
    "When we desperately need to stick together at that…"

    hide kiokoeye with dissolve

    show Asha Sighing with zoomin

    a "“The most you can hope for in this moment is Waceera’s safely return, and answering all of these accusations herself."

    show Asha Default with zoomin

    a "“But I am ready to answer the other questions you might have.”"

    hide Asha with dissolve

    bbg "“How much longer were you going to keep the existence of the Outer World a secret?”"
    obg "“Is there a traitor among us?”"
    dbg "“What if they kill us all? This is not an academy, but a jail!”"

    scene blackscreen with fade

    "I buried my face in my hands while listening to the half-baked answers Asha gave."
    "This council was doomed before it’d begun. What had I expected?"

    scene academyclass with fade

    "However before I gave in to such thoughts, Haru poked me. Startled, I looked at her."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    h "“Vena, who is the person over there?”"

    "(…Huh?)"

    show Ealdwine Default with dissolve:
        xpos 0.74 zoom 1

    "Since my attention was totally drawn in by the meeting, I hadn’t realize the stranger standing in the doorway."
    "So they’d already begun set a watch on us."

    hide kiokoeye with dissolve

    show Ealdwine Default with dissolve:
        ypos 1.25 zoom 1.3

    v "“I don’t know, but that’s the uniform of the Academy.”"

    hide Ealdwine with dissolve

    "(Hah… How offending… How humiliating!)"
    "Certainly we were going to be treated like animals kept in cage here."
    "What was there to do, other than submitting to this fate though?"

    scene academyhallway with dissolve

    "(Phew…)"
    "After many hours, the meeting had finally ended."
    "And we were yet to find solutions, still stuck right at the starting point."

    show Asha Default at right with dissolve

    v "“You can’t shrug their questions off forever.”"

    "Haru had gone to help others, and at long last we were alone with Asha. I hadn’t approached her amidst the crowd in order to avoid unwanted attention."

    show Asha Concerned with dissolve

    a "“Which calls for finding Waceera as soon as possible.”"
    v "“What is the plan?”"

    show Asha Ruminant with dissolve

    a "“Arranging various expeditions.”"

    "Questioning, I raised a brow."

    v "“To where? I thought you said that we couldn’t go back to Silver Hollow due to the state it’s in.”"

    show Asha Default with dissolve

    a "“I didn’t mean Silver Hollow.”"
    a "“What I meant was the Land of the Dead.”"

    "I took a deep breath. It was clear as day what she was thinking of."

    v "“I don’t think I can convince Kioko for that.”"

    show Asha ClosedEye with dissolve

    pause 2.0

    show Asha Default with dissolve

    a "“We should try at least.”"

    v "“I will, but don’t expect much.”"

    show Asha Sighing with dissolve

    $Shore.locked = False
    $Shore.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    a "“It would be enough if she could manage to send one of us to the {color=#f00}Shore{/color}.”"

    v "“That can be arranged.”"

    show Asha Default with dissolve

    "She rubbed my shoulder."

    show Asha Smiling with dissolve

    a "“Alright, I trust you. Even more than anyone else here.”"

    show Asha Sideway with dissolve

    a "“Also, Vena…”"

    hide Asha with dissolve

    scene academyhallway with zoomin

    "I understood that Asha was going to say something of great importance from the way she dragged us to an even a more isolated spot."
    "I looked at her in confusion while she checked the passersby in the area with a spell she quickly cast."
    "After confirming we were alone, she glanced at me with eyes that were relieved."

    show Asha Default with dissolve

    a "“The things I will say now shall stay within the Light Bearers.”"

    show Asha Concerned with dissolve

    a "“I think what happened to us, who or what did caused this is related to someone from the outside world.”"

    "I weighed all in my head before answering. While I couldn’t refuse the existence of such possibility, fathoming offender’s potential gain from it was hard."

    v "“Do you have any proof regarding that? Something you realized?”"

    "She was not a person to make false statements."

    hide Asha with dissolve

    $Rune_Cards.locked = False
    $Rune_Cards.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    "I watched her taking out two pieces of paper from the skirt she wore. Tilting my head and paying more attention, I grasped these were {color=#f00}rune cards{/color}."

    a "“‘Traitor’.”"

    "She held one of the cards to my face, then did the same for the other."

    a "“‘Stranger’.”"

    "It wasn’t wise to ignore what Asha predicted, as she was the best fortune-teller among us."
    "After all, the infamous prophecy of the Black Massacre belonged to her."
    "(Funny; even knowing it beforehand there’d been nothing we could do to prevent it from happening.)"
    "(However this time…)"
    "I frowned."

    show Asha Default with dissolve

    v "“What would you suggest? We are stuck here. There’re Royal Knights at every corner.”"

    show Asha Sideway with dissolve

    a "“Not just us… Odd things also happen in Whemond.”"

    v "“And you assume there’s a correlation between those.”"

    show Asha Default with dissolve

    a "“That is also their assumption.”"

    "By “they” I realized that she was talking about the prominent figures of this country."

    a "“Tonight, we will hold a meeting with the other Light Bearers.”"
    a "“The King’s sons, and the Grand Duke of Pertone will join us.”"

    "I nodded."

    v "I nodded."

    show Asha Smiling with dissolve

    a "“Great, because someone should keep Almasi in check before she goes and starts a war.”"

    hide Asha with dissolve

    "I laughed and patted her on the back."
    "After deciding when would be the meeting would be, and who would inform whom about it, we parted ways."
    "(I must find Haru. I shouldn’t leave her alone with those wolves for so long.)"
    "Absentmindedly, I took the next turn that led to the Southern Wing-"

    scene academyhallway with hpunch

    # Buraya CG gelecek!

    v "(…!)"

    u "“Ooof!”"

    "…And a girl bumped into me right then."
    "Before she fell though, I caught her by the shoulders, making her stand properly."

    v "“Are you okay?!”"

    "There was a tune of concern in my voice although I scolded her."

    u "“Get away from me, you foolish peasant! Never dare to touch me again.”"

    "(…)"
    "(…What?)"
    "Not believing what I’d heard, I yanked my hands free."

    show Orphina Default with dissolve:
        ypos 0 zoom 1.2

    v "“Pardon?”"

    u "“Pay attention to where you are heading!”"

    "(You’re being too much.)"
    "I grimaced.    "

    v "“Apologies, it is hard for a person of my height to see what’s going on down below.”"

    show Orphina Annoyed with dissolve
    pause 1.5
    show Orphina AnnoyedSide with dissolve

    u "“…Tch.”"

    hide Orphina with dissolve

    "She walked towards me and bumped into me on purpose, then got away hastily."
    "In the meantime I was still trying to recover from such impudence."
    "I called behind her back."

    v "“What happened to the ‘no contact’ rule? It almost seems like you’re the one seeking to break it.”"

    "But she didn’t turn back."
    "(Who let this sassy kid in?)"
    "I shrugged, thinking she was not even worth my time."

    scene academylivingroom with fade

    "Night had finally come after a very long day."
    "And my work was far from done. Our meeting was scheduled for later."
    "I had never been one to avoid responsibilities, but even I had a hard time imagining the workload of the coming days."
    "(I wonder what the King’s sons will talk about. They will at least provide some useful information, I hope.)"

    show Haru Default:
        ypos 0.18 xpos 0.3 zoom 1.0
    show Kioko Eyesclosed:
        ypos 0.18 xpos 0.8 zoom 1.0
    with dissolve
    k "“I… Want to tell you something.”"

    k "“But please don’t panic.”"

    "…"
    "(Too late, Kioko. It’s impossible not to freak out when it comes to you.)"
    "I looked at her, concerned."

    show Kioko Concerned:
        ypos 0.18 xpos 0.765

    k "“I think… I think I saw someone in my room today.”"

    "My eyes widened for a brief second."
    "(Get yourself together. If you get anxious then she sure will too.)"

    show Haru Gaping zorder 1 at left with ease:
        yalign 1 zoom 1.8

    h "“What?”"
    v "“Who?”"

    show Kioko Concerned

    k "“I-I don’t know.”"
    k "“It might have been a dream, I’m not sure.”"

    hide Haru
    hide Kioko

    scene shd with flash

    show VoidCrawler with dissolve
    pause 2.0
    scene academylivingroom with flash

    show Haru Gaping:
        yalign 1
    show Kioko Concerned:
        xpos 0.8 ypos 0.18 zoom 1.0

    "Could they be I thought of?"
    "What if they’d come back to get rid of Kioko since she’d seen their face?"
    "Though, maybe we were worrying for nothing."

    v "“Kioko, calm down.”"

    show Kioko Shy with dissolve:
        xpos 0.801 ypos 0.18

    k "“I had just woken up, and I realized someone was in the room with me. She was standing next to the window.”"

    show Haru Concerned with dissolve

    h "“What did she look like? Couldn’t she be just one of your friends?”"

    show Kioko Concerned with flash

    k "“No! No… I don’t have a friend like that.”"

    show Kioko Concerned with dissolve

    k "“She had ginger hair. But I couldn’t see her face clearly, for I was sleepy.”"

    show Kioko Eyesclosed with dissolve:
        xpos 0.835 ypos 0.18

    k "“She walked towards me. I was so scared that I couldn’t move! I must have passed out from sheer fright. When I opened my eyes again, it was later and she was gone.”"

    "I reached to her forehead. Watching her memories would be more useful than listening to her."

    v "“If it is okay, I’ll take look myself.”"

    "By nodding her head, she gave a wordless permission. I took a deep breath, and awaken my magic."

    hide Kioko
    hide Haru
    with dissolve

    # Buraya CG gelecek!

    "What caught my attention first was how blurry the memory was."
    "I could hardly see the woman before Kioko."

    "Ginger hair, light skin, lips that curled upwards…"
    "But there was nothing else."

    "Even with so few details, I could tell this was a stranger indeed."
    "After analysing the dream a little more, I left her mind to avoid wasting my mana."

    scene academylivingroom with fade

    show Kioko Default:
        xpos 0.8 ypos 0.18 zoom 1.0
    show Haru Default:
        xpos 0.3 ypos 0.18 zoom 1.0

    "Both of my sisters were looking at me with curious eyes."

    v "“Either you saw someone who then clouded your memories, or it really was just a dream.”"

    show Haru Concerned with ease:
        yalign 1 zoom 1.8

    h "“Either you saw someone who then clouded your memories, or it really was just a dream.”"

    "I shook my head."
    "Usually when memories were clouded or erased, I could immediately tell by detecting the lingering traces of magic."
    "But this time, I didn’t feel anything artificial, or out of place."
    "This meant that either Kioko was confusing a dream with reality, which was highly probable given how sleepy she had been at that moment."
    "Or Kioko had indeed had a stranger in her room, a stranger that was very skilled at manipulating memories."
    "Just like Kioko’s first memory loss like after the Massacre…"

    h "“Could they be someone from this Academy?”"

    v "“I’m not sure. She wasn’t wearing any uniform, and didn’t look like one of our people. Kioko, why didn’t you inform us sooner?”"

    show Kioko Eyesclosed with dissolve

    k "“I didn’t want to cause an unnecessary scene.”"

    "I reached out and took her hand in mine. This kind of dilemmas could have dangerous consequences."

    v "“Don’t ever think like that. These are rough times, you should inform us of anything you suspect.””"

    h "“This is so weird. What are we going to do?”"

    v "“I…”"

    "I had an idea. Perhaps this would hold me back from the investigation, but still…"
    "(Nothing matters more than my sisters.)"
    "Plus Kioko was surely key to solving this mystery; protecting her, being there for her were also responsibilities of mine."

    v "“Kioko, would you like to sleep in my room for now?”"

    show Kioko Concerned with dissolve:
        ypos 0.18 xpos 0.765

    k "“I don’t want to be a burden.”"

    v "“Oh hush, you’re my sister.”"

    k "“But wouldn’t I be in the way of your work?”"

    v "“No, you’re my priority.”"

    show Haru Troubled with dissolve

    h "“She can… She could sleep in my room too. I can take care of her.”"

    "I looked at Haru aloft in wonder."
    "(What’s next? Is she going to say that she missed Silver Hollow?)"
    "To be frank… It would be more likely to assume she would prefer to stay alone in order to escape from the Academy."

    v "“No. What if something happens to you?”"

    show Haru Sideway with dissolve

    h "“Listen, I know I am nowhere powerful as you, but it’s not like I don’t know what I’m doing.”"

    "She was right."
    "Haru could replenish her mana faster than any other Silver Hollow resident, which provided her great potential."
    "(Of course, she doesn’t have the slightest clue about making use of this advantage but that is another story.)"
    "Yes, practical magic was her thing, however when it came to the complex spells, “dreadful” would be the word you would use to describe her attempts."
    "Her speed was what reassured me that they could get themselves out from any dangerous scenario."

    v "“So be it. But if anything unusual catches your attention, then you need to inform me about it without hesitating.”"
    v "“Are we clear?”"

    "Both of them nodded in agreement."

    hide Haru
    hide Kioko
    with dissolve

    "(Just to be safe, I should cast some protection spells.)"

    scene academyhallwaynight with fade

    "I was late for the meeting."
    "And since I didn’t know the Academy very well, teleporting was out of question."
    "Asha also warned us about the casting spells around the Outsiders, to be cautious of not scaring them."
    "(It is almost comical to think that they are the same people who built huge stone walls, invented enormous “transportation vehicles”. And yet they are afraid of such simple spells.)"

    scene academyhallwaynight with dissolve:
        xpos 0.2 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    "(Alright, it must be here.)"

    play sound doorknocking noloop

    "After knocking on the door, I entered the room without waiting for an answer."

    scene 4knights with fade

    pause 1.5

    scene 4knights with fade:
        xpos 0.9 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade:
        xpos 0.6 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade:
        xpos 0.3 ypos 1.8 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade:
        xpos 0.1 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade

    "The first thing that caught my eye were the unfamiliar faces sitting on the couch near the centre of attention."
    "After a moment, I realized that the blond trio must be the princes, and the other one should be the Grand Duke."
    "Their motionless seating arrangement reminded me of something I'd seen while visiting a neighbouring village, a collection of beautiful dolls lined up inside a glass display case."
    "Each one of them looked gorgeous, dazzling almost. But I was not one to be impressed by such things."

    a "“Vena! There you are, we’ve been waiting for you.”"

    "I heard Asha’s cheerful welcome and the Grand Duke’s grumbling behind the paper he held at the same time."

    gr "“Yes, we, a whole room full of people, were waiting for your arrival.”"
    gr "“You have quite the nerve to be late, unapologetic, and disrespectful towards the heirs of the throne simultaneously.”"
    gr "“Especially as the last charge carries the death penalty in some cases.”"

    "I gaped at him, shocked."
    "This was the second time today I had been scolded like that."

    scene academyhallway with flash
    show Orphina Gritting with dissolve
    pause 2.0
    hide Orphina
    scene 4knights with flash

    "What kind of place was this? He was the one with the nerve to threaten me like that!"

    v "“It’s your country, your king and your throne. Not mine. None of those concern me.”"

    "Finally he deigned to grace me with eye contact. He didn’t even bother to conceal the look of chilling rage that curdled in his bright blue orbs."
    "He glared at me as if I was his enemy. I couldn’t stop my lips back from twisting into a wry smile in response."

    gr "“I would like to remind you which country, which king and which throne you are currently under the protection of, {i}Lady Vena{/i}.”"

    "He pronounced my name in a sarcastic tone."

    u "“It’s all fine. She’s telling the truth anyway.”"

    "Grand Duke took a deep breath, and focused on the paper before him once again."

    gr "“Your Highness, I heartily suggest you to use this opportunity to teach the young lady some manners, it’s best if you nip this kind of behaviour in the bud.”"

    "(Young lady?)"
    "It was this arrogant boy who was young, not me."

    v "“Sorry to inform you {i}Grand Duke{/i}, but to be precise I am 386 years old.”"

    "He twitched, a shock going through his features, quickly and carefully hidden. His attention returned to the paper."

    gr "“How wonderful, how wonderful! You’ve spent all these years without learning proper manners.”"

    "(…)"


    a "“Ahem!”"

    "Asha must have realized how my mana had begun to gather up around me, because of my anger."

    a "“Let’s not fight, we are trying to work together after all.”"
    a "“Duke, please don’t forget that Vena is from another world, another culture. She’s not a disrespectful person, and is in fact Waceera’s favourite.”"
    a "“She is also the person that helps me the most.”"

    gr "“Hah…”"

    a "“Vena… Let me introduce you to the people we will work with.”"
    a "“His Highness the First Prince Lionel Nikolas Asquith…”"
    a "“His Highness the Second Prince Landon Cyril Asquith…”"
    a "“His Highness the Third Prince Andrel Xerxes Asquith…”"
    a "“And His Excellency the Grand Duke of Pertone, Marley Augustine Arkwright.”"

    scene academylivingroom with fade
    show Marley Irritated with dissolve:
        xpos 0.7 ypos 0 zoom 1.1


    m "“You left out the other titles and holdings of the Princes, not to mention you didn’t address them with proper courtesy.”"

    show Asha Confused at left with dissolve

    a "“Pardon?”"

    show Marley Sigh with move:
        yalign 1 zoom 1.1

    m "“Cyril is the Duke of Credale, and Xerxes is Millford’s.”"
    m "“And Lionel, Brefcaster’s.”"

    "He called those kids simply by their first names, something he would have scolded anyone else that did the same. They must be close, I realized."
    "And maybe the man also wanted to show his political strength off too, given how he spoke in such a fearless tone."

    show Asha Default with dissolve

    a "“Ah… I see.”"

    "(Why are you letting him walk over you Asha?)"

    hide Marley with dissolve
    pause 0.5
    show Cyril Irritated at right with dissolve

    c "“Please don’t listen to him, it’s really not important.”"

    hide Asha with dissolve
    pause 0.5
    show Lionel Default with dissolve:
        xpos 0.26 ypos 0 zoom 1.1

    l "“Yes, let’s not waste any more time with petty squabbles.”"
    l "“I assume you are all aware of the reason why we are gathered here tonight.”"

    "The room filled with murmurs of approval. In the meanwhile, Now that I was out of the spotlight, I got myself a seat out of sight in order to observe how all this would unfold."


    l "“{i}Marley{/i}, please explain the situation”"
    "There was a clear disdain in Lionel’s voice."

    "It was weird to see how people used each other’s first names to mock them in this world, and used their family names to honour them instead."
    "(What nonsense.)"

    hide Cyril
    hide Lionel
    with dissolve
    show Marley Neutral at truecenter with dissolve:
        yalign 1 zoom 1.2

    "Folding the paper, Marley threw it to the table before him in a rakish fashion."
    "He observed everyone else in the room while crossing his legs."
    "(Funny… The lowest rank among them was his, yet he held the title for being the most conceited as well.)"

    $Crimson_Bay.locked = False
    $Crimson_Bay.locked_persistent = False
    show text "A new Grimoire unlocked!" with dissolve
    hide text with dissolve

    m "“Whemond is the pride and joy of the Crimson Bay. If you don’t know, it’s high time for you to learn.”"
    m "“If something is going wrong in Whemond, it means something is going wrong with our trade.”"

    show Marley Eyesclosed with dissolve
    m "“Something going wrong in trading would not only anger us, but also our impatient customers beyond this land.”"
    m "“I don’t even talk about how such event would shake the Kingdom as a whole.”"

    "Marley’s words were dripping with condescending patience, as if he was addressing a room of children. His body language was another matter entirely; he looked like he might fly into a rage if this explanation took any longer than it needed to."

    show Marley Neutral with dissolve:
        yalign 1 zoom 1.2

    m "“The long-sustained, unshakeable peace of Whemond has been taking hits over the last year by things that were beyond our understanding.”"

    show Marley Frowning with dissolve:
        yalign 1 zoom 1.2

    m "“And what a coincidence! All these events have started to happen just before your arrival.”"

    "He paused heavily for dramatic effect. Asha, however, took the opportunity to speak up."

    show Marley Neutral:
        yalign 1 zoom 1.2
    show Asha Default at left with dissolve

    a "“Well, a few thousand years of peace of Silver Hollow against Aelthus’ a few centuries old peace… We are not in a good situation either.”"

    "Confused, Marley looked at her."

    m "“Thousands? I thought it was merely a thousand years since your people’s disappearance.”"

    hide Marley with dissolve
    hide Asha with dissolve

    "(…Ah.)"
    "Even for a brief time, what he said echoed in my mind."
    "I shouldn’t have been surprised any longer. It’d not been a secret that Asha and the others had been born in the Outer World ever since the last month."
    "Was it the fact that Waceera had lied to me that bothered me?"
    "(No, no… She must have had a reason, or she wouldn’t have done such thing.)"
    "I glanced around the room."
    "Considering most of the Light Bearers were as old as Asha, they must also have been born in this world."
    "Then why hadn’t they talked about it before?"
    "The answer was actually as clear as day. But I had a hard time admitting it."
    "(Because of the circles…)"
    "To distract myself from the grim thoughts trying to get ahold of me, I tried instead to focus on the room’s conversation."

    scene blackscreen with fade
    pause 1.5
    scene academylivingroom with fade

    "It took a while for meeting to reach an end. They had informed us about the state of Whemond briefly, and talked about the things they needed our help for."
    "(To the depths of Shore with Whemond! I wouldn’t care if the city was burnt to the ground.)"
    "We were supposed to report to them any unusual sightings."
    "Which reminded me of what had happened to Kioko earlier, Perhaps that was something to be reported. But then, how much could a prisoner trust to their guard?"
    "The only people who knew about Kioko’s relevance to the Black Massacre, other than Haru and myself, were Asha and Zuri."
    "Out of the corner of my eye, I looked at Almasi."

    show Almasi Default with dissolve:
        yalign 1 zoom 1.2

    "(I’ve no intention of throwing her to these wolves.)"

    hide Almasi with dissolve

    show Marley Neutral at truecenter with dissolve:
        yalign 1 zoom 1.2

    m "“…Yes. And with that, I am concluding this meeting.”"

    show Marley Eyesclosed with dissolve
    m "“But before that… We need two witches to assist me and Lionel, to deliver the reports…”"

    show Marley Cocky with dissolve
    m "“And to be the spokesperson of both sides.”"

    "(Witch…)"
    "This was what outsiders had been calling us."
    "Sometimes it was pronounced like a curse, and other times it was called like a fact known to everyone."
    "But I was aware of something."
    "No matter the reason it was used, there was always a shunning tone behind the word."
    "And I couldn’t help but feel uncomfortable."
    "…"
    "Marley stared at Asha."

    show Marley Mocking with dissolve:
        yalign 1 zoom 1.2

    m "“Earlier, you told me about your sister. I guess it would be the two of you that would work with us, or are you so busy that you would pass the job off to someone else?”"

    "There was a clear insinuation in those words, despite how kindly they were said. I gritted my teeth."
    "Asha on the other hand, giggled."

    a "“Haha, no. I will see to this myself, however Zuri… She’s not able to work for now, so instead…”"

    hide Marley with dissolve

    "I felt a hand on my back."
    "(You’re kidding me.)"

    a "“Vena, whom would you prefer to work with?”"

    "I genuinely gasped for a second, then cleaned up my act. Outrageous as it was, I was not going to sell her down the river."

    v "“You should pick first.”"

    a "“Youngsters first.”"


    menu:
        "There was no point in protesting. I glanced at the figures sitting across the room one by one again, and made a choice."

        "Lionel":
            jump venalionel

        "Marley":
            jump venamarley



label venalionel:


    "Getting along with the Royal family sounded more advantageous than having the favour of a Duke…"
    "And it was a task I shouldn’t leave in Asha’s hands."

    v "“Then I’ll work with the Li-… Prince Lionel…”"
    "Remembering to address them properly, I had quickly corrected myself."

    show Lionel Laughing with dissolve:
        ypos 0.05

    l "“Alright then… I think we will get along pretty well.”"

    "Even though I arched a brow at this statement, the Prince didn’t elaborate."

    hide Lionel with dissolve
    show Asha Default at left with dissolve

    a "“And I am working with the Grand Duke.”"

    show Marley Eyesclosed with dissolve:
        zoom 1.1 xpos 0.75 ypos 0.0

    m "“I will send a Bee at first light for you to take to the Arkwright manor.”"

    hide Marley
    hide Asha
    with dissolve
    show Lionel Default with dissolve:
        ypos 0.05

    l "“I will do so as well, for your arrival to the Palace, my lady.”"

    "{i}Lady{/i}… It’d been merely a day since our arrival at the city but I had realized already that everyone here was obsessed with titles."

    v "“I shall see you in the morning then, {i}my Prince{/i}.”"

    show Lionel Laughing with dissolve

    "Lionel laughed heartily at my response."
    "Upon reflection, spending time with a fine young man could be worthier of my time than aging a millennia in a single night with that grumpy Duke."
    pause 3.0
    return

label venamarley:

    "I couldn’t let Asha deal with that man. I had no doubt she would be eaten alive."
    "(Also someone should keep that man in check in case he proves to be more of a hindrance than a help.)"

    show Marley Sigh with dissolve

    "Narrowing my eyes, I glared at him. From the way Marley sighed, I sensed that he understood my intention."

    v "“I’ll work with the Grand Duke.”"

    show Marley Troubled with dissolve

    m "“You really wish to torment us both, don’t you?”"

    show Marley Irritated with dissolve

    m "“Fine then, so be it. Tomorrow, at first light, I will send a ship to collect you from the Academy.”"

    show Marley Sigh with dissolve

    m "“If you were to be late, the Arkwrights would withdraw their support for this project as a whole.”"

    "I smiled daringly."

    v "“‘Being late’ was not a phrase in my book before, and it still wouldn’t be if someone hadn’t restricted the usage of magic.”"

    hide Marley with dissolve

    "Asha sighed upon our exchange."

    show Asha concerned with dissolve

    a "“I hope this ordeal will be finalized before one of you attacks the other.”"

    show Asha ClosedEye with dissolve

    a "“In any case, it’s quite late. Let’s end this meeting here.”"

    pause 3.0
    return



return
