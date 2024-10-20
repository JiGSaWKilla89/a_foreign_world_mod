default persistent._good_choice_color = "#0F0"
default persistent._default_good_choice_color = "#0F0"

default persistent._bad_choice_color = "#F00"
default persistent._default_bad_choice_color = "#F00"

default persistent._recommended_choice_color = "#FF0"
default persistent._default_recommended_choice_color = "#FF0"

default persistent._best_choice_color = "#00F"
default persistent._default_best_choice_color = "#00F"

default persistent._dealers_choice_color = "#F0F"
default persistent._default_dealers_choice_color = "#F0F"

init 1000 python:
    """
    Within this script is all the functions necessary to list, 
    extract and compare files.
    The main function here is the walthrough_dict' that returns the walkthrough data
    """
    import os

    use_archive_format = True
    
    def walkthrough_dict():
        green = persistent._good_choice_color
        blue = persistent._best_choice_color
        yellow = persistent._recommended_choice_color
        red = persistent._bad_choice_color
        pink = persistent._dealers_choice_color

        _dech = "{color=[persistent._dealers_choice_color]}Dealers Choice{/color}"
        _goch = "{color=[persistent._good_choice_color]}Good Choice{/color}"
        _bach = "{color=[persistent._bad_choice_color]}Bad Choice{/color}"
        _recc = "{color=[persistent._recommended_choice_color]}Recommended{/color}"
        _bech = "{color=[persistent._dealers_choice_color]}Best Choice{/color}"

        return {
            ('e1.rpyc', 651) : {
                "Allow your thoughts to wander" : {
                    "wt" : f"",
                    "hint" : [f"{_recc}"],
                    "color" : yellow
                    },
                },
            ('e1.rpyc', 2485) : {
                "Okay" : {
                    "wt" : f"",
                    "hint" : [f"{_recc}", "d1_esther_cuddle added to choices"],
                    "color" : yellow
                    },
                },
            ('e1.rpyc', 2539) : {
                "Let your mind wander" : {
                    "wt" : f"",
                    "hint" : [f"{_recc}"],
                    "color" : yellow
                    },
                },
            ('e1.rpyc', 2637) : {
                "Cum inside" : {
                    "wt" : f"",
                    "hint" : [f"{_dech}"],
                    "color" : pink
                    },
                "Pull out" : {
                    "wt" : f"",
                    "hint" : [f"{_dech}"],
                    "color" : pink
                    },
                },
            ('e1.rpyc', 4947) : {
                "Let your dark thoughts take over" : {
                    "wt" : "",
                    "hint" : [f"{_recc}"],
                    "color" : yellow
                    },
                },

            ('e2.rpyc', 423) : {
                "Keep your explanation short" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d3_drive_01_short added to choices", "Less reading"],
                    "color" : pink
                    },
                "Explain yourself in detail" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d3_drive_01_long added to choices", "More reading for the reader"],
                    "color" : pink
                    },
                },
            ('e2.rpyc', 655) : {
                "Try to stay and watch" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d3_bra_stay added to choices"],
                    "color" : pink
                    },
                "Excuse yourself" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d3_bra_leave added to choices"],
                    "color" : pink
                    },
                },
            ('e2.rpyc', 809) : {
                "Leave the room and close the door behind you" : {
                    "wt" : f"",
                    "hint" : ["d3_bath_leave_01 added to choices"],
                    },
                "Enter the room" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d3_bath_go_in_01 added to choices"],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 815) : {
                "Explain things through the door" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d3_bath_leave_through added to choices"],
                    "color" : pink
                    },
                "Go back inside and explain things" : {
                    "wt" : "",
                    "hint" : [f"{_dech} {_recc}", "d3_bath_leave_back added to choices"],
                    "color" : pink
                    },
                "Let [Cecilia] deal with it" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d3_bath_leave_cecilia added to choices"],
                    "color" : pink
                    },
                },
            ('e2.rpyc', 849) : {
                "I'm sure" : {
                    "wt" : f"",
                    "hint" : ["d3_bath_through_01 added to choices"],
                    },
                "Fuck it" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d3_bath_through_02 added to choices"],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 922) : {
                "Tell her to turn around" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d3_bath_2b_turn added to choices"],
                    "color" : yellow
                    },
                "No, let's get this over with" : {
                    "wt" : f"",
                    "hint" : [],
                    },
                },
            ('e2.rpyc', 1110) : {
                "Stay and listen" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", 
                        "d3_lucy_listen added to choices", 
                        "oldman_heard added to memories",
                        "d3_lucy_listen added to memories"
                        ],
                    "color" : yellow
                    },
                "Interrupt them" : {
                    "wt" : f"",
                    "hint" : ["d3_lucy_interrupt added to choices"],
                    },
                },
            ('e2.rpyc', 1464) : {
                "Pretend you didn't notice" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                "Say something" : {
                    "wt" : f"",
                    "hint" : [],
                    },
                },
            ('e2.rpyc', 1471) : {
                "Let her continue" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                "Confront her" : {
                    "wt" : f"",
                    "hint" : [],
                    },
                },
            ('e2.rpyc', 1485) : {
                "That's it" : {
                    "wt" : f"",
                    "hint" : [],
                    },
                "Let her continue" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 1501) : {
                "Okay" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 1557) : {
                "Let her continue" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 1600) : {
                "Let her do her thing" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 1644) : {
                "Think about what could have been" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 1877) : {
                "Ask her what she was about to say" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 1973) : {
                "Give in and kiss her" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d4_sue_kiss added to choices"],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 2175) : {
                "Ask her about abilities" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d4_training_detail added to choices", "oldman_heard added to memories"],
                    "color" : yellow
                    },
                "Ask her for a short summary" : {
                    "wt" : f"",
                    "hint" : ["oldman_heard added to memories"],
                    },
                },
            ('e2.rpyc', 2886) : {
                "Tell me" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d4_amber_tell_me added to choices"],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 2973) : {
                "Discuss things in detail" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d4_discussion_detail added to choices"],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 3862) : {
                "Let her do her thing" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d4_sue_sex added to choices"],
                    "color" : yellow
                    },
                },
            ('e2.rpyc', 4170) : {
                "Let your mind wander" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },

            ('e3.rpyc', 255) : {
                "Teach her about finishing what she starts" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                "Ask her to stop" : {
                    "wt" : f"",
                    "hint" : ["d5_sue_nocum added to choices"],
                    },
                },
            ('e3.rpyc', 274) : {
                "This is so hot" : {
                    "wt" : f"",
                    "hint" : ["d5_sue_handjob added to choices"],
                    },
                "This won't cut it" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d5_sue_sex added to memories"],
                    "color" : yellow
                    },
                },
            ('e3.rpyc', 551) : {
                "Tell [Tracy] to leave [Sue] in your bed" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d5_sue_mcs_bed added to choices"],
                    "color" : yellow
                    },
                },
            ('e3.rpyc', 1477) : {
                "Take your time" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d5_sauna_flirt added to choices"],
                    "color" : yellow
                    },
                },
            ('e3.rpyc', 2018) : {
                "Leave" : {
                    "wt" : f"",
                    "hint" : ["d6_tracy_leave_01 added to choices"],
                    },
                "Have some fun" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d6_tracy_leave_04 added to choices"],
                    "color" : yellow
                    },
                },
            ('e3.rpyc', 2032) : {
                "I changed my mind" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d6_tracy_leave_02 added to choices"],
                    "color" : yellow
                    },
                "No, just leave" : {
                    "wt" : "",
                    "hint" : ["d6_tracy_leave_03 added to choices", "d5_tracy_01 added to memories"],
                    },
                },
            ('e3.rpyc', 2191) : {
                "Allow yourself to live through an old memory" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e3.rpyc', 3442) : {
                "It's revealing" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d6_lucy_outfit_01 added to choices"],
                    "color" : pink
                    },
                "It suits her well" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d6_lucy_outfit_02 added to choices"],
                    "color" : pink
                    },
                "She looks beautiful" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d6_lucy_outfit_03 added to choices"],
                    "color" : pink
                    },
                },
            ('e3.rpyc', 3719) : {
                "Tell [Sue] she should let [Aurora] leave" : {
                    "wt" : f"",
                    "hint" : ["d6_hottub_01 added to choices"],
                    },
                "Tell [Aurora] that she can join you if she wants" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d6_hottub_02 added to choices"],
                    "color" : yellow
                    },
                },
            ('e3.rpyc', 3820) : {
                "Sounds good" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d6_sue_aurora_hottub_01 added to choices", "d6_aurora_hottub added to memories"],
                    "color" : yellow
                    },
                "Not my thing" : {
                    "wt" : f"",
                    "hint" : ["d6_sue_aurora_hottub_02 added to choices", "d6_aurora_hottub added to memories"],
                    },
                },
            ('e3.rpyc', 3949) : {
                "Go down the path of wishful thinking" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },

            ('e4.rpyc', 183) : {
                "Sure. It's going to be a long ride anyway" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e4.rpyc', 466) : {
                "Help her wash her hands" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e4.rpyc', 2566) : {
                "That won't be necessary" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d8_tracy_safe added to choices"],
                    "color" : pink
                    },
                "Let [Sue] create water chains" : {
                    "wt" : "",
                    "hint" : [f"{_dech} {_recc}", "d8_tracy_bondage added to choices"],
                    "color" : pink
                    },
                },
            ('e4.rpyc', 3102) : {
                "Sounds like a good idea" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d8_massage added to choices"],
                    "color" : yellow
                    },
                "Maybe another time" : {
                    "wt" : "",
                    "hint" : ["d8_no_massage added to choices"],
                    },
                },

            ('e5.rpyc', 441) : {
                "Go to the shower" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d9_tracy_sex added to choices"],
                    "color" : yellow
                    },
                "I shouldn't do this, especially today" : {
                    "wt" : "",
                    "hint" : ["d9_tracy_no_sex added to choices"],
                    },
                },
            ('e5.rpyc', 1052) : {
                "Try to relieve some stress with [Sue]" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d9_sue_sex added to choices"],
                    "color" : yellow
                    },
                },
            ('e5.rpyc', 1163) : {
                "Transition into doggy style" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", "d9_sue_sex_doggy added to choices", "d9_sue_sex added to memories"],
                    "color" : yellow
                    },
                },
            ('e5.rpyc', 2130) : {
                "I love you, but I want an open relationship" : {
                    "wt" : "",
                    "hint" : [f"{_recc}","d9_fiona_openRelationship added to choice"],
                    "color" : yellow
                    },
                "I'm sorry" : {
                    "wt" : "",
                    "hint" : ["d9_fiona_apology added to choices"],
                    },
                },
            ('e5.rpyc', 2217) : {
                "That's a trick question, right?" : {
                    "wt" : "",
                    "hint" : [f"{_recc}", ],
                    "color" : yellow
                    },
                },
            ('e5.rpyc', 3770) : {
                "[Tracy]" : {
                    "wt" : "",
                    "hint" : [f"{_dech} {_recc}", "d10_threesome_tracy added to choices"],
                    "color" : pink
                    },
                "Sue" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d10_threesome_sue added to choices"],
                    "color" : pink
                    },
                "Neither" : {
                    "wt" : "",
                    "hint" : [f"{_dech}", "d10_threesome_nobody added to choices"],
                    "color" : pink
                    },
                },
            
            ('game/mod/replays.rpy', 210) : {
                "Cum inside" : {
                    "wt" : f"",
                    "hint" : [f"{_dech}"],
                    "color" : pink
                    },
                "Pull out" : {
                    "wt" : f"",
                    "hint" : [f"{_dech}"],
                    "color" : pink
                    },
                },
            ('game/mod/replays.rpy', 779) : {
                "Teach her about finishing what she starts" : {
                    "wt" : "",
                    "hint" : [f"{_recc}"],
                    "color" : yellow
                    },
                },
            ('game/mod/replays.rpy', 798) : {
                "This won't cut it" : {
                    "wt" : "",
                    "hint" : [f"{_recc}"],
                    "color" : yellow
                    },
                },
            ('game/mod/replays.rpy', 1430) : {
                "Transition into doggy style" : {
                    "wt" : "",
                    "hint" : [f"{_recc}"],
                    "color" : yellow
                    },
                },
            }

    valid_dic_items = [#Changes Every Update
        ('e1.rpyc', 2485), ('e2.rpyc', 809), ('e2.rpyc', 922),
        ('e2.rpyc', 1464), ('e2.rpyc', 1557), ('e2.rpyc', 1471),
        ('e2.rpyc', 1501), ('e2.rpyc', 1485), ('e3.rpyc', 2018),
        ('e3.rpyc', 2032)
        ]

    e1_ignore_lines = [#Changes Every Update
        2486
        ]
    e2_ignore_lines = [#Changes Every Update
        923
        ]
    e3_ignore_lines = [#Changes Every Update
        2019
        ]
    e4_ignore_lines = [#Changes Every Update
        ]
    e5_ignore_lines = [#Changes Every Update
        7, 1602, 1605, 4859
        ]
    screens_ignore_lines = [#Changes Every Update
        319, 449, 480, 743, 809, 1806
        ]
 
    ignore_list = [
        ]

    end_list = [
        ".flac", ".mp3", ".ogg", "opus", ".wav", #Audio Extensions
        ".webm", ".avi", ".mp4", ".mkv", ".ogv", #Video Extensions
        ".webp", ".png", ".jpg", #Image Extensions
        #".rpyc", ".rpa", #Renpy Extensions
        ".ttf", ".otf", ".ttc", #Font Extensions
        ".txt", #Other Extensions
        ".save", "persistent", ".json",
        ]

    def read_rpy_file(file):
        try:
            with renpy.open_file(file, encoding="utf-8") as readfile:
                return readfile.readlines()
        except:
            with open(os.path.join(config.basedir, file), "r", encoding="utf-8") as readfile:
                return readfile.readlines()

    def check_dic(current_dictionary, scripts, use_precise=True):
        """
        Generate a dictionary from 'scripts' containing
        'short_key', 'name' and 'path'
        This grabs the full .rpy file while busy

        Iterate over 'generated_dictionary' and 'current_dictionary'
        to do comparisons of files and lines

        Uses two functions to find the menu lines to see if they match 'current_dictionary'

        Function 'find_closest_menu_before_name' uses a range checker to match where 
        menu is found and searches backwards using a distance checker (Precise Search)

        Function 'find_menu_before_name' uses a range checker to match where
        menu is found and searches backwards no distance (Fuzzy Search)

        Outputs data to 'walkthrough_check.txt' to make corrections and check

        """

        counter = 0
        generated_dictionary = {}

        def find_closest_menu_before_name(lines, name, r_count, out=False):
            closest_menu_line = None
            min_distance = float('inf')

            for i, line in enumerate(lines):
                line = line.replace("\\","")
                # Check if the name, including double quotes, is in the line
                if name in line:
                    # Check if this `name` line is after `r_count`
                    if i >= r_count:
                        # Search backwards from the current line to find the nearest `menu`
                        for j in range(i, -1, -1):
                            if 'menu' in lines[j]:
                                # Calculate distance from `r_count` to the found `menu`
                                distance = abs(r_count - j)
                                if distance < min_distance:
                                    if out:
                                        print(f"Found {name} in {line.strip()} at {i+1}")
                                    min_distance = distance
                                    closest_menu_line = j + 1  # Convert to 1-indexed
                                break  # Stop searching backwards once we find the closest menu
            return closest_menu_line

        def find_menu_before_name(lines, name, out=False):
            for i, line in enumerate(lines):
                if name in line:
                    # Search backwards from the current line
                    for j in range(i, -1, -1):
                        if 'menu' in lines[j]:
                            if out:
                                print(f"Found {name} in {line.strip()} at {i+1}")
                            # Return the line number (1-indexed)
                            return j + 1
            return None
        
        def output(line):
            p = os.path.join(config.basedir, "walkthrough_check.txt")
            with open(p, 'a') as file:
                print(line)
                file.write("{}\n".format(line))

        for short_key, name, path in scripts:
            generated_dictionary[short_key] = [name, read_rpy_file(path), path.replace("extracted_files/","")]

        # Iterate over the generated dictionary and the current walkthrough dictionary
        for key, value in generated_dictionary.items():
            for wt_key, wt_value in current_dictionary.items():
                r_count = wt_key[1]
                # Check if the name in value[0] is part of the current wt_key[0]
                if f"{value[0] if use_archive_format else f'game/{value[0]}'}" in wt_key[0]:
                    for name in wt_value:
                        # Find the closest menu line number
                        ln = find_closest_menu_before_name(value[1], f'"{name}"', r_count) #Precise Search
                        al = find_menu_before_name(value[1], f'"{name}"') #Fuzzy Search
                        # Create the tuple with the filename and the line number
                        if use_archive_format:
                            d = ("{}c".format(value[2]), ln) if use_precise else  ("{}c".format(value[2]), al) #Create the correct value .rpyc and line number
                        else:
                            d = ("game/{}".format(value[2]), ln) if use_precise else  ("game/{}".format(value[2]), al) #Create the correct value .rpyc and line number
                        # Print the result with the correct key and value
                        if wt_key != d and not wt_key in valid_dic_items:
                            counter += 1
                            output("Current: {}\nNew: {}\nLine: {}\nCould Be Mistaken For a Sub Menu\n".format(wt_key, d, name))
        return f"Total Items not matching correctly: {counter}"

    def filter_wt(fil):
        """

        'fil' needs to be the full path eg '"new scripts/Student Interaction.rpy"' or
        'script.rpy'

        It will match the lines from the file with the walkthrough dictionary
        """
       
        out = []

        for script, i in walkthrough_dict().keys():
            if fil in script:
                out.append(i)
       
        return out

    def get_rpyc_files(ignore_list=ignore_list, end_list=end_list):
        """
        
        This Function Gets all the files mainly '.rpy'
        files.
        
        Add files to ignore in 'ignore_list'
        
        Add extensions to ignore in 'end_list'

        """

        folder = os.path.join(config.gamedir, "extracted_files")
        if not os.path.exists(folder):
            os.mkdir(folder)

        for file in renpy.list_files():
            if file.startswith(("python-packages", "mod", "tl")):
                continue
            if not file in ignore_list:
                if file.endswith(".rpyc"):
                    chunk = b""
                    with renpy.file(file) as readfile:
                        with open(os.path.join(folder, file), "wb") as writefile:
                            while True:
                                chunk = readfile.read((2 ** 10))
                                if not chunk:
                                    break
                                writefile.write(chunk)

    def get_menu_lines(filename, ignore_lines):
        """
        This Function will find all the menu lines in the script
        
        Function will output data to 'menu_finder.txt' in the base
        game dir

        Uses external Function 'read_rpy_file' to open the files within
        the archives

        """
        def replacing(item):
            item = item.replace("extracted_files/", "")
            
            return item+("c" if use_archive_format else '')

        output_data = []
        data = read_rpy_file(filename)
        p = os.path.join(config.basedir, "menu_finder.txt")

        for i, line in enumerate(data, 1):
            if "menu:" in line and not i in ignore_lines:
                output_data.append((replacing(filename), i))
            elif "menu " in line and not i in ignore_lines:
                output_data.append((replacing(filename), i))
        if output_data:
            with open(p, "a") as file:
                for c, i in enumerate(output_data, 1):
                    file.write(f"{c} {str(i)}\n")
                file.write("\n")

    def update_check_walkthrough():
        """
        Use this to check if the lines match up after
        every update an get new menu items.

        Uses external function 'get_menu_lines'
        whilst checking to find current_lines using 'filter_wt' and ignore lists

        Uses external function 'check_dic'

        """
        folder = os.path.join(config.basedir, "extracted_files")
        files = os.listdir(folder)
        for f in files:
            if f.endswith(".rpyc"):
                try:
                    os.unlink(os.path.join(folder,f))
                except:
                    print("File Not Found")
        files = [i.replace(".rpy", "") for i in files if i.endswith(".rpy")]

        for i in files:
            try:
                data = eval(i+"_ignore_lines")
            except:
                data = []
            get_menu_lines(f"extracted_files/{i}.rpy", filter_wt(f"{i}")+data)
        check_dic(walkthrough_dict(),[(f"{i}", f"{i}", f"extracted_files/{i}.rpy") for i in files])

init -2000 python early:
    def clean_root():
        import shutil
        valid = [
            'AForeignWorld.exe', 
            'AForeignWorld.py', 
            'AForeignWorld.sh', 
            'errors.txt', 
            'extracted_files', 
            'game', 
            'lib', 
            'log.txt', 
            'menu_finder.txt', 
            'renpy', 
            'traceback.txt', 
            'walkthrough_check.txt',
            'UnRen-1.0.11d.bat']

        folder = os.path.join(config.gamedir, "extracted_files")
        new_folder = os.path.join(config.basedir, "extracted_files")

        files = os.listdir(config.basedir)
        
        for file in files:
            if file not in valid:
                try:
                    if os.path.isdir(os.path.join(config.basedir, file)):
                        shutil.rmtree(os.path.join(config.basedir, file))
                    else:
                        os.unlink(os.path.join(config.basedir, file))
                except Exception as e:
                    print(f"Error: {e}")

        try:
            shutil.move(folder, new_folder)
            print(f"Folder moved from {folder} to {new_folder}")
        except Exception as e:
            print(f"Error: {e}")
    clean_root()

#check_dic(walkthrough_dict(),[("sc", "script", "script.rpy")])


    """
    Run 'get_rpyc_files()' to get the rpyc files from archive

    Close game then run UNREN and option 2 make sure to put unren in root folder
    

    !!! IMPORTANT!!!
    Move the folder extracted_files in gamedir to the root_dir

    The run 'update_check_walkthrough()'
    """