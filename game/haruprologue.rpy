define v = Character("Vena", ctc= "ctc_blink" , ctc_position="nestled")
define h = Character("Haru", ctc= "ctc_blink" , ctc_position="nestled")
define k = Character("Kioko", ctc= "ctc_blink" , ctc_position="nestled")
define a = Character("Asha", ctc= "ctc_blink" , ctc_position="nestled")
define al = Character("Almasi", ctc= "ctc_blink" , ctc_position="nestled")
define bbg = Character("Başka Bir Gümüş Oyuk Sakini", ctc= "ctc_blink" , ctc_position="nestled")
define obg = Character("Öteki Gümüş Oyuk Sakini", ctc= "ctc_blink" , ctc_position="nestled")
define dbg = Character("Another Silver Hollow Resident", ctc= "ctc_blink" , ctc_position="nestled")
define gr = Character("Grandük", ctc= "ctc_blink" , ctc_position="nestled")
define m = Character("Marley", ctc= "ctc_blink" , ctc_position="nestled")
define c = Character("Cyril", ctc= "ctc_blink" , ctc_position="nestled")
define l = Character("Lionel", ctc= "ctc_blink" , ctc_position="nestled")
define x = Character("Xerxes", ctc= "ctc_blink" , ctc_position="nestled")
define u = Character("???", ctc= "ctc_blink" , ctc_position="nestled")
define bks = Character("A Woman's Voice", ctc= "ctc_blink" , ctc_position="nestled")
define io = Character("Ionyr", ctc= "ctc_blink" , ctc_position="nestled")
define narrator = Character(None, ctc= "ctc_blink" , ctc_position="nestled")

init:
    $ flash = Fade(.25, 0, .75, color="#fff")

#GRIMOIRE ENTRIES ----------------------------------



#GRIMOIRE ENTRIES END HERE-------------------------------

label haruprologue:

    stop music fadeout 1.0

    scene blackscreen

    "The desire for the unknown surrounded my body with its flames."
    "And resistance was in vain."

    scene traincomp with fade
    show Kioko Eyesclosed:
        xpos 0.27 ypos 0.2
    show Vena Default:
        xpos 0.74
    with dissolve
    h "“It’s surprising to see that she can sleep.”"

    "Vena glanced at Kioko from the corner of her eyes and sighed."

    v "“And it’s surprising to see how you can be brimming with joy after all the things that happened.”"

    "I puffed out my cheeks in annoyance. "

    $Silver_Hollow.locked = False
    $Silver_Hollow.locked_persistent = False

    h "“We don’t get the chance to leave {color=#f00}Silver Hollow{/color} every day. This is a first-”"

    show Vena Frowning with dissolve

    v "“And the last.”"

    "I couldn’t finish my sentence before she interrupted me."
    "Every time she talked, her words grew more toxic, more wounding."
    "(This must be because of the state of our Circles… Acting normally might be the best approach here.)"

    "Thank the stars, she changed the topic afterwards."

    show Vena Looking Sideways with dissolve

    v "“She couldn’t sleep a wink these past few days due to the stress.”"

    hide Vena with dissolve

    show Kioko Eyesclosed with dissolve:
        zoom 1.5

    "I knew that. Even though our bond had become loose ever since, I was still feeling the roots of Kioko’s stress in my heart as well."
    "However I wasn’t able to soothe her."
    "These new feelings, which were complete strangers to me, had put me in a weird, confused state I couldn’t handle at all."

    hide Kioko with dissolve
    show Kioko Eyesclosed:
        xpos 0.27 ypos 0.2
    show Vena Frowning:
        xpos 0.74
    with dissolve

    h "“I think everyone here suffers from a similar problem.”"

    v "“Everyone except you.”"

    "(Here we go again.)"
    "Ever since we’d set foot on this world, Vena’s scolding had become ceaseless."
    "After glaring at her for a while I focused my gaze at somewhere beyond the window. Nowadays, whenever we argued there was this unfamiliar pang of pain I felt in my stomach, making me want to vomit."
    "Realizing that I was failing to comfort myself even after taking several deep breaths, I couldn’t help but ask permission to leave the compartment, which started to feel stuffy."

    h "“I will get some air.”"

    show Vena Arching Eyebrow with dissolve

    v "“Where are you going?”"

    "I stood up."

    h "“Just taking a walk in the aisle. My legs have gone numb.”"

    "Vena took a deep breath."

    show Vena Sigh with dissolve
    pause 1.0

    v "“Alright. Just don’t get yourself into any trouble.”"

    "I nodded slightly before opening the door and almost threw myself into the corridor."
    "It was surprising to see her to give me permission, and I didn’t want to risk it by wasting more time in the compartment."

    play sound slidedoor

    scene traincorridor with fade

    pause 1.0

    "The sunlight was fighting its way through the dirty glass, catching on my eyelashes like fire.  "
    "Where I’d come from, the sun had never risen in the sky. The glory of the day had always been bestowed upon the stars that hung over the deep blue sheets above."
    "Now, however this one big star reigned alone on the horizon; not allowing its siblings on the stage till the dusk."
    "(Well, I can’t read the stars anyways. It's not all bad though; this huge star gives more mana compared to the others.)"
    "The daylight coming from the sun made me feel powerful like nothing ever had before."
    "I’d been feeling this way ever since we had arrived here. The same sentiment must also be the case for the others."
    "(…)"

    "How angry would Vena get if she heard those thoughts. Thinking about the scolding I could get was enough to make me shudder."

    play sound walking

    scene traincorridor with fade:
        xpos 0.2 ypos 1.6 xanchor 0.5 yanchor 1.0 zoom 2

    pause 2.0

    stop sound

    "I got closer to one of the windows and putting a hand under my chin, I started to daydream while watching the everchanging view."
    "What kind of place was Whemond? How did people spend a day there?"
    "How did their houses look, what did they prefer to eat?"
    "All these questions were occupying my head."
    "And not just now, but they had been in my mind ever since the day we’d heard about the city, back in the small village that we had first sought shelter in."
    "My heart fluttered with the sweet things that the winds of freedom whispered."
    "However the calm state I finally maintained met its end once again thanks to the voice coming from behind me."

    u "“Haru? What are you doing here?”"

    "Slowly, I turned and forced a smile."

    h "“Just wanted to get some air Asha, how about you?”"

    show Asha Smiling with dissolve

    "Her signature know-it-all grin appeared on her face in return."

    a "“Oh, I am trying to make sure that no one leaves their compartment.”"

    h "“Ah… Hahah…”"

    "I began to scratch my back in an embarrassed way, which made Asha giggle. Taking her time, she came next to me steadily."

    show Asha Smiling at truecenter with dissolve:
        zoom 1.5

    a "“It’s okay, I can understand. The rooms are small and you feel like suffocated.”"

    "Asha’s eyes glowed with the traces of her mana while I was nodding at what she’d said."
    "An unfamiliar presence made itself known in my mind."

    show Asha Default with dissolve

    a "“But by contrast with everyone else, it’s not your fears that suffocate you. Even more, you’re excited, happy almost.”"

    "Nervously I bit my lip."

    h "“Vena gets angry at me because of that. She thinks that I’m disrespecting the dead.”"

    a "“I don’t agree with her. It was not only our sisters we lost. We also were torn out from our roots, floated in the wild wind with nowhere to go.”"

    show Asha Looking Sideways with dissolve

    a "“And found ourselves in the middle of this land, foreign, at least for you.”"
    a "“Not every person can react in the same way.” "

    show Asha Smiling with dissolve

    $Waceera_Entry.locked = False
    $Waceera_Entry.locked_persistent = False

    a "“However you should also put yourself in Vena’s place. {color=#f00}Waceera{/color} is very… Very dear to her.”"
    a "“Her strange disappearance, in such a dire time as this, has deeply upset your sister.”"

    "I tilted my head."

    h "“Do you seriously think she’s not dead?”"

    show Asha Eyesclosed with dissolve
    pause 2.0
    show Asha Smiling with dissolve

    a "“More like I hope she’s not. Making sure that no one’s drowning in such melancholic thoughts is my duty.”"

    u "“Melancholic? That shameless whore’s death could only be a matter of celebration.”"

    "(Ah, Almasi…)"
    "The quarrel which I felt like was about to start soon sent me into a panicked state once again."

    $Almasi_Entry.locked = False
    $Almasi_Entry.persistent_locked = False

    "{color=#f00}Almasi{/color} was walking towards us, each step as solid as a hammer."

    "Her coal-black eyes were fixated on Asha with a visible rage while her lips curved to let a sneer out."

    hide Asha
    show Asha Default:
        xalign 0.5
        linear 0.5 xpos 0.15
    show Almasi Default at right with dissolve

    $Night_Mother.locked = False
    $Night_Mother.persistent = False

    al "“What? Are you now the new {color=#f00}Night Mother{/color} since your useless sister is gone?”"

    "(Thank the stars Asha is a calm person.)"

    a "“That’s not an intention of mine. I am nothing but a shepherd that guides the little sheep out of the danger.”"

    "She sent me a meaningful smile after saying those."

    show Asha Smiling with dissolve

    "But it was not enough to convince Almasi, it seemed."

    show Almasi Frowning with dissolve

    al "“As you said, a shepherd is a guide. Not someone that puts leash on the sheep.”"
    al "“Little one, don’t let this woman poison your mind.”"

    "(Oh uh. Don’t involve me in this.)"
    "Not knowing what to say, my eyes wandered around the hallway, avoiding direct eye contact."

    hide Asha with dissolve
    hide Almasi with dissolve

    "I didn’t want to pick a side."
    "Surely if Vena was in my place, she could defend Asha very well."
    "Yet here I was, thinking Asha was not that innocent at all, even though Almasi was being incredibly belligerent. "
    "After a few seconds, Asha placed her hand on my shoulder gently."

    show Asha Smiling at truecenter with dissolve:
        zoom 1.5

    a "“Haru, you should return to your compartment.”"

    show Asha Looking Sideways with dissolve

    a "“You should as well, Almasi.”"

    show Almasi at left with dissolve

    al "“And since when have I been taking orders from you?”"

    show Asha Eyesclosed with dissolve

    "Asha sighed deeply."
    "(Even her patience has a limit.)"

    show Asha Default with dissolve

    $Whemond.locked = False
    $Whemond.persistent_locked = False

    a "“They could have banished us from these lands, yet they wish to assist us {color=#f00}in the capital.{/color}”"

    show Asha Frowned with dissolve

    a "“The only thing that was asked from us is that we follow their rules. Is it too hard to sit quietly without causing a scene for a few hours?”"

    show Almasi Frowned with dissolve

    al "“You can’t speak to me in that tone.”"

    show Almasi Angry with dissolve

    al "“Your spineless, good for nothing sisters and you might perceive ‘not being banished from these lands’ as a success but it’s nothing more than an insult for me.”"

    hide Almasi with dissolve

    "(This is not my fight, I don’t have to interrupt. I don’t want to burden myself with this.)"
    "I chanted silently to calm myself despite the tension between the two."

    hide Asha
    show Asha Frowned at right with dissolve
    show Almasi Angry at left with dissolve

    al "“Whemond had already been a home for us once, those are our lands. Pertone, the Divine Woods-”"

    show Asha Sighing with dissolve

    a "“Alma, that’s enough.”"

    "Unable to bear to witness the sparks between the two anymore, I stepped in."

    h "“Well… I am returning to my compartment.”"

    show Asha Default with dissolve
    pause 2.0
    hide Almasi with dissolve
    hide Asha with dissolve

    "There was a look in Asha’s eyes, almost saying “poor thing”. Passing the two with fast steps, I walked towards our compartment."

    scene traincorridor with dissolve:
        zoom 1.2
        xalign 0.75
        yalign 0.3
        linear 1 xalign 0.5
    pause 1.0

    al "“Don’t forget to send my regards to your Waceera-loving sister.”"

    "Her attitude was getting out of hand. Holding the doorknob, I started to talk without looking at her face."

    h "“No, thanks. Though you can tell her about your complaints yourself.”"

    play sound slidedoor

    scene traincomp with fade
    pause 2.0

    show Kioko Neutral:
        xpos 0.27 ypos 0.2
    show Vena Irritated:
        xpos 0.74
    with dissolve

    v "“Did something happen? I heard someone yelling.”"

    "It was surprising to hear Vena ask that, since she had a habit of using her powers to eavesdrop on other's conversations."
    "Anyways, this at least meant I didn’t have to deal with her temper for now."

    h "“The usual arguments, you know. Nothing else.”"

    hide Kioko
    hide Vena
    with dissolve

    "Vena first arched her brow, then shrugged which I assumed for to show that she wouldn’t chase it."
    "And I let the pit made from my nightmares envelop me into a deep slumber afterwards."

    scene blackscreen with fade
    pause 1.0

    "The clock had almost reached midnight when we arrived in Whemond."

    $Royal_Academy.locked = False
    $Royal_Academy.persistent_locked = False

    "That we had been led to the {color=#f00}Royal Academy{/color} in a rush had made me a little upset since I was looking forward to see the capital, but at least the city could be perfectly viewed from our room. "
    "Also on the plus side, the Academy didn’t look like anything I’d seen before."
    "Everything was so different than our rustic, isolated woods; the ornaments, decorations, the atmosphere…"

    scene whemond with fade

    a "“Ladies, if you’re this impressed already, I can’t imagine your reactions over the sunset! It always looks like the sun bleeds right into the sea.”"
    a "“And in the dawn, it is gloriously reborn from the blood coloured tides to light the sky once more.”"
    a "“Alas, I have to admit… Almost everything has changed since I was here the last time.”"

    v "“A disgrace is what this place is. There’s not a single thing to be impressed about.”"
    v "“Not once did I think that the light magic could be used in such a useless way.”"

    "I couldn’t find the strength to argue with her. I was tired, however it turned out that Kioko loved the scenery beneath us just as I."

    k "“Well, I… I think the lights look pretty.”"

    "I turned to her in pure astonishment. It was not like Kioko to voice her thoughts that opposed Vena’s."
    "Even though a snort left her nostrils, Vena didn’t take it further. Asha was giggling in the meantime."

    a "“Don’t worry, you will have the opportunity to go on a trip into the city after things have settled more I think.”"

    play sound loudthud
    pause 1.0
    scene whemond with vpunch
    "(!)"
    "A sudden sound coming from Vena’s side made all of us turn to her."

    scene academylivingroom with fade
    pause 0.5

    show Vena Irritated with dissolve

    v "“Asha, I beg you to not to put such atrocious thoughts into anyone’s mind.”"
    v "“Not Haru’s, nor Kioko’s, nor anyone else’s.”"

    show Vena Irritated:
        xalign 0.5
        linear 0.5 xpos 0.8
    show Asha Default at left with dissolve

    a "“What’s the problem? We can arrange a one-day trip.”"

    show Vena Angry with dissolve

    v "“Absolutely not.”"

    show Vena Frowning with dissolve

    v "“We are in a very difficult time that requires extra care. The reason why all this happened in the first place is still a mystery.”"

    show Vena Angry with dissolve

    v "“Unless they have a death wish then our people should never leave this Academy.”"

    show Vena Frowning with dissolve

    v "“In fact, even if it’s exactly what they wish for, you still shouldn’t let them. As a leader it’s one of your priorities to seek everyone’s safety, Asha.”"

    show Vena Looking Sideways with dissolve

    v "“Let alone we are not here to amuse ourselves, we have casualties.”"

    "A pause followed her words. Curiously, I stared at Vena, and then at Asha."
    "(If a fight breaks out I am fleeing to my room.)"

    show Asha Grinning with dissolve

    "But instead of the anticipated quarrel, there was Asha’s laughter."

    a "“You’re just like Waceera.”"

    show Vena Frowning with dissolve

    v "“How nice it is to see that you can laugh. You shouldn’t dismiss the importance of this situation. Especially with Almasi being on your tail like this, looking for any possible mistake you might make.”"

    show Asha Smiling with dissolve

    a "“It seems you don’t see me as worthy of your trust as Waceera.”"

    show Vena Eyesclosed with dissolve
    pause 2.0

    "Before giving a response, Vena closed her eyes and paused a little bit."

    v "“I am speaking up for your own good, please don’t turn it into a competition.”"

    a "“That I won’t, let’s just say I’m stating a fact.”"

    show Asha Eyesclosed with dissolve

    a "“Oh Vena… There’s no reason for you to worry. We will find Waceera, and get back to Silver Hollow. I can assure you.”"

    "She glanced over the room. When no answer was given, Asha put her shawl on, then stood up."

    hide Vena with dissolve
    show Asha Eyesclosed with dissolve:
        zoom 1.5

    a "“I shouldn’t bother you three anymore. It is time for you to sleep.”"

    show Kioko Laughing at right with dissolve

    k "“You still act like we are little kids, Asha.”"

    show Asha Default:
        xalign 0.2
        linear 1 xpos 0.6

    "Gently, Asha ruffled Kioko’s hair."

    a "“That is because you are little children from my perspective. And you will always remain as such for me.”"

    pause 1.0
    hide Kioko with dissolve
    hide Asha with dissolve

    play sound doorclose

    "(Children…)"
    "She’d spoken just like the mothers of little children in the village that we had stayed at before arriving to Whemond."
    "The reason for it might be that Asha had grown up here in the Outer World, instead of Silver Hollow."
    "Because the “mother” notion had come into my life upon our arrival to Aelthus."
    "Though I suppose I had sometimes seen Zuri's eyes filled with a strange yearning whenever she looked at Kioko."
    "(Ah… My own mother…)"

    scene blackscreen with flash
    pause 2.5
    scene academylivingroom with flash

    "…"
    "As if the bad memories had physically turned into a lump in my throat, I forced myself to swallow them down."
    "Then met Vena’s gaze."

    h "“So… We are returning to our rooms?”"

    "As I spoke, something I realized made my mood change drastically."
    "This marked the first time I was going to sleep without my sisters, alone."
    "(Would it make me a bad person to feel a little excited about this?)"

    show Vena Default with dissolve:
        xpos 0.74

    v "“You two can leave. I still have work to do.”"

    show Kioko Default with dissolve:
        xpos 0.27 ypos 0.18

    k "“Please don’t tire yourself out.”"

    hide Vena
    hide Kioko
    with dissolve

    "After agreeing with Kioko’s remark and wishing a good night, I saw myself out."

    scene academybedroom with fade
    pause 2.0
    scene academybedroom with dissolve:
        ypos -0.1 zoom 1.5

    play sound sitting

    "Only when I sat down on the soft sheets did I notice how tired I actually was."
    "Still, the sweet call of sleep was not enough to stop me from watching the city laid out beyond the glass."

    scene whemond with fade

    "(Whemond…)"
    "(Since Vena’s not here, I can watch it to my heart’s content.)"
    "With the enthusiasm of a little kid, I leaned on the windowsill and began to daydream."
    "How did the city look with the morning light? What if they adorned the plaza with flowers and garlands in festivals?"
    "Could we stay here to join a celebration anyway? When would they let us go outside? I wanted to meet with the local folk and run in the streets so bad that I could almost feel the cobble stones beneath my feet."
    "There was also the famous “bleeding sun” view too."
    "Were I not exhausted I would have waited till the dawn, and checked it to see if it was as glorious as people had said."

    scene academybedroom with fade:
         zoom 1.2

    "(But now, I should sleep.)"
    "(After all, tomorrow is a busy day.)"

    scene blackscreen with fade
    pause 3.0

    scene academyclass with fade
    show Vena Eyesclosed with dissolve:
        xpos 0.3 ypos 1

    play sound commotion
    pause 4.0
    stop sound

    v "“For the last time Haru, you have to leave this alone.”"

    h "“I’m asking just out of curiosity, curiosity!”"

    hide Vena with dissolve

    "As if she was running away from me, her steps quickened."
    scene academyclass with vpunch
    "I ran towards Vena and grasped her arm."

    play sound sitting

    h "“Vena!”"

    show Vena Looking Sideways with dissolve:
        ypos 1.6 zoom 1.5

    "Finally her attention returned to me."
    "She looked distracted."
    "Whatever was running through her mind made Vena give up with a deep sigh."

    show Vena Eyesclosed with dissolve:
        ypos 1.6 zoom 1.5

    v "“Haru, listen.”"

    "Catching my two hands in hers, she guided them to her heart."
    "This made me realize how much I missed her warmth since we had done nothing but arguing for a long time."

    show Vena Concerned with dissolve

    "However when I peeked up at Vena’s eyes, I saw the traces of concern instead of the affection I sought."

    v "“If I told you that I understood what you are actually going through, that would be a lie.”"

    show Vena Looking Sideways with dissolve

    v "“I can’t understand your current mood in any way.”"
    v "“I can’t tell if a storm is raging in your head and you’re not showing it, or if your mind is as calm as the sea on a sunny day Haru.”"

    show Vena Sigh with dissolve

    v "“But you should never put yourself in such position, nor us.”"

    "Taking a deep breath, I slowly freed my hands from Vena’s."

    show Vena Default with dissolve

    v "“We don’t know how improved this ‘Magitech’ of theirs is.”"
    v "“But given how plain, far from complicated your magic is I can tell that there’s a great chance of you getting caught.”"
    v "“So don’t ever try to do that.”"

    hide Vena with dissolve

    play sound walking

    "I didn’t want to hear what she was saying any longer."

    v "“Haru, did you hear me?”"

    h "“Yes, yes…”"

    "She was right next to me after all. It was impossible to not to."

    stop sound

    scene academyclass:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.2

    play sound sitting

    "Gently, I pushed through the crowd to reach an empty seat. Vena took the one next to mine as well."
    "Today Kioko was absent. And to be honest, that was the usual."
    "Before, Waceera hadn’t let her participate in the meetings. And today, she had simply stated that she was too worn out to join."
    "(I wish I could skip the meetings like that too.)"

    "Vena had brought a memory stone with her to record the contents of the meeting and show those to Kioko later."

    "However, I knew Kioko, and it was obvious to me that she was only going to accept the stone out of kindness, and would never actually check the memory out."
    "And even if I could see that happening, Vena probably had to be aware of that possibility too."

    scene academyclass
    play sound doorclose

    show Zuri Default at left with dissolve
    show Asha Default at right with dissolve

    "My thoughts were interrupted at that moment with Asha and her sister’s entrance to the classroom."

    hide Zuri with dissolve

    show Asha Default:
        xalign 0.8
        linear 0.5 xpos 0.6

    "While Asha was busy getting on the stage and checking the people in the room, Zuri took a seat on the front row."

    a "“Nice… You’re all here- oh, except one person.”"

    "She looked at our way to emphasize her words."

    show Asha Looking Sideways with dissolve:
        ypos 1.5 zoom 1.5

    a "“Which is okay.”"
    a "“I promised you that once we arrived to Whemond, I would try to answer whatever questions you may have.”"

    show Asha Default with dissolve

    a "“And today, I am here to keep my word-”"

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    al "“You can start with explaining why you think your sister might be alive.”"

    "Vena seemed angrier at this claim than Asha did."
    "A total silence followed Waceera’s words, and everyone was curious about how Asha was going to answer."

    hide kiokoeye with dissolve

    show Asha Sighing with dissolve
    pause 2.0
    show Asha Default with dissolve

    a "“There’s no point in lying.”"
    a "“The circle which I, Waceera and Zuri shared was looser than the others.”"

    play sound commotion

    "Honestly, it was not shocking to hear that after all the things we’d been through in the last month."
    "Funny how this kind of scandal was the new normal for me."

    stop sound

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    al "“So you admit the fact that you made us live like puppets while benefitting from the system this whole time, right?”"

    show Asha Eyesclosed with dissolve

    a "“…”"

    show Asha Default with dissolve

    a "“I wouldn’t call it benefitting.”"

    show Asha Eyesclosed with dissolve

    "“This was Waceera’s decision. To provide us longer lives…”"

    al "“Nonsense!”"

    show Asha Default with dissolve

    a "“My only responsibility at this meeting, is telling you the truth.”"

    show Asha Frowning with dissolve

    a "“The reasons behind Waceera’s actions are things that you can only learn from her.”"

    show Asha Eyesclosed with dissolve

    a "“I know this might get you irritated, but I have no other answer than this to give.”"

    show Asha Looking Sideways with dissolve:
        ypos 1.0 zoom 1.0

    a "“Therefore, I would suggest you to keep your provocations for her return.”"

    hide kiokoeye with dissolve
    hide Asha with dissolve

    "Normally, meaning in our case, circles blended its members’ individual identities into one collective unit."
    "They helped us to understand each other better, strengthen our spells, lengthen our lives, and not dwell on things that were “unnecessary”…"
    "As a side effect though, when one of us got an injury, all of us had the same scar too…"
    "…And when one of us died, then all of us died."
    "After the Black Massacre had taken place and Waceera had disappeared, we’d felt reassured to see the other two sisters had been safe and sound since they shared the same circle."
    "Though things had changed when one morning Asha had blurted out the possibility of Waceera’s death."
    "Drawing a deep breath, I brought my hands up to the sides of my head."

    play sound commotion

    "A symphony of chaos was taking place in the room with Almasi’s yellings and her applauders."
    "I didn’t want to listen to that. No, I was downright refusing to. What had been done, had been done. There was no point in discussing it forever."
    "So my focus shifted away from the clamour and onto the details of the room instead."

    stop sound

    scene academyclass:
        zoom 1.2

    "These desks must belong to the students of this Academy."
    "Back in Silver Hollow, the disdain I felt for our theoretical lessons had been so strong even with the existence of the circle. The ambiance here might even encourage me to study."
    "Slowly, I traced the wood with my finger. Carved letters, formulas and charts that I couldn’t make much of, were on the surface."
    "When I raised my head again to look at the classroom, a figure standing in the doorway caught my attention."

    scene academyclass with dissolve:
        zoom 1.0

    show Ealdwine Default with dissolve:
        ypos 1.2 zoom 1.2

    pause 2.0
    hide Ealdwine with dissolve
    show Ealdwine Default with dissolve:
        xpos 0.74 zoom 1.0

    "I had never seen that person before, and they were not one of us."
    "Lightly, I nudged Vena with my elbow."

    h "“Vena, who is the person over there?”"

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“I don’t know, but that’s the uniform of the Academy.”"

    hide kiokoeye with dissolve

    "Ah, before our arrival, Asha had told us that the Kingdom would watch our every move."
    "Because of that, it sounded logical to me that this person was listening to this boring meeting of ours because of the task they had been given rather than their own will."
    "The person’s facial features reminded me of a kid’s. The white hair which fell on their shoulders looked so silky, as if it was made of cotton."
    "A bewitching aura surrounded them that could easily capture people."
    "But also, it confused me to no end."

    h "“Vena…”"

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“Hmm?”"

    h "“That person… Do you think they are a girl, or a boy?”"

    hide kiokoeye with dissolve

    "Since we’d only had “women” in Silver Hollow, “men” were an enigma for us."
    "The first thing I’d noticed had been how their voices were bolder than ours, as the wind had carried the tunes for me."
    "Their chests were as flat as solid walls, and some gentlemen’s height seemed almost tall enough to compete with poplars."
    "The chins they took pride in were strong and the features that graced their faces were angular."
    "Every one of them seemed to be ready to bring down the mountains if it was needed. Actually, even if they were weak, they looked confident enough to try."
    "Or maybe they simply acted like that since that was what was expected from them."
    "However this youngster standing on the doorstep, did not look like a woman or a man. It was almost as if they were stuck between the two."
    "After checking them over for a moment, Vena spoke."

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“I don’t know.”"

    "Her voice had a confused tone. It was funny to find out there were things that even Vena would get befuddled over."

    v "“I think he’s a man.”"

    h "“I guess.”"

    hide kiokoeye with dissolve

    "Once again, my eyes were on the stranger. Putting my chin in one hand, I started to watch them."
    "A boy or a girl, they were cute either way."

    show Ealdwine Surprised with dissolve

    "After a while though, the person turned their head in my direction and our gazes met."

    hide Ealdwine with dissolve

    scene academyclass with hpunch

    "With the panic of getting caught, I hurriedly tried to fix my posture and look somewhere else."
    "…Which caused me to accidentally knock the memory stone off the desk."
    "But thanks to my reflexes I caught the stone mid-air with a quick burst of wind magic, and landed it in my hands."

    v "“Be careful, Haru.”"

    h "“Sorry.”"

    show Ealdwine Grinning Eyesclosed with dissolve

    "When I glanced at the stranger again, I saw them laughing at me."
    "(…How embarrassing.)"

    scene sundown with fade

    "The rest of the day was spent on various tasks and chores that needed to be done in the Academy."
    "(Open this box, count those supplies, check if anyone needs anything, ask them if they are happy, etcetera, etcetera…)"
    "Though when the time came for the sun to set, I dropped what I was working on and got a place in front of the window."

    play sound seagull

    "(So? The sun’s about to disappear in the horizon! Don’t tell me that this dull sky was what you described as “bloody”.)"

    scene blackscreen with fade

    "While I was complaining about being misinformed, the sun got even closer to the sea and suddenly the world around me changed."

    scene sundown with fade

    "(Ooh…)"
    "(Wow…)"

    h "“Everything looks red!”"

    "I mumbled aloud in surprise."
    "I was not sure which shocked me more; the change of the sky, or the crimson shade of the sea, or the scarlet sun that really looked as if it was bleeding."
    "And this scenery unfolded every day before the citizens of Whemond."
    "Two times at that… To them, this was simply normal."

    h "“Hah…”"
    stop sound

    "(How could this be “normal”?)"
    "I held out my hand. The red sunlight was dancing on my skin, gathering more power under it than I could have ever done before."
    "One could never run out of mana in a place such as this."
    "The magic was almost materializing in the air."
    "Yet from what I’d heard, the people here were so distant from it, even for how they were graced by its presence every single day."
    "(How ironic…)"
    "Taking a deep breath, I admired the view one last time before getting back to work."
    "I couldn’t help but think about the bitter emotions I was going to feel if we ever left this place."

    scene academylivingroom with fade
    pause 1.5
    show Kioko Default:
        xpos 0.27 ypos 0.18
    show Vena Default:
        xpos 0.74
    with dissolve

    v "“…That’s all. You can see the rest with the memory stone.”"

    k "“Thank you, Vena.”"

    hide Kioko
    hide Vena
    with dissolve

    "We were eating the food that Asha had handed us."
    "Deep down I felt upset over how busy the day had been."
    "(Kioko is so lucky.She spent the whole day laying in her room. And no one dares to question it too!)"
    "At least this settling in madness was going to end soon."
    "After that point, the rest of our problems would be on the shoulders of our Light Bearers."
    "(Maybe this would give me the chance to slip away from the Academy.)"
    "Seriously, I didn’t wish to be trapped in here for stars know how long."

    show Kioko Eyesclosed with dissolve:
        xpos 0.3 ypos 0.18

    k "“I… Want to tell you something.”"
    k "“But please don’t panic.”"

    "My spoon froze mid-air while I stared at Kioko curiously."
    "Vena also set her plate aside, preparing herself what was to come."

    k "“…”"

    "(Nice, we’ve already panicked.)"
    "And here I’d been having silly dreams of slipping away. Great."

    show Kioko Neutral with dissolve

    k "“I think…”"

    show Kioko Concerned with dissolve:
        xpos 0.265 ypos 0.18

    k "“I think I saw someone in my room today.”"

    "I couldn’t help but gawk at her."

    h "“What?”"

    show Vena Frowning with dissolve:
        xpos 0.74

    v "“Who?”"

    show Kioko Concerned with dissolve

    k "“I-I don’t know.”"
    k "“It might have been a dream, I’m not sure.”"

    "Just like any other time she was distressed, Kioko began to bite her nails."
    "Vena then leaned and took Kioko’s hand away from her mouth."

    show Vena Default with dissolve

    v "“Kioko, calm down.”"

    k "“I had just woken up, and I realized someone was in the room with me. She was standing next to the window.”"

    show Vena Arching Eyebrow with dissolve

    h "“What did she look like? Couldn’t she be just one of your friends?”"

    show Kioko Gasping with dissolve:
        xpos 0.3 ypos 0.18

    k "“No! No… I don’t have a friend like that.”"

    show Kioko Eyesclosed with dissolve

    k "“She had ginger hair. But I couldn’t see her face clearly, for I was sleepy.”"

    "Unable to restrain her hands, she started to gesture frantically while talking."

    show Kioko Concerned with dissolve:
        xpos 0.265 ypos 0.185

    k "“She walked towards me. I was so scared that I couldn’t move! I must have passed out from sheer fright. When I opened my eyes again, time had passed and she was gone.”"

    "Once again, Vena reached to my young sister and placed her fingers on Kioko’s temple."
    "(Ah, she’s going to watch her memories.)"

    v "“If it is alright, I’ll take a look myself.”"

    show Kioko Eyesclosed with dissolve:
        xpos 0.3 ypos 0.18

    "Nodding, Kioko got herself ready for the coming intrusion."

    hide Vena
    hide Kioko
    with dissolve

    "Shortly after, a faint blue light began to glow from both Vena’s fingers and eyes, proving that the spell had started."
    "Psychic magic was Vena’s profession."
    "I was always bewildered at how these complex spells that needed a steady focus and lots of mana were as easy as breathing for her."
    "(Envying… Now that’s a different subject.)"
    "My heart held none of it because I couldn’t forget Asha’s words on this type of magic:"

    scene blackscreen with fade

    show Asha Eyesclosed with dissolve

    a "“People who want to improve themselves on this field also invite madness to loom over their bed.”"

    hide Asha with dissolve

    scene academylivingroom with fade
    pause 1.5

    "It was not easy. No, not even close to easy…"
    "Spend too much time on playing mind tricks, and soon the line between reality and lies would become blurry."
    "I didn’t think Vena would ever reach that phase thanks to her unshakeable nature."
    "Yet, even she sometimes delved into people’s dreams unintentionally, or at least the dreams of those who occupied her thoughts most often."
    "(Well, we are used to it. But if it ever happens here she might find herself in trouble.)"
    "Maybe what made her so tense was that she could feel others’ emotions and thoughts all the time."

    pause 2.0

    "Before long, Vena withdrew her hand and put some distance between herself and Kioko."
    "Curiously, I stared at the two."

    show Kioko Neutral:
        xpos 0.3 ypos 0.18
    show Vena Looking Sideways:
        xpos 0.74
    with dissolve


    v "“Either you saw someone who then clouded your memories, or it really was just a dream.”"

    h "“Can’t you tell the difference, Vena?”"

    show Vena Default with dissolve

    "This could be a first."
    "(Or a second… If we counted what happened to Kioko back in the Silver Hollow.)"
    "She shook her head as an answer."

    h "“Could they be someone from this Academy?”"

    show Vena Frowning with dissolve

    v "“I’m not sure. She wasn’t wearing any uniform, and didn’t look like one of our people. Kioko, why didn’t you inform us sooner?”"

    show Kioko Eyesclosed with dissolve

    k "“I didn’t want to cause an unnecessary scene.”"

    show Vena Concerned with dissolve

    "Quickly, Vena grabbed Kioko’s hand."

    v "“Don’t ever think like that. These are rough times, you should inform us of anything you suspect.”"

    "We grew silent for a while."

    h "“This is so weird. What are we going to do?”"

    show Vena Looking Sideways with dissolve

    v "“I…”"

    "Vena drew a breath."

    show Vena Default with dissolve

    v "“Kioko, would you like to sleep in my room for now?”"

    show Kioko Gasping with dissolve

    k "“I don’t want to be a burden.”"

    show Vena Frowning with dissolve

    v "“Oh hush, you’re my sister.”"

    show Kioko Concerned with dissolve:
        xpos 0.265 ypos 0.18

    k "“But wouldn’t I be in the way of your work?”"

    show Vena Eyesclosed with dissolve

    v "“No, you’re my priority.”"

    hide Kioko
    hide Vena
    with dissolve

    "This must be the part which I should intervene by saying I would take the responsibility for Kioko."

    $Light_Bearer.locked = False
    $Light_Bearer.persistent_locked = False

    "With that, Vena could carry her tasks as a {color=#f00}Light Bearer{/color} and wouldn’t worry herself over us."
    "But I…"
    "(Hah…)"
    "Looking after Kioko was not an easy job."
    "She was probably the only person that could unveil the mysteries of the Black Massacre."

    $Ashas_Prophecy.locked = False
    $Ashas_Prophecy.persistent_locked = False

    $Kiokos_Confession.locked = False
    $Kiokos_Confession.persistent_locked = False

    "For now, the only ones who had known of {color=#f00}Asha’s prophecy{/color} and {color=#f00}Kioko’s confession{/color} were me, Vena, Asha, and possibly Zuri."
    "What if another person, let’s say someone or something related to the Black Massacre was after Kioko? How was I going to protect her in such an occurrence?"
    "And if I were to set all these excuses aside…"
    "I didn’t want my hard-earned freedom to be taken from my hands just like that. For the first time in my life I was going to be on my own, even if that was limited."
    "It was selfish of me, yes, but I resented the idea."
    "So I decided to not to object."

    show Vena Default with dissolve:
        xpos 0.3

    v "“Then I need to notify Asha that I won’t be able to join the Light Bearers’ meeting.”"

    "Gulping, I lowered my head and stared at my hands."
    "(Don’t feel guilty, don’t feel guilty.)"

    scene academybedroom with fade
    pause 2.0
    scene academybedroom with dissolve:
         zoom 1.2

    "After spending more time in the common room, we went to our own separate rooms."
    "{i}Phew{/i}… What a busy day it had been!"
    "Privacy at long last."
    "I’d been watching the city that was alive right under my feet for a while, reflecting on the events of today."

    scene whemond with fade

    "The clock had struck midnight a long time ago. But I wasn’t sleepy at all."
    "People had been rattling in the streets all night. Sometimes wind carried the voices of the drunkards, and the other times it was the whispers of the secrets that were told under the security of the pitch black night."
    "After a few hours though, the lights that illuminated the shops were put out one by one, and most of the citizens went back to their homes."

    scene academybedroom with fade:
         zoom 1.2

    "It must be fun."
    "An independent life that was free of chains, anxiety, abnormalities…"
    "How wonderful that must be to do whatever you wished whenever you wished."
    "Drowning in my troubles, I pressed my lips firmly together."
    "My knuckles went white from clasping them around the windowsill with too much force in the meanwhile."
    "Why couldn’t we have this life, this freedom too? Now that the Silver Hollow was gone, nothing held us back from blending in the outside world."
    "(You shouldn’t think like that, you shouldn’t think like that.)"
    "Getting up, I climbed and sat on the windowsill."
    "My mind was busy with the talk I’d had with Vena today."

    scene academyclass with flash
    show Vena Default with dissolve

    h "“Guess they wouldn’t let us out, hm Vena?”"

    v "“More like they would hold us prisoners here until the day we return home.”"

    show Vena Eyesclosed with dissolve

    v "“If they let us return at all…”"

    show Vena Default with dissolve

    h "“Why wouldn’t they if they don’t want us here? I think you’re worrying over nothing.”"
    h "“Do you think we can go outside in secret?”"

    show Vena Frowning with dissolve

    v "“…”"

    hide Vena with dissolve

    scene academybedroom with flash:
         zoom 1.2

    "After my last question, we had argued."
    "What kind of monstrosity could be outside anyway? No one would dare to touch me with the guardians and the sheer number of witnesses down there."
    "On the other side, if I sneaked out, got myself in trouble and had to ask for help, I was going to be caught red handed."

    scene academyclass with flash

    show Vena Sigh with dissolve:
        xpos 0.3

    v "“But you should never put yourself in such position, nor us.”"

    scene academybedroom with flash:
         zoom 1.2

    "I bit my lip in a nervous fashion."
    "Vena and Kioko must be asleep now, meaning if I wanted to see the city there couldn’t be a greater opportunity than tonight."
    "However going outside…"
    "Narrowing my eyes, I looked in the direction of the city."

    scene whemond with fade

    "There was a magic barrier surrounding the Academy."
    "{i}Funny{/i}… What would be considered a masterpiece by this world’s standards was such a callow piece of work for us that even I, not the brightest scholar, could pick out the flaws in the spell easily."
    "Still, flying through the barrier was out of question."
    "Also, there were probably incantations set in the grounds of the Academy to detect any teleportation magic."
    "So from Vena’s perspective, it was impossible for me to go out without getting caught."
    "The corners of my mouth tugged upward upon this thought."
    "How surprised Vena would be if she knew about the number of times that I had snuck out back in the Silver Hollow. And I was sure that the same trick would work in this case too."
    "On the other hand, it was nauseating to think about the nagging I would receive from Vena if I got caught."

    menu:
        "(…)"

        "I want to go out.":
            jump outside

        "Maybe I should stay inside.":
            jump inside


label outside:

    "(Just once… I don’t think it will be a problem if it’s for once. I would come back soon and stop bothering people with my fixation.)"
    "I extended my hand towards the outside."
    "The wind began to gather in my palm, then my fingers started to turn into particles of dust."
    "First my hands, feet, arms and whole body followed shortly after."
    "And finally, I was one with the breeze."

    scene sundown with fade

    "(It always feels like the first time.)"
    "Every time it felt like I was free from the chains that kept me bound to the ground."
    "I rose and rose into the night sky and passed the barrier easily, proving my earlier anticipation right. Far above the city, I was dancing with the wind and the clouds."
    "I had discovered this talent of mine in my much younger days. As far as I knew, no one else in our village was able to do this."
    "And my friends who’d known of it were already-"
    pause 2.0
    "No, such thoughts were not welcomed now."
    "I had a more important mission at that moment: Spending this night having fun."

    scene whemond with fade

    "Turning down, I glanced at the city again. The distance between me and the Academy grew quite wide."
    "All these big houses, well paved roads, the ships that were moving on the land or in the sky were firsts for me. Actually, even this broad sea was a first."

    scene whemond with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    "The 83 years of my life had been spent in a forest with log cabins, breathing the same air with the same faces, and bathing in a grey coloured dull lake."
    "The sun had never risen there even for once, the sky had always had the same tint no matter what time of the day we’d been in."
    "How could it be possible to not get excited for the Outer World when one were in my shoes?"

    scene whemond with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.2

    "(Alright… Now that I managed to sneak out, where should I land?)"
    "A place hidden from view was probably the best choice."
    "It also should not be far from the town centre."

    scene whemond with dissolve:
        xpos 0.8 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.2

    "I focused on an alleyway surrounded with massive buildings. The structures almost looked too enormous to be individual houses and I was not sure if they were.  The street was also not that far away from the illuminated areas that I wished to visit."
    "I started to descend."

    scene whemond with dissolve:
        xpos 0.8 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.5

    pause 1.0
    scene alleyway with fade

    "From the looks of the things, there was no one around. I got closer to the ground."
    "Starting with my fingertips, my body began to materialize to its full form then."
    "(Hehehe… No problems so far, great!)"
    "Now, where was the market square-"
    "{i}…Huh?{/i}"
    "The voices from a group of people startled me, so I pulled my hood up immediately."
    "If someone happened to see me, I should act normal and not draw attention."

    play sound walking

    "Walking casually at a slow pace, I let the wind carry what was being spoken to my ears."

    stop sound

    bks "“Xerxes, you shouldn’t have come here at this hour.”"

    x "“Can’t I miss my fiancée?”"
    x "“Lea… I am so in love with you that every night that passes without seeing your face even once is a torment for me.”"

    "(Aha! How interesting, how interesting!)"
    "I changed my direction to the source of the voice, rather than fleeing. Love, romance, those were very distant notions for me and the other residents of the Silver Hollow."
    "I couldn’t help but feel curious."
    "I was going to have just a peek and then return."

    play sound walking

    scene alleyway with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    pause 1.5
    stop sound

    "The voices were coming from an enormous garden surrounded by iron bars."
    "But what surprised me was the figure that crouched before bars. Apparently there was another audience of the event."

    show Cyril HoodDefault with dissolve

    "(Here, I am not weird! Other people are also watching.)"

    hide Cyril with dissolve

    "As silently as possible, I walked over to stand beside the hooded person. The man named Xerxes, and the woman named Lea were hugging each other amidst a garden full of roses."
    "Thinking it was a good idea to share my thoughts, I slightly leaned to the other stranger that was busy watching them."

    h "“Isn’t it beautiful? This is the first time I’ve witnessed such event-”"

    scene alleyway with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    play sound sitting

    "But at that moment, the hooded figure jumped to his feet and-"

    scene alleyway with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    show Cyril HoodSword with dissolve

    "And swung his sword at me!"
    "If I was not fast enough it could have sliced me in half!"
    "(What should I do? Maybe cast a spell?)"

    show Cyril HoodDefault with dissolve
    pause 1.0
    show Cyril HoodDefault with dissolve:
        ypos 1.5 zoom 1.5
    pause 0.5
    hide Cyril

    "Yet before I could decide, the man grabbed me, and began to drag me to the other end of the street while his hand was covering my mouth."

    scene alleyway with dissolve:
        zoom 1.0

    "A distant voice echoed in my ears."

    x "“Who’s there?!”"

    "I wanted to cry for help."
    "Though no matter how much I shook, or struggled, it was not possible for me to free myself from the iron grip of the stranger’s arms."
    "(Good job Haru… Not even five seconds passed and you got yourself in trouble.)"
    "There was no other choice than to bear out the consequences."

    pause 3.0
    return

label inside:

    scene academybedroom with fade:
         zoom 1.2

    play sound sitting

    "With slow movements, I backed away from the window."
    "Perhaps this was a bad idea after all. It was actually easy to get out from the Academy, and then to come back."
    "But what if something unexpected took place down there?"
    "What if Vena realized that I was absent? What was going to happen then?"
    "The worst of all was the possibility of a conflict occurring between Aelthus and our ranks because of me."
    "Then Vena would give me an earful about it and I wouldn’t be able to shut her up."
    "They would never let me out after that, and I would be stuck in here forever."
    "I closed the window as if I was bidding farewell to my dreams, then flopped down on the bed."

    scene academybedroom with dissolve:
        zoom 1.0

    "(Well, at least Asha told us there will be times for us to go out.)"
    "I would pester Vena about it, till she got a headache and wouldn’t be able to say “No.”"
    "This sounded much safer and proper than acting on my own."
    "(Still though…)"
    "I got up my bed and went to the common room."

    scene academylivingroom with fade

    "As I guessed, Kioko and Vena had gone to bed. There was no light leaking under the crack of their door either."
    "(Is there anyone else awake at this time in the Academy?)"

    scene academylivingroom with dissolve:
        xpos 0.7 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 1.2

    "I walked to the part of the room where the shelves were. Although my gaze was fixated on the jars, my mind was wandering at somewhere else."
    "Every common room of the Academy opened onto six bedrooms, and each bedroom had two beds. Normally, they should be shared amongst the same number of students."
    "However Vena, by using the advantage of her closeness to Asha, had succeeded in reserving one common room just for us and us alone, leaving the other 4 bedrooms empty."
    "Of course, this situation had raised some complaints from our people."
    "(…But I must admit, I’m happy that it’s just us here.)"
    "I was not constantly being reminded of what had happened and could be alone with my dreams."

    scene academylivingroom with dissolve:
        zoom 1.0

    "The time didn’t seem to pass."
    "I wondered if leaving my room at night was forbidden or not."
    "Yes, it was late, however I came to the conclusion that there wouldn’t be a problem if I stayed within the Academy grounds."
    "And also, I would get even more familiar with the building."

    scene academylivingroom with dissolve:
        xpos 0.2 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 1.2

    play sound doorclose

    scene academyhallwaynight with fade

    "It was hard to see anything in the darkness."
    "Forming a ball of light in my palm, I started walking."

    "There should only be the common rooms in this wing of the structure."
    "From what I remembered, there was a garden somewhere in the building as well. But I had only got a glimpse of it on our arrival."
    "Flowers, fountains and benches had covered that place, and beneath it, the city was laid out."
    "(Having a picnic there could be great, maybe I should try to convince Kioko.)"
    "(Now… I think this direction leads to that wing.)"

    "After some wrong turns and a lot of pointless backtracking, I had gotten nowhere."
    "Even worse, I had somehow lost my way while I was at it."
    "Stomping my foot, I began to grumble in frustration."

    h "“Is this a labyrinth, or a school?!”"
    h "“What kind of academy would be this complicated?!”"
    h "“Stupid Haru, just how can you get lost, how…”"

    "I tried to calm myself down."
    "After all, in the words of the Outsiders, I was a witch."
    "I could illuminate my footsteps to track the way back to my room any time. It shouldn’t be that hard."
    "I only needed a piece of myself to cast the spell- for example a strand of my hair, or a clipping of nail. Using blood to make the spell even more efficient, but it wasn’t necessary."
    "Blowing out my cheeks in frustration, I reached up to pull a hair out of my head, but at that moment a sound distracted me."

    play sound doorknocking
    pause 1.0
    play sound doorknocking
    pause 2.0

    "Listening carefully, I tried to determine the source."
    "(It’s probably coming from one of the rooms ahead of me.)"

    play sound walking

    "I walked towards the sound cautiously."

    scene academyhallwaynight with dissolve:
        xpos 0.2 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 1.2

    stop sound
    pause 1.0

    "In the end, it lead me to a door."
    "The sound kept repeating. Was something stuck in there?"
    "I put my hand on the doorknob, wondering. I turned the handle and began to pull the door open when-"

    "Another hand slammed the door back."
    "Yelping with fear, I turned to see the hand’s owner."

    scene blackscreen with fade

    u "“How can I help you, my lady?”"

    "I couldn't manage to get a single word out."

    u "“You shouldn’t leave your room this late. Especially considering the dangerous situation the witches are in at the moment…”"

    "White hair, red eyes…"
    "{i}Ah, yes{/i}! It was the person I had seen this morning."

    h "“You’re a man!”"

    u "“…Of course I am.”"

    "(…)"
    "I had voiced my thought without even realizing."

    h "“Yes, yes you are… Haha…”"

    "I rubbed the back of my neck, agitated how I had just embarrassed myself."

    "But he suddenly burst into laughter."

    u "“Okay, okay, now I remember. You’re her.”"

    "Pulling his hand away from my side, he let me straighten up."

    scene academyhallwaynight with fade

    show Ealdwine Eyesclosed with dissolve

    u "“The couple that couldn’t decide if I was a man or a woman this morning.”"

    "I blinked in surprise."

    h "“You heard!”"

    show Ealdwine Smiling with dissolve

    u "“Was it supposed to be a secret?”"

    h "“No, no… It’s just… Did you use magic?”"

    "He began to chuckle again."

    show Ealdwine Grinning Eyesclosed with dissolve

    u "“And why wouldn’t I? This is an academy of magic.”"

    show Ealdwine Smiling with dissolve

    u "“Or do you think witches are the only ones that can use it?”"

    h "“No! I didn’t mean it like that. It’s just that people here seem so distant from the magic, at least in my observations so far.”"

    show Ealdwine Confused with dissolve

    u "“Hmm, you might have a point.”"

    "After these words, he took a few steps back and slightly bowed."

    show Ealdwine Default with dissolve

    u "“My name is Ionyr Foliot.”"

    io "“I am a teaching assistant at this academy.”"

    "(Should… Should I bow too?)"
    "After debating on it for a while, I just went with introducing myself plainly."

    h "“I am Haru.”"

    show Ealdwine Eyesclosed with dissolve

    io "“Glad to make your acquaintance, Haru.”"

    show Ealdwine Default with dissolve

    io "“Let me accompany you to your room.”"

    h "“There’s no need for that!”"

    "I waved my hands in front of me frantically. Causing scandals was not on my priorities right now."

    h "“I can go myself, there’s no need to burden yourself.”"

    show Ealdwine Eyesclosed with dissolve

    io "“Alright then, I wish you a good night.”"

    show Ealdwine Default with dissolve:
        ypos 1.5 zoom 1.5

    io "“And Haru, please keep in mind it's not safe to go out at these hours.”"

    hide Ealdwine with dissolve

    "I nodded my head in response and started walking back the way that I had come from."
    "Though before turning the corner I looked back, only to see Ionyr still standing at the same spot where I had left him, smiling at me so, so innocently."

    pause 3.0
    return
































return
