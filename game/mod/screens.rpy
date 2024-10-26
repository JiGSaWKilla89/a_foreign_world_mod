init 5:# Screens

    screen navigation():
        $ screen_vis = renpy.get_screen("color_picker_mr") or renpy.get_screen("color_picker_wt")#If(renpy.get_screen("color_picker_mr"),Hide("color_picker_mr",transition=dissolve))
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.5
            spacing -40
            if main_menu:
                imagebutton:
                    pos (-10, 0)
                    idle "gui/overlay/main_menu_button_start_idle.png"
                    hover "gui/overlay/main_menu_button_start_hover.png"
                    action Start(),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])
            else:
                imagebutton:
                    pos (-10, 0)
                    idle "gui/overlay/main_menu_button_menu_idle.png"
                    hover "gui/overlay/main_menu_button_menu_hover.png"
                    action MainMenu(),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

                imagebutton:
                    pos (-10, 0)
                    idle "gui/overlay/main_menu_button_save_idle.png"
                    hover "gui/overlay/main_menu_button_save_hover.png"
                    action ShowMenu("save"),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

            imagebutton:
                pos (-10, 0)
                idle "gui/overlay/main_menu_button_load_idle.png"
                hover "gui/overlay/main_menu_button_load_hover.png"
                action ShowMenu("load"),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

            imagebutton:
                pos (-10, 0)
                idle "gui/overlay/main_menu_button_preferences_idle.png"
                hover "gui/overlay/main_menu_button_preferences_hover.png"
                action ShowMenu("preferences"),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

            if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
                imagebutton:
                    pos (-10, 0)
                    idle "mod/images/main_menu_button_music_idle.png"
                    hover "mod/images/main_menu_button_music_hover.png"
                    action ShowMenu("musicroom"),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])
            
            if JGSLoadable("replays") and not _in_replay:
                imagebutton:
                    pos (-10, 0)
                    idle "mod/images/main_menu_button_replays_idle.png"
                    hover "mod/images/main_menu_button_replays_hover.png"
                    action ShowMenu("replays"),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

            if _in_replay:
                imagebutton:
                    pos (-10, 0)
                    idle "mod/images/main_menu_button_end_replay_idle.png"
                    hover "mod/images/main_menu_button_end_replay_hover.png"
                    action EndReplay(confirm=True),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])


            imagebutton:
                pos (-10, 0)
                idle "gui/overlay/main_menu_button_about_idle.png"
                hover "gui/overlay/main_menu_button_about_hover.png"
                action ShowMenu("about"),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

            if renpy.variant("pc"):
                imagebutton:
                    pos (-10, 0)
                    idle "gui/overlay/main_menu_button_quit_idle.png"
                    hover "gui/overlay/main_menu_button_quit_hover.png"
                    action Quit(confirm=not main_menu),If(screen_vis,[Hide("color_picker_mr",transition=dissolve),Hide("color_picker_wt",transition=dissolve)])

    screen main_menu():
        use mod_check()
        $ tooltip = GetTooltip()

        tag menu
        add gui.main_menu_background
        frame:
            style "main_menu_frame"
        use navigation
        if (steam_build):
            hbox:
                pos (490, 860)
                vbox:
                    pos (0, 5)
                    spacing 15
                    hbox:
                        spacing 5
                        add "gui/flags/us-flag.png" yalign .5
                    hbox:
                        spacing 5
                        add "gui/flags/sp-flag.png" yalign .5
                    hbox:
                        spacing 5
                        add "gui/flags/gm-flag.png" yalign .5
                    hbox:
                        spacing 5
                        add "gui/flags/china-flag.png" yalign .5
                vbox:
                    ypos -5
                    spacing -8
                    textbutton "{b}{font=DejaVuSans.ttf}English{/font}{/b}":
                        action Language(None)
                        text_size 30
                        xalign 1
                    textbutton "{b}{font=DejaVuSans.ttf}Español{/font}{/b}":
                        action Language("Spanish")
                        text_size 30
                        xalign 1
                    textbutton "{b}{font=DejaVuSans.ttf}Deutsch{/font}{/b}":
                        action Language("German")
                        text_size 30
                        xalign 1
                    textbutton "{font=gui/Fonts/SourceHanSans.otf}简体中文{/font}":
                        action Language("chinese")
                        text_size 30
                        xalign 1
                        ypos -15
        imagebutton:
            idle "gui/Discord_idle.png"
            hover "gui/Discord_hover.png"
            pos (460, -5)
            action OpenURL("https://discord.com/invite/gJsRt428U3")
        if not steam_build:
            add "gui/MainMenu_Banner_underlay.webp":
                xpos -820
            vbox:
                spacing 10
                pos (480, 680)
                text _("STEAM"):
                    style "main_menu_title"
                    font "gui/Fonts/Mova.ttf"
                    size 65
                    color "#fff"
                    xalign .5
                    outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]
                imagebutton:
                    idle "gui/AForeignWorld_Banner_01.webp"
                    hover "gui/AForeignWorld_Banner_02.webp"
                    action OpenURL("https://store.steampowered.com/app/2174320")
                imagebutton:
                    idle "gui/AFamiliarWorld_Banner_01.webp"
                    hover "gui/AFamiliarWorld_Banner_02.webp"
                    action OpenURL("https://store.steampowered.com//app/2229110")
        if gui.show_name:
            vbox:
                style "main_menu_vbox"
                text _("A FOREIGN WORLD"):
                    style "main_menu_title"
                    font "gui/Fonts/Mova.ttf"
                    size 90
                    color "#fff"
                    outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]
                text "{font=gui/Fonts/SourceHanSans.otf}HighbornTiger{/font}":
                    style "main_menu_version"
                    color "#fff"
                    size 25
                    outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]
                    kerning 52

        vbox:
            xalign 1.0
            text _("{b}{u}[jg_1]JiG[jg_3][jg_2]SaW[jg_3]{/u}{/b}\nMOD Installed"):
                size gui.mod_info_size
                outlines [(2, "#fff9", 1, 1)]
                text_align 0.5
                font "mod/CM-Font.otf"

            textbutton _("Mod Features"):
                xalign 1.0
                text_size gui.text_size
                text_outlines [(2, "#0009", 1, 1)]
                text_align 1.0
                action ShowMenu("mod_features")
                tooltip _("Click me to view mod features")
    
            if mod_updated[0] not in ["Mod up-to-date", "JSON Error", "Could Not Connect to Host", "HTTP Error", "Timeout", "Request Error", "None"]:
                textbutton ("%s"%"Update Available" if mod_updated[0] != "Game Version Newer Than Mod" else "Check for updated mod"):
                    xalign 1.0
                    text_size gui.text_size
                    text_outlines [(2, "#0009", 1, 1)]
                    text_align 1.0
                    action OpenURL(gui.mod_update_url)
                    tooltip _("Click me to get updated mod")
                if mod_changelog:
                    textbutton "Mod Changelog":
                        xalign 1.0
                        text_size gui.text_size
                        text_outlines [(2, "#0009", 1, 1)]
                        text_align 1.0
                        action ShowMenu("mod_changelog")
                        tooltip _("View Mod Changelog")

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

    screen say(who, what, slow_effect=persistent._slow_effect, slow_effect_delay=persistent._effect_delay, always_effect=persistent._always_effect):

        zorder 101
        style_prefix "say"



        window:
            id "window"



            if persistent.TextBoxVisible and persistent.TextBoxHidden == False:
                background Transform(style.window.background, alpha = 1)
            else:
                background Transform(style.window.background, alpha = 0)

            if persistent.TextBoxHidden == False:
                if who is not None:

                    window:
                        id "namebox"
                        style "namebox"
                        text who id "who":
                            xpos 20
                            ypos 36
                            if persistent._fancy_text:
                                slow_effect slow_effect
                                slow_effect_delay slow_effect_delay
                                always_effect always_effect

            if persistent.TextBoxHidden == False:
                text what id "what":
                    if persistent._fancy_text:
                        slow_effect slow_effect
                        slow_effect_delay slow_effect_delay
                        always_effect always_effect
            else:
                text what id "what" ypos 1900:
                    if persistent._fancy_text:
                        slow_effect slow_effect
                        slow_effect_delay slow_effect_delay
                        always_effect always_effect




        if persistent.SideImages:
            if not renpy.variant("small"):
                if not persistent.TextBoxHidden:
                    add SideImage() xalign 0.05 yalign 1.05

    screen shortcuts():
        style_prefix "shortcuts"
        zorder 300
        default shown = False
        default show_button = False

        mousearea:
            align (1.0, 0.05)
            xysize (gui.text_size,gui.text_size)
            hovered SetLocalVariable("show_button", True),With(dissolve)
            unhovered SetLocalVariable("show_button", False),With(dissolve)

        if shown:
            button:
                padding (0,0,0,0)
                add "#000" alpha .9
                add "splashText"
                xysize (config.screen_width, config.screen_height)
                action SetLocalVariable("shown", False),With(dissolve)
            key "game_menu" action SetLocalVariable("shown", False),With(dissolve)

            text _("Click anywhere to close or the ? button") align (0.98, 0.98)

        if show_button:
            textbutton "?" action ToggleLocalVariable("shown"),With(dissolve) align (1.0, 0.05)

    screen mod_changelog():
        $ tooltip = GetTooltip()
        tag menu

        use game_menu(_("Mod Changelog"), scroll="viewport"):
            vbox:
                spacing 10
                for i in mod_changelog:
                    text "%s"%i

    screen mod_check():
        timer 600 action SetVariable("mod_updated", get_latest_mod()) repeat True
        
    screen mod_features():
        $ tooltip = GetTooltip()
        tag menu

        use game_menu(_("Mod Features"), scroll="viewport"):
            vbox:
                spacing 10
                if gui.jg_mod_version == config.version:
                    use mod_options_text
                else:
                    text _("Mod is outdated {a=gui.mod_update_url}Click Here{/a} to Check for New Version")
                    text _("Most mod options will work")
                    null height 20
                    use mod_options_text
                    
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

    screen mod_options_text():
        text _("Report any issues you find with the mod {a=[gui.mod_issues]}Here{/a}") tooltip _("Github issues tracker")
        text "Walkthrough"
        text _("1. Walkthrough Suggestions Toggled using {a=#:None}{color=#f00}(W){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("2. Walkthrough Tooltips Toggled using {a=#:None}{color=#f00}(Shift+T){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
            text _("Music Player")
            text _("1. Music Player can be Toggled ingame using {a=#:None}{color=#f00}(M){/color}{/a}") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
            text _("2. Hovering over Volume Slider allows mousewheel up/down control") xoffset 50
        text "Say Dialogue"
        text _("1. Fancy Text Toggled using {a=#:None}{color=#f00}(F){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("2. Text Effect Toggled using {a=#:None}{color=#f00}(E){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("3. Text Always Effect Toggled using {a=#:None}{color=#f00}(R){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("Credit to {a=https://github.com/yukinogatari/Ren-Py-FancyText}yukinogatari{/a} for the original Fancytext Module Modified by\n[gui.mod_dev] for newer Ren'Py Compatibility") xoffset 50 tooltip _("yukinogatari Github")
        text _("Custom Save Names")
        text _("1. Toggle Custom Savenames using {a=#:None}{color=#f00}(Shift+S){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("Hotkeys")
        text _("1. Toggle Choice Hotkeys using {a=#:None}{color=#f00}(C){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("2. Hotkeys on Choice Menus using {a=#:None}{color=#f00}(1-9 or NUM 1-9){/color}{/a}") xoffset 50 tooltip _("1-9 or NUM 1-9 on choice menus")
        text _("3. Hotkeys on Confirm using {a=#:None}{color=#f00}(Y/N){/color}{/a}") xoffset 50 tooltip _("Y/N on confirmation screens")
        text _("Notifications")
        text _("1. Toggle Notification Stack/Standard using {a=#:None}{color=#f00}(N){/color}{/a} or in preferences menu") xoffset 50 tooltip _("This can be toggled in the main menu or in the game")
        text _("Credit to {a=https://github.com/RenpyRemix/multi-notify}RenpyRemix{/a} for stackable notifications") xoffset 50 tooltip _("RenpyRemix Github")
        text _("Credit to {a=https://github.com/valery-iwanofu/renpy-shader-collection}valery-iwanofu{/a} for color picker") xoffset 50 tooltip _("valery-iwanofu Github")
        text ""
        if mod_updated[0] not in ["Mod up-to-date", "JSON Error", "Could Not Connect to Host", "HTTP Error", "Timeout", "Request Error", "None"]:
            text _("Latest MOD update available at {a=[gui.mod_update_url]}[gui.mod_dev]{/a}") tooltip _("Mod Developer")
        text _("If you like what I do consider {a=[gui.donate_mod]}Buying me a beer{/a}") tooltip _("Mod Developer BuyMeACoffee Page")
        text _("And lastly {a=[gui.developer_support]}[gui.developer_name]{/a} for developing [config.name!t]") tooltip _("Developer Patreon")

    screen confirm(message, yes_action, no_action):

        ## Ensure other screens do not get input while this screen is displayed.
        modal True

        zorder 200

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150

                    textbutton (_("Yes") if not persistent._choice_hotkeys else _("(Y)es")) action yes_action
                    textbutton (_("No") if not persistent._choice_hotkeys else _("(N)o")) action no_action

        ## Right-click and escape answer "no".
        key "game_menu" action no_action
        if persistent._choice_hotkeys:
            key "K_y" action yes_action
            key "K_n" action no_action

    screen game_menu(title, scroll=None, yinitial=0.0):

        style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        frame:
            style "game_menu_outer_frame"

            hbox:

                ## Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            transclude

                    else:

                        transclude

        use navigation

        imagebutton:
            pos (50, 900)
            idle "gui/overlay/main_menu_button_return_idle.png"
            hover "gui/overlay/main_menu_button_return_hover.png"
            if title.lower() == _("Walkthrough Colors").lower():
                action Hide("color_picker_wt", transition=dissolve)
            elif title.lower() == _("Music Player Settings").lower():
                action Hide("color_picker_mr", transition=dissolve)
            else:
                action Return()

        label title.upper()

        if main_menu:
            key "game_menu":
                if title.lower() == _("Walkthrough Colors").lower():
                    action Hide("color_picker_wt", transition=dissolve)
                elif title.lower() == _("Music Player Settings").lower():
                    action Hide("color_picker_mr", transition=dissolve)
                else:
                    action ShowMenu("main_menu")
        else:
            key "game_menu":
                if title.lower() == _("Walkthrough Colors").lower():
                    action Hide("color_picker_wt", transition=dissolve)
                elif title.lower() == _("Music Player Settings").lower():
                    action Hide("color_picker_mr", transition=dissolve)
                else:
                    action Return()

    screen preferences():

        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):

            vbox:

                hbox:
                    box_wrap True

                    if renpy.variant("pc") or renpy.variant("web"):

                        vbox:
                            style_prefix "radio"
                            label _("Display\n[jg_s]")
                            textbutton _("Window"):
                                action Preference("display", "window")
                            textbutton _("Fullscreen"):
                                action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "check"
                        label _("Skip\n[jg_s]")
                        textbutton _("Unseen Text"):
                            action Preference("skip", "toggle")
                        textbutton _("After Choices"):
                            action Preference("after choices", "toggle")
                        textbutton _("Transitions"):
                            action InvertSelected(Preference("transitions", "toggle"))

                    vbox:
                        style_prefix "check"
                        label _("Textbox\n[jg_s]")
                        textbutton _("Side Images"):
                            action ToggleVariable("persistent.SideImages")
                        textbutton _("Hidden"):
                            action ToggleVariable("persistent.TextBoxHidden")
                        if persistent.TextBoxHidden == False:
                            textbutton _("Visible"):
                                action ToggleVariable("persistent.TextBoxVisible")

                    vbox:
                        style_prefix "check"
                        label _("Language\n[jg_s]")
                        textbutton "English":
                            action Language(None)
                        textbutton "Español":
                            action Language("Spanish")
                        textbutton "Deutsch":
                            action Language("German")
                        textbutton "{font=gui/Fonts/SourceHanSans.otf}简体中文{/font}":
                            action Language("chinese")

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Fancy Text\n[jg_s](Shift+F)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_fancy_text", True),SetField(preferences, "text_cps", 120)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_fancy_text", False),SetField(preferences, "text_cps", 0)

                    vbox:
                        style_prefix "check"
                        label _("Savename\n[jg_s](Shift+S)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_custom_savename", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_custom_savename", False)
                    
                    vbox:
                        style_prefix "check"
                        label _("Notifications\n[jg_s](N)")
                        textbutton _("{size=-10}%s{/size}"%("Notification Stack" if persistent._notify_custom else "Notification Standard")):
                            action ToggleField(persistent, "_notify_custom")

                    vbox:
                        style_prefix "check"
                        label _("Support Mod\n[jg_s]{}".format("On" if persistent._support_mod_display else "Off"))
                        textbutton _("On"):
                            action SetField(persistent, "_support_mod_display", True)
                        textbutton _("Off"):
                            action SetField(persistent, "_support_mod_display", False)

                null height (4 * gui.pref_spacing)

                if persistent._fancy_text:
                    hbox:
                        box_wrap True
                        
                        vbox:
                            style_prefix "check"
                            label _("Effect\n[jg_s](E)")
                            textbutton _("[persistent._slow_effect_title]"):
                                action SlowEffectChange(True)

                        vbox:
                            style_prefix "check"
                            label _("Always Effect\n[jg_s](R)")
                            textbutton _("[persistent._always_effect_title]"):
                                action AlwaysEffectChange(True)

                        vbox:
                            style_prefix "slider"
                            label _("Effect Delay:\n[jg_s]%s Seconds"%EffectDelayDisplay())

                            bar:
                                value FieldValue(persistent, "_effect_delay",
                                    range=1.0,
                                    style="slider",
                                    max_is_zero=False,
                                    step=.1,
                                    force_step=True)

                            textbutton _("Default"):
                                action SetField(persistent, "_effect_delay", 0.2)

                    null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Walkthrough\n[jg_s](W)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_walkthrough", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_walkthrough", False)
                    if persistent._walkthrough:
                        vbox:
                            style_prefix "check"
                            label _("Choice Hints\n[jg_s](Shift+T)")
                            textbutton _("Enabled"):
                                action SetField(persistent, "_choice_tooltips", True)
                            textbutton _("Disabled"):
                                action SetField(persistent, "_choice_tooltips", False)
                        vbox:
                            style_prefix "check"
                            label _("Adjust WT Colors\n[jg_s]")
                            textbutton _("Change") action Show("color_picker_wt", transition=dissolve)
                    vbox:
                        style_prefix "check"
                        label _("Choice Hotkeys\n[jg_s](C)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_choice_hotkeys", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_choice_hotkeys", False)

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    
                    if JGSLoadable("music_room") and JGSLoadable("music_room_screen"):
                        vbox:
                            style_prefix "check"
                            label _("Music Overlay\n[jg_s]{}".format("On" if persistent._music_overlay else "Off"))
                            textbutton _("On"):
                                action SetField(persistent, "_music_overlay", True)
                            textbutton _("Off"):
                                action SetField(persistent, "_music_overlay", False)
                    
                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True
                    vbox:
                        label _("Text Speed:\n[jg_s]%s"%TextSpeed())

                        bar:
                            value Preference("text speed")

                        label _("Auto-Forward Time:\n[jg_s]%s"%AutoForwardTime())

                        bar:
                            value Preference("auto-forward time")

                    vbox:

                        if config.has_music:
                            label _("Music Volume:\n[jg_s]%s"%VolumeDisplay('music'))

                            hbox:
                                bar:
                                    value Preference("music volume")

                        if config.has_sound:

                            label _("Sound Volume:\n[jg_s]%s"%VolumeDisplay('sfx'))

                            hbox:
                                bar:
                                    value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test"):
                                        action Play("sound", config.sample_sound)

                        if config.has_voice:
                            label _("Voice Volume:\n[jg_s]%s"%VolumeDisplay('voice'))

                            hbox:
                                bar:
                                    value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test"):
                                        action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

    screen color_picker_wt():
        default activate = False
        default option = ""
        default field = ""
        use game_menu(_("Walkthrough Colors")):
            vbox:
                hbox:#Good Choice
                    spacing 15
                    vbox:
                        textbutton _("Good Choice Color"):
                            
                            action If(option == "_good_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_good_choice_color"), SetScreenVariable("field", "_good_choice_color")])
                            text_color persistent._good_choice_color
                            text_hover_color adjust_brightness(persistent._good_choice_color, -50)
                    vbox:
                        textbutton _("Reset"):
                            action SetField(persistent, "_good_choice_color", persistent._default_good_choice_color) 
                            sensitive persistent._good_choice_color != persistent._default_good_choice_color
                hbox:#Bad Choice
                    spacing 15
                    vbox:
                        textbutton _("Bad Choice Color"):
                            action If(option == "_bad_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_bad_choice_color"), SetScreenVariable("field", "_bad_choice_color")])
                            text_color persistent._bad_choice_color
                            text_hover_color adjust_brightness(persistent._bad_choice_color, -50)
                    vbox:
                        textbutton _("Reset"):
                            action SetField(persistent, "_bad_choice_color", persistent._default_bad_choice_color) 
                            sensitive persistent._bad_choice_color != persistent._default_bad_choice_color
                hbox:#Recommended Choice
                    spacing 15
                    vbox:
                        textbutton _("Recommended Choice Color"):
                            action If(option == "_recommended_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")],  
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_recommended_choice_color"), SetScreenVariable("field", "_recommended_choice_color")])
                            text_color persistent._recommended_choice_color
                            text_hover_color adjust_brightness(persistent._recommended_choice_color, -50)
                    vbox:
                        textbutton _("Reset"):
                            action SetField(persistent, "_recommended_choice_color", persistent._default_recommended_choice_color) 
                            sensitive persistent._recommended_choice_color != persistent._default_recommended_choice_color
                hbox:#Best Choice
                    spacing 15
                    vbox:
                        textbutton _("Best Choice Color"):
                            action If(option == "_best_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_best_choice_color"), SetScreenVariable("field", "_best_choice_color")])
                            text_color persistent._best_choice_color
                            text_hover_color adjust_brightness(persistent._best_choice_color, -50)
                    vbox:
                        textbutton _("Reset"):
                            action SetField(persistent, "_best_choice_color", persistent._default_best_choice_color) 
                            sensitive persistent._best_choice_color != persistent._default_best_choice_color
                hbox:#Dealers Choice
                    spacing 15
                    vbox:
                        textbutton _("Dealers Choice Color"):
                            action If(option == "_dealers_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_dealers_choice_color"), SetScreenVariable("field", "_dealers_choice_color")])
                            text_color persistent._dealers_choice_color
                            text_hover_color adjust_brightness(persistent._dealers_choice_color, -50)
                    vbox:
                        textbutton _("Reset"):
                            action SetField(persistent, "_dealers_choice_color", persistent._default_dealers_choice_color) 
                            sensitive persistent._dealers_choice_color != persistent._default_dealers_choice_color

            if activate:
                use color_picker(FieldSimpleValue(persistent,option), field)

    screen quick_menu():
        zorder 100

        if quick_menu:
            if persistent.TextBoxVisible and persistent.TextBoxHidden == False:
                add "gui/textbox.png"
            if persistent.TextBoxHidden == False:
                if persistent.TextBoxVisible:
                    vbox:
                        if persistent.SideImages:
                            xalign .01
                        else:
                            xalign .12
                        yalign .97
                        spacing 1
                        use quick_menu_buttons
                    if not _in_replay:
                        imagebutton:
                            idle "gui/tb_memory_idle.png"
                            hover "gui/tb_memory_hover.png"
                            action Show("memory")
                            xalign .88
                            yalign .97
                else:
                    vbox:
                        xalign .01
                        yalign .97
                        spacing 1
                        use quick_menu_buttons("_02")
                    if not _in_replay:
                        imagebutton:
                            idle "gui/tb_memory_idle_02.png"
                            hover "gui/tb_memory_hover.png"
                            action Show("memory")
                            xalign .99
                            yalign .97

    screen quick_menu_buttons(def_qm=""):
        if persistent._quickmenu_rollback:
            imagebutton:
                idle "gui/tb_back_idle{}.png".format(def_qm)
                hover "gui/tb_back_hover.png"
                action Rollback()
        if persistent._quickmenu_skip:
            imagebutton:
                idle "gui/tb_skip_idle{}.png".format(def_qm)
                hover "gui/tb_skip_hover.png"
                action Skip() alternate Skip(fast=True, confirm=True)
        if persistent._quickmenu_auto:
            imagebutton:
                idle "gui/tb_auto_idle{}.png".format(def_qm)
                hover "gui/tb_auto_hover.png"
                action Preference("auto-forward", "toggle")
        if not _in_replay:
            if persistent._quickmenu_save:
                imagebutton:
                    idle "gui/tb_save_idle{}.png".format(def_qm)
                    hover "gui/tb_save_hover.png"
                    action ShowMenu('save')
        else:
            if persistent._quickmenu_end_replay:
                imagebutton:
                    idle "mod/images/tb_replay_idle{}.png".format(def_qm)
                    hover "mod/images/tb_replay_hover.png"
                    action EndReplay(confirm=True)
        
        if persistent._quickmenu_hide:
            imagebutton:
                idle "mod/images/tb_hide_idle{}.png".format(def_qm)
                hover "mod/images/tb_hide_hover.png"
                action Function(switch_Textbox_visibility)
        if not _in_replay:
            if persistent._quickmenu_qsave:
                imagebutton:
                    idle "gui/tb_qsave_idle{}.png".format(def_qm)
                    hover "gui/tb_qsave_hover.png"
                    action QuickSave()
            if persistent._quickmenu_qload:
                imagebutton:
                    idle "gui/tb_qload_idle{}.png".format(def_qm)
                    hover "gui/tb_qload_hover.png"
                    action QuickLoad()
        if persistent._quickmenu_prefs:
            imagebutton:
                idle "gui/tb_pref_idle{}.png".format(def_qm)
                hover "gui/tb_pref_hover.png"
                action ShowMenu('preferences')

    default persistent._quickmenu_rollback = True
    default persistent._quickmenu_skip = True
    default persistent._quickmenu_auto = True
    default persistent._quickmenu_save = True
    default persistent._quickmenu_hide = True
    default persistent._quickmenu_qsave = True
    default persistent._quickmenu_qload = True
    default persistent._quickmenu_prefs = True
    default persistent._quickmenu_end_replay = True

    transform choice_Q():
        easein .5 alpha 0.0
        pause .25
        easein .5 alpha 1.0
        repeat 4

    screen choice(items):
        $ tooltip = GetTooltip()
        style_prefix "choice"

        default walkthrough = ""
        default hint = ""
        default shown = True
        default animate = True

        timer 6 action SetLocalVariable("shown", False),SetLocalVariable("animate", False),With(dissolve)

        default operators = {
            "<=" : operator.le,   # less than or equal to
            "<"  : operator.lt,   # less than
            ">"  : operator.gt,   # greater than
            ">=" : operator.ge,   # greater than or equal to
            "==" : operator.eq,   # equal tom
            "!=" : operator.ne,   # not equal
            }
        mousearea:
            align 0.0, 0.0
            xysize (50,50)
            hovered SetLocalVariable("shown", True),With(dissolve)
            unhovered SetLocalVariable("shown", False),With(dissolve)
        if shown:
            textbutton "?":
                if animate:
                    at choice_Q 
                action NullAction() 
                tooltip wt_choice_tooltip
                style "_default"
                text_style "_default"
                text_size 50
                text_outlines [(2, "#0009", 1, 1)]
                text_color "#FFFFFFA3"

        vbox:
            for count, i in enumerate(items, 1):
                $ _choice_wt = ""
                $ _choice_hint = ""
                $ _choice_color = gui.text_color
                $ _choice_size = gui.text_size
                if renpy.loadable("mod/walkthrough.rpy"):
                    $ _choices = WalkthroughData(renpy.get_filename_line(), i.caption)
                    if _choices != (None, None, None, None):
                        $ _choice_wt, _choice_hint, _choice_color, _choice_size = _choices

                if isinstance(_choice_wt, dict):
                    $ var_wt = getattr(store, _choice_wt.get("var"))
                    $ op_wt = operators.get(_choice_wt.get("operator"))
                    $ com_wt = _choice_wt.get("value")
                    $ disp_wt = op_wt(var_wt, com_wt)
                    $ walkthrough = _choice_wt.get('msg') if disp_wt else _choice_wt.get('alt_msg')
                elif isinstance(_choice_wt, list):
                    $ walkthrough = custom_join(_choice_wt, " ")
                elif isinstance(_choice_wt, str):
                    $ walkthrough = _choice_wt

                if isinstance(_choice_hint, dict):
                    $ var_hint = getattr(store, _choice_hint.get("var"))
                    $ op_hint = operators.get(_choice_hint.get("operator"))
                    $ com_hint = _choice_hint.get("value")
                    $ disp_hint = op_hint(var_hint, com_hint)
                    if isinstance(_choice_hint.get('msg'), list):
                        $ _hint = custom_join(_choice_hint.get('msg'))
                    elif isinstance(_choice_hint.get('msg'), str):
                        $ _hint = _choice_hint.get('msg')
                    if isinstance(_choice_hint.get('alt_msg'), list):
                        $ _hint_alt = custom_join(_choice_hint.get('alt_msg'))
                    elif isinstance(_choice_hint.get('alt_msg'), str):
                        $ _hint_alt = _choice_hint.get('alt_msg')
                    $ hint = _hint if disp_hint else _hint_alt
                elif isinstance(_choice_hint, list):
                    $ hint = custom_join(_choice_hint)
                elif isinstance(_choice_hint, str):
                    $ hint = _choice_hint

                $ number = "{size=-5}{alpha=.5}%s{/alpha}{/size}. "%(count % 10) if count < 10 and persistent._choice_hotkeys else ''
                $ wt_data = " {b}{size=[_choice_size]}{color=[_choice_color]}%s{/color}{/size}{/b}"%(walkthrough) if persistent._walkthrough else ""
                $ output = "{}{}{}".format(number, i.caption, wt_data)

                textbutton output:
                    action i.action
                    text_color _choice_color
                    if hint and persistent._walkthrough and persistent._choice_tooltips:
                        tooltip "{}".format(hint)
                    xminimum 1800
                        

                key "K_{}".format(count) action (i.action if persistent._choice_hotkeys else NullAction())
                key "K_KP_{}".format(count) action (i.action if persistent._choice_hotkeys else NullAction())

        vbox:
            spacing 42
            xpos 410
            yoffset -15
            for i in items:
                $ sex  = i.kwargs.get("sex", False)
                $ info = i.kwargs.get("info", False)
                if sex:
                    imagebutton:
                        idle "images/screens/heart.png"
                        hovered Show("displayTextMenuIconSex")
                        unhovered Hide("displayTextMenuIconSex")
                        action NullAction()

                elif info:
                    imagebutton:
                        idle "images/screens/book.png"
                        hovered Show("displayTextMenuIconInfo")
                        unhovered Hide("displayTextMenuIconInfo")
                        action NullAction()

                else:
                    imagebutton:
                        idle "images/screens/Null_icon.png"
        if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    at choice_appear(.5)
                    style_prefix "tooltip"
                    hbox:
                            text tooltip

    transform choice_appear(t=1):
        alpha 0.0
        easein t alpha 1.0

    screen input(prompt):
        zorder 101
        style_prefix "input"

        window:
            background Transform(style.window.background, alpha=persistent.say_window_alpha)

            has vbox:
                xalign gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos

            text prompt:
                style "input_prompt"
                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]
                at input_appear(.5)

            input id "input" at input_appear(.5):
                length 50 
                if gui.use_custom_caret:
                    caret "custom_caret"

            vbox:
                style_prefix "input_hint"
                textbutton _("Confirm %s")%(u"{font=DejaVuSans.ttf}\u23CE{/font}"):
                    at input_appear(.5)
                    action GetText("input","input"),With(dissolve)

        key "input_enter" action GetText("input","input"),With(dissolve)

    screen file_slots(title):

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
        default savename = VariableInputValue('save_name', False)
        default the_page = VariableInputValue("_go_to_page", False)

        use game_menu(title):

            fixed:
                if persistent._custom_savename:
                    if title.lower() == _("save") and not page_name_value.get_page() in ["auto", "quick"]:
                        button:
                            ypos gui.mod_savename_input_ypos
                            xpos gui.mod_savename_input_xpos
                            style "page_label"

                            key_events True
                            action savename.Toggle()

                            input:
                                id "input"
                                length 26
                                size gui.mod_savename_input_size
                                prefix _("Enter A Save Name: ")
                                value savename
                                if gui.use_custom_caret:
                                    caret "custom_caret_2"
                                style "page_label_text"

                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                button:
                    ypos gui.mod_save_page_input_ypos
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value
                        if gui.use_custom_caret:
                            caret "custom_caret"

                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            vbox:

                                add FileScreenshot(slot) xalign 0.5 yalign 0.5 #xysize WideRatio(config.thumbnail_width)

                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"

                                text FileSaveName(slot):
                                    style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
                            if FileLoadable(slot):
                                textbutton _("X"):
                                    action FileDelete(slot)
                                    align (1.0,0.0)
                                    style_prefix "file_slots_delete"

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<"):
                        action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q"):
                            action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]":
                            action FilePage(page)

                    textbutton _(">"):
                        action FilePageNext()

        button:

            key_events True
            xalign 1.0
            action the_page.Toggle()
            hbox:
                
                xsize gui.mod_save_goto_page_xsize
                ysize gui.mod_save_goto_page_ysize
                input:
                    style "page_label_text"
                    align (0.0, 0.5)
                    prefix _("Go To Page: ")
                    allow [str(i) for i in range(0,10)]
                    if gui.use_custom_caret:
                        caret "custom_caret"
                    length 3
                    value the_page
                textbutton _("Go"):
                    text_style "page_label_text"
                    align (1.0,0.5)
                    if _go_to_page.isdigit():
                        action FilePage(int(_go_to_page)),SetVariable("_go_to_page",""),the_page.Disable()

                if _go_to_page.isdigit():
                    key "input_enter" action FilePage(int(_go_to_page)),SetVariable("_go_to_page",""),the_page.Disable()

    transform input_appear(t=1):
        alpha 0.0
        easein t alpha 1.0

    screen callstack():
        if not jgs_develop:
            timer .1 action Hide("callstack")
        $ current_line = renpy.get_filename_line()
        $ callstack = renpy.get_return_stack()
        $ mode = renpy.get_mode()
        vbox:
            ypos 50
            text _("Current Line: [current_line!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
            text _("Mode: [mode]") outlines [(2, "#0009", 1, 1)] color "#0F0"
            if callstack:
                text _("CallStack: [callstack!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
                textbutton _("Clear Stack") action Function(renpy.set_return_stack, [])

    screen tooltip(tooltip, **kwargs):
        $ f_align = kwargs.get("align", (0.5, 0.05))
        if isinstance(tooltip, str):
            pass
        elif isinstance(tooltip, list):
            $ tooltip = "\n".join(tooltip)
        if tooltip:
            frame:
                at choice_appear(.5)
                align f_align
                style_prefix "tooltip"
                hbox:
                    text tooltip size gui.text_size

    screen notify_item(msg, use_atl=True):
        zorder 1500
        tag notify_item

        style_prefix "notify_item"

        frame:

            if use_atl: # ATL not used for history

                at custom_notify_appear

            text msg text_align 0.5

    screen notify_container():
        zorder 1000
        tag notify_container
        fixed:
            align (0.5, (0.05 if persistent._quick_menu_layout == "top_center" else 0.0))
            #pos (5, 50)

            vbox:
                xalign 0.5
                yalign (0.05 if persistent._quick_menu_layout == "top_center" else 0.02)
                #xmaximum 250
                spacing 5

                # We index on the time the notification was added as that
                # is unique. Using index helps manage the ATL nicely
                if notify_messages:
                    for msg_info index msg_info[1] in reversed(notify_messages):
                        if msg_info[1] > time.time() - notify_duration:
                            use notify_item(msg_info[0])

    transform custom_notify_appear():
        xalign 0.5
        #ypos (10 if persistent._quick_menu_layout == "top_center" else 0)

        yoffset -15.0 yzoom 0.0 zoom 0.7 alpha 0.5

        easein 1.0 yoffset 0.0 yzoom 1.0 zoom 1.0 alpha 1.0

        pause 2.0

        easeout 1.0 yoffset -15.0 yzoom 0.0 zoom 0.1 alpha 0.0

        pause .5

        function finish_notify

    screen start_buttons():

        vbox:
            pos (35, 880)
            text _("Do you want to Uncensor the background?"):
                size 25
                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

            text _("Check this game out on Steam and add it to your wishlist."):
                size 25
                outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

        textbutton _("{b}A Foreign World - Steam{/b}"):
            pos (50, 950)
            text_size 50
            action OpenURL("https://store.steampowered.com/app/2174320"), Jump("start_02")
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]



        textbutton _("{b}Continue{/b}"):
            pos (1600, 950)
            text_size 50
            action Hide("start_buttons"), Return()
            text_outlines [ (absolute(2), "#0d0d0d", absolute(1), absolute(1)) ]

        key "dismiss" action Hide("start_buttons"), Return()
