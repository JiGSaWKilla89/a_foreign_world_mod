init 1:
    style memory_vscrollbar is gui_vscrollbar:
        unscrollable "hide"

    screen memory():
        style_prefix "memory"
        zorder 150
        modal True

        add "images/screens/memory_01.png"

        text _("MEMORY"):
            ypos 60
            xalign .3
            font "gui/Fonts/Mova.ttf"
            size 100
            outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

        text _("PEOPLE"):
            pos (200, 200)
            font "gui/Fonts/Mova.ttf"
            size 80
            outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]



        viewport:
            xpos 850
            ypos 300
            xmaximum 800
            ymaximum 600
            mousewheel True
            scrollbars "vertical"
            has vbox:
                spacing 20


            if "d1_night_forrest_aurora" in memory:
                textbutton _("{b}The clothes they wore when they came here{/b}"):
                    xmaximum 700
                    text_size 40
                    action Show("memory_clothes")
                    text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "d1_drive" in memory:
                textbutton _("{b}Information I know about their world{/b}"):
                    xmaximum 700
                    text_size 40
                    action Show("memory_world")
                    text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]






        viewport:
            xpos 200
            ypos 300
            xmaximum 500
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox


            hbox:
                if "MC_heard" in memory or "clay_heard" in memory:
                    if "MC_seen" in memory:
                        add "images/screens/memory/MC_icon_01.png"
                    else:
                        add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[MC!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_mc")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "aurora_heard" in memory:
                hbox:
                    add "images/screens/memory/aurora_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Aurora!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_aurora")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "tracy_heard" in memory:
                hbox:
                    add "images/screens/memory/Tracy_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Tracy!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_tracy")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "sue_heard" in memory:
                hbox:
                    add "images/screens/memory/Sue_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Sue!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_sue")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "megan_heard" in memory:

                hbox:
                    if "megan_seen" in memory:
                        add "images/screens/memory/Megan_icon_02.png"
                    else:
                        add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Megan!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_megan")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "esther_heard" in memory:
                hbox:
                    if "esther_seen" in memory:
                        add "images/screens/memory/Esther_icon_01.png"
                    else:
                        add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Esther!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_esther")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "lucy_heard" in memory:
                hbox:
                    add "images/screens/memory/Lucy_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Lucy!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_lucy")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "sally_heard" in memory:
                hbox:
                    if "sally_seen" in memory:
                        add "images/screens/memory/Sally_icon_01.png"
                    else:
                        add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Sally!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_sally")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "amber_heard" in memory:
                hbox:
                    if "amber_seen" in memory:
                        add "images/screens/memory/Amber_icon_01.png"
                    else:
                        add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Amber!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_amber")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "monique_heard" in memory:
                hbox:
                    if "d2_monique_seen" in memory:
                        add "images/screens/memory/Monique_icon_02.png"
                    else:
                        add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Monique!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_monique")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "fiona_heard" in memory:
                hbox:
                    add "images/screens/memory/Fiona_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Fiona!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_fiona")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "fifa_heard" in memory:
                hbox:
                    add "images/screens/memory/Fifa_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Kent!u] [Lambert!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_fifa")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "emily_heard" in memory:
                hbox:
                    add "images/screens/memory/emily_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Emily!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_emily")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "cecilia_heard" in memory:
                hbox:
                    add "images/screens/memory/Cecilia_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Cecilia!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_cecilia")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "morris_heard" in memory:
                hbox:
                    add "images/screens/memory/Morris_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Morris!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_morris")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "clay_heard" in memory:
                hbox:
                    add "images/screens/memory/Clay_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Clay!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_clay")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "colby_heard" in memory:
                hbox:
                    add "images/screens/memory/Colby_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Colby!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_colby")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "nathaniel_heard" in memory:
                hbox:
                    add "images/screens/memory/Nathaniel_icon_01.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}[Nathaniel!u]{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_nathaniel")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            if "oldman_heard" in memory:
                hbox:
                    add "images/screens/memory/icon_locked.png"
                    textbutton _("{font=gui/Fonts/Mova.ttf}THE OLD MAN{/font}"):
                        ypos 30
                        xpos 20
                        text_size 40
                        action Show("memory_oldMan")
                        text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]






        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_mc():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"


        if "MC_seen_02" in memory or "emily_heard" in memory:
            add "images/screens/memory/MC_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)


        default MC_custom = VariableInputValue("MC", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[MC!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = MC_custom)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

                style_prefix "memory"

            if "clay_heard" in memory:
                text _("I've been working for the Department of Strategic Defense. Short, DSD. A government organization that differs from the rest. People usually know the Federal Bureau of Investigation, FBI, or the Central Intelligence Agency, CIA. In contrast to them, the DSD operates in the shadows. Few have heard about it, and fewer know that this so-called Department is merely a front to fund people like me who can make various problems disappear without causing a big scene.")

                text _("But I'm no longer doing this kind of work.")

            if "d3_cecilia" in memory:
                text _("I'm engaged to [Fiona], the vice president's daughter. Back when I was an agent, she has been kidnapped, and I helped save her.")

            if "d4_training_bed" in memory:
                text _("I told [Fiona] I wanted to have kids with her, and she agreed.")

            if "d8_fiona_marry" in memory:
                text _("After showing up drunk at my doorstep, telling me she still loves me, [Fiona] onsidedly decided that we are married now.")
                text _("She is the one that makes me believe that I can have a normal life. I'm reminded of who I want to be when I'm around her. The longer she was away, the closer I got to being the person I used to be. It's my past, so I can't leave it behind like it never happened. But I promised myself I wouldn't go back. Without [Fiona], this promise started to crumble.")
                text _("I think hearing that I might die made [Fiona] forget whatever caused her to leave in the first place. She wants me to act like her husband, but I'm unsure if she can shoulder what this entails.")
                text _("I do hope that she can, though.")


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_mc")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_aurora():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "aurora_seen_01" in memory:

            add "images/screens/memory/Aurora_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)


        default Aurora_custom = VariableInputValue("Aurora", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Aurora!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Aurora_custom)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_night_forrest_aurora" in memory:
                text _("Hot-tempered, but it seems like she yields to authority relatively well. It could also be that she respects a good argument. When [Tracy] told her to stop attacking the night we first met, she did. But she only stopped protesting after [Tracy] explained her reasoning."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_nathaniel_conversation" in memory:
                text _("[Nathaniel] came here to get [Aurora]. There is some connection between him and her. He said she was his. This could be anything from her being his slave to her being his sister."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_lunch" in memory:
                text _("[Aurora] is angry. Yes, she was aggressive and prone to violence from the beginning, but she contained it for the time being. Even when she got shot at, she knew not to fight back."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_bra" in memory:
                text _("She's strong. Not only do the other members of their group act like she is stronger than them, but [Aurora] also positioned herself to protect the group when they first met [Cecilia]."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_lucy_listen" in memory:
                text _("Misandry. It's the hatred and contempt of men. Who knows where I picked that word up, but it does describe [Aurora]'s state of mind. From what I heard, she feels that way because her father forced her into an arranged marriage with [Nathaniel]."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_dinner" in memory:
                text _("She locked herself into this false reality where everything was hopeless. I didn't think I could get through to her by being compassionate, so I called her out instead. This was a gamble that turned out surprisingly well. She apologized and helped me prepare dinner. Her mind is still in a lot of turmoil, but it was a good start."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_shopping" in memory:
                text _("The next day I made sure to have [Aurora] spend the afternoon with me. Repeated interactions might be the way to go. She is already warming up to me. Eventually, she should be willing to let me copy her ability."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d6_aurora_01" in memory and not "d6_aurora_02" in memory:
                text _("The future is now. [Aurora] offered me her ability. She is not quite there yet, but this is a big step in the right direction. I didn't think she would cave so fast."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d6_aurora_02" in memory:
                text _("She allowed me to copy it. Technically I now have her ability. The only problem is that I can't control it yet. But as far as I understand, it's only a matter of time until I can tame it. Things turned out well sooner than I expected."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d6_aurora_hottub" in memory:
                text _("[Aurora] joined me and [Sue] in the hot tub. I didn't see that coming, which might mean I should reevaluate my image of her. It must have been a test of sorts. I promised her not to pursue her sexually, and she tried to see if I'll keep my word. Either that, or there is something I'm wrong about. No, it was probably just a test. I should keep my eyes open since there might be more coming."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_training" in memory:
                text _("During training, she usually only talks about how to best utilize her ability. She is a good teacher. Apparently, the way to control her ability has a long tradition. She is teaching me techniques that feel like they've been perfected through generations. [Aurora] knows about her mother and grandmother, but I think a much longer tradition is standing behind them."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("She is observing me. Maybe she is slowly coming to grips with me not being her enemy. She has become rather quiet. She no longer wears her emotions on her sleeve, and I don't know what she is thinking. I do believe our relationship has become better, though."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "tracy_notes" in memory:
                text _("[Tracy] mentioned in her notes quite a few horrible things [Nathaniel] did to [Aurora]. He turned torturing her into a game. He wouldn't lay a finger on her unless she asked for it herself. She never did. When her mother discovered that [Aurora] had become a target of this psycho, she attempted to assassinate him. It didn't work. Instead, he called for [Aurora] and made her watch while he killed her mother."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("I know what humans are capable of, but reading those notes was hard. I had to stop a couple of times."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_aurora_trust" in memory:
                text _("She probably trusts me. I know it doesn't seem that way, but if she actually thought what she was saying, she would act differently. She sees herself as a protector of the other girls. That's why she checked in with me after hearing I would build a harem."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_training" in memory:
                text _("I should figure out what happened the night the old man died. [Sue] told me [Aurora] wasn't just a bystander, but she probably fought alongside [Nathaniel]. I doubt she had much choice, though."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25




            if "ability_info_unlocked" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("Her eyes catch fire when she feels threatened. This might be a giveaway for when she is about to use her ability."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d1_night_forrest_aurora" in memory:
                text _("She can create a large flame in a concise amount of time. That's what it looks like on the surface. But she didn't start a wildfire. When she attacked me in the forest, her flame didn't spread to the nearby trees. This could be possible if the flame only burned for a fraction of a second, but in that time, I wouldn't have been able to dodge away. It doesn't make sense. Is [Aurora] able to control the things her flames affect?"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d1_parking_bullet" in memory:
                text _("She was shot. No. But she should have been shot. Somehow she was able to stop that bullet before it hit her. If this officer had missed, my car would have been damaged, but it wasn't. It's like the bullet disappeared."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_sauna_01" in memory:
                text _("The bullet didn't disappear. I later found it lying in my car untouched. [Aurora] said that she doesn't technically create fire, but she only creates heat and light. This would also explain what happened to that bullet. She can manipulate energies, which means she simply took away the bullet's kinetic energy."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_discussion" in memory:
                text _("Apparently, she can cause as much destruction as a nuke. Hard to believe, but why should I start doubting her words at this point? We've left behind the realm in which things are still reasonable long ago."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_training" in memory:
                text _("I can feel the power hidden in her ability. It's hard to say if it can rival that of a nuke, but it's also not impossible."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25






        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_aurora")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_amber():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "amber_seen" in memory:
            add "images/screens/memory/Amber_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)

        default Amber_custom = VariableInputValue("Amber", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Amber!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Amber_custom)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            text _("[Tracy] referred to her as someone more knowledgeable than herself regarding their world. It seems like she helped them travel to my universe."):
                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                xpos 10
                xmaximum 1100
                size 25

            if "d2_amber_con_01" in memory:
                text _("She is smart. But because of that, I'm not sure if she is genuine."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("A bubbly woman that loves to talk about ideas. I asked her if she was a scientist, and she said yes. I asked her if her ability means she is always right, and [Sue] rolled her eyes. That's probably a no, then."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("She thinks [Nathaniel] saw something in me. Otherwise, he wouldn't have left me alive."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_amber_con_02" in memory:
                text _("When she examined me to find out if [Nathaniel] transferred an ability to me, she was worried. I asked her about it, but she made up some harmless reasons to hide her true feelings."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_amber_internet" in memory:
                text _("I introduced her to the internet, and she took it relatively well. She has been clicking through pages like mad, but I have no doubt she understood most of the information she saw there."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_amber_sue" in memory:
                text _("She is trying to fix the problems she sees around her. First, she wants to do things around the house, and then she tries to help out [Sue]. It might still be a coincidence, but maybe that's the kind of person she is. If she's not studying, then she needs to solve something."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d6_amber_curse" in memory:
                text _("Back in her world, she has studied a variety of topics. One of them is curses. In the conversation she mentioned this part of her past, another thing became clear to me. I now understand why [Sue] rolled her eyes when I asked if [Amber] is always right. Because of her ability, [Amber] can connect dots at an unbelievable rate. It's impressive. Still, this doesn't mean she is infallible. If she was, she would have predicted my problem with [Sue]'s curse and corrected the misconception before it could become a problem. Yes, I expected a lot here, but I rather think too big than too small. In the end, [Amber] is still human. That's what I realized."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_amber_01" in memory:
                text _("I told her about my theory that [Aurora]'s ability might work on the exact mechanism as nuclear bombs. I thought she could freely turn matter into energy. The idea was stupid, but [Amber] didn't immediately dismiss it. Instead, I think she pretended to think about it for a day and then broke the news that almost all of their abilities rely on energy being created out of nowhere and that [Aurora] wasn't special in that regard. She was being considerate of me. Maybe she even thought there was an angle that I saw that she was missing and wanted to confirm it."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "tracy_notes" in memory:
                text _("The man [Amber] was promised to was a racist. That's what [Tracy]'s notes say. This guy seems like a disgusting human being with a boring life and too much time on his hands. Not only does he drink too much and becomes abusive, but he also believes black people are inferior. He refused to touch [Amber]. I'm not sure if she took it as a blessing. At least she didn't need to escape his lust like [Megan] and [Monique]. But being viewed as disgusting must have been traumatizing, too."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("I was careless, letting her access the internet without supervision. It's too late. By now, she must have read about the history of slavery, the civil rights movement, and Nazi Germany."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_amber_talkDate" in memory:
                text _("Pain seems to be her kryptonite. I can't say that I expected this turn of events. It makes sense. [Amber] never suggested I should copy her ability, even though she seems like the type to offer if it was the rational thing to do. The others were hesitant, so she could have stepped up and said that pain isn't the end of the world. Maybe she even wanted to do that but knew she couldn't back up her words."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_amber_date" in memory:
                text _("[Amber] was the first one to give me a condition before I could copy her ability. She wanted me to take her out on a date so she could experience it at least once before she died. I thought she might be like [Sue] or [Tracy], and she has fallen for me, but just because it happened twice doesn't mean I've become an irresistible chick magnet. I should keep my ego in check and not get ahead of myself."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25



            if "d2_amber_ability" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("Quick thinking. She can process information at a faster rate than normal human beings."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_amber")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_sue():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "d1_sue_seen" in memory:
            add "images/screens/memory/Sue_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)

        default Sue_custom = VariableInputValue("Sue", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Sue!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Sue_custom)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_night_forrest_aurora" in memory:
                text _("When we first met in the forest, she flirted with me. This might be a defense mechanism that helps her find someone who can protect her. That is if she isn't consciously aware that she did it. Seduction is a powerful weapon. If you're not the biggest fish, you might be able to seduce him and earn his favor."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d1_night_hospital" in memory:
                text _("But soon after, she also flirted with the nurse. It's unlikely that she did so because she seeks security. This reminds me of evolutionary mismatch. A behavior that manifests in certain situations because it's beneficial can also leak into similar situations where it doesn't matter or is counterproductive."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("The doctor provoked a different reaction. [Sue] seemed uncomfortable around him. Her eyes looked for help. It makes it likely that she instinctively flirts with good-looking people whom she doesn't perceive as a threat."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_healing_sue" in memory:
                text _("The wound [Sue] received when she first came here has been healed by [Sally]. It's like [Sue] hasn't been hurt in the first place."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            else:
                if "d1_parking_leave" in memory and not "d2_healing_sue" in memory:
                    text _("We had to leave before someone from the hospital could sew up her wound. We might need to return, even though the injury didn't look that bad. Maybe the hospital wanted to sew it up since it makes them more money?"):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25



            if "d2_pool" in memory:
                text _("On the second day, I had some time for myself and decided to relax downstairs in the pool. At this point, [Sue] tried to seduce me. She said she wasn't tasked to do so by the group. Judging from the fact that she has had a flirty tone since the first time we met, I'm inclined to believe her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_shower" in memory:
                text _("This is getting ridiculous. {i}Can you teach me how to use a shower?{/i} I've never had a woman be so persistent in trying to sleep with me. I know it's partly because she's from an earth where circumstances might permit this type of thing to be a winning strategy. Then again, it might be something else. I know very little about [Sue] because she tried to get into my pants in every interaction I had with her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_massage" in memory:
                text _("After [Sally] fixed me up, she came to give me a massage. Of course, it was a good excuse, but I think she also did so out of genuine concern."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_morning_sue" in memory:
                text _("And then, the next day, she apologized for her behavior and asked what she could do better. She is trying her best, and it seems cruel to keep rejecting her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_sue_sex" in memory:
                text _("Looks like I'm no longer rejecting her. We had sex."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_sue_sex" in memory:
                text _("Twice."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_sue_coma" in memory:
                if "d6_sue_awake" in memory:
                    text _("She volunteered to have her ability copied and paid the price for it. She was in a coma."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25
                else:
                    text _("She volunteered to have her ability copied and paid the price for it. She is in a coma."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "d7_sue_shaving" in memory:
                text _("[Cecilia] told me that [Sue] insisted on shaving her private area. How much do you want to bet she had this idea from [Amber]? Apparently, [Cecilia] couldn't refuse and gave in to her demands. It seems like [Sue]'s agreeable side only shines when she is with me."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d8_fiona_marry" in memory:
                text _("Now that [Fiona] has come back, things have become complicated."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "tracy_notes" in memory:
                text _("Tracy mentioned in her notes that [Sue] has been intimate with both [Sally] and [Amber]."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d9_sue_sex" in memory:

                if "d5_sue_sex" in memory:
                    text _("Third time is a charm."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                text _("I slept with [Sue]. And this time I really did it... Not even I can find an excuse for it. I slept with her before I talked to [Fiona]. Seems like I'm determined to burn this bridge down. Only being with [Fiona] is off the table. There is no way this is going to work."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
            else:
                if "d9_sue_handjob" in memory:
                    text _("I caved after [Sue] mentioned that I should try having multiple women. Who knows, maybe I'll like it. It's not a solid argument, and I'd hate it if she believed she convinced me with that. But it seems like I'm determined to burn down my bridge with [Fiona]. Only being with her is off the table. Everything considered, there is no way this is going to work."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "d10_sue_breaking_down" in memory:
                text _("[Sue] has a hard time figuring out how to act. When I told her [Fiona] is okay with an open relationship, she should have been happy, but her reaction almost seemed like she had given up hope. She managed to bounce back to her usual self, but this moment confirms once again that a lot is going on in her head."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_sue_haremQueen" in memory:
                text _("[Sue] dragged [Tracy] into one of her schemes. This is a no-go. She can't just pressure others into having sexual stuff. I need to talk to her about this."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


            if "d4_sue_ability" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                if not "curse_heard_02" in memory:
                    text _("[Sue] only unlocks her full power when she gives herself to a man."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if not "curse_heard_02" in memory:
                if "d4_sex" in memory:
                    text _("She only gets aroused by the touch of a man."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "d4_sue_pool_sex" in memory or "d5_training_sueAbility" in memory:
                text _("She controls water."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "curse_heard_01" in memory:
                text _("{size=35}{b}Curse:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                if not "curse_heard_02" in memory:
                    text _("Her increased libido is part of her curse, which can be inherited, but won't be given when copying her ability."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25
                else:
                    text _("[Sue]'s curse isn't as straightforward as [Tracy]'s or [Megan]'s. It covers multiple things."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25
                    text _("The curse was created to prevent your lover from ever leaving you. This curse makes it so that when [Sue] finally falls in love, she will never fall out of love."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25
                    text _("In addition, this curse increases her libido, locks parts of her ability, and makes her numb to women's touch. I'm not exactly sure why those were added. They somewhat make sense, but it's not like they will add much to making sure your lover will never want to leave you. The first part of this curse would be more than enough."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25




        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_sue")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_tracy():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Tracy_01.png" pos (70, 50)

        default Tracy_name = VariableInputValue("Tracy", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Tracy!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Tracy_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_night_forrest_aurora" in memory:
                text _("She was able to tell [Aurora] what to do. In the end, it was her that had the final say in how the group should act."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d1_drive" in memory:
                text _("She was the person who spoke to me the most. Maybe she is considered particularly articulate. Someone that can hold her own in essential conversations with strangers."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("On the drive to the hospital, she sat next to me in the front. She acted as a buffer between the rest of the girls and me. You would instinctively try to put a physical distance between someone dangerous and someone you want to protect. She might very well be the leader of their group."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d1_night_offer_tracy" in memory:
                text _("She offered herself to me. I said no. Why did she back out so quickly if she tried to seduce me? Since she is from a different world, this might be a cultural difference. A formal offer that is supposed to be rejected?"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_morning" in memory:
                text _("[Esther] confirmed it. [Tracy] is the leader of their group. She knows what she has to do, but it seems like she doesn't have the temperament for the job."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_drive_tracy" in memory:
                text _("On occasion, she lets her guard down around me, like the second day in the car when we drove to get [Sally], [Amber], and [Monique]."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_discussion_02" in memory:
                text _("She tries to be a good leader capable of making harsh decisions, but she lacks the temperament for that. Still, when we had our strategy meeting, she pushed back against me. Either I'm wrong, and she is more disagreeable than I thought, or she was purposefully trying to act tough No matter what. She won't like it, but she might actually have what it takes to be a leader."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_evening_01" in memory:
                text _("One thing she still needs to learn is to voice her opinion more often. There were multiple instances when she had a different view than me, and a simple glance made her concede. This works about as long as her opinion isn't the right one. Which it wasn't in those cases but in others, it might be. If she doesn't speak up, I might need to actively go and ask for her input."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_tracy_01" in memory:
                text _("She offered to have sex with me. Again. This time around, it was a little different, though. She should know that this kind of action isn't necessary to secure my help. Maybe it's not as clear as I think it is. That, or there is different motivation for her latest actions."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_tracy_02" in memory:
                text _("She offered to have sex with me. Again. This time around, it was a little different, though. She wanted to do it. Yes, there are parts of her that were still reluctant. She was nervous and couldn't relax. But whenever I offered her a way out, she wanted me to keep going. When I pushed a boundary, she didn't put up any resistance. Still, it wasn't the right time to go all the way. She might have been okay with it, but it certainly wouldn't have been a pleasant experience for her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                if "d8_fiona_marry" in memory:
                    text _("Now that [Fiona] has come back, things have become complicated."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "tracy_notes" in memory:
                text _("[Tracy] decided to write me a couple of notes summarizing their lives before they came here and any interesting information I should know about. She could have told me, but I must admit that reading this information was much more manageable. She could talk openly without any embarrassment, anger, or sadness getting in the way. Especially what happened to [Aurora] would have been hard to talk about face to face."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d9_tracy_no_sex" in memory:
                text _("I think she likes me. I know... Wild assumption. It's not like she offered to have sex with me, so... Wait. That's literally what she did. But she was also shy and reluctant about it. Knowing her past in that fucked up world, I'm still reluctant to take her actions at face value. But the more I talk to her, the easier it is to believe she would be open to going further."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d9_tracy_sex" in memory:
                text _("We had sex before I even talked to [Fiona]. Obviously, it was a mistake, but... I can't bring myself to feel bad about it. It looks like the self-hatred for hurting [Fiona] hasn't caught up with me. But putting that aside, [Tracy] is truly lovely. I shouldn't have difficulty falling in love with someone like her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_tracy_confess" in memory:
                text _("It's rare to see a woman in her mid-twenties who is this bad at dealing with her feelings. Well, it's probably her first love. I knew she was shy. I didn't imagine her running away after telling me she liked me, though. It's so sweet, it's already comical."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_training" in memory:
                text _("Lovely my ass. [Tracy] doesn't hold back when teaching me how to fight. She seems to put a lot of faith in [Sally]. If this is what training will be like, I can understand why she pushed for [Sally] to heal me every evening."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("[Sue] told me something interesting with the potential to be really fucked up. When [Nathaniel] killed the old man, [Tracy]'s mother also died. But apparently [Nathaniel] wasn't fighting alone. He had [Aurora] at his side. It sounded like there was a chance [Aurora] killed [Tracy]'s mother."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25




            if "d1_tracy_wings" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                if not "d2_drive_tracy" in memory:
                    text _("Fucking wings... There is no use in denying it. She defies everything I ever knew true. People like her could easily be why our depiction of angels is what it is today. If she can fly, then I'm done. Let's ignore the fact that the wings came out of nowhere. Sustaining them with enough energy to fly would be unimaginable. It won't surprise me if she surpasses the limits of human beings."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25
                else:
                    text _("Wings. That's the first thing. Not only can she create them from nowhere, she even has the ability to use them."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                    text _("The second thing is her strength. I haven't seen it yet, but she claims to be strong enough to lift a car. She has faster reaction times and better senses. Again, not confirmed."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "curse_heard_02" in memory:
                text _("{size=35}{b}Curse:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("[Amber] told me [Tracy]'s wings aren't part of her ability. Instead, she has inherited them from her mother like a curse that's passed down through generations. I don't think it has any negative consequences, so the word curse might be misleading in this case."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25





        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_tracy")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_sally():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "sally_seen_02" in memory:
            add "images/screens/memory/Sally_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)

        default Sally_name = VariableInputValue("Sally", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Sally!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Sally_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_night_forrest_aurora" in memory and not "d2_healing_sue" in memory:
                text _("She is referred to as someone that would be able to fix the issue of a group member being wounded. Maybe someone with medical training. A doctor or a nurse. In the simplest of cases, she could be an elderly woman that offers experience when trouble arises."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_healing_sue" in memory:
                text _("The healer of their group. She seems to be very close to [Sue]. It's hard to tell through her formal facade, but I felt a familiarity between those two."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                if "d2_healing_mc" in memory:
                    text _("At last, even she asked if I wanted to spend the night with her. I cut her off before she was able to put it into words, but that doesn't change the fact that this was what she tried to say. Either I'm very good-looking, or it's unusual for a man to help out nine women and not sleep with at least one."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                if "d3_healing" in memory:
                    text _("[Sally] was amazed by the images she found on the web. One benefit of having a few billion people around is that a couple hundred can go ahead and create clean and concise representations of the human body in multiple levels of abstraction."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                if "d8_massage" in memory or "tracy_notes" in memory:
                    text _("She has been healing me every day. She is always polite and keeps a professional distance. She works around the house and never complains."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                if "d8_massage" in memory:
                    text _("I was surprised to hear from [Tracy] that [Sally] might be the only one of them who truly loved the old man."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                else:
                    if "tracy_notes" in memory:
                        text _("I was surprised to read in [Tracy]'s notes that [Sally] might be the only one of them who truly loved the old man."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1100
                            size 25

                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("She can heal someone's injuries."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                if "d2_healing_mc" in memory:
                    text _("[Sally] uses magic to reconstruct the body of another person. She can read someone's body by touching it. Any mistake she makes can be very severe. That is why she takes her time when healing."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                if "d3_healing" in memory:
                    text _("Screw taking her time! She fixed my shoulder, knees, and hip in less than half an hour. Oh, and she removed my scars like it was nothing. I don't see a reason why she wouldn't be able to recreate a fully functional arm in case I lose mine for some reason. How long will it take? Maybe an additional five minutes?"):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25






        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_sally")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_monique():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "monique_seen" in memory:
            add "images/screens/memory/Monique_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)

        default Monique_name = VariableInputValue("Monique", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Monique!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Monique_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if not "d2_monique_seen" in memory:
                text _("[Esther] mentioned her name. Another woman that's part of their group."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
            else:
                text _("I'm pretty sure I didn't leave a good impression on her. The part of her body that I felt was pretty soft. I didn't even need to feel her nipple pressing into my palm to know I groped her breast."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_discussion" in memory:
                text _("Even though she now has clothes, [Monique] is still walking around invisible. Strangely enough, you get used to seeing a flying set of clothes hover around the house. At least we no longer bump into each other."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "tracy_notes" in memory:
                text _("[Tracy]'s notes about [Monique] reminded me of the plot from horror movies. Whenever the man she was promised to got drunk, [Monique] stripped naked, turned invisible, and hid, hoping she wouldn't be found by this rampaging lunatic that often beat his wives. You could say that she had it better than [Megan] since she was able to disappear in ways she couldn't be found easily, but it's not like that would make it any better. Eventually, [Amber] realized that [Megan] was determined to die rather than be raped by this drunk lunatic. She also saw how [Monique]'s story wouldn't end happily, so she took both and ran."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d9_monique_blanket" in memory:
                text _("I caught her sleeping in my room, and now she avoids me even more. Putting that blanket over her was a rather stupid idea if the goal was to get closer to her. I already had the feeling that [Monique] was spying on me. I doubt that [Tracy] asked her to do it, so she probably does it independently. I should be extra careful when I'm reading something others shouldn't see, but other than that, I don't mind her sneaking around. Maybe it makes her feel safe and secure."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_monique_seen" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("She can turn herself completely invisible."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_monique")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_megan():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "megan_seen" in memory:
            add "images/screens/memory/Megan_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)

        default Megan_name = VariableInputValue("Megan", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Megan!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Megan_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "megan_seen" in memory:
                if Megan == "Megan":
                    text _("A fox. And she's called Megan."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "d1_drive" in memory:
                text _("I haven't seen her as a girl yet, but I'm sure I heard her voice. She is the one who pointed out that I was watching them. It's just an assumption, but with her being a fox, I'd say she has heightened senses in general or is simply better at seeing in the dark than your average human."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_discussion" in memory:
                text _("She has clothes, but she still walks around in her fox form. That means she doesn't trust me, right?"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_megan_pet" in memory:
                text _("I saw [Monique] pet her. I would have treated her like a woman that happens to run around as a fox, but maybe she becomes more animal-like than I thought."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d8_massage" in memory:
                text _("[Tracy] mentioned that [Megan] escaped the advances of her first man by turning into her fox form. She must look quite beautiful because in her eyes, the moment I see her appearance, I might fall for her and try something inappropriate. It's as I thought. If I can make her trust me, she will have no problem walking around as a human."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "tracy_notes" in memory:
                text _("From [Tracy]'s notes I know that the man [Megan] was promised to often drank and beat his wives. It's the reason [Amber] decided to take both [Megan] and [Monique] and ran away. In his drunken state, he tried to make [Megan] turn back to being human by kicking her around. [Amber] judged that if this continues, eventually, he will kill [Megan] that way."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d9_morning_megan" in memory:
                text _("Something strange happened. [Megan] willingly interacted with me. She only asked me to prepare breakfast for her, but that still counts. I can build from there."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_breakfast" in memory:
                text _("She did it again! [Tracy] almost ruined the moment, but I made it work. For some reason, [Megan] wants me to make her breakfast. She is trying to do something. It can't be for convenience's sake since she went out of her way to ask me. I tried to pet her, but she ran away. Later, she came back and finished her breakfast. I could have tried to pet her once again, but I didn't."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


            if "megan_seen" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("She can transform into a fox."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


            if "curse_heard_02" in memory:
                text _("{size=35}{b}Curse:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("Apparently, [Megan] has fluffy ears and a tail, even when she isn't walking around as a fox."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25



        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_megan")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_lucy():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Lucy_01.png" pos (70, 50)

        default Lucy_name = VariableInputValue("Lucy", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Lucy!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Lucy_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_parking_leave" in memory:
                text _("Stone cold. A gun was fired right next to her, and she didn't even flinch. [Tracy] said she's from my earth. If so, then she might have been through a lot. She has a high-pitched voice. Trauma victims sometimes fall back to the voice they had when they have been traumatized. This reasoning doesn't work backward, so there is no telling if she suffered trauma in her youth. I should still keep it in mind."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_lucy_con" in memory:
                text _("I found out that she's blind. I didn't even notice it the night we first met. There has to be a scared little girl in her somewhere, right? At least when she's around me, she knows how to hide it."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_lucy" in memory:
                text _("She teared up and cried. Maybe not a scared little girl, but frustrated and full of regret? I didn't poke around to find out more. Relying on those women to directly tell me about their situation might be unreasonable."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_lucy" in memory:
                text _("[Lucy] lost her eyesight in that other world, but it's not her that told me. [Esther] explained it."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d6_lucy_01" in memory:
                text _("Her behavior is a little strange. Whenever I mention something new, she already knows about it, but when asked, she doesn't remember her childhood. The complicated thing is that I believe her in both instances. Normally, I'd refer her to a therapist to work through her amnesia, but in the current situation, that's difficult. I might not be able to get around a long and deep conversation just between the two of us. [Esther] means well, but she often gives [Lucy] the opportunity to hide her thoughts, and I don't need that when I try to understand what's really going on."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_reunion_lucy_01" in memory:
                text _("She forgot that she had a sister. Well, she also forgot her parents, but this one is different. She was regaining her memories relatively well, but this new snippet of information turned her world upside down."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_lucy_01" in memory:
                text _("I now understand her reaction a little better. In one way or another, [Lucy] thought she knew which memories she had lost. She knew she had forgotten the name of her parents or the smell of their house, but when it came to her sister, she forgot her entirely. Regaining her memories also isn't going as smoothly as I thought it did. She struggles a lot silently. I think [Esther] has noticed and is taking extra care of her. First, I thought it was because [Lucy] is blind, but I no longer believe this explanation is sufficient."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d8_lucy_con" in memory:
                text _("She is thinking about the future. [Tracy] once mentioned that [Lucy] probably believes that I can defeat [Nathaniel]. By now, I'm sure that's not the case. She might want to believe in me, but she just can't do it. In her eyes, the future looks grim. But I'm glad she opened up and showed her true feelings."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("[Tracy]'s notes mentioned that the old man liked to talk to [Lucy]. When I talked to her about this, she explained a few things about the old man. [Lucy] listened to his stories and silently came to a sad realization. The old man is no hero. She hesitates to describe him as cowardly, but it's going in that direction."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("Apparently the old man blinded Lucy on purpose. She doesn't hate him, though. Man, they lived in a sick world..."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d10_lucy_con" in memory:
                text _("[Lucy] made the first step and asked to call her sister. I think this is really good progress. She is trying to reconnect with her family. I was afraid she would try to shield herself, and I might need to push her slightly. It's good to know that there is one less thing to worry about."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_lucy")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_esther():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        if "esther_seen" in memory:
            add "images/screens/memory/Esther_01.png" pos (70, 50)
        else:
            add "images/screens/memory/locked.png" pos (70, 50)

        default Esther_name = VariableInputValue("Esther", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Esther!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Esther_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_night_hospital" in memory:
                text _("Voluntary scapegoat. It might be rough to phrase it like that, but she rather let herself get captured than drag down either [Lucy] or [Tracy]. Maybe a sense of self-loathing, an instinct to protect, or simply a naive assumption that no harm could befall her? Hard to tell."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d1_night_esther_offer" in memory:
                text _("She also offered herself to me. She asked [Tracy] if they drew lots, indicating that even if this offer of theirs is cultural, it's not something they want to do. It seems like a chore they do for the benefit of their group. Even without the concern of them trying to seduce me to catch me off guard, it might have been the right thing to refuse them from a moral perspective."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_morning" in memory:
                text _("I think her social status is as high or even higher than [Tracy]'s. She undermined her authority and overruled [Tracy]'s decision to be cautious of me."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_esther_con" in memory:
                text _("Also, she was sent to tell me about their decision to stay at my house for a while. That should confirm that she stands close to the top of their group."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "tracy_notes" in memory:
                text _("[Tracy] mentioned in her notes that [Esther] grew up sheltered. Because of her ability, she was treated like a special existence in the castle. You could mistake her for a princess if you didn't know their circumstances. [Tracy] didn't write it directly, but the old man treated her like a grandchild. Because of their world's anti-incest rules, that's unlikely. He probably felt guilty for locking away her ability and gave her special privileges to compensate for that."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d2_morning" in memory:
                text _("{size=35}{b}Ability:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("She uses lifeforce as a source of power."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_esther")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_fiona():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Fiona_01.png" pos (70, 50)

        default Fiona_name = VariableInputValue("Fiona", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Fiona!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Fiona_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_fiona_call" in memory:
                text _("I figured that she wouldn’t be able to sleep very well. I never thought that it would come in handy. At least she didn’t cry when she heard my voice."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_cecilia" in memory:
                text _("She is the daughter of the vice president. [Fiona] was kidnapped three years ago to extrude pressure on her father. That's when I first met her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_cecilia" in memory:
                text _("By now, I've proposed to her."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d4_training_bed" in memory:
                text _("I also asked her to have kids. She even agreed."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_fiona_01" in memory:
                text _("She FaceTimed me to find out if I'm alright. Sadly, it wasn't me, but [Aurora] who had my phone at that time. She must have thought I moved on and was spending my time with another woman. [Fiona] turned off her phone, drowned her feelings in wine, and decided to come to our house and fight for my heart."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("She said she still loves me."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d8_fiona_marry" in memory:
                text _("I'm unsure she can handle spending the rest of her life with me. I'm not even sure if I want her to put up with me. Wouldn't it be the selfless thing to want her to find happiness elsewhere? But I'm also not sure if I want that. No I don't. But It might be the right thing."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d8_fiona_bye" in memory:
                text _("Tomorrow we are going to talk."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d9_fiona_talk" in memory:
                text _("A round of applause, please. [Fiona] told me I could build myself a harem, and the next time she wants to run away, she'll at least talk to me beforehand! I'd say I've won the jackpot, but obviously, life isn't that simple. I do believe she means what she said, and I now know that she is determined to be with me. Still, it feels like she'll eventually tell me she made a mistake and can't do it. Maybe it's just because she said those words before. I'm not sure. For now, I'll trust her words and go from there."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


            if "d10_fiona_morning" in memory:
                text _("Thank god she didn't have time to eat breakfast with [Tracy] and [Sue]. She said she was okay with other women, but I'm not sure what will happen if these three sit down and start talking."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_fiona")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_cecilia():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Cecilia_01.png" pos (70, 50)

        default Cecilia_name = VariableInputValue("Cecilia", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Cecilia!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Cecilia_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d3_blackroom" in memory:
                text _("She is one of the agents sent to help out [Colby]. She has no field experience, which means she is very underqualified to be sent on this mission. [Fiona]'s father was probably pulling some strings to make this happen."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                if "d3_drive" in memory:
                    text _("[Cecilia] was the one who made the connection between my past self and me. She said that she had to do a presentation about me. I wasn't aware that they now teach my missions, but it's also not surprising."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                if "d3_cecilia" in memory:
                    text _("She also figured out my connection to [Fiona] and her father. This was predictable, but I would have liked to nudge her into my corner for one or two days before she had to decide where she should put her trust and loyalty."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "d4_cecilia_beds" in memory:
                text _("The good thing is that she is looking up to me. If it comes down to it, she will probably do the right thing and help out this group of women."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_cecilia" in memory:
                text _("[Cecilia] bought me a new frame. Of course, she was the one that broke it in the first place. You could say it's the least she can do in her situation. She also told me that she is on my side. The sad thing is that I can't take her words at face value. She's probably genuine, but I should still be careful."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_cecilia")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_emily():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Emily_01.png" pos (70, 50)

        default Emily_name = VariableInputValue("Emily", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Emily!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Emily_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            text _("Bakery girl. I couldn’t even tell that she is going through a lot."):
                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                xpos 10
                xmaximum 1100
                size 25

            if "d3_bakery" in memory and not "d7_bakery" in memory:
                text _("Her brother is still in the hospital."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d7_bakery" in memory:
                text _("When I last saw her, she was happy. Her brother has woken up from his coma."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_emily")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_mia():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/locked.png" pos (70, 50)

        default Mia_name = VariableInputValue("Mia", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Mia!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Mia_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            text _(""):
                xpos 10
                xmaximum 1100
                size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_mia")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_colby():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Colby_01.png" pos (70, 50)

        default Colby_name = VariableInputValue("Colby", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Colby!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Colby_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30


            if "d1_colby_organization" in memory or "fiona_heard" in memory:
                text _("DSD. He is working for my former employer."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            else:
                text _("DSD. He is probably working for my former employer."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_drive" in memory:
                text _("He knows who I am by now, but he decided against telling anybody. He probably judged that the consequences would be too great. The problem is that I can no longer go into a pissing contest with him because he can destroy my peaceful little life."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d5_blackroom" in memory:
                text _("He is an excellent agent. I need to be careful, or he will beat me at my own game."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d6_colby_call" in memory:
                text _("For example, he didn't use the information about [Lucy]'s family as leverage. I would have made him regret that decision if he did, that's for sure. Instead, he offered this info for free. I would be in a rough spot if I had to explain my actions to the DSD. Using the attack on [Aurora] to justify my antagonism to him will only work so long. He must have realized that something was off and tried not to provide me with additional ammunition that I could use to slow down this mission."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_colby")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_clay():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Clay_01.png" pos (70, 50)

        default Clay_name = VariableInputValue("Clay", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Clay!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Clay_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_night_forrest_aurora" in memory or "d1_clay_01" in memory:
                text _("He faked his death three years ago."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("This time he is actually dead, though."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25
                text _("He was a good man."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_clay")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_morris():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Morris_01.png" pos (70, 50)

        default Morris_name = VariableInputValue("Morris", default=True, returnable=False)

        hbox:
            pos (700, 100)
            text _("[Morris!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Morris_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            text _("What an annoying guy. I would have avoided him if he wasn't so good at what he does after we first met. It’s still hard to believe that I became friends with a guy like that. Good thing that he’s still in business."):
                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                xpos 10
                xmaximum 1100
                size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_morris")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_fifa():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/Fifa_01.png" pos (70, 50)

        hbox:
            pos (700, 100)
            text _("[Kent!u] [Lambert!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d1_fifa_call" in memory:
                text _("He is [Fiona]'s father."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("It's good to know that my name still carries weight among people that know of me."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

            if "d3_cecilia" in memory:
                text _("He is the vice president."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_fifa")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_nathaniel():
        style_prefix "memory"
        zorder 151
        modal True

        default Nathaniel_name = VariableInputValue("Nathaniel", default=True, returnable=False)

        add "images/screens/memory_01.png"

        add "images/screens/memory/Nathaniel_01.png" pos (70, 50)

        hbox:
            pos (700, 100)
            text _("[Nathaniel!u]"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            imagebutton:
                pos (10, 13)
                idle "images/screens/edit.png"
                hover "images/screens/edit2.png"
                action Show("name_input", name = Nathaniel_name)

        viewport:
            pos (700, 200)
            xmaximum 1150
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            if "d2_nathaniel_conversation" in memory:

                if not "d4_discussion_01" in memory:
                    text _("A man from this other world. He appears to be relatively young. I should ask [Tracy] about his age. I should know if I'm dealing with a young adult or an old child."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                    text _("He said that [Aurora] was his and that [Tracy] took her from him. What did he mean by that?"):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                else:
                    text _("A man from this other world. He appears to be relatively young. From what [Tracy] said, he should be about 25 years old. A young adult that received everything he wanted from an early age. It could be too simple to assume he's just another spoiled child but it kind of looks that way."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

                    text _("[Aurora] was one of the women sent to him to be his wife and have children. I'm still determining what happened, but [Tracy] mentioned something about [Nathaniel] attacking the old man's castle. They usually live in different parts of the earth, so that's likely when they met. It might also be the moment [Aurora] joined their group."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 1100
                        size 25

            if "tracy_notes" in memory:
                text _("Sadistic prick..."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25



            if "d2_nathaniel_conversation" in memory:
                text _("{size=35}{b}Abilities:{/b}{/size}"):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("He can fly or hover. While doing so, he can move very fast."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("When [Tracy] tried to help me, [Nathaniel] did something to make her pass out."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25

                text _("He was able to give me an ability."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25



        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_nathaniel")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_world():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"



        hbox:
            pos (150, 100)
            text _("THEIR WORLD"):
                size 80
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]


        viewport:
            pos (150, 200)
            xmaximum 1630
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 50

            hbox:
                spacing 30
                add "images/screens/memory/memory_theirworld_01.png"
                vbox:
                    yalign .5
                    spacing 30
                    text _("[Tracy] told me that they are from another earth. When I asked her if they are from a different planet, she insisted on our worlds being the same but our universes being different. It sounds like they are from a parallel universe where there was a breaking point that made her earth differ from mine."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 800
                        size 25

                    text _("The population where they come from is down to 100.000 people. That's not a lot for an entire world."):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        xpos 10
                        xmaximum 800
                        size 25

                    if "d2_amber_con_01" in memory:
                        text _("Worse. There are only 167 men left. Apparently, the rest were killed during some gruesome war."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 800
                            size 25

            if "d4_discussion_01" in memory:
                hbox:
                    spacing 30
                    vbox:
                        yalign .5
                        spacing 30

                        text _("A backward society where people live in castles and wars are fought with magic."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 800
                            size 25

                        text _("Yes, they have magic. But they don't use it like we use technology. Maybe that's because it's more tied to one person rather than magic being a general concept that can be used by everyone and everywhere."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 800
                            size 25

                    add "images/screens/memory/memory_theirworld_02.png"



        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_world")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

    screen memory_oldMan():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"

        add "images/screens/memory/locked.png" pos (70, 50)

        hbox:
            pos (700, 100)
            text _("OLD MAN"):
                size 60
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

        vbox:
            pos (700, 200)
            spacing 30

            if "d3_lucy_listen" in memory or "d4_discussion_01" in memory:
                text _("He's [Aurora]'s father."):
                    outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                    xpos 10
                    xmaximum 1100
                    size 25


        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_oldMan")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]


    screen memory_clothes():
        style_prefix "memory"
        zorder 151
        modal True

        add "images/screens/memory_01.png"



        hbox:
            pos (150, 100)
            text _("CLOTHES"):
                size 80
                font "gui/Fonts/Mova.ttf"

                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]


        viewport:
            pos (150, 200)
            xmaximum 1630
            ymaximum 700
            mousewheel True
            scrollbars "vertical"
            has vbox:

                spacing 30

            hbox:
                spacing 30
                add "images/screens/memory/memory_clothes_TS_500.png"
                vbox:
                    yalign .5
                    spacing 30
                    text _("[Tracy!u] AND [Sue!u]"):
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                        size 40
                        font "gui/Fonts/Mova.ttf"



                    if not "d2_store" in memory:
                        text _("It's interesting. [Tracy] and [Sue] seem to wear the same outfit. An armor-like leather dress, a belt, gloves, and a metal plate protecting one of their shoulders. The whole attire reminds me of the depiction of a female warrior from ancient times."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25

                        text _("Then again, there is also a difference. [Sue]'s metal plate is silver, and [Tracy]'s seems to be golden. Here, you'd assume that the one with the golden plate would have a higher social status than the silver plate. But if these women are from a different earth, then I can't just make this assumption. Gold might be common where they are from and therefore not valued. Who knows?"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25
                    else:
                        text _("It's interesting. [Tracy] and [Sue] seem to have worn the same outfit. An armor-like leather dress, a belt, gloves, and a metal plate protecting one of their shoulders. The whole attire reminded me of the depiction of a female warrior from ancient times."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25

                        text _("Then again, there is also a difference. [Sue]'s metal plate is silver, and [Tracy]'s seems to be golden. Here, you'd assume that the one with the golden plate would have a higher social status than the silver plate. But if these women are from a different earth, then I can't just make this assumption. Gold might be common where they are from and therefore not valued. Who knows?"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25



            hbox:
                spacing 30
                vbox:
                    yalign .5
                    spacing 30

                    text _("[Aurora!u]"):
                        size 40
                        font "gui/Fonts/Mova.ttf"
                        outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]

                    if not "d2_store" in memory:
                        text _("[Aurora] isn't wearing much of anything. It's surprising that her clothes even stay in place. It looks more like a sculpture than actual clothes. A dragon whose tail covers what's between her legs and whose wings cover her breasts. It's hard to believe that this is very practical. She might not be someone who is expected to move a lot, or she couldn't afford to wear something like this."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25

                        text _("She is also wearing skin-tight red shorts. Maybe that's just me knowing nothing about how to dress but this piece of clothing doesn't seem to fit in with the artistic dragon lingerie."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25

                    else:
                        text _("[Aurora] didn't wear much of anything. It's surprising that her clothes even stayed in place. It looked more like a sculpture than actual clothes. A dragon whose tail covers what's between her legs and whose wings cover her breasts. It's hard to believe that this is very practical. She might not be someone who is expected to move a lot, or she couldn't afford to wear something like this."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25

                        text _("She was also wearing skin-tight red shorts. Maybe that's just me knowing nothing about how to dress but this piece of clothing didn't seem to fit in with the artistic dragon lingerie."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25

                add "images/screens/memory/memory_clothes_aurora_500.png"



            hbox:
                spacing 30
                add "images/screens/memory/memory_clothes_sally_500.png"
                vbox:
                    yalign .5
                    spacing 30
                    if not "d2_store" in memory:
                        if not "sally_seen" in memory:
                            text _("[Lucy!u]"):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                size 40
                                font "gui/Fonts/Mova.ttf"

                            text _("[Lucy] is wearing a long skirt and a matching shirt. Both of which seem to be of high quality. They look surprisingly beautiful. Something you might even find on my earth."):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                xpos 10
                                xmaximum 1000
                                size 25
                        else:
                            text _("[Lucy!u] AND [Sally!u]"):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                size 40
                                font "gui/Fonts/Mova.ttf"

                            text _("[Lucy] and [Sally] are wearing long skirts and matching shirts. Both of which seem to be of high quality. They look surprisingly beautiful. Something you might even find on my earth."):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                xpos 10
                                xmaximum 1000
                                size 25
                    else:
                        text _("[Lucy!u] AND [Sally!u]"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            size 40
                            font "gui/Fonts/Mova.ttf"

                        text _("[Lucy] and [Sally] were wearing long skirts and matching shirts. Both of which seemed to be of high quality. They looked surprisingly beautiful. Something you might even find on my earth."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1000
                            size 25



            if "d1_drive" in memory:
                vbox:
                    yalign .5
                    spacing 30

                    if not "d2_store" in memory:
                        text _("[Megan!u]"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            size 40
                            font "gui/Fonts/Mova.ttf"
                        text _("[Megan] isn't wearing anything. Does that mean she isn't wearing anything when she transforms back to her human form?"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1480
                            size 25
                    else:
                        text _("[Megan!u] AND [Monique!u]"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            size 40
                            font "gui/Fonts/Mova.ttf"
                        text _("[Megan] and [Monique] didn't wearing anything."):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            xpos 10
                            xmaximum 1480
                            size 25

            if "colby_heard" in memory:
                hbox:
                    spacing 30
                    vbox:
                        yalign .5
                        spacing 30
                        text _("[Esther!u]"):
                            outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                            size 40
                            font "gui/Fonts/Mova.ttf"

                        if not "d2_store" in memory:
                            text _("[Esther] is wearing elegant clothes that remind me of something precious. The colors purple and gold in ancient times were the biggest signs of the rich and powerful."):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                xpos 10
                                xmaximum 1000
                                size 25
                        else:
                            text _("[Esther] was wearing elegant clothes that reminded me of something precious. The colors purple and gold in ancient times were the biggest signs of the rich and powerful."):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                xpos 10
                                xmaximum 1000
                                size 25
                    add "images/screens/memory/memory_clothes_esther_500.png"

            if "amber_seen" in memory:
                hbox:
                    spacing 30
                    add "images/screens/memory/memory_clothes_amber_500.png"
                    vbox:
                        yalign .5
                        spacing 30
                        if not "d2_store" in memory:
                            text _("[Amber!u]"):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                size 40
                                font "gui/Fonts/Mova.ttf"

                            text _("[Amber] wears an elegant outfit decorated by wolf sculls. It reminds me of something the heroine of a fairytale would wear."):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                xpos 10
                                xmaximum 1000
                                size 25
                        else:
                            text _("[Amber!u]"):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                size 40
                                font "gui/Fonts/Mova.ttf"

                            text _("[Amber] wore an elegant outfit decorated by wolf sculls. It reminded me of something the heroine of a fairytale would wear."):
                                outlines [ (absolute(1), "#0d0d0d", absolute(1), absolute(1)) ]
                                xpos 10
                                xmaximum 1000
                                size 25




        textbutton _("{font=gui/Fonts/Mova.ttf}RETURN{/font}"):
            pos (1600, 950)
            text_size 60
            action Hide("memory_clothes")
            keysym ('K_RETURN', 'K_KP_ENTER')
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]
