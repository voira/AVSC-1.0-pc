define v = ("Vena")
define h = ("Haru")
define k = ("Kioko")
define a = ("Asha")
define al = ("Almasi")
define bbg = ("Başka Bir Gümüş Oyuk Sakini")
define obg = ("Öteki Gümüş Oyuk Sakini")
define dbg = ("Diğer Bir Gümüş Oyuk Sakini")
define gr = ("Grandük")
define m = ("Marley")
define c = ("Cyril")
define l = ("Lionel")
define x = ("Xerxes")
define u = ("???")
define bks = ("Bir Kadın Sesi")
define io = ("Ionyr")

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
    show Kioko ClosedEye at left with dissolve
    show Vena Default at right with dissolve

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

    show Vena Sideway with dissolve

    v "“She couldn’t sleep a wink these past few days due to the stress.”"

    hide Vena with dissolve

    show Kioko ClosedEye with dissolve:
        zoom 1.5

    "I knew that. Even though our bond had become loose ever since, I was still feeling the roots of Kioko’s stress in my heart as well."
    "However I wasn’t able to soothe her."
    "These new feelings, which were complete strangers to me, had put me in a weird, confused state I couldn’t handle at all."

    hide Kioko
    show Kioko ClosedEye at left with dissolve
    show Vena Frowning at right with dissolve

    h "“I think everyone here suffers from a similar problem.”"

    v "“Everyone except you.”"

    "(Here we go again.)"
    "Ever since we’d set foot on this world, Vena’s scolding had become ceaseless."
    "After glaring at her for a while I focused my gaze at somewhere beyond the window. Nowadays, whenever we argued there was this unfamiliar pang of pain I felt in my stomach, making me want to vomit."
    "Realizing that I was failing to comfort myself even after taking several deep breaths, I couldn’t help but ask permission to leave the compartment, which started to feel stuffy."

    h "“I will get some air.”"

    show Vena ArchedEye with dissolve

    v "“Where are you going?”"

    "I stood up."

    h "“Just taking a walk in the aisle. My legs have gone numb.”"

    "Vena took a deep breath."

    show Vena Default with dissolve

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
        xpos 0.1 ypos 1.7 xanchor 0.5 yanchor 1.0 zoom 2.0

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

    show Asha Sideway with dissolve

    a "“And found ourselves in the middle of this land, foreign, at least for you.”"
    a "“Not every person can react in the same way.” "

    show Asha Smiling with dissolve

    $Waceera_Entry.locked = False
    $Waceera_Entry.locked_persistent = False

    a "“However you should also put yourself in Vena’s place. {color=#f00}Waceera{/color} is very… Very dear to her.”"
    a "“Her strange disappearance, in such a dire time as this, has deeply upset your sister.”"

    "I tilted my head."

    h "“Do you seriously think she’s not dead?”"

    show Asha ClosedEye with dissolve
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

    show Asha Sideway with dissolve

    a "“You should as well, Almasi.”"

    show Almasi at left with dissolve

    al "“And since when have I been taking orders from you?”"

    show Asha ClosedEye with dissolve

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
        zoom 2.0
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

    show Kioko Default at left with dissolve
    show Vena Default at right with dissolve

    v "“Did something happen? I heard someone yelling.”"

    "It was surprising to hear Vena ask that, since she had a habit of using her powers to eavesdrop on other's conversations."
    "Anyways, this at least meant I didn’t have to deal with her temper for now."

    h "“The usual arguments, you know. Nothing else.”"

    hide Kioko with dissolve
    hide Vena with dissolve

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
    scene whemond
    pause 1.0
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

    show Vena Sideway with dissolve

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

    "Before giving a response, Vena closed her eyes and paused a little bit."

    show Vena ClosedEye with dissolve

    v "“I am speaking up for your own good, please don’t turn it into a competition.”"

    a "“That I won’t, let’s just say I’m stating a fact.”"

    show Asha ClosedEye with dissolve

    a "“Oh Vena… There’s no reason for you to worry. We will find Waceera, and get back to Silver Hollow. I can assure you.”"

    "She glanced over the room. When no answer was given, Asha put her shawl on, then stood up."

    hide Vena with dissolve
    show Asha ClosedEye with dissolve:
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

    show Vena Default at right with dissolve

    v "“You two can leave. I still have work to do.”"

    show Kioko Default at left with dissolve

    k "“Please don’t tire yourself out.”"

    hide Vena with dissolve
    hide Kioko with dissolve

    "After agreeing with Kioko’s remark and wishing a good night, I saw myself out."

    scene academybedroom with fade
    pause 2.0
    scene academybedroom with dissolve:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

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
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "(But now, I should sleep.)"
    "(After all, tomorrow is a busy day.)"

    scene blackscreen with fade
    pause 3.0

    scene academyclass with fade
    show Vena ClosedEye with dissolve:
        xpos 0.3 ypos 1

    play sound commotion
    pause 4.0
    stop sound

    v "“For the last time Haru, you have to leave this alone.”"

    h "“I’m asking just out of curiosity, curiosity!”"

    hide Vena with dissolve

    "As if she was running away from me, her steps quickened."
    # Slow screen shake gelecek.
    "I ran towards Vena and grasped her arm."

    play sound sitting

    h "“Vena!”"

    show Vena Sideway with dissolve

    "Finally her attention returned to me."
    "She looked distracted."
    "Whatever was running through her mind made Vena give up with a deep sigh."

    show Vena ClosedEye with dissolve:
        ypos 1.5 zoom 1.5

    v "“Haru, listen.”"

    "Catching my two hands in hers, she guided them to her heart."
    "This made me realize how much I missed her warmth since we had done nothing but arguing for a long time."

    show Vena Concerned with dissolve

    "However when I peeked up at Vena’s eyes, I saw the traces of concern instead of the affection I sought."

    v "“If I told you that I understood what you are actually going through, that would be a lie.”"

    show Vena Sideway with dissolve

    v "““I can’t understand your current mood in any way.”"
    v "“I can’t tell if a storm is raging in your head and you’re not showing it, or if your mind is as calm as the sea on a sunny day Haru.”"

    show Vena Sighing with dissolve

    v "“But you should never put yourself in such position, nor us.”"

    "Taking a deep breath, I slowly freed my hands from Vena’s."

    show Vena Default with dissolve:
        xpos 0.4 ypos 1.0 zoom 1.0

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
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.0

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

    show Asha Sideway with dissolve:
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

    show Asha ClosedEye with dissolve

    a "“…”"

    show Asha Default with dissolve

    a "“I wouldn’t call it benefitting.”"

    show Asha ClosedEye with dissolve

    "“This was Waceera’s decision. To provide us longer lives…”"

    al "“Nonsense!”"

    show Asha Default with dissolve

    a "“My only responsibility at this meeting, is telling you the truth.”"

    show Asha Frowning with dissolve

    a "“The reasons behind Waceera’s actions are things that you can only learn from her.”"

    show Asha ClosedEye with dissolve

    a "“I know this might get you irritated, but I have no other answer than this to give.”"

    show Asha Sideway with dissolve:
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
        xpos 0.5 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    "These desks must belong to the students of this Academy."
    "Back in Silver Hollow, the disdain I felt for our theoretical lessons had been so strong even with the existence of the circle. The ambiance here might even encourage me to study."
    "Slowly, I traced the wood with my finger. Carved letters, formulas and charts that I couldn’t make much of, were on the surface."
    "When I raised my head again to look at the classroom, a figure standing in the doorway caught my attention."

    scene academyclass:
        zoom 1.0

    show Ealdwine Sideway at right with dissolve

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

    "Gümüş Oyuk’ta sadece “kadın” nüfusu olduğu için “erkek”ler hayatıma Aelthus ile birlikte girmiş bir başka kavramdı."
    "Birçoğu kadınlardan daha uzundu. Sesleri daha kalındı."
    "Göğüsleri yontulmuş bir mermer gibi düz, bazılarının boyları ise kavak ağaçlarıyla yarışacak kadar uzundu."
    "Çeneleri sertti, yüzleri köşeliydi."
    "Her biri dağları, devleri tepip devirmeye hazır görünüyordu. Aslında güçsüz olsalar bile kendilerini böyle hissediyor gibilerdi."
    "Bu, kapıda duran genç ise ne erkeksi ne de kadınsıydı. Sanki ikisi arası bir yerde takılmıştı."
    "Vena bir süre o kişiye bakıp, sonra konuştu."

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“Ben de bilemedim.”"

    "Sesi düşünceli çıkmıştı. Vena’nın bile ikileyeceği şeylerle karşılaşmak çok komikti."

    v "“Herhalde erkek.”"

    h "“Galiba.”"

    hide kiokoeye with dissolve

    "Gözlerim tekrardan çocuğun üzerinde gezinmeye başladı. Bir elimi çeneme dayayarak kendisini izlemeye koyuldum."
    "Kız da olsa erkek de olsa çok sevimli görünüyordu."

    show Ealdwine Surprised with dissolve

    "Fakat bir süre sonra çocuk kafasını benden yana kaldırmış, gözlerimiz buluşmuştu."

    hide Ealdwine with dissolve

    scene academyclass with hpunch

    "Yakalanmanın paniğiyle oturuşumu düzeltmeye ve bakışlarımı kaçırmaya çalışmış, bu süreçte yanlışlıkla Vena’nın taşını masadan ittirivermiştim."
    "Lakin reflekslerim sayesinde taş düşüşe geçmeden bir rüzgar büyüsü yardımıyla onu havada yakalamış, ardından kendi avucuma getirmiştim."

    v "“Dikkat et Haru.”"

    h "“Özür dilerim.”"

    show Ealdwine Grinning with dissolve

    "Kafamı kaldırıp kapıya baktığımda çocuğun bana bakarak güldüğünü gördüm."
    "(…Ne utanç verici.)"

    scene sundown with fade

    "Toplantı bittikten sonra Akademi içerisinde verilen çeşitli görevleri yerine getirmiştik."
    "(O kutuyu aç, bu erzağı say, sor bakalım eksik bir ihtiyacı olan var mı, herkes mutlu mu falan filan işte.)"
    "İş güneşin batışını izlemeye gelinceyse, elimde ne var ne yok umursamadan bırakıp pencerenin kenarına konuşlanmıştım."

    play sound seagull

    "(E hani? Battı batacak neredeyse! Sakın demeyin bana kanlı gökyüzünden kastınızın bu olduğunu.)"

    scene blackscreen with fade

    "Ben hayıflanırken güneş denize iyice yaklaşmış ve semanın renkleri bir anda değişivermişti."

    scene sundown with fade

    "(Ooh…)"
    "(Vay…)"

    h "“Kıpkırmızı oldu cidden de!”"

    "Şaşkınlığımı gizleyemeyip kendi kendime söylenmiştim."
    "Gökyüzünün değişimine mi, denizin kıpkırmızı oluşuna mı yoksa güneşin gerçekten de kanar gibi gözükmesine mi daha çok hayret etmeliydim bilemiyordum."
    "Ve bu sahne, buradaki insanların normaliydi. Her gün iki kez onları bu görüntü bekliyordu."

    h "“Hah…”"
    stop sound

    "(Böyle bir şey nasıl “normal” olabilirdi?)"
    "Elimi kaldırıp ileri doğru uzattım. Güneş ışınları tenime temas ediyor ve vücudumda hiç hissetmediğim kadar güç topluyordu."
    "Böyle bir yerde yaşamak demek, bir insanın asla manasının bitmemesi demekti."
    "Havada resmen sihir vardı."
    "Buna rağmen ayaklarımın altındaki bu şehrin insanları, duyduklarıma göre büyüye bir o kadar uzaktı."
    "(Ne ironik…) Derin bir iç çekip işlerime dönmeden önce manzaraya bir daha baktım."
    "Şimdiden buradan ayrılırsak yaşayacağım buruk acıyı düşünüyor, kendi kendimi üzüyordum."

    scene academylivingroom with fade
    pause 1.5
    show Kioko Default at left with dissolve
    show Vena Default at right with dissolve

    v "“…Benim anlatacaklarım bu kadar. Geri kalanını anı taşından izleyebilirsin.”"

    k "“Teşekkürler Vena.”"

    hide Kioko with dissolve
    hide Vena with dissolve

    "Birlikte Asha’nın dağıttığı yemeklerden yiyorduk. İçten içe günün bu kadar yorucu geçmesinden ötürü şikayetleniyordum."
    "(Kioko çok şanslı… Bütün gün rahat rahat odasında yatabildi. Kimse de ona bir şey demiyor!)"
    "En azından yakında yerleşme işlerimiz bitecekti."
    "O zaman geriye kalan problemlerin birçoğunu çözmek Işık Hamillerinin omuzlarına düşecekti."
    "(Belki bu bana sıvışma şansı verirdi.)"
    "Gerçekten aylarca buraya kısılıp kalmak istemiyordum."

    show Kioko ClosedEye at left with dissolve

    k "“Bir şey… Diyeceğim.”"
    k "“Fakat lütfen paniklemeyin.”"

    "Vena tabağını bir kenara koyup kulak kesilmişti."
    "Benimse çatalım Kioko’ya meraklı bir şekilde bakarken havada kalmıştı."

    k "“…”"

    "(Güzel, şimdiden panikledik.)"
    "Tam da kaytarabilirim diyordum oysaki."

    show Kioko Sideway with dissolve

    k "“Sanırım ben… Bugün odamda birini gördüm.”"

    "Şaşkınlıkla bakakalmıştım."

    h "“Ne?”"

    show Vena Frowning at right with dissolve

    v "“Kimi?”"

    show Kioko Concerned with dissolve

    k "“B-Bilmiyorum ki.”"
    k "“Rüya da olabilir, tam emin değilim.”"

    "Ne zaman sıkıntıya girse yaptığı gibi tırnağını yemeye başlamıştı."
    "Vena öne doğru eğilip nazikçe elini ağzından çekti."

    show Vena Default with dissolve

    v "“Kioko, sakin ol.”"

    k "“Yeni uyanmıştım. Sonra odamda biri olduğunu fark ettim. Cam kenarında duruyordu.”"

    show Vena Arched with dissolve

    h "“Nasıl biriydi? Arkadaşlarından biri olmasın?”"

    show Kioko Protesting with dissolve

    k "“Hayır! Hayır… Öyle bir arkadaşım yok benim.”"

    show Kioko ClosedEye with dissolve

    k "“Turuncu saçları vardı. Yüzünü tam göremedim ama, uykuluydum.”"

    "Ellerini kollarını kontrol edemiyor, konuşurken bir sürü jest kullanıyordu."

    show Kioko Concerned with dissolve

    k "“Yanıma geldi sonra. Çok korktum, hareket edemedim, ardından öylece uyuyakaldım!”"

    "Vena tekrardan ona doğru uzanıp parmaklarını şakağına yerleştirdi."
    "(Ah, anılarını izleyecek.)"

    v "“Müsaadenle bir de ben bir bakacağım.”"

    show Kioko ClosedEye with dissolve

    "Kioko onaylarcasına kafasını sallayıp kendisini hazırladı."

    hide Vena with dissolve
    hide Kioko with dissolve

    "Ardından Vena’nın gözlerinden de parmak uçlarından da çıkan mavi, cılız bir ışık büyünün başladığını göstererek odaya yayılmıştı."
    "Zihne dair büyüler Vena’nın uzmanlık alanıydı."
    "Normalde uzun bir odak ve çokça mana gerektiren bu büyülerin Vena için nefes almak kadar kolay olmasına hep hayret etmişimdir."
    "(Özenmek… O ayrı bir konu şimdi.)"
    "Özenmiyordum çünkü “Psişik alanında uzmanlaşmayı tercih edenler kendilerine büyük tehlikeleri de davet etmiş olurlar.” derdi Asha."
    "Bu kolay bir zanaat değildi."
    "İnsan kendisini çok kaptırırsa gerçeklikten kolayca kopabilirdi."
    "Vena’nın, kontrol bağımlısı olduğunu göz önünde bulundurursak, bu seviyeye geleceğini hiç düşünmüyordum."
    "Ama o bile ara sıra elinde olmadan başkalarının rüyalarını gasp ediyordu."
    "Belki de bu kadar sinirli olmasının sebebi başkalarının düşüncelerinin, ruh hallerinin sürekli kendisini dürtüklemesiydi."
    "Aradan çok geçmeden Vena kendini geri çekip Kioko ile arasına mesafe koymuştu."
    "Merakla ikisine baktım."

    show Kioko Default at left with dissolve
    show Vena Sideway at right with dissolve

    v "“Ya gelen her kimdiyse anılarını bulutlamış ya da gerçekten rüya görmüşsün.”"

    h "“Ayırt edemiyor musun, Vena?”"

    show Vena Default with dissolve

    "Bu bir ilk olabilirdi."
    "(Veya iki… Gümüş Oyuk’ta Kioko’nun başına gelenleri de sayarsak…)"
    "Kafasını {i}hayır{/i} anlamında sallamıştı."

    h "“Bu akademiden bir kimse olabilir mi?”"

    show Vena Frowning with dissolve

    v "“Sanmam. Üniforma giymiyordu, bizden birine de benzemiyordu. Kioko, bize neden daha önceden haber vermedin?”"

    show Kioko ClosedEye with dissolve

    k "“Gereksiz panik yaratmak istememiştim.”"

    show Vena Concerned with dissolve

    "Vena hızlıca Kioko’nun elini kavradı."

    v "“Sakın böyle şeyler düşünme. Çalkantılı bir dönemdeyiz o yüzden şüpheli görünen her şeyi bize söylemelisin.”"

    "Bir süre sessizlik olmuştu."

    h "“Çok garip gerçekten… Ne yapacağız?”"

    show Vena Sideway with dissolve

    v "“Ben…”"

    "Vena derin bir iç çekti."

    show Vena Default with dissolve

    v "“Kioko, benim odamda yatmak ister misin?”"

    show Kioko Gaping with dissolve

    k "“Sana yük olmayı istemem.”"

    show Vena Frowning with dissolve

    v "“Lütfen saçma şeyler söyleme, sen benim kardeşimsin.”"

    show Kioko Concerned with dissolve

    k "“Ama işine engel olmaz mıyım?”"

    show Vena ClosedEye with dissolve

    v "“Hayır, önceliğim sizsiniz.”"

    hide Kioko with dissolve
    hide Vena with dissolve

    "Sanırım bu noktada araya girip Kioko’nun sorumluluğunu benim üstleneceğimi söylemem en doğru seçenek olurdu."
    "Böylece Vena bir Işık Hamili olarak görevlerini yerine getirebilecek, aynı zamanda da gözü arkada kalmayacaktı."
    "Ama ben…"
    "(Hah…)"
    "Kioko’ya bakmak öyle kolay bir iş değildi."
    "Kara Katliam’ın sır perdesini aralayabilecek belki de tek kişiydi."
    "Şimdilik Asha’nın kehanetinden ve Kioko’nun itirafından sadece ben, Vena, Asha ve muhtemelen Zuri haberdardık."
    "Ya bir başka insan, diyelim ki Kara Katliam’a sebep olan kişi yahut şey Kioko’nun peşine düşmüştüyse? Ben onu olası bir acil durumda nasıl savunabilirdim?"
    "Bütün bu bahaneleri bir kenara bırakırdıysam da…"
    "Hayatımda ilk kez tek başıma kalacak olmanın, tek özgürlük şansımın ellerimden öylece alınmasını istemiyordum."
    "Belki de bunu kabul etmek utanç vericiydi lakin istemiyordum işte."
    "O yüzden, en nihayetinde ses çıkarmamaya karar verdim."

    show Vena Default with dissolve:
        xpos 0.3

    v "“Öyleyse Asha’ya Işık Hamilleri için düzenlenen toplantıya gidemeyeceğimi bildirmem lazım.”"

    "Yutkundum ve kafamı eğip ellerime baktım."
    "(Suçlu hissetme, suçlu hissetme.)"

    scene academybedroom with fade
    pause 2.0
    scene academybedroom with dissolve:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Oturma odasında bir süre daha vakit geçirdikten sonra odalarımıza ayrılmıştık."
    "Of… Ne yorucu bir gün olmuştu ama!"
    "En nihayetinde kendimle baş başa kalabilmiştim."
    "Bir süredir cam kenarına kurulmuş, olan biteni değerlendirirken altımda nefes alan şehri izliyordum."

    scene whemond with fade

    "Saat gece yarısını geçeli çok olmuştu. Benimse gözüme uyku girmiyordu."
    "Akşam boyunca insanlar vızır vızır sokaklarda dolanmış, rüzgar kulaklarıma kah ayyaşların kahkahalarını kah gecenin karanlık örtüsüne güvenilip söylenen sırları taşımıştı."
    "Ardından dükkanların ışıkları bir bir sönmüş, insanlardan birçoğu evlerine dönmüştü."

    scene academybedroom with fade:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Ne kadar çok eğleniyor olmalılardı."
    "Stresten, zincirlerden, olağanüstü durumlardan uzak; özgür bir hayat…"
    "Ne güzel olmalıydı insanın istediği zaman istediğini yapabilmesi."
    "Sıkıntılarım nefes almamı güçleştirirken dudaklarımı birbirine gergince bastırdım."
    "Bir taraftan bir elimle pencere pervazını kavramış ve zavallı tahtayı eklemlerim beyazlayana kadar sıkmıştım."
    "Ben de bu hayatı, bu özgürlüğü istiyordum. Ne vardı hazır Gümüş Oyuk yok olmuşken de buraya yerleşiverseydik, insanlarla kaynaşıverseydik? Ne olurdu?"
    "(Böyle düşünmemelisin, böyle düşünmemelisin.)"
    "Yatağımda doğrulup pencereye tırmandım, ardından pervaza oturdum."
    "Bu sırada aklımda Vena’yla sabah gerçekleştirdiğim konuşma vardı."

    scene academyclass with flash
    show Vena Default with dissolve

    h "“Sanırım buradan çıkmamıza izin vermezler, hm Vena?”"

    v "“Daha çok dönüş günümüze dek tutsaklarıyız diyebiliriz.”"

    show Vena ClosedEye with dissolve

    v "“Tabii gitmemize izin verirlerse…”"

    show Vena Default with dissolve

    h "“Bizi burada istemiyorlarsa neden vermesinler ki? Boşuna endişeleniyorsun bence.”"
    h "“Acaba gizlice dışarı çıkabilir miyiz?”"

    show Vena Frowning with dissolve

    v "“…”"

    hide Vena with dissolve

    scene academybedroom with flash:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Son sorumun ardından tartışmıştık."
    "Dışarıda en fazla ne olabilirdi ki? Bir sürü insanın, muhafızın gözü önünde herhalde bana saldırmazlardı."
    "Öte yandan başıma bir şey gelmesi durumunda yardım istersem Akademi’den izinsiz çıktığım da belli olacaktı."

    scene academyclass with flash

    show Vena Sighing with dissolve:
        xpos 0.3 zoom 1.5

    v "“Ama kendini de bizi de zor bir duruma sokmamalısın.”"

    scene academybedroom with flash:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Gergince alt dudağımı dişledim."
    "Vena ve Kioko şu an uyuyor olmalıydı, yani şehri görmek istiyorduysam bundan daha uygun bir an yoktu."
    "Fakat dışarı çıkmak…"
    "Gözlerimi kısıp şehre doğru baktım."

    scene whemond with fade

    "Akademi’nin etrafında bir sihir kalkanı vardı."
    "{i}Komik{/i}… Muhtemelen burası için usta işi sayılacak bu bariyeri benim, yani derslerinde pek de parlak olmayan bir öğrencinin dahi görmesi aslında kalitesi hakkında çok şey söylüyordu."
    "Yine de bu, kalkanı uçarak geçemezsiniz demekti."
    "Sanıyordum ki ışınlanmaları saptamak için Akademi’nin içinde de çeşitli efsunlar vardı."
    "Yani Vena’ya göre benim herhangi bir kaçma denememde yakalanmamam imkansızdı."
    "Dudaklarım bu düşünce karşısında yavaşça yukarı kıvrılmıştı."
    "Kimseye yakalanmadan kaç kez Gümüş Oyuk’tayken dışarı çıktığımı bilseydi ne kadar da şaşırırdı. Kendi yöntemim sayesinde buradan da sıvışabileceğimi biliyordum."
    "Öteki taraftan da bir problem çıkar da başım belaya girer, Vena’yla tartışırız diye dertleniyordum."

    menu:
        "(…)"

        "Dışarı çıkmak istiyorum.":
            jump outside

        "Belki de içeride kalmalıyım.":
            jump inside


label outside:

    "(Bir kerecik… Sanıyorum ki bir kerecik dışarı çıkmaktan bir şey olmaz. Hemencecik geri gelirim hem, aynı zamanda bu konuda daha fazla kafa da ütülemem.)"
    "Elimi ileriye doğru uzattım."
    "Rüzgar avucumun içine toplanmaya başlamış, ardından parmaklarım yavaşça toz bulutlarına dönüşerek havaya karışmıştı."
    "Bunu ellerim, ayaklarım, kollarım, bacaklarım ve en sonunda bütün vücudum sırayla izledi. Ve ben en sonunda rüzgarla bir oldum."

    scene sundown with fade

    "(Her seferinde ilk kez yapıyormuşum gibi hissettiriyor.)"
    "Her defasında beni bağlayan hayali zincirlerden kurtulmuş gibi hissediyordum."
    "İçim içime sığmayarak yükseldim de yükseldim, sihir bariyerini hiçbir sorun yaşamadan geçtim, ardından şehrin üzerinde diğer rüzgar bulutlarıyla dans etmeye başladım."
    "Bu yeteneğimi çok küçük yaşlarda keşfetmiştim. Bildiğim kadarıyla köyde bunu benden başka yapabilen bir kız da yoktu."
    "Ve bundan haberi olan arkadaşlarım da zaten-"
    pause 2.0
    "Hayır, yersiz düşüncelere dalmanın vakti değildi."
    "Daha önemli bir görevim vardı: En azından bu geceyi eğlenerek geçirebilmek."

    scene whemond with fade

    "Dönüp tekrardan şehre baktım. Akademi’den oldukça uzaklaşmıştım şimdi."
    "Hayatımda ilk kez böyle koca binalar, döşeli yollar, uçan ya da hareket eden araçlar, hatta deniz görüyordum ben."

    scene whemond with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    "83 yılımı bir ormanda, ağaç kulübelerde, aynı insanlarla aynı havayı soluyarak ve gri renkli bir gölde yıkanarak geçirmiştim."
    "Güneş bile doğmazdı, sabah akşam gök aynı renkti."
    "Dış Dünya’ya karşı heyecanlanmamak benim gibi bir insan için nasıl mümkün olabilirdi?"

    scene whemond with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.0

    "(Tamam, pekala. Yakalanmamayı başardığıma göre şimdi nereye insem acaba?)"
    "Herhalde gözlerden ırak bir yere inmek en iyisiydi."
    "Öte yandan bu yer şehir merkezinden de çok uzak olmamalıydı."

    scene whemond with dissolve:
        xpos 0.8 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Yüksek binaların süslediği bir arka sokağa gözümü diktim. Koca koca evler vardı bu bölgede. Gezmek, görmek istediğim ışıklı alanlara da çok uzak sayılmazdı."
    "Yere inmeye koyuldum."

    scene whemond with dissolve:
        xpos 0.8 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.5

    pause 1.0
    scene alleyway with fade

    "Kimsecikler yok gibi görünüyordu. Yere iyice yaklaştım."
    "Önce parmak uçlarım, ardından tüm vücudum tekrardan insan formunu almıştı."
    "(Hehehe… Buraya kadar hiçbir sorun yaşamadım, süper!)"
    "Şimdi, o rengarenk ışıklar ne tarafta kalıyordu-"
    "{i}…Huh?{/i}"
    "Duyduğum bir grup insan sesiyle paniklemiş, hemen kukuletamı gözlerimi kapatacak şekilde yüzüme geçirmiştim."
    "Eğer biri beni görürse sakin olmalı, üzerime şüphe çekmemeliydim."

    play sound walking

    "Ağır adımlarla yürürken bir taraftan da rüzgarın kulağıma konuşmaları taşımasına izin verdim."

    stop sound

    bks "“Xerxes, bu saatte buraya gelmemeliydin.”"

    x "“Nişanlımı özleyemez miyim?”"
    x "“Lea… Sana o kadar aşığım ki seni görmediğim her gece bana ıstırap gibi geliyor.”"

    "(Aha! Ne kadar ilginç, ne kadar ilginç!)"
    "Yolumu az önce kaçtığım insanlara doğru çevirmiştim. Aşk, romantizm, bunlar hep bana ve diğer Gümüş Oyuk sakinlerine uzak hislerdi. O yüzden merakım körüklenmişti."
    "Şöyle ucundan bir bakıp, geri dönecektim."

    play sound walking

    scene alleyway with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    pause 1.5
    stop sound

    "Sesler demir korkuluklarla çevrili koca bir bahçeden geliyordu."
    "Fakat beni daha da şaşırtan şey çitlerin önünde yere çökmüş bir figür görmek oldu. Anlaşılan o da konuşanları izliyordu."

    show Cyril HoodDefault with dissolve

    "(İşte, ben garip bir insan değilim. Başkaları da izliyor!)"

    hide Cyril with dissolve

    "Olabildiğince sessiz bir şekilde arkadan yaklaştım. İsmi Xerxes olan adam ve diğer kadın bahçenin ortasında birbirlerine sarılmaktaydılar."
    "Önümdeki çocukla yorumlarımı paylaşmanın iyi bir fikir olduğunu düşünerek eğildim."

    h "“Çok güzel değil mi? Hayatımda ilk kez böyle bir şeye şahit oluyorum-”"

    scene alleyway with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    play sound sitting

    "Fakat o an kukuletalı figür ayaklanmış ve-"

    scene alleyway with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    show Cyril HoodSword with dissolve

    "Kılıcını bana doğru savurmuştu!"
    "Yeterince hızlı olmasaydım deşip geçecekti neredeyse."
    "(Ne yapmalıyım? Büyü mü yapmalıyım?)"

    show Cyril HoodDefault with dissolve
    pause 1.0
    show Cyril HoodDefault with dissolve:
        ypos 1.5 zoom 1.5
    pause 0.5
    hide Cyril

    "Fakat benim daha karar vermeme kalmadan çocuk üzerime atılmış, eliyle ağzımı kapatıp beni sokağın öteki tarafına sürüklemeye başlamıştı."

    scene alleyway with dissolve:
        zoom 1.0

    "Arkamızdan az önceki kişinin bağırdığını duydum."

    x "“Kim var orada?!”"

    "(Ben! Lütfen yardım et!)"
    "Ne kadar silkelensem de, çırpınsam da çocuğun ellerinden bir türlü sıyrılamıyordum."
    "(Çok güzel Haru… Yere indiğin gibi başını derde soktun.)"
    "Sonuçlarına katlanacaktım artık."

    pause 3.0
    return

label inside:

    scene academybedroom with fade:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    play sound sitting

    "Camın kenarından ağır hareketlerle geri çekildim."
    "Belki de bu kötü bir fikirdi. Aşağıya inmesi, geri gelmesi kolaydı."
    "Ama ya aşağıdayken ters bir şeyler olsaydı?"
    "Ya da Vena yokluğumu fark etseydi? O zaman ne olacaktı?"
    "En kötüsü de bizimkilerle Aelthus arasında diplomatik bir sıkıntının benim yüzümden çıkması olurdu."
    "O zaman Vena sonsuza dek konuşurdu. O zaman onu asla susturamazdım."
    "Ve sonsuza kadar burada tıkılı kalırdım."
    "Hayallerime veda edercesine camı kapattım."

    scene academybedroom with dissolve:
        zoom 1.0

    "(Olsun, Asha bizi dışarı götürmeyi düşündüğünü söylemişti sonuçta.)"
    "Hem ben de Vena’ya baskı yapar dururdum. En sonunda başı ağrır, “Hayır.” diyemezdi."
    "Ayrıca kendi başıma buyruk davranmaktansa böylesi daha uygun geliyordu kulağa."
    "(Yine de…)"
    "Yatağımdan kalktım ve salona çıktım. Uykum yoktu."

    scene academylivingroom with fade

    "Kioko ve Vena tahmin ettiğim gibi odalarına çekilmişlerdi. Kapılarının altından da ışık gelmiyordu."
    "(Acaba başka uyanık olan var mıdır Akademi’de?)"

    scene academylivingroom with dissolve:
        xpos 0.7 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Rafların olduğu kısma doğru yürüdüm. Gözlerim kavanozları inceliyor lakin aklım başka yerlerde cirit atıyordu."
    "Normalde Akademi’deki her ortak odaya altı oda, haliyle de on iki yatak düşmekteydi."
    "Fakat Vena, Asha’ya yakın olmasının ayrıcalığını kullanıp bir ortak odayı tamamıyla kendimize ayırtmayı başarmıştı."
    "Bu durum insanlar arasında şikayetler yükseltmemiş değildi tabii."
    "(…Ama yalnız kalabildiğimiz için mutlu olduğumu itiraf etmem lazım.)"
    "Böylece olan biten bana her dakika hatırlatılmıyordu; kendimle, hayallerimle baş başa kalabiliyordum."

    scene academylivingroom with dissolve:
        zoom 1.0

    "Vakit geçmemekteydi."
    "Acaba odamı terk etmeme bir şey derler miydi?"
    "Geç olmuştu evet lakin Akademi sınırları içerisinde kaldığım müddetçe bir sorun çıkacağını sanmıyordum."
    "Hem ben de binayı daha iyi tanımış olurdum."

    scene academylivingroom with dissolve:
        xpos 0.2 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    play sound doorclose

    scene academyhallwaynight with fade

    "Karanlık olduğundan bir şeyleri seçmek zordu."
    "Avucumda küçük bir ateş topu oluşturup yürümeye başladım."

    "Yapının bu kanadında sadece ortak odalar olması lazımdı."
    "Yanlış hatırlamıyorduysam, binanın bir noktasında bahçesi de vardı. Fakat sadece ilk geldiğimizde görebilmiştim."
    "Çiçeklerin, çeşmelerin ve bankların süslediği bir bahçeydi bu, altında da koca bir şehir manzarası yatıyordu."
    "(Orada bir şeyler yiyip içmek güzel olmalı, belki Kioko’yu piknik yapmaya ikna ederim.)"
    "(Şimdi… Sanırım bu yönden gitmem gerekiyor.)"

    "Bir süre boyunca yürümüş lakin hiçbir yere varamamıştım."
    "Dahası, artık nasıl geri döneceğimi de bilmiyordum."
    "Sinirle tepindim."

    h "“Labirent mi burası yahu? Okul, okul!”"
    h "“Okul dediğin böyle karmaşık mı olur?!”"
    h "“Nasıl kaybolursun, salak Haru, salak Haru…”"

    "Kendimi sakinleştirmeye çalıştım."
    "Ben ne de olsa, dışarıdaki insanların deyimiyle, bir cadıydım."
    "Ayak izlerini aydınlatabilirdim. Hiç yapmamıştım ama çok da zor olacağını sanmıyordum."
    "Bana ait küçük bir parça da -saçım, tırnağım veya büyüyü daha etkili yapmak için kanım- sadece kendiminkileri aydınlatmama yarayabilirdi."
    "Öfleyerek saçımdan bir tutam koparmaya yeltendim fakat o an duyduğum bir ses dikkatimi dağıtmıştı."

    play sound doorknocking
    pause 1.0
    play sound doorknocking
    pause 2.0

    "Dikkat kesilip nereden geldiğini saptamaya çalıştım."
    "(Herhalde ileriki odalardan birinden…)"

    play sound walking

    "Ağır adımlarla sese doğru yürümeye başladım. Aynı zamanda etrafımı da kolluyordum."

    scene academyhallwaynight with dissolve:
        xpos 0.2 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    stop sound
    pause 1.0

    "En sonunda bir kapının önünde duraksadım."
    "İşte buradan geliyordu. Acaba içeriye bir şey mi tıkılıp kalmıştı?"
    "Merakla elimi kapı tokmağına götürdüm."

    "Fakat ben kapıyı açmadan önce bir el kapıyı sertçe geri ittirmişti."
    "Korkudan yerimden sıçrayarak arkama döndüm."

    scene blackscreen with fade

    u "“Size nasıl yardım edebilirim, leydim?”"

    "Şaşkınlıktan bir süre cevap verememiştim."

    u "“Bu saatlerde dışarıya çıkmamanız lazım. Özellikle cadıların içinde bulunduğu tehlikeli durumu düşünürsek…”"

    "Beyaz saçlar, kırmızı gözler…"
    "{i}Ah, evet{/i}! Sabahleyin gördüğüm çocuktu bu."

    h "“Sen erkeksin!”"

    u "“Elbette öyleyim.”"

    "(…)"
    "Fark etmeden düşüncemi sesli olarak söylemiştim."

    h "“Evet, evet, öylesin. Haha…”"

    "Tedirgince ensemi kaşıdım. Resmen rezil etmiştim kendimi!"

    "Bir anda gülmeye başladı."

    u "“Tamam, tamam. Hatırladım. Sen O’sun.”"

    "Ardından elini kafamın yanından çekmiş, doğrulmama izin vermişti."

    scene academyhallwaynight with fade

    show Ealdwine ClosedEye with dissolve

    u "“Bu sabah konsey esnasında benim kız mı erkek mi olduğuma karar veremeyen ikili.”"

    "Gözlerimi kırpıştırdım. Şaşırmıştım."

    h "“Duymuşsun!”"

    show Ealdwine Smiling with dissolve

    u "“Sır olması mı gerekiyordu?”"

    h "“Yoo… Hayır, sadece… Büyü mü kullandın?”"

    "Tekrardan gülmeye başlamıştı."

    show Ealdwine ClosedEyeGrinning with dissolve

    u "“Neden kullanmayayım? Burası bir büyü akademisi.”"

    show Ealdwine Smiling with dissolve

    u "“Yoksa büyü sadece cadılara has bir şey mi sanıyorsunuz?”"

    h "“Hayır! Öyle demek istemedim. Sadece buraya vardığımızdan beri sizlerin büyüye karşı biraz mesafeli olduğunu gözlemledim, o kadar.”"

    show Ealdwine SidewayThinking with dissolve

    u "“Hmm, bu konuda haklı sayılırsın.”"

    "Bu sözlerden sonra geri çekilip önümde hafifçe eğildi."

    show Ealdwine Default with dissolve

    u "“İsmim Ionyr Foliot.”"

    io "“Bu akademinin bir öğretim görevlisiyim.”"

    "(Acaba ben de eğilmeli miyim?)"
    "Emin olamayıp yerimde bir süre sallandıktan sonra kendimi tanıttım."

    h "“Ben de Haru.”"

    show Ealdwine ClosedEye with dissolve

    io "“Tanıştığıma memnun oldum, Haru.”"

    show Ealdwine Default with dissolve

    io "“Sana odana kadar eşlik edeyim.”"

    h "“Gerek yok, gerek yok!”"

    "Ellerimi önümde hızlıca salladım. Skandal yaratmak istemiyordum."

    h "“Ben kendim giderim, senin kendini yormana gerek yok.”"

    show Ealdwine ClosedEye with dissolve

    io "“Peki öyleyse, iyi geceler dilerim.”"

    show Ealdwine Default with dissolve:
        ypos 1.5 zoom 1.5

    io "“Ve Haru, bu saatlerde dışarı çıkmamaya özen göster.”"

    hide Ealdwine with dissolve

    "Kafamı “Tamam.” anlamında sallayıp, geldiğim yöne doğru yürümeye başladım."
    "Koridordan dönmeden önce; başımı son kez çevirip baktığımda Ionyr’in hala aynı yerde durmuş, bana bakıp gülümsediğini görmüştüm."

    pause 3.0
    return
































return
