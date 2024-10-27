label galleryRename:
    default persistant.galleryRename = False
    default galleryMC = VariableInputValue("MC", default=True, returnable=False)
    return

default persistent._replay_name = "Jack"

init python:
    def set_replay_name():
        global MC
        persistent._replay_name = MC

    config.after_load_callbacks.append(set_replay_name)


    class ReplayData():
        ReplayList = []
        def __init__(self, image, label, title, description='', scope={}, locked=False):
            self.idle = Transform(image, zoom=0.23, matrixcolor=BrightnessMatrix(0.0))
            self.hover = Transform(image, zoom=0.23, matrixcolor=BrightnessMatrix(0.2))
            self.title = title
            self.label = label
            self.scope = scope
            self.locked = locked
            self.description = description
            ReplayData.ReplayList.append(self)

define replay_1 = ReplayData(
    "d1_tracy_fantasy_15_01", 
    "galleryscene1", 
    _("Tracy Fantasy"),
    scope={"MC" : persistent._replay_name})
define replay_2 = ReplayData(
    "d2_fantasy_esther_11", 
    "galleryscene2", 
    _("Fantasy Esther"),
    scope={"MC" : persistent._replay_name})
define replay_3 = ReplayData(
    "d3_fantasy_sue_14_01", 
    "galleryscene3", 
    _("Fantasy Sue"),
    scope={"MC" : persistent._replay_name})
define replay_4 = ReplayData(
    "d4_sex_03", 
    "galleryscene4", 
    _("Sue Pool"),
    scope={"MC" : persistent._replay_name})
define replay_5 = ReplayData(
    "d5_morning_03_01", 
    "galleryscene5", 
    _("Sue Handjob"),
    scope={"MC" : persistent._replay_name})
define replay_6 = ReplayData(
    "d5_fiona_memory_19", 
    "galleryscene6", 
    _("Fiona Memory"),
    scope={"MC" : persistent._replay_name})
define replay_7 = ReplayData(
    "d9_tracy_sex_55", 
    "galleryscene7", 
    _("Tracy Sex"),
    scope={"MC" : persistent._replay_name})
define replay_8 = ReplayData(
    "d9_sue_sex_08", 
    "galleryscene8", 
    _("Sue Sex"),
    scope={"MC" : persistent._replay_name})
define replay_9 = ReplayData(
    "d10_threesome_18", 
    "galleryscene9", 
    _("Threesome"),
    scope={"MC" : persistent._replay_name})
define replay_10 = ReplayData(
    "d11_sue_12", 
    "galleryscene10", 
    _("Sue Sex"),
    scope={"MC" : persistent._replay_name})
            

style replays_text:
    text_align 0.5
    align (0.5,0.5)
    outlines [(2, "#0009", 1 ,1)]

style replays_vbox:
    spacing 10

screen replays():
    $ tooltip = GetTooltip()
    style_prefix "replays"
    tag menu
    use game_menu(_("Replays"), scroll="viewport"):

        vpgrid:
            cols 3
            spacing 35
            allow_underfull True
            
            for replay in ReplayData.ReplayList:
                vbox:
                    imagebutton:
                        idle replay.idle
                        hover replay.hover
                        action Replay(replay.label, scope=replay.scope, locked=replay.locked) tooltip replay.description
                    text replay.title

    if tooltip:
        ## Use With Renpy Version Below 7.5 and 8.0
        #frame:
        #    style_prefix "tooltip"
        #    hbox:
        #        text tooltip
        ## Use With Renpy Version Above 7.5 and 8.0
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                at choice_appear(.5)
                style_prefix "tooltip"
                hbox:
                    text tooltip


label galleryscene1:
    show d1_tracy_fantasy_02 with dissolve
    tr "Why don't you take this off?"
    # MC grabs her wrist before she can unbutton your shirt
    show d1_tracy_fantasy_03 with dissolve
    tr "I know you are hesitant, but there is no need."
    # Tracy buries her face in your chest and places your other hand on her butt
    show d1_tracy_fantasy_04_01 with dissolve
    tr "Don't you want it, too?"
    tr "Please?"
    show d1_tracy_fantasy_04_02 with dissolve
    tr "You should relieve some stress."
    "You feel her warm belly. Her chest pressing against yours."
    show d1_tracy_fantasy_04_03 with dissolve
    "[Tracy] moves to caress the bulge in your pants."
    # She lifts her chin to your ear
    show d1_tracy_fantasy_05 with dissolve
    tr "Hold me tight."
    "Her sweet voice reaches all the way down your dick producing a tingling sensation on the way."
    show screen in_animation with dissolve
    show d1_tracy_fantasy_06 with dissolve
    # Tracy kisses your neck
    pause(1)
    show d1_tracy_fantasy_07 with dissolve
    hide screen in_animation with dissolve
    "You tightly grab her ass and pull it apart."


    tr "Mmmmm."
    # Ass shot
    show d1_tracy_fantasy_08 with dissolve
    tr "Now we are talking."

    mc "You wanted this."
    tr "Wha-"
    mc "Don't complain afterward."

    show d1_tracy_fantasy_09 with dissolve
    "You forcefully turn her around and press her against the wall."

    tr "Ah!"
    # MC places a hand on her mouth
    show d1_tracy_fantasy_10 with dissolve
    mc "We wouldn't want to wake the others."
    pause(1)
    mc "Are you going to scream?"
    "[Tracy] shakes her head."
    mc "Good girl."
    show d1_tracy_fantasy_11 with dissolve
    "You remove your hand and instantly go in for a kiss."
    show d1_tracy_fantasy_12 with dissolve
    "Her hands that went to explore your body... You plug them and pin them against the wall."
    "As you look into her eyes, you can see a sliver of uncertainty."
    "It quickly vanishes and changes into a smile."
    tr "Take off your shirt."
    show d1_tracy_fantasy_13 with dissolve
    "You press your face into her breasts, finding and nibbling on her nipples."
    tr "Ahhh..."
    tr "You can release my hands. I'll behave myself."

    show d1_tracy_fantasy_14 with dissolve
    "You step back to take off your clothes."
    "[Tracy] wants to help, but you keep her at a distance."

    show d1_tracy_fantasy_15_02 with fade
    "You slide your dick between her thighs, feeling her welcoming warmth."
    tr "What are you waiting for?"
    mc "Ask me to do it."
    show d1_tracy_fantasy_15_01 with Dissolve(2)
    tr "Fuck me..."

    show d1_tracy_fantasy_16 with Dissolve(2)
    "You push your dick into her dripping pussy."
    "[Tracy] grants you a cute moan of surprise as her inside is getting stretched."
    tr "Yes. Yes!"
    tr "Fuck me... I want you to fuck me."
    tr "Ah!"
    pause(2)
    mc "Keep talking."
    tr "Make me your whore."
    tr "U... Use me for your pleasure."
    tr "I want to feel you deep inside me."
    tr "Please..."
    "[Tracy] smiles like she thought of something."
    tr "Keep slamming your cock into my tight little pussy."
    tr "Cum."
    tr "I want to feel your load dripping down my legs."
    tr "Shoot it onto my face and make me lick it all up."
    tr "I want it."
    tr "Please give me your cum."

    menu:
        "Cum inside":
            show d1_tracy_fantasy_17 with flash
            tr "Mmmmm."
            tr "Thank you, Sir."
            tr "I promise I'll be a good girl for you."
            $ renpy.end_replay()


        "Pull out":
            show d1_tracy_fantasy_18 with flash
            tr "Mmmmm."
            tr "Thank you, Sir."
            tr "I promise I'll be a good girl for you."
            $ renpy.end_replay()


label galleryscene2:
    show screen in_animation with dissolve
    scene d2_esther_03 with fadehold
    pause(2)
    show d2_fantasy_esther_01 with dissolve
    pause(1)
    hide screen in_animation with dissolve
    # d2_fantasy_esther_01
    mc "You took your time."
    es "I'm sorry, sir. We had lots to talk about."
    mc "Sure."
    pause(1)

    show d2_fantasy_esther_02 with dissolve
    es "We-"
    mc "It just feels like you all don't appreciate the things I did for you."
    show d2_fantasy_esther_03 with dissolve
    es "You don't have to tell me. Of course, I remember it all very clearly."
    mc "Well, maybe I do."
    show d2_fantasy_esther_04 with dissolve
    mc "If you took this long, then it's hard to imagine you put in a good word for me."
    mc "And that after I went out of my way to break you out of jail. I didn't have to do that, you know?"
    mc "It was actually quite difficult."
    show d2_fantasy_esther_05 with dissolve
    es "I'm very thankful. And I did put in a good word for you, but we wanted to ensure everyone is comfortable relying on you."
    mc "Comfortable, huh..."
    mc "You make it sound so normal."
    mc "I know I offered, but it's you that need help, not me."
    show d2_fantasy_esther_06 with dissolve
    es "I'm aware-"
    show d2_fantasy_esther_07 with dissolve
    mc "It sounds like I need to qualify to you. But honestly, I could just  throw you all out and avoid the giant headache that's coming along with your group."
    mc "What would you do if I wasn't so kind?"
    mc "You should be begging for my help."
    hide d2_fantasy_esther_05
    show d2_fantasy_esther_05 with dissolve
    "[Esther] nods. She doesn't really know how to respond to your words."
    pause(1)
    mc "What are you waiting for?"
    show d2_fantasy_esther_08 with dissolve
    es "Hmmm?"
    mc "Beg me to stay here."
    pause(1)
    show d2_fantasy_esther_09 with dissolve
    es "[MC], would you please allow us to stay at your house a little longer? We don't know this world and would be lost without your help."
    "You shake your head."
    show d2_fantasy_esther_10 with dissolve
    mc "I'm sitting, and you are standing. It's like you're talking down to me."
    mc "Try again."
    mc "Convince me to let you stay."

    show d2_fantasy_esther_11 with dissolve
    "[Esther] reluctantly kneels down and lowers her head."
    es "Please. We would be lost without your help."
    es "Allow us to stay. We'll do anything."

    mc "I don't know."
    mc "You fell to your knees, but maybe you're just acting submissive."
    mc "I'm not sure if you're actually committed."
    es "I am committed."
    mc "It doesn't feel that way."
    pause(2)
    es "Please tell me how I can prove myself."

    show d2_fantasy_esther_12 with dissolve
    mc "Take off your shirt."
    "As she follows your order, you take off your pants."

    show d2_fantasy_esther_13 with dissolve
    mc "Come here. I want you to kiss my cock."
    show d2_fantasy_esther_14 with dissolve
    "[Esther] hesitates."
    mc "Don't act coy."
    mc "You've offered to do it before."
    mc "Follow through on your word."

    mc "Stick out your tongue."
    show d2_fantasy_esther_15 with dissolve
    mc "Put it into your mouth."
    mc "Wrap your lips around and suck it."
    show d2_fantasy_esther_16_01 with Dissolve(2)
    mc "That's good."
    mc "Maybe if you make me cum, I'll consider helping your people."

    mc "You better give it all you have."
    show d2_fantasy_esther_16_02 with Dissolve(2)
    mc "If it hasn't become clear yet, I'm your only hope."
    mc "Without me, you're fucked."
    mc "You can't defend against [Nathaniel], you can't win against the organization, you might even randomly get run over by a bus."

    pause(1)
    mc "That's right."
    mc "You're doing a good job."
    mc "I'm about to cum."
    mc "Listen carefully. When I do, you swallow it."
    mc "I don't want to see a single drop. The moment it enters your mouth, you swallow."
    mc "Do you understand?"
    "[Esther] nods."
    mc "Good."
    mc "Here it comes."

    show screen in_animation with dissolve
    show d2_fantasy_esther_17 with Dissolve(1.5)
    pause(2)
    show d2_fantasy_esther_18 with Dissolve(.3)
    hide screen in_animation with Dissolve(.1)
    # 18 pull up
    "After you cum, you pull her up to her feet. She hasn't swallowed yet, so your cum should still be in her mouth."
    mc "Do it."
    "[Esther] gulps it down."

    pause(1)
    mc "This is good enough for now."
    $ renpy.end_replay()


label galleryscene3:
    show screen in_animation with dissolve
    scene d3_bath_03 with fadehold
    pause(2)
    show d3_fantasy_sue_02 with dissolve
    hide screen in_animation with dissolve
    # d3_fantasy_sue_02
    "You approach [Sue]."
    "Not saying anything makes her a little nervous. She is naked after all."
    # 03 MC leans in and whispers in her ear
    show d3_fantasy_sue_03 with dissolve
    mc "Sure."
    mc "What is it you want to know?"
    "You kiss her cheek and pull back, leaving her a little flustered."
    show d3_fantasy_sue_04 with dissolve
    su "[Lucy] said something about cleaning yourself while standing under a stream of water."

    show d3_fantasy_sue_05 with dissolve
    mc "And?"
    su "I want to try it."
    mc "Hmmm. It can't be avoided then."

    show d3_fantasy_sue_06 with dissolve
    su "Why are you taking off your clothes?"
    mc "I'll need to show you how it's done."
    mc "Isn't that what you wanted?"
    pause(1)
    mc "[Sue]?"
    show d3_fantasy_sue_07 with dissolve
    su "Ah! Yes, that would be great!" with vpunch

    mc "Get in the shower then."
    show d3_fantasy_sue_08 with dissolve
    su "Like this?"
    mc "Do you see the metal knob? Try pulling it."

    show d3_fantasy_sue_09 with dissolve
    "[Sue] jumps back as the cold water hits her body."
    mc "Don't be afraid. This is normal."
    mc "See, it's already getting warm."

    su "[MC]?"
    mc "What is it?"
    su "Is this..."
    "Your dick is rubbing on [Sue]'s leg."

    mc "Well, this much should be normal. It's not like I can help it."
    su "Do you want me to-"
    mc "But we are here to clean you up, aren't we? Let us not forget why we are here."
    mc "Go on, step under the stream."

    show d3_fantasy_sue_10 with dissolve
    su "Tell me if I'm doing something wrong."
    mc "First we'll rinse off any sweat or dirt that's on your skin."
    show d3_fantasy_sue_11 with dissolve
    "You go ahead and rub her body."
    pause
    show d3_fantasy_sue_12_01 with dissolve
    "Of course, there is nothing innocent about this, but at least at first, you stay in safe areas."
    # MC kneels down looking at Sue's pussy rubbing her legs
    pause
    show d3_fantasy_sue_12_02 with dissolve

    su "[MC]?"
    mc "We have to make sure not to miss anything."
    show d3_fantasy_sue_13 with dissolve
    su "Is that so?"
    mc "Yes, that's quite important."
    su "If that's the case, then... Maybe we should-"
    show d3_fantasy_sue_14_02 with dissolve
    su "Ah!"
    "[Sue] lets out a cute scream as you force your hand between her legs."

    mc "Some areas of the body are more important than others and require special attention."
    "A smile, then a nod."
    mc "Let's take care of it first so it will be out of the way."
    show d3_fantasy_sue_14_01 with dissolve
    mc "Later we are going to use soap, but both of your holes are sensitive. Soap is quite abrasive and might do more harm than good."
    su "Both?"
    mc "We are still going to clean them thoroughly, but for now, we will only use plain water."

    show d3_fantasy_sue_15 with dissolve
    "You turn off the water."
    mc "Before we can do that, though, we will have to prep them first."
    show d3_fantasy_sue_16_02 with dissolve
    "You lick your index finger and circle her anus."
    show d3_fantasy_sue_16_01 with vpunch
    mc "Do you understand what I'm saying?"
    su "I think so."
    mc "And? You want to be clean, don't you?"
    "[Sue] nods."

    "You press in until the tip of your finger vanishes inside her asshole."
    mc "Squeeze my finger."
    su "Are you sure?"
    mc "Trust me. Squeeze, then relax."
    "You keep pressing inward with your finger. As [Sue] relaxes, your finger finally glides in fully."
    mc "That's right."
    "You want to widen her hole, so you keep your finger all the way inside, and  do circling motions."


    show d3_fantasy_sue_18 with dissolve
    mc "Can you feel this?"
    su "It feels weird."
    mc "You'll get used to it."
    mc "Eventually I might even train you to enjoy it."
    su "Yes. Thank you, [MC]."

    show d3_fantasy_sue_17 with dissolve
    mc "I'm going to start to get a little rough. You don't mind, do you?"
    su "Oh..."
    "[Sue] can feel how your finger is moving in and out of her ass. At first it's slow, but then you increase the speed."

    # change perspective
    hide d3_fantasy_sue_17 with dissolve
    "It's a strange feeling."
    "She doesn't know how to react and, in her confusion, starts to moan."
    "Someone is fingering her. It might not be her pussy, but moans are the right response, right?"
    "It's obvious that something extremely lewd is being done to her."
    show d3_fantasy_sue_19 with dissolve
    "She should be enjoying it, right?"
    "Now that she thinks about it, this does feel nice."
    "She had this tingling feeling ever since she stepped into the shower with [MC]."
    "He washed her, touched her."
    show d3_fantasy_sue_20 with dissolve
    "It felt amazing."
    "And now he is fingering her asshole. And that feels amazing, too."

    show d3_fantasy_sue_17 with Dissolve(2)
    su "(That's right...)"
    "There is only one thing to do. [Sue] reaches back and grabs your dick."
    show d3_fantasy_sue_21 with dissolve
    hide d3_fantasy_sue_17
    "While being fingered, she starts giving you a handjob."

    mc "You're greedy."
    mc "I like it."

    mc "Today it's only one finger, but eventually you will take my dick up there."
    mc "I hope you are looking forward to it."
    su "If this pleases you, then- Ah! It will be my pleasure."

    "You're standing in the shower, so you don't even announce that you're close."
    show d3_fantasy_sue_22 with flash
    "With your finger up her ass, you squirt your cum inside the cabin."
    su "Is that cum?"
    mc "You've never seen it?"
    "[Sue] shakes her head."
    mc "Next time, I'll make you eat it."
    stop music fadeout 3
    show black with Dissolve(3)
    $ renpy.end_replay()


label galleryscene4:
    su "Mmmhh, you smell good, Sir."
    stop music fadeout 1
    show d4_pool_12_01 with dissolve
    play music "audio/music/erotic/Feel Me.wav"
    "[Sue] places her hand on your leg."
    show d4_pool_12_02 with dissolve
    su "I haven't told you what I can do with my ability yet, have I?"
    su "I love the water because it feels like home."
    show d4_pool_14 with dissolve
    "[Sue] creates two little people."
    show d4_pool_13 with dissolve
    "You put your hand around her shoulder and pull her closer."
    su "Oh. That feels nice."
    su "Thank you, [MC]."
    show d4_pool_15 with dissolve
    mc "Your ability is to create little figures?"
    su "I command water. I'm connected to it."
    mc "Is that one me?"
    su "Yes."
    mc "Cute."
    su "When it comes to water, I can do whatever I want."
    mc "And that one is you?"
    "[Sue] nods."
    mc "Why are we naked?"
    su "You'll see."
    show d4_pool_16 with dissolve
    pause
    show d4_pool_17 with dissolve
    pause
    show d4_pool_18 with dissolve
    pause(.5)
    mc "Do you want me to do this to you?"
    su "Just planting some ideas. You can do whatever you want. I think you know that, right?"
    show d4_pool_19 with dissolve
    mc "So if I want to kiss you, I'd just…"
    show d4_pool_20 with dissolve
    "You lift her chin."
    su "Yes."
    pause(2)
    mc "If I were that little figure of yours, you could just make me do it."
    su "I want you."
    show d4_pool_21 with dissolve
    "You let your lips touch."
    mc "Like this?"
    su "More."
    mc "Patience."
    mc "Open your mouth."
    show screen in_animation with dissolve
    show d4_pool_22 with dissolve
    pause(1)
    show d4_pool_23 with dissolve
    hide screen in_animation with dissolve
    "When kissing, you let your tongue slide into her mouth."
    su "Mmm."
    show d4_pool_24 with dissolve
    "[Sue] slides her hand into your trunks."
    "You feel her hand wrap around your penis."
    su "You're already hard, Sir."
    mc "Come here."
    show d4_pool_25_01 with dissolve
    "You pull her onto your lap."
    pause
    show d4_pool_25_02 with dissolve
    pause(1)
    mc "Those are very beautiful."
    show d4_pool_26 with dissolve
    "[Sue] bites her lip as you touch her breasts."
    pause(1)
    mc "(So sensitive.)"
    show d4_pool_27 with dissolve
    "You can feel the warmth of her vagina through the fabric of your trunk."
    "[Sue] goes in for a kiss."
    "Her lips feel moist and soft. She runs her finger through that short beard of yours."
    show d4_pool_28_02 with dissolve
    mc "(Such a great ass.)"
    pause
    show d4_pool_28_01 with dissolve
    "Her warm body glides over your skin as you grab her by the ass and pull her closer."
    mc "(She's so turned on.)"
    "You massage her ass."
    su "[MC]!"
    mc "(This little has her screaming my name.)"
    show d4_pool_29 with dissolve
    su "I… I want to feel you inside me!"
    mc "Patience. We still need to get upstairs to my room."
    su "I want you now. Please, [MC]."
    hide d4_pool_29 with dissolve
    mc "My bed is in my room."
    su "And we are down here. What does it matter?"
    mc "You said it yourself. You've been living with that itch your entire life. You can hold out for a few more minutes, right?"
    show d4_pool_29 with dissolve
    su "Do I have to?"
    mc "Yes."
    mc "I want you to wait for me in my room."
    "[Sue] nods."
    mc "Don't worry. I won't make you wait for long."
    show d4_pool_30 with dissolve
    "[Sue] gives you one last kiss, making sure you understand how unbearable the thought of her waiting for you is."
    show screen in_animation with dissolve
    pause(1.5)

    show d4_pool_31 with Dissolve(2)
    pause(1.5)
    hide screen in_animation with dissolve
    mc "(So, I actually decided to give in. Seems like you didn't manage to change me after all…)"
    stop music fadeout 3
    show screen in_animation with dissolve
    pause(1.5)

    scene d4_sex_01 with fadehold
    hide screen in_animation with dissolve
    "When you go upstairs, [Amber] smiles at you knowingly."
    mc "[Cecilia]?"
    am "She already left."
    show d4_sex_02 with dissolve
    "You turn around to enter your room."
    mc "(It's been a while.)"

    show d4_sex_03 with fade
    play music "audio/music/erotic/Feel Me.wav"
    pause(1)
    mc "(She's already naked.)"
    "You smile."
    mc "(I didn't see her clothes downstairs.)"
    mc "(Chances are, [Sue] came to the pool naked.)"
    mc "(To get to my room she had to walk past those of the other members of her group.)"
    mc "(I guess it's not just [Amber] that knows what we are about to do.)"
    pause(1)
    su "Am I doing something wrong?"
    pause(1)
    mc "No. You're lovely."
    show d4_sex_04 with dissolve
    "[Sue] tries to restrain herself while watching you undress."
    pause(1)
    mc "Have you ever seen a penis?"
    "[Sue] shakes her head."
    mc "No, but you've touched one before."
    su "Yours."
    mc "Earlier, I touched your breasts. They were very sensitive."
    su "I'm numb to a female's touch."
    mc "You don't feel it if [Tracy] touches you?"
    su "I do, but it doesn't turn me on."
    mc "But if I were to touch you?"
    su "It feels nice."
    mc "I like the idea. Let's see if I can make you feel... Nice."
    show d4_sex_05 with dissolve
    pause(2)
    "[Sue] already breaths heavily."
    su "[MC]!"
    mc "Do you want me to keep going?"
    su "Please."
    mc "I like the way your breasts jiggle. Maybe we should forget about the sex, and I just keep doing this?"
    mc "That would be fun, wouldn't it?"
    su "I want you..."
    mc "What was that?"
    su "Please, [MC]. I want you inside me!"
    mc "And I want to see your breasts jiggle. I think we have a conflict of interest here."
    su "Mmmhhh!"

    pause(2)
    mc "Hm."
    mc "There is only one solution, right?"
    mc "I'll have to find another way to make your breasts bounce."


    show black with dissolve
    hide d4_sex_05
    "You push her onto her back."

    su "Put it in."
    show d4_sex_06 with dissolve
    mc "So demanding."
    mc "What about, {i}I've lived my entire life with this itch. What does it matter if I have to wait a little longer?{/i}"
    pause(2)
    mc "You're numb to a female's touch, huh?"
    mc "So if I tap my dick on your pussy, that's the first thing you've ever felt down there that made you all hot and bothered?"
    su "You're my first!"

    hide black
    show black with dissolve
    "You push your dick into her already more than wet pussy."
    mc "(Maybe I didn't need so much foreplay after all.)"

    su "Ah!"
    mc "Are you alright?"

    "[Sue] nods."

    show d4_sex_10_01 with dissolve
    hide d4_sex_06
    su "Hmmmm..."
    "[Sue] moans loudly."
    mc "The others might hear you."
    su "L-Let them hear."
    mc "Hard to speak, huh?"
    "[Sue] lets her head fall back, enjoying every single one of your thrusts."

    show d4_sex_09_01 with fade
    hide d4_sex_10_01
    pause(1)
    su "In the... My... My breasts."
    mc "I know. Told you I'd get them bouncing somehow."
    mc "But if you're still talking, I'm not doing my job right."

    show d4_sex_09_02 with dissolve
    hide d4_sex_09_01
    "You increase the speed a little."

    mc "(Now, that's the kind of eye contact you need to seduce someone.)"
    mc "(Three days.)"
    mc "(How did you do it, [Sue]?)"
    mc "(No.)"
    show d4_sex_10_02 with dissolve
    hide d4_sex_09_02
    mc "(Why did I hold out for so long?)"
    mc "(That's not like me.)"

    show d4_sex_09_02 with dissolve
    hide d4_sex_10_02
    mc "I'm close."
    su "I want it."
    "It's not easy, but [Sue] finds herself some gaps between her moans where she can talk."
    su "Cum for me, [MC]!"
    mc "Now."

    show d4_sex_11 with flash
    hide d4_sex_09_02
    "You pull out and finish yourself on her belly."

    pause(2)
    "[Sue] is trying to regulate her breathing."
    mc "That good, huh?"
    "She looks at you and smiles. There are probably no words that would do this moment justice."
    show screen in_animation with dissolve
    pause(1)

    stop music fadeout 5
    show d4_sex_12 with fade
    pause(2)
    hide screen in_animation with dissolve
    su "I should clean myself up."
    "You nod."
    su "Can I come back to your room afterward?"
    mc "I'll probably be asleep, then."
    su "I want to be with you."
    mc "I don't mind."
    su "Thank you, Sir."

    show d4_sex_13_01 with fadehold
    play music "audio/music/erotic/Pleasure.wav"
    pause(2)
    sa "And?"
    show d4_sex_13_02 with dissolve
    pause(1)
    "[Sue] can't stop smiling. There is cum dripping down her belly, but she doesn't mind."
    "Still smiling, she nods."
    su "We did it."
    pause(1)
    $ renpy.end_replay()


label galleryscene5:
    show screen black with trans_time
    show screen showTime(1, "Do", "08:03") with trans_time
    scene black
    pause(1)
    play music "audio/music/erotic/Feel Me.wav"
    hide screen showTime with trans_time
    hide screen black with trans_time
    pause(.5)
    "You smile."
    show d5_morning_01_01 with Dissolve(2)
    mc "That's a new one."
    su "Good morning, [MC]."
    mc "Did I miss my alarm?"
    su "I switched it off. You don't mind me waking you up instead, do you?"
    mc "It's unconventional."
    mc "Usually, you'd ask the person beforehand if you can wake them up this way."
    su "Is it unpleasant?"
    "You feel [Sue]'s breast rubbing against your body."

    menu:
        "Ask her to stop":
            mc "I'm awake now. You can stop."
            su "Are you sure?"
            mc "Yes."
            $ renpy.end_replay()

        "Teach her about finishing what she starts" (sex = True):
            mc "No."
            show d5_morning_01_02 with dissolve
            hide d5_morning_01_01
            "[Sue] smiles and increases the speed at which she is jerking you off."
            su "Will you cum for me, [MC]?"
            mc "(Where is this confidence coming from?)"
            su "Yesterday, you came all over me."
            su "Why don't you do that again?"
            su "This time I want to feel it on my chest."
            su "Please [MC]."

            menu:
                "This is so hot" (sex = True):
                    su "Don't make me wait too long. I can't take it."
                    su "I want it now. Only thinking about you shooting your load makes me so horny."
                    su "There is this warm feeling inside my chest."
                    su "It's even hard to speak, but I want you to know how I feel."
                    mc "I'm about to cum."
                    show d5_morning_07_01 with flash
                    hide d5_morning_01_02
                    "You shoot your load over [Sue]'s chest."
                    show d5_morning_07_02 with dissolve
                    scene d5_morning_08_01 with fade
                    play music "audio/music/erotic/Pleasure.wav"
                    su "What are you going to do now, [MC]?"
                    mc "I need to see if [Amber] has already left to get breakfast. I also want to take a shower after a night like this."
                    su "Can I take it with you?"
                    mc "The shower?"
                    "[Sue] nods."
                    $ renpy.end_replay()


                "This won't cut it" (sex = True):
                    "Having her give you a simple hand job will take too long. Instead of leaning back and having [Sue] do all the work, you take charge, grab [Sue], and turn her around."
                    show d5_morning_03_01 with dissolve
                    hide d5_morning_01_02
                    su "[MC]?!?"
                    show d5_morning_03_02 with dissolve
                    "You place your hand on her ass and playfully pull at one of her pussy lips."
                    mc "You have such a beautiful pussy. I want to use it."
                    show d5_morning_04_02 with dissolve
                    "[Sue] is taken aback. How could she keep a clear head in such a situation? Especially the way you casually touch her pussy takes away all her composure."
                    show d5_morning_04_01 with dissolve
                    "She realizes that you didn't do anything yet."
                    hide d5_morning_04_02
                    hide d5_morning_03_02
                    hide d5_morning_04_01 with Dissolve(2)
                    su "Are you asking for permission?"
                    mc "What does it look like?"
                    show d5_morning_04_01 with dissolve
                    su "Please fuck me, [MC]."
                    show d5_morning_02_01 with dissolve
                    "You push your dick inside her warm vagina."
                    mc "(Now, this is a way to be woken up. How about I return the favor the next time we are sleeping together? I'm sure [Sue] would love to wake up with a dick on her face.)"
                    su "Oh, [MC]!"
                    show d5_morning_02_02 with dissolve
                    mc "(Maybe I should not fuck [Sue] in the morning. The others might dislike waking up to her moans.)"
                    mc "(On the other hand, I do like to hear her scream. She said she only feels it if a man touches her. And she said I am her first.)"
                    mc "I'm about to cum. I want to finish on your chest."
                    "[Sue] licks her lips."
                    su "Please [MC]. Cum for me."
                    show d5_morning_05 with dissolve
                    "When you pull out, it only takes a few more strokes until you shoot your load. [Sue]'s eyes light up when she sees the cum spraying all over her breasts."

                    mc "Good morning, [Sue]."
                    su "Thank you."
                    $ renpy.end_replay()


label galleryscene6:
    show d5_fiona_memory_02 with Dissolve(1)
    pause(1.5)
    show d5_fiona_memory_03 with dissolve
    pause(1.5)
    show d5_fiona_memory_04 with dissolve
    hide screen in_animation with dissolve
    mc "Are you satisfied with it?"
    fi "Hmmm."
    show d5_fiona_memory_05 with dissolve
    fi "Do you think it's tilted?"
    mc "You really don't have any faith in my abilities, do you?"
    mc "I even sketched it out. Yeah, it should be straight now."
    hide d5_fiona_memory_05 with dissolve
    pause(1)
    fi "Maybe it should lean more to the right."
    mc "I'll fix it tomorrow, if you insist."
    mc "But it's modern art. Wouldn't a slight tilt only add to it?"

    show d5_fiona_memory_06 with dissolve
    "[Fiona] smiles, knowing full well what you're trying to do."
    show d5_fiona_memory_07 with dissolve
    fi "Was it so much work that you want to convince me to leave it be?"
    mc "Come now. It's the slight imperfections that make art. Nowadays if we want to preserve something to its fullest detail, we simply take a picture."
    mc "Making the brush strokes flow together forming a magnificent painting is where the art lies."
    show d5_fiona_memory_08 with dissolve
    fi "Are you making fun of modern art?"
    mc "Maybe a little."
    mc "But I also don't really know how to tell you, but... Look at it again. The lines are slightly off center. It's literally part of the artwork."

    show d5_fiona_memory_09 with dissolve
    fi "Oh..."
    mc "You're doing the thing where it's not actually the lamp you're thinking about, right?"
    fi "Maybe."
    mc "Is it because of yesterday?"
    show d5_fiona_memory_10 with dissolve
    mc "I thought you agreed. I even sensed excitement. What's the problem? Did you change your mind?"
    fi "That's not it."
    mc "What is it, then? Are you afraid I'll put a baby in you the moment you're not looking?"

    pause(1)
    fi "What changed? We said we would wait until we are married. Why do you want to hurry?"
    mc "Isn't it normal for a guy to want to make love to his girlfriend? When I asked you to marry me, you knew I wanted to have a family."
    show d5_fiona_memory_11 with dissolve
    fi "You're doing it again. You're not addressing the issue."
    mc "So that's it. You're worrying about me."
    fi "Of course, I worry. You haven't been sleeping these past few days. I hoped you would eventually talk to me."
    mc "Like I am right now?"
    show d5_fiona_memory_12 with dissolve
    fi "No. I want you to actually want to share your problems. Now it's like I'm forcing you."
    mc "I just don't want to worry you."
    hide d5_fiona_memory_12 with dissolve
    fi "And how did that work?"

    pause(1)
    mc "Okay."
    mc "I was thinking about going back to my old life."
    mc "Well, I didn't for long. Having the thought is a problem, right? What if one day I can't come up with an answer to why I should stay away from my old job?"
    mc "So the next few days I've been thinking about how I can make sure to always have a good reason."
    hide d5_fiona_memory_05
    show d5_fiona_memory_05 with dissolve
    fi "Kids?"
    mc "Yeah. That's one way, isn't it?"
    fi "But they'll grow up. Won't you then..."
    mc "We can always make new ones, right?"
    show d5_fiona_memory_13 with dissolve
    fi "How many do you want?!?"
    mc "How many will you give me?"
    fi "Eh..."

    pause(1)
    mc "For now, how about we start with one and go from there?"
    hide d5_fiona_memory_07
    show d5_fiona_memory_07 with dissolve
    "[Fiona] smiles and nods."
    mc "Let's do it then."
    hide d5_fiona_memory_08
    show d5_fiona_memory_08 with dissolve
    fi "Like now?"
    mc "Yes, [Fiona]."
    mc "I want you."
    show d5_fiona_memory_14 with dissolve
    mc "Right now."

    show d5_fiona_memory_15 with fadehold
    "You gently relieve your fiance of her clothes the same way she does with you."
    mc "Are you ready to get filled up?"
    fi "Not yet."
    # 16 animation
    show d5_fiona_memory_16 with Dissolve(1)
    "You reach down and rub her pussy."
    fi "[MC]!"
    mc "Relax and enjoy."

    pause
    show d5_fiona_memory_17 with fadehold
    fi "I'm ready. You can..."
    show d5_fiona_memory_18 with Dissolve(1)
    mc "What?"
    show d5_fiona_memory_19 with dissolve
    fi "{size=20}You can fuck me.{/size}"
    mc "Can you speak up, I didn't quite hear you."
    show d5_fiona_memory_20 with Dissolve(1)
    "Before [Fiona] can get angry at you for making her say this twice, you push your dick inside her."
    mc "You're cute when you're embarrassed."
    mc "But you're my fiance. You shouldn't be embarrassed about wanting to get fucked."

    "[Fiona] wants to protest, but it would be quite comical for her to stress that she didn't actually say that she wanted to get fucked while getting fucked and thoroughly enjoying it."

    pause
    stop music fadeout 3
    show black with Dissolve(3)
    $ renpy.end_replay()


label galleryscene7:
    stop music fadeout 3
    scene d9_tracy_sex_01 with fadehold
    play music "audio/music/Erotic/Feel Me.wav"
    pause
    show d9_tracy_sex_02 with dissolve
    pause
    show d9_tracy_sex_03 with vpunch
    tr "[MC]!"
    show d9_tracy_sex_04 with dissolve
    tr "I thought you…"
    mc "I changed my mind."
    show d9_tracy_sex_05 with dissolve
    tr "What are you doing?"
    mc "Do you mind that I'm here?"
    show d9_tracy_sex_06 with dissolve
    "[Tracy] averts her face."
    mc "This again…"
    show d9_tracy_sex_07 with dissolve
    tr "It's okay."
    mc "Okay, huh? Is that all you want to say?"
    hide d9_tracy_sex_07 with dissolve
    mc "I think I know how you feel, but I'm going to need more than this."
    mc "Do you mind if I kiss you?"
    tr "No."
    mc "Do you want me to kiss you? Think about it. It's not the same question."
    show d9_tracy_sex_08 with dissolve
    tr "Yes."
    # MC closing the distance
    show d9_tracy_sex_09 with dissolve
    mc "I'm not convinced."
    # MC's face close to Tracy's
    show d9_tracy_sex_10 with dissolve
    "[Tracy] closes her eyes."
    show d9_tracy_sex_11 with dissolve
    "For a short moment, her lips touch yours."
    "A quick peck."
    show d9_tracy_sex_12 with dissolve
    pause(1)
    mc "This must have taken a lot of courage."
    mc "Alright."
    # Image of MC pressing his lips on Tracy's
    show d9_tracy_sex_13 with dissolve
    pause
    # Image of MC pulling back a bit
    show d9_tracy_sex_14 with dissolve
    mc "You can push me away. I don't mind."
    pause(1)
    show d9_tracy_sex_15 with dissolve
    tr "I don't understand."
    tr "Didn't you say that people in your world think this is wrong?"
    mc "Can you keep a secret?"
    "[Tracy] nods."
    mc "I've never considered myself a particularly moral person."
    mc "I like you [Tracy]."
    mc "I tried, but I can't ignore that. If I didn't show you, I'd regret it."
    hide d9_tracy_sex_15 with dissolve
    mc "Yes, there is [Fiona]. I hope she can accept it. But if she can't…"
    mc "I like her too, but if she can't, then maybe we weren't meant for one other."
    mc "Does this make sense?"
    "[Tracy] nods once again."
    mc "You haven't pushed me away yet… Do I have to try harder?"
    mc "I mean, you're naked and I'm so close. Do you think it's okay because you're stronger than me?"
    mc "I have your ability. Don't think it's going to be easy to overpower me. If you don't want this then you have to try and stop me."
    # You let your hand glide along her waist.
    show d9_tracy_sex_16 with dissolve
    mc "(Is she not going to move? She is expecting me to lead…)"
    mc "(Fine. Don't mind if I do.)"
    # 17 On the floor
    show d9_tracy_sex_17 with dissolve
    "You pick her up and gently lay her down on the floor."
    # 18 MC POV
    show d9_tracy_sex_18 with dissolve
    mc "Is this what you want?"
    tr "Yes."
    mc "I'm not going to restrain myself. Is that okay?"
    # 19
    show d9_tracy_sex_19_02 with dissolve
    "[Tracy] grabs your hand and places it between her breasts."
    tr "Just because my heart is racing… You don't have to hold back."
    # MC sucking on Tracy's nipple. She is lying down, her legs together, and her pelvis turned to the side. (In my head, this is a really hot image; idk if I can describe it, though.)
    show d9_tracy_sex_20 with dissolve
    tr "Ahhhh…"
    mc "I like hearing that you."
    show d9_tracy_sex_21 with dissolve
    "You gently caress her belly."
    "Soft moans escape her mouth."
    show d9_tracy_sex_22 with dissolve
    "Amplified by the walls, they echo through the empty room."
    "The floor is cold. It's a sweet contrast to the warm water of the shower."
    show d9_tracy_sex_23 with dissolve
    "Since you've copied [Tracy]'s ability, you've noticed that cold and warmth no longer feel uncomfortable."
    "Your range of suitable temperatures seems to have increased."
    hide d9_tracy_sex_22
    hide d9_tracy_sex_23 with dissolve
    "This doesn't mean you can't feel and enjoy things like the warm sensation of [Tracy]'s skin."
    "Her body is heating up under your touch. All that even though you haven't yet touched her thighs."
    # 24 licking neck
    show d9_tracy_sex_24 with dissolve
    "You were afraid that since she has been training her body for years, she would be numbed to touch."
    "Her reaction when you lick her neck suggests the opposite. Your soft and gentle touch must be an unusual new sensation."
    # 25 Side of face
    show d9_tracy_sex_25 with dissolve
    "At first, she was tense and tried to move away."
    "You simply continued to caress her until she was able to enjoy it properly."
    # 26 side of breasts
    show d9_tracy_sex_26 with dissolve
    "Now she is still moving, but it's different. She no longer wants to escape, but she leans into your hands."
    # 27 arch
    show d9_tracy_sex_27 with dissolve
    "When you come back to her hip she arches her back and lets out another moan."
    # 28 Hand on knee
    show d9_tracy_sex_28 with dissolve
    "After quite a while of sweet torture you finally decide to explore those beautiful thighs of her."
    "Up until now she has kept them firmly locked together."
    show d9_tracy_sex_29 with dissolve
    "You kiss her waiting for her to give you an opportunity to slide your fingers in between her legs."
    show d9_tracy_sex_30 with dissolve
    "[Tracy] shivers as your fingers first brush over her most sensitive area."
    show d9_tracy_sex_31 with dissolve
    "You rest your hand down there."
    "While [Tracy] is still overwhelmed by the pleasurable sensation you let your thumb glide through her pubes."
    "They are well-trimmed. [Cecilia] told [Sue] about shaving, but [Tracy] was already like this when she showed herself naked on the first day."
    # 32 animation
    show d9_tracy_sex_32 with Dissolve(1)
    "With that thought in mind you start moving your fingers."
    "Even though your movements are slow [Tracy] grants you the occasional moan."
    # 33 animation
    show d9_tracy_sex_33 with Dissolve(1)
    hide d9_tracy_sex_32
    "Her eyes are different from the other day."
    "You're not sure if it's her or if it's you that caused the change, but today, you can clearly see the part of her that wants to do this."
    "Her eyes are sparkling with lust. Her cheeks red, her breathing heavy."
    # 34 animation
    show d9_tracy_sex_34 with Dissolve(1)
    hide d9_tracy_sex_33
    "You put your lips onto hers to make sure."
    "Yes… Her tongue is greedy."
    "She is so turned on."
    show d9_tracy_sex_35 with Dissolve(1)
    hide d9_tracy_sex_34
    "[Tracy] reaches for your hand and pushes it further between her legs. You've been teasing her clit and lips, but it seems [Tracy] isn't satisfied."
    # MC face close to Tracy's ear
    show d9_tracy_sex_36 with dissolve
    mc "Do you want more?"
    "She nods."
    mc "I need you to do something for me."
    show d9_tracy_sex_37 with dissolve
    "You pull away your hand that was still gently teasing her pussy, and bring it up to her lips."
    mc "Suck on my finger…"
    # 38 animation
    show d9_tracy_sex_38 with dissolve
    "[Tracy] obediently follows your request."
    "She left her legs open, allowing you easy access whenever you feel like touching her pussy."
    mc "(Such a good girl…)"
    show d9_tracy_sex_39 with dissolve
    hide d9_tracy_sex_38
    "Your now wet finger is the first thing that you push into her pussy."
    "[Tracy] lets out a cute squirm while realizing that things are getting more serious."
    # 40 animation fingering 3 fingers
    show d9_tracy_sex_40 with Dissolve(1)
    "At first, you only used one, but you quickly worked your way up to three fingers. She is so wet… You didn't need her spit."
    "A few seconds ago [Tracy] sucked your finger obediently, but apparently this wasn't necessary. Still, she looked really hot doing it."
    show d9_tracy_sex_41 with fadehold
    hide d9_tracy_sex_40
    "You pull back your hand. [Tracy] doesn't understand. She moves her pelvis toward you seeking your touch."
    show d9_tracy_sex_42 with dissolve
    "Your hand that likes to stay busy is looking for the sensation of soft tits and hard nipples."
    tr "[MC]?"
    mc "I need another favor…"
    tr "Wha-"
    show d9_tracy_sex_43 with dissolve
    "You pinch her nipple."
    tr "Ah!"
    hide d9_tracy_sex_43 with dissolve
    mc "I want you to do something for me."
    tr "What?"
    show d9_tracy_sex_44 with fade
    "With quick movements, you pull [Tracy] on top of you."
    "If she were alert, there would be no way you could surprise her, but another cute scream confirms that [Tracy] is currently showing you one of her more vulnerable sides."
    show d9_tracy_sex_45 with dissolve
    "You look into her uncertain eyes."
    "You can feel her warm thighs resting on your hip."
    mc "Help me undress."
    show d9_tracy_sex_46 with dissolve
    mc "(It's clear as day.)"
    mc "(Her expression changed.)"
    mc "(Reflected in her eyes is the type of passion that an inexperienced woman like [Tracy] wouldn't be able to fake.)"
    mc "(Maybe even professional actresses would have a hard time forming such an expression.)"
    show d9_tracy_sex_47 with dissolve
    "[Tracy] pulls your shirt out of your shorts."
    mc "Wow…"
    show d9_tracy_sex_48 with dissolve
    "You expected her to simply pull it up."
    "Instead, [Tracy] has learned from what you did to her. She lets her fingers wander up your belly in search of your chest."
    "Your head rests on the hard tiles as you enjoy a sensation you haven't felt in a while."
    "[Sue] touched you before, but it didn't feel the same way."
    "Since it was so unexpected you feel like you're about to burst."
    show d9_tracy_sex_49 with fade
    "You sit up which confuses [Tracy]. She thought it was her turn to make you feel good."
    tr "[MC]?"
    mc "I want you. Now…"
    "There is no way you can just lean back. You quickly strip out of your shirt."
    stop music fadeout 2

    show d9_tracy_sex_50 with fadehold
    play music "audio/music/Erotic/Pleasure.wav"
    "While standing up, you try to pull [Tracy] up with you, but her legs betray her."
    "It's only for a second, but you can't help but feel a little proud."
    show d9_tracy_sex_51 with dissolve
    "Your shorts are gone."
    mc "([Tracy] must have an idea of what I'm about to do, but she is still not running.)"
    mc "(Well... She had every opportunity.)"
    mc "(I'm done asking if it's okay.)"
    show d9_tracy_sex_52 with dissolve
    "In the next moment you find yourself entangled in a passionate kiss."
    "She reaches for your dick."
    "You chuckle at her inexperience. She is trying to put your dick inside her even though you're in no position to do that right now."
    show d9_tracy_sex_53 with dissolve
    "You gently take her arms and place them around your neck."
    mc "The benefits of superhuman strength…"
    "[Tracy] feels a wall at her back."
    show d9_tracy_sex_54 with dissolve
    "You lift up one of her legs which allows you to easily slide into her."
    "As she notices what you are about to do, [Tracy] braces herself."
    # 55 pain
    show d9_tracy_sex_55 with dissolve
    "The sensation is much different from that of mere fingers."
    "You lift her other leg which means you're now supporting her full weight."
    show d9_tracy_sex_56 with dissolve
    "It doesn't even register as effort. Her ability unlocked so many new possibilities."
    "Your dick is resting in a very comfortable place, patiently waiting as you allow [Tracy] a moment to understand the situation."
    mc "I'm sorry… I don't think I'm going to last very long."
    show d9_tracy_sex_57 with dissolve
    mc "(She doesn't understand why that would matter.)"
    mc "(It doesn't matter.)"
    # 58 animation
    show d9_tracy_sex_58 with dissolve
    "Keeping her pinned between you and the wall you start moving."
    "It's beautiful to observe the change in [Tracy]'s expression. She is wearing her emotions on her sleeve."
    "At first, it's still strange… But with every new thrust, she gets more and more used to being penetrated."
    # 59 animation
    show d9_tracy_sex_59_01 with dissolve
    hide d9_tracy_sex_58
    "Once again you notice her warmth."
    "Her moans echo throughout the room."
    "You'd love to hear her scream your name once again, but she doesn't."
    # 60 look away moaning
    show d9_tracy_sex_60 with dissolve
    hide d9_tracy_sex_59_01
    mc "(Maybe she is too shy to do so.)"
    mc "(But she is also not hiding her pleasure.)"
    mc "(It's written all over her face.)"
    mc "Don't hold back."
    # 59
    show d9_tracy_sex_59_01 with dissolve
    hide d9_tracy_sex_60
    mc "I want to hear you."
    mc "(This feels too good.)"
    tr "Ah... This is... Eh..."
    mc "Should I slow down?"
    show d9_tracy_sex_58 with dissolve
    hide d9_tracy_sex_59_01
    tr "No!"
    mc "(There she is.)"
    "You smile from ear to ear."
    mc "Scream my name."
    tr "Huh?"
    tr "Ah!"
    mc "I want to hear you scream my name, [Tracy]."
    tr "[MC]?"
    # 59 fast
    show d9_tracy_sex_59_02 with dissolve
    hide d9_tracy_sex_59_01
    "While you were considerate at first, your thrusts have become hard and fast."
    tr "Ahhh! Ahhh… Mmmm- Ah!"
    "The moans have become constant."
    tr "[MC]!"
    "[Tracy] pulls you closer."
    mc "That's right…"
    "You're so close to the edge."
    # 59 very fast
    show d9_tracy_sex_59_03 with dissolve
    hide d9_tracy_sex_59_02
    "Once again, you increase the speed of your thrusts."
    "[Tracy] is already at her limit. Even though she is surprised that you were able to go faster, she has been moaning with all she has."
    "The added pleasure that can't be released builds up, making her feel like she is about to explode."
    "She is not sure what happened, but her body all of a sudden feels like it's no longer under her control."
    "[Tracy] is having her first orgasm."
    "You try to hold out so she can ride it for a while, but as you already mentioned… There is no way you can last long."
    "At the last moment, you pull out your cock."
    # 61 cum
    show d9_tracy_sex_61 with flash
    hide d9_tracy_sex_59_03
    "Still holding on to [Tracy], you finish yourself off."
    show d9_tracy_sex_62 with dissolve
    "The cum is dripping down her leg."
    stop music fadeout 7

    pause
    show d9_tracy_sex_63 with dissolve
    "[Tracy] is trying to regulate her breathing."
    show d9_tracy_sex_64 with dissolve
    "You sabotage her efforts by going in for another kiss."
    "She happily accepts."
    pause(1)
    "You smile."
    mc "I think I changed my mind. I'm also going to take a shower."
    show d9_tracy_sex_65 with dissolve
    "[Tracy] smiles from ear to ear."
    tr "I don't mind."
    mc "(Such a cheeky remark… Does that mean it only took this much for her to warm up to me? Ha. You should have told me sooner.)"
    # MC standing under the shower. Focus on Tracy in the background
    scene d9_tracy_sex_66 with fadehold
    tr "I should keep what we did a secret, right?"
    "You smile."
    mc "(Fuck…)"
    mc "(Why am I still so happy?)"
    mc "Yeah, that would probably be for the best…"
    tr "I understand."
    show d9_tracy_sex_67 with dissolve
    mc "But I'm not going to keep it from [Fiona]."
    show d9_tracy_sex_68 with dissolve
    mc "Even after what we did just now, I want her to stay. She probably won't, but I'm still going to tell her. I owe her this much."
    show d9_tracy_sex_69 with dissolve
    tr "Are you not going to pursue her if she decides to walk away?"
    mc "I'd hope so. Honestly… I might be too selfish to let her go."
    show d9_tracy_sex_70 with dissolve
    mc "I like myself more when I'm with [Fiona]. She reminds me to be a better person. But it also feels like I'm putting on a mask. Do you understand?"
    "[Tracy] shakes her head slowly."
    tr "I'm sorry."
    mc "No problem. Give it time. You'll be able to see it."
    show d9_tracy_sex_71 with dissolve
    mc "But let me ask you. What do you want? Have you thought about that yet?"
    "[Tracy] nods."
    mc "What conclusion did you reach?"
    tr "I... I think I want to spend my life with you."
    mc "(Such a straightforward and simple answer.)"
    mc "Anything else?"
    show d9_tracy_sex_72 with dissolve
    tr "Isn't that already a lot?"
    mc "Let me ask differently."
    mc "[Fiona]. Do you want me to break up with her?"
    pause(1)
    hide d9_tracy_sex_72 with dissolve
    tr "You don't have to do that."
    mc "Are you sure?"
    tr "I told you. I don't understand your people."
    pause(1)
    tr "Is that weird?"
    mc "It is. But I like it. It's just too good to be true. I could hear it a hundred times and I still won't believe that you mean it."
    mc "Well having one woman who's willing to share her boyfriend isn't all that special. If you have two, that's when the fun begins."
    show d9_tracy_sex_73 with dissolve
    tr "[Sue] and maybe [Fiona]?"
    mc "Who knows?"
    mc "I'm going to tell you tomorrow."
    mc "Deal?"
    hide d9_tracy_sex_73 with dissolve
    "[Tracy] nods."
    mc "I guess we should go back to the house. They are waiting for us with lunch."
    show d9_tracy_sex_74 with vpunch
    tr "Ah! Of course!"
    "[Tracy] hurriedly puts on her clothes."
    $ renpy.end_replay()


label galleryscene8:
    mc "Let's have sex. You're okay with it, right?"
    show d9_training_66 with dissolve
    "[Sue]'s jaw drops."
    hide d9_training_66 with dissolve
    "Then her eyes begin to sparkle."
    su "Yes of course I'm okay with it!"
    mc "Come here."


    scene d9_sue_sex_01 with fadehold
    pause
    mc "I've already noticed that you're not wearing a bra."
    su "[MC]?"
    "[Sue] is holding back moans."
    show d9_sue_sex_02 with dissolve
    "You're only caressing her nipples, but it must already feel fairly intense."
    mc "What is it?"
    show d9_sue_sex_03 with dissolve
    su "N-No… It's alright."
    mc "Are you sure?"
    "[Sue] nods."
    mc "Sorry. You looked like you needed a pinch before you could believe that this wasn't a dream."
    su "That's alright. Thank you."
    show d9_sue_sex_04 with dissolve
    "In return [Sue] reaches for your penis."
    mc "So impatient."
    su "Do you want me to be more resolved?"
    "You sigh."
    mc "(That's no fun.)"
    mc "Come here."
    show d9_sue_sex_05 with dissolve
    "[Sue] stands up on her toes, but you still have to lean forward to reach her ear."
    mc "Just be yourself."
    show d9_sue_sex_06 with dissolve
    su "Can I really?"
    mc "Show me what I'm getting myself into."
    "[Sue] bites her lip."
    stop music fadeout 2
    show d9_sue_sex_07 with dissolve
    su "I think those clothes are a bit impractical. You need to take them off to use your penis."
    play music "audio/music/Erotic/Sexy Vibes (Short Loop).wav" fadein 5
    "She drops to her knees, and as she does, she strips you out of both your shorts and boxers."
    "You help her and kick them to the side."
    show d9_sue_sex_08 with dissolve
    pause
    show d9_sue_sex_09 with dissolve
    "A quick kiss on your cock."
    hide d9_sue_sex_09 with dissolve
    "It's like the breeze before a storm."
    show d9_sue_sex_10 with dissolve
    "[Sue] is gently tickling your balls as she enjoys the view of your growing member in front of her eyes."
    show d9_sue_sex_11 with dissolve
    "And a well-timed pause."
    show d9_sue_sex_12 with dissolve
    "The fact that she didn't go in right away makes this moment strangely arousing."
    show d9_sue_sex_13 with dissolve
    "There it is."
    "[Sue] eagerly takes your cock into her mouth."
    "You're curious about what's to come."
    # hottube
    show d6_hottub_20 with dissolve
    mc "(Back in the hot tub, [Sue] used some very pleasurable techniques to get me off. The question is if she can do the same without-)"
    # 15
    show d9_sue_sex_15 with Dissolve(1)
    mc "Ah, wow…"
    "Yes, yes she can."
    "Her mouth feels warm and soft."
    "The surprising part is the way she makes you squirm involuntarily. Her tongue is producing sensations you haven't felt before. Her pace is quick, her technique magnificent."
    "Well, magnificent might be the wrong word."
    show d9_sue_sex_16 with dissolve
    "It's a very sloppy blowjob."
    "Apparently, [Sue] doesn't mind getting her clothes dirty."
    "You understand how this might not be the most prominent thing on her mind right now."
    "You're barely able to think about it yourself, and all you have to do is stand there and enjoy it."
    show d9_sue_sex_17 with dissolve
    "[Sue] shows you a mischievous smile. She is looking straight at you, her mouth open, the tip of your dick resting on her tongue."
    mc "(Fucking hell, don't scare me like this. You're up to no good, aren't you?)"
    show d9_sue_sex_18 with dissolve
    "She takes a moment where she doesn't work on your dick directly. Instead, she is licking both her palms."
    "(Why are you…)"
    "The answer comes sooner than expected."
    # 19 animation
    show d9_sue_sex_19_01 with dissolve
    mc "(Oh boy… Where the fuck did she pick up this technique?)"
    mc "([Amber]... I'm-)"
    show d9_sue_sex_19_02 with dissolve
    hide d9_sue_sex_19_01
    mc "(Fuck! I'm afraid we'll need to talk.)"


    mc "(That feels so good.)"
    mc"(I'm not sure how long I can hold myself back.)"
    menu:
        "Do I want to cum like this, or do I actually want to fuck her too?"
        "Enjoy [Sue]'s blowjob" (sex = True):
            mc "Mmmm…"
            pause
            show d9_sue_sex_19_03 with dissolve
            hide d9_sue_sex_19_02
            pause
            show d9_sue_sex_19_02 with dissolve
            hide d9_sue_sex_19_03
            pause
            show d9_sue_sex_19_03 with dissolve
            hide d9_sue_sex_19_02
            # if not sex with Tracy
            mc "Slow down. I'm going to cum."
            "[Sue] giggles. She has no intention of stopping."
            mc "I'm going to cum…"
            show d9_sue_sex_32 with flash
            "Like the good girl she promised to be, [Sue] keeps on presenting her tongue."
            "Your big load shoots all over her face."

            show d9_sue_sex_33 with dissolve
            "It's been a while since you've given a proper facial, and [Sue] is there for it."
            "You're not sure if you've ever seen someone so proud."
            "Well, at least you're certain that you haven't seen someone that can give you such a proud smile while cum is dripping down their face."
            su "How was it?"
            "You laugh."
            mc "(Is she expecting a grade? To be honest, it's hard to put into words.)"
            mc "Have you been practicing?"
            "[Sue] nods proudly."
            mc "With whom?"
            show d9_sue_sex_34 with dissolve
            "She looks away shyly."
            "There is a man standing next to you, made purely of water."
            show d9_sue_sex_35 with dissolve
            mc "Why does he have tits?"
            su "I thought you wouldn't want to see a man right now."
            mc "I don't mind. Show me."
            show d9_sue_sex_36 with dissolve
            "The female-like figure with a dick is turning into a well built figure..."
            mc "Is that me?"
            "She nods."
            hide d9_sue_sex_34
            show d9_sue_sex_34 with dissolve
            "[Sue] is still looking away. That way it is easier to admit to what she does when she has free time around the house."
            mc "That's one way to use your ability."
            su "But I only used it to practice sucking dick. That's all."
            mc "Huh?"
            show d9_sue_sex_37 with dissolve
            "You come down to the floor where [Sue] is still kneeling. You scoop up some of your cum and push it into her mouth."
            mc "Are you trying to say that I'm the only one who is allowed to fuck you?"
            su "Mmmm…"
            "It's hard for [Sue] to speak with your thumb still inside her mouth."
            "She nods, confirming your suspicion."
            "[Sue] thought you might get jealous of your water self if she would use it to fuck herself."
            "People like to say that self-love is important, but you doubt that anybody was thinking about this kind of situation when they said it."
            "You take out your thumb. [Sue] has been playing with it using her tongue."
            su "I wouldn't feel it anyway."
            mc "Why is that?"
            su "Doesn't really matter."
            mc "Tell me. I want to know."
            su "It's a side effect of my curse. I don't actually feel pleasure unless I'm being touched by a man."
            mc "And have you been touched by a man before?"
            "[Sue] smiles remembering all your prior encounters."
            su "I've touched you a couple of times."
            mc "And the old man?"
            su "Not really. Back at his castle, he didn't care much about me. I wasn't an important person."
            mc "So, this was the first time..."
            su "It felt awesome, thank you."
            $ renpy.end_replay()

        "Transition into doggy style" (sex = True):
            mc "I think I understand… You're quite good at this."
            show d9_sue_sex_20 with dissolve
            hide d9_sue_sex_19_02
            "[Sue] gives you a proud smile."
            mc "It's only fair if I give you a reward, then."
            mc "Why don't you take off your clothes?"
            show d9_sue_sex_21 with dissolve
            "There is a moment of hesitation, but in the end, [Sue] gladly follows your request."
            show d9_sue_sex_22 with dissolve
            "You come down onto the floor."
            "[Sue] has created a matt of water that is more comfortable than kneeling on the hard floor."
            "She is such a smart girl."
            # Image of you kneeling in front of an excited Sue
            mc "Turn around. I want to take you from behind."
            # Sue presenting her ass
            show d9_sue_sex_23 with dissolve
            mc "I've already heard about it. There are arguments for going natural, but I don't mind either way."
            mc "I hope your bare pussy keeps reminding you of me."
            show d9_sue_sex_24 with dissolve
            "You let your hand glide between her legs."
            mc "I also heard that it feels excitingly different when wearing panties."
            "You tap on her pussy, sending shivers through her body."
            "The reaction from [Sue] suggests that it is working."
            show d9_sue_sex_25 with dissolve
            "She pushes her body back against your hand."
            mc "So impatient…"
            mc "I'll give you what you want. Don't worry."
            # 26 animation
            show d9_sue_sex_26 with dissolve
            "After pushing your dick into her inviting pussy, you start fucking her at a fast pace."
            "You're both excited. The moment you realized that [Sue] was dripping wet, you decided to go all out."
            "Moans echo through the pool area."
            mc "(She's so loud.)"
            show d9_sue_sex_27 with dissolve
            hide d9_sue_sex_26
            "Hoping to keep this from the others in the house, you use your ability to create a room that muffles [Sue]'s screams."
            "It's also a good way to keep you from blowing your load prematurely."
            # 28 animation
            show d9_sue_sex_28_01 with dissolve
            "As your mind comes back to focusing on [Sue], you're surprised to find her pussy clenching around your cock."
            mc "(She is cumming already…)"
            mc "(I thought she'd be more vocal about it.)"
            su "Mmmhh! Ah! Ahh…. Fuck! Mmmm…"
            # 28 slow
            show d9_sue_sex_28_00 with dissolve
            hide d9_sue_sex_28_01
            "You slow down your thrusts to let her calm down a little."
            mc "(Well… Don't think that just because you already came, I'm going to stop.)"
            mc "Scream for me, baby."
            # 28 fast
            show d9_sue_sex_28_02 with dissolve
            hide d9_sue_sex_28_01
            su "Mmmmhhh…"
            mc "(If I interpret this correctly, that's a {i}make me scream. I'm here for it{/i} sound.)"
            su "Ah!"
            # 28 hard and fast
            show d9_sue_sex_28_03 with dissolve
            hide d9_sue_sex_28_02
            "You grab a hold of her ass while starting to fuck her both hard and fast."
            "It's time for you to cum too."
            "By now, [Sue] has noticed your water walls."
            # 29 animation
            show d9_sue_sex_29 with dissolve
            hide d9_sue_sex_28_03
            "She bites her fingers, hoping that will keep her quiet, but it doesn't really help."
            "Her moans are different, but they are still just as loud as before."
            show d9_sue_sex_28_03 with dissolve
            hide d9_sue_sex_29
            pause
            "You reach the edge…"
            show d9_sue_sex_30 with dissolve
            "In the last moment, you pull out your dick and finish yourself off on her back."
            mc "(It's been a while since I had such a perfect backshot.)"
            show d9_sue_sex_31 with dissolve
            "As you let go of her ass, [Sue] drops to the ground."
            su "Thank you, [MC]."
            mc "You're welcome."
            $ renpy.end_replay()


label galleryscene9:
    scene d10_threesome_30 with dissolve
    "[Sue] quickly climbs over your legs and removes [Tracy]'s shirt. She wants to make sure [Tracy] doesn’t have time to change her mind."
    "Her concerns were misplaced. The only reason [Tracy] hesitated is because [MC] chose her over [Sue]. It gave her butterflies."

    show d10_threesome_31 with dissolve
    tr "Your pants."
    su "I got it."

    show d10_threesome_32 with dissolve
    "You're about to stand up when [Sue] clarifies that you don't have to bother. The two of them intend to keep their word. You won't have to do anything. All you have to do is enjoy yourself."

    show d10_threesome_33 with dissolve
    tr "He's not hard yet."
    "[Sue] is taking off her clothes too."
    su "Don't worry. Give him some time."

    show d10_threesome_34 with dissolve
    tr "I know…"

    show d10_threesome_35 with dissolve
    "[Tracy] comes close enough to feel her breath when she speaks. She doesn't want [Sue] to hear her."
    tr "[MC]?"
    "You feel her warm lips touching your dick."
    tr "Am I not pretty enough for you?"
    "Blood is rushing towards your second head."
    mc "I told you this morning."

    show d10_threesome_36 with dissolve
    "[Tracy] goes in for a kiss."
    pause(1)

    show d10_threesome_37 with dissolve
    tr "I guess you still like me."
    mc "Do you want to hear it again? Just to be sure?"

    show d10_threesome_38 with dissolve

    mc "Don't close your eyes. I want you to look at me while you are riding my cock."
    tr "Are you ready, then?"
    mc "[Sue]..."

    show d10_threesome_39 with dissolve
    "She lifts your cock so [Tracy] can sit on it."


    show d10_threesome_40 with fade
    "It begins slowly and sensually. [Tracy] is trying to get used to this position. Yesterday, you were in control. It's the first time she is going to set the pace."
    "[Sue] bites her lip. She wants to tell [Tracy] to speed up because she promised to make it quick."
    "Then again she knows you would say something if you were displeased with the situation."

    show d10_threesome_41 with dissolve
    hide d10_threesome_40
    "Instead of criticizing [Tracy] she takes your hand and places it on her thigh."
    "She tried to remind you that it's okay to touch."
    "With your left hand caressing [Sue]'s thigh you still have to find something to do with your right. The natural thing to do is to caress [Tracy] as she is riding your cock."

    show d10_threesome_42_02 with dissolve
    hide d10_threesome_41
    "And that's what you do."
    "She is rather soft."

    show d10_threesome_42_01 with dissolve
    hide d10_threesome_42_02
    "[Tracy] bites her lip and increases her speed."
    "Earlier during training she moved a lot faster, though."
    "There is still room. But judging from her expression you don't have to worry about [Tracy] going superhuman crazy on your cock anytime soon. This speed seems to be plenty."
    "Instead, you worry that once she voices her opinion, she won't be satisfied with just one or two rounds."

    show d10_threesome_44 with dissolve
    hide d10_threesome_42_01
    "You imagine laying in bed after a long night. The morning sun is falling through the window. [Tracy] is lying next to you."
    "Your eyes meet, and it's undeniable that she is asking to go again."

    show d10_threesome_42_01 with dissolve
    hide d10_threesome_44
    "The mental image almost makes you cum right away."
    tr "Ah…"
    mc "(Is she holding back because [Sue] is there?)"
    mc "I want to hear you."
    tr "Ah! [MC]!"
    mc "That's better. You don't have to hide anything."
    tr "Y-Yes… Ahhhh."

    show d10_threesome_43 with dissolve
    hide d10_threesome_42_01
    "The hall where only blunt grunts could be heard recently is now filled with moans. Mainly from [Tracy] but also some soft ones from [Sue]."
    "All you have to do is lean back and enjoy yourself."


    show d10_threesome_45 with fade
    hide d10_threesome_43
    "[Sue] gently turns your head her way."
    su "Are you enjoying yourself?"
    mc "What do you think?"

    show d10_threesome_48 with dissolve
    su "I'm greedy. I think you should have chosen to fuck me."
    mc "Ah… Sorry about that."
    su "It's okay."
    mc "Next time."

    hide d10_threesome_48 with dissolve
    su "Since you can talk I might need to tell [Tracy] to go faster."
    mc "Let her have her fun. She is doing a good job. It's just not that easy to make me stutter."
    su "Is that a challenge?"
    "You smile."
    mc "As I said. Next time."

    show d10_threesome_46 with dissolve
    "[Sue] goes in for a kiss."

    show d10_threesome_47 with dissolve
    "You take your hand from her leg and pinch one of her nipples."
    su "Ah!"
    mc "How about you stay closer and we check if I'm good at multitasking."
    su "Did you forget what we agreed on? Just relax. I'm sure [Tracy] will be proud if she manages to make you cum quickly."
    mc "I'm getting there."
    su "Are you close?"
    "You nod."
    su "Then please show [Tracy] how much you are enjoying her pussy."

    scene d10_threesome_43 with dissolve
    "[Sue] goes back to watching from the side. You can't even reach her thigh anymore."
    "[Tracy] is patiently waiting for your focus to return to her, all while still keeping busy with your dick."
    pause(1)
    mc "You're so beautiful."
    tr "Th… Thank you. Ah! Y-You… you're also…"

    show d10_threesome_36 with dissolve
    hide d10_threesome_43
    "Before [Tracy] can return the compliment, you go in for another kiss."
    "You didn't want to hear her say that you're also beautiful. It's like saying I love you too. It feels forced."
    show d10_threesome_42_01 with dissolve
    "Once you allow [Tracy] to catch her breath she seems to have forgotten what she wanted to say."
    mc "Are you having fun?"
    "Tracy nods while licking her lips."
    mc "Good."
    tr "W-what about you?"
    mc "Am I having fun?"
    pause(1)
    mc "I'm about to cum [Tracy]. Is that enough of an answer?"
    tr "You're… Is there something I should do?"

    show d10_threesome_49 with dissolve
    hide d10_threesome_42_01
    "There isn't enough time to explain. You grab [Tracy]'s ass and lift her off your cock."

    show d10_threesome_50 with flash
    "Once you're no longer inside of her, you finish yourself off grinding at the outside of her pussy."
    mc "Thank you [Tracy]... This was great."





    #$ choices.append("d10_threesome_sue") check if they have any use ripsonGR
    scene d10_threesome_51 with fade
    "[Sue] quickly takes off her shirt. It's like she's trying to ensure you can't suddenly change your mind."
    "She calls out to [Tracy] and gestures towards your crotch."
    "[Tracy] helps to relieve you of your pants while [Sue] finishes undressing."

    show d10_threesome_52 with dissolve
    "Before [Tracy] can point out that you're not hard yet, [Sue] already went ahead and began doing something about it."


    show d10_threesome_53 with dissolve
    su "Mm…"

    show d10_threesome_54 with dissolve
    mc "You're good at this."
    su "It's only going to get better."
    mc "I hope that's true."

    show d10_threesome_55 with dissolve
    su "[Tracy]?"
    tr "Hm?"
    su "Why don't you take off your clothes too? Don't be shy."
    tr "Yes."

    show d10_threesome_56 with dissolve
    "By now, your member has grown to full size."
    "[Sue] goes ahead and sits down on your cock."

    show d10_threesome_57_01 with fade
    su "Ahhhh…"
    "You're not sure if her moans are performative. But you also know that [Sue] is very sensitive so maybe she is enjoying herself that much."

    show d10_threesome_57_02 with dissolve
    hide d10_threesome_57_01
    "It doesn't take long for her to get used to being in control and to increase her speed."
    su "Mmmm.. Ah…. [MC], that's…"
    "[Tracy] obviously doesn't know what to do."
    mc "Come here."
    show screen in_animation with dissolve
    show d10_threesome_58_01 with dissolve
    hide d10_threesome_57_02
    pause(.5)
    show d10_threesome_58_02 with dissolve
    pause(.5)
    hide screen in_animation with dissolve




    "You grab her waist and pull her beside you."
    show d10_threesome_59 with dissolve

    mc "Talk to me. What's going inside that head of yours."
    tr "N-nothing."
    mc "Really? I think it's impossible to be in this situation and have no thoughts at all."
    mc "Look at [Sue]. Even she is thinking about something."

    show d10_threesome_60 with dissolve
    hide d10_threesome_59
    "[Sue] smirks at [Tracy]'s shy expression."
    mc "See."
    tr "I'm sorry…"
    mc "No problem."
    mc "I would like to hear your opinion more often."
    mc "It doesn't have to be now, though. Just something to keep in mind for the future. It might be a lot to ask in this kind of situation."
    "[Tracy] voices a sound of agreement."
    "[Sue] kept riding your cock at maximum speed during your short exchange with [Tracy]."

    show d10_threesome_61_01 with dissolve
    hide d10_threesome_60
    "Once your attention comes back to her, she noticeably slows down."
    su "Mmmhhh… [MC]... It's a shame that we don't have too much time."

    show d10_threesome_62 with dissolve
    "She goes in for a kiss while riding you sensually."
    su "Which do you prefer? Slow or fast? I'm fine with either."
    mc "Fast. But there is a time and a place for both."

    show d10_threesome_61_02 with dissolve
    hide d10_threesome_61_01
    "[Sue] goes back to what she did in the beginning."
    "She also prefers to go fast. She just hoped she could ride your dick a bit longer if she did it slowly and sensually."

    show d10_threesome_63 with dissolve
    hide d10_threesome_61_02
    "The room that has heard way too many manly grunts is finally filled with sweet moans."
    "[Sue] is excellent."
    "She only watched while you've been exhausting yourself with [Tracy]. Maybe she was even fantasizing about this exact situation."
    su "Ah… [MC]! Mmmhhh…"
    mc "I'm getting close."
    su "Please cum for me!"

    show d10_threesome_61_03 with dissolve
    hide d10_threesome_63
    "[Sue] goes all out for the ending."
    mc "I'm about to cum."
    su "Fill me with your cum, [MC]!"
    mc "(Huh?)"
    "You realize that [Sue] has no intention of pulling out."
    "Trying to salvage the situation, you grab her by the ass and pull her off your dick."
    "Not a moment too soon."

    show d10_threesome_64 with flash
    "Once you've pulled out, your dick begins shooting."
    mc "(Fuck! I'm awake.)"
    mc "(That's way better than coffee.)"
    "This short little scare woke you up from your tired state."
    mc "(I forget that [Sue] probably wouldn't mind getting pregnant.)"
    $ renpy.end_replay()


label galleryscene10:
    show d11_sue_12 with fade
    "The moment your alone, [Sue] slides her hands under your shirt."

    if "d4_sue_sex" in choices or "d9_sue_sex" in choices:
        mc "Greedy as always..."

    mc "It must have been hard laying still while [Sally] pretended you weren't there."
    su "I know when to hold back."
    mc "You're not holding back now, are you."
    su "No."

    show d11_sue_13 with dissolve
    mc "What do you want, [Sue]?"

    show d11_sue_14 with dissolve
    su "I want to please you, [MC]."
    mc "That's not what I meant."
    mc "You must have dirty thoughts. What's going through your head when you see me?"
    su "I think about you grabbing me."

    show d11_sue_15_01 with dissolve
    "You take her waist and pull her closer."
    mc "Like this?"

    show d11_sue_15_02 with dissolve
    su "Not quite..."
    mc "(Still a bit too tame, is it?)"
    mc "(How about this then?)"

    show d11_sue_16 with dissolve

    mc "Like this?"
    "[Sue] nods."
    mc "Go on. Do we kiss in your fantasy?"
    su "You can kiss me if you want."
    mc "(If I want? That's a no then. Come on, [Sue]. You know better than this.)"

    show d11_sue_17 with dissolve
    "You gently squeeze." with vpunch
    "[Sue] has some physical enhancement mixed into her ability. This little wouldn't hurt a normal person, and compared to them she is much stronger."
    "Then again, you've copied [Tracy]'s ability. If you gave it your all, she'd be in trouble."
    "You feel her gulp."
    mc "How did your fantasy continue? I think I didn't hear you."

    show d11_sue_18 with dissolve
    pause(1)
    su "You threw me on the bed."
    mc "Say it all."

    hide d11_sue_17
    hide d11_sue_18 with dissolve
    su "You ripped off my clothes and fucked me."
    mc "And ruined the clothes I bought?"
    "[Sue] tries to nod."
    mc "Well we can't do that, can we?"

    show d11_sue_17 with dissolve
    su "No."
    su "You held my neck and asked me to strip out of my trousers. You forced your other hand into my mouth making me gag. Then you used my spit to lube up your cock."
    mc "Such a dirty mind. You must like it rough."

    show d11_sue_19 with dissolve
    su "Yes."
    mc "The next time I might need to bring some rope."
    "[Sue] nods."
    "You smile."


    scene d11_sue_19 with fade
    mc "Then let's get to it."

    show d11_sue_20 with vpunch
    "You release [Sue]'s neck and push her away."

    show d11_sue_21 with dissolve

    pause
    mc "Strip."


    show d11_sue_22 with dissolve
    mc "Wait."

    show d11_sue_23 with dissolve
    pause
    mc "Slower."
    show d11_sue_24 with dissolve
    pause
    show d11_sue_25 with dissolve
    pause



    show d11_sue_26_02 with fade
    pause

    menu:
        "Be rough" if True:
            #$ choices.append("d11_sue_sex_rough")


            show d11_sue_27 with dissolve
            su "Ah!"
            "You push her onto the bed."

            show d11_sue_28 with vpunch
            "She looks a little frightened."
            "You can't tell if it's an act."


            show d11_sue_29 with dissolve
            "It doesn't matter."
            mc "Be a good girl and wait."
            "You finish undressing in front of her eyes."

            show d11_sue_30 with dissolve
            mc "There we go."
            "When you climb onto the bed, [Sue] instinctively moves away."

            show d11_sue_31 with dissolve
            mc "Where are you going?"
            su "It's..."
            su "I don't know."
            mc "Come here."

            show d11_sue_32 with dissolve
            "Once she's within reach, you grab her head and kiss her."
            "Her tongue gives her away. She is very much into this."
            mc "Check if you are wet."
            su "I am."
            mc "Check anyway."

            show d11_sue_33 with dissolve

            su "Here."
            mc "Good girl."
            mc "Now spread your legs so I can fuck your cunt."
            mc "I know you can't wait to feel my dick inside you."
            su "Yes, [MC]."



            show d11_sue_34 with dissolve
            mc "Who is a good girl?"
            su "Me."
            "With that you push your dick inside her."

            show d11_sue_35 with fade
            su "Ahhhhhh!"
            "Screw taking it easy. She is wet anyway, so you go fast right away."
            "[Sue] has a hard time holding back."


            show d11_sue_36 with Dissolve(1.5)
            "Her moans can be heard outside the room."
            am "Why don't we go downstairs?"
            mo "Yes!"


            hide d11_sue_36 with dissolve
            su "Mmmmhhh..."
            mc "You're too loud."
            "[Sue] is looking around. She can't find anything to muffle her moans."
            "Of course, she wouldn't bite into your pillow. It's yours after all."

            show d11_sue_37 with dissolve
            hide d11_sue_35

            mc "That won't do."

            show d11_sue_38 with dissolve
            "You pull out your dick."
            "[Sue] would like to protest, but right now you're the one who is fucking, and she is supposed to lay there and take it."

            show d11_sue_39 with dissolve
            mc "Open your mouth."

            show d11_sue_40 with dissolve

            mc "(So obidient.)"
            "You use her panties as a gag."

            show d11_sue_41 with dissolve

            mc "That's better."

            show d11_sue_35 with fade
            "You're back inside her."
            "[Sue] has a dirty mind. She must have thought of using panties as a gag."
            "She didn't expect it in the moment, though."
            "Her moans are muffled."
            mc "Such a beautiful little pussy."
            mc "The next time we spar, and I pin you down..."
            mc "Are you going to spread your legs then too?"

            show d11_sue_42 with dissolve
            hide d11_sue_35
            mc "Don't look away."
            mc "Show me your eyes."

            show d11_sue_43 with dissolve
            mc "I'm going to cum on your face."
            "[Sue] nods."
            mc "You can use your panties to whipe it away."
            mc "Of course, you can also eat it. I don't care."
            show d11_sue_35 with fade
            pause
            show black with dissolve
            pause(1)
            show d11_sue_44 with flash
            pause
        "Surprise her and be gentle" if True:
            #$ choices.append("d11_sue_sex_tame")


            show d11_sue_45 with fade
            "You kiss the back of her hand."
            mc "Let's not do this today."
            "[Sue] nods."

            mc "Do you also have a wholesome fantasy?"

            show d11_sue_46 with dissolve
            "[Sue] blushes."
            mc "(That's a no, then.)"
            mc "(Or maybe it's too wholesome.)"
            mc "I do."

            show d11_sue_47 with dissolve
            pause
            show d11_sue_48 with dissolve
            pause
            show d11_sue_49_02 with dissolve





            su "That's good too."
            mc "Is it?"
            pause(1)
            "You smile."
            mc "I think it is."



            hide d11_sue_48
            show d11_sue_48 with dissolve
            mc "Do you think you are ready, or do we need lube?"
            su "What do you mean?"


            show d11_sue_50 with dissolve
            mc "Are you wet?"
            su "Yes. You can fuck me."
            mc "I can sleep with you."
            su "That's what I said."
            mc "No."


            hide d11_sue_49_02
            show d11_sue_49_02 with dissolve
            mc "Let me show you the difference."
            su "Please do."
            mc "Never speechless."
            mc "I love that about you."



            show d11_sue_51 with dissolve
            mc "You're sensitive. We are going to use that."


            show d11_sue_52 with dissolve
            "[Sue] feels your dick gently resting on her pussy."
            "Greedy for stimulation, she moves her pelvis."
            "You give her what she wants and put it in."
            mc "Better?"
            su "Are you going to tease me?"
            mc "I told what we were going to do."
            mc "There is no rush in making love."
            "Even though you say that, you don't intent do let her wait for long."


            show d11_sue_35 with fade
            "You go in for a kiss, and as you do you begin to move."
            su "Mmmmhhh..."
            "This would have been a moan if it wasn't for the kiss."
            "Your gentle thrusts are doing the trick. [Sue] is slowly losing herself in the pleasure."
            "The same goes for you."
            "While your mind was still trying to explore all kinds of scenarios, you managed to tame it."


            show d11_sue_53 with Dissolve(2)

            "You focus on her lips. There are many things she can do with that mouth but all of them don't matter. Her delicate lips are soft to the touch."
            "A tongue that likes to explore. [Sue] understood the assingment and turned down the naughtiness. That doesn't mean your tongues don't touch every now and then."
            "Her breath tingles on your skin. She's reluctant to part from you, but both of you need air."


            "Her thighs are gently rubbing at your belly, while you keep thrusting."


            hide d11_sue_53 with Dissolve(1)
            "Every sensation can be explored."
            "Your mind is running circles, but you don't care at all."
            "Let it think about whether you can acutually feel the mountains and valleys of her vagina every you fully enter, and your crotch is pressing against hers."
            "Think about it twice. There is no answer. With [Tracy]'s ability it might be possible, but maybe you are just imagining it."

            su "[MC]..."
            mc "[Sue]."
            su "Thank you."


            show d11_sue_54 with dissolve
            "You could tell her that she is welcome. Instead you playfully lick her face."
            "[Sue] smiles."



            hide d11_sue_54 with dissolve

            mc "I'm about to cum."
            su "[MC]?"
            mc "What is it?"
            su "Please cum inside me."
            pause(1)
            mc "I can't do that."

            show d11_sue_55 with dissolve
            "[Sue] looks dejected."
            su "Okay."


            show d11_sue_56 with dissolve
            "You pull out and finish on her belly."


    #$ memory.append("d11_sue_sex")

    stop music fadeout 2
    $ renpy.end_replay()
