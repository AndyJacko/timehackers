from time import sleep
import os

pause_time = 2
andy_alive = 1 
michal_alive = 1
lasharn_alive = 1
saihar_alive = 1

intro_txt = '''
              ::::::::::: ::::::::::: ::::    ::::  ::::::::::   
                  :+:         :+:     +:+:+: :+:+:+ :+:          
                  +:+         +:+     +:+ +:+:+ +:+ +:+          
                  +#+         +#+     +#+  +:+  +#+ +#++:++#     
                  +#+         +#+     +#+       +#+ +#+          
                  #+#         #+#     #+#       #+# #+#          
                  ###     ########### ###       ### ##########     
        
    :::    :::     :::      ::::::::  :::    ::: :::::::::: :::::::::   :::::::: 
    :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  :+:        :+:    :+: :+:    :+: 
    +:+    +:+  +:+   +:+  +:+        +:+  +:+   +:+        +:+    +:+ +:+
    +#++:++#++ +#++:++#++: +#+        +#++:++    +#++:++#   +#++:++#:  +#++:++#++ 
    +#+    +#+ +#+     +#+ +#+        +#+  +#+   +#+        +#+    +#+        +#+ 
    #+#    #+# #+#     #+# #+#    #+# #+#   #+#  #+#        #+#    #+# #+#    #+# 
    ###    ### ###     ###  ########  ###    ### ########## ###    ###  ########\n\n'''

room_1_txt = '''
    !xxxxxxxxxxxx       xxxx    xxx    xxx    xxxx    xxxx     xxxxxx!
    !      xxxxxxxxxxxx    xxxx   xxxx   xxx    xxx    xxxx     xxxxx!
    !              xxxxxxx   xxxx   xxx   xxx   xxxx   xxxx    xxxxx !
    ! xxxxxxxx          xxxx   xxx  xxx   xxx   xxx    xxxx    xxxx  !
    !xxxxxxxxxxxxxxx      xxxx   xx  xxx  xxx   xxx   xxxx    xxxx   !
    !x            xxxxxxx   xxx   xx  xx  xxx   xxx   xxxx   xxxx    !
    !                  xxxx   xxx  x  xx  xxx  xxx   xxx    xxxx    x!
    !xxxxxxxxxxxxxxxxx    xxxx  xx  x  x  xx  xxx   xxx   xxxxx    xx!
    !xxx            xxxxxx   xxx xx x  x  x  xx   xxx    xxxx    xxxx!
    !       xxxxxxx       xxx  xx x x xx x  xx  xxx    xxx    xxxxx  !
    !  xxxxxxxxx    xxxxxxxx  xx x x    x xx  xx   xxxx    xxxxx     !
    !xxxx         xxxx       xxx x x x x x xx  xxxx    xxxxx     xxxx!
    !---+------------------------------------------------------------!
    !.. |". /  /  /  /...............................................!
    !...|.-". /  /  /................................................!
    !.. | _.-". /  /.................................. .|  |.........!
    !...|"  _.-". / .......... /\  .-"""-.  /\  ...... ||  || .......!
    !.. |-""   _.-".......... //\\\\/  ,,,  \//\\\\ ...... \\\\()//........!
    !   |_.-"" .............. |/\| ,;;;;;, |/\| ........={}=. .......!
    !.. | ................... //\\\\\;-"""-;///\\\\ ....../ /`'\ \.......!
    ! ^.|.^" ............... //  \/   .   \/  \\\\ .....` \  / ' ......!
    !'^\+/^` .............. (| ,-_| \ | / |_-, |) .......`'..........!
    !'/`"'\` ................ //`__\.-.-./__`\\\\  ....................!
    ! ......  ...  ......... // /.-(() ())-.\ \\ ........../\\\\/\\\\\....!
    !......./\\\\_//\........ (\ |)   '---'   (| /) .......///"-'\\\\\...!
    !......// O O \\\\........ ` (|  ......   |) `  ...................!
    !x....//..`"'..\\\\......... \\) ........  (/ .....................x!
    !x................................................ /\('')/\.....x!
    !x................................................ \ .... / ....x!
    !----------------------------------------------------------------!\n\n'''

room_2_txt = '''
    !xxxxxxxxxxxx       xxxx    xxx    xxx    xxxx    xxxx     xxxxxx!
    !      xxxxxxxxxxxx    xxxx   xxxx   xxx    xxx    xxxx     xxxxx!
    !              xxxxxxx   xxxx   xxx   xxx   xxxx   xxxx    xxxxx !
    ! xxxxxxxx          xxxx   xxx  xxx   xxx   xxx    xxxx    xxxx  !
    !xxxxxxxxxxxxxxx      xxxx   xx  xxx  xxx   xxx   xxxx    xxxx   !
    !x            xxxxxxx   xxx   xx  xx  xxx   xxx   xxxx   xxxx    !
    !                  xxxx   xxx  x  xx  xxx  xxx   xxx    xxxx    x!
    !xxxxxxxxxxxxxxxxx    xxxx  xx  x  x  xx  xxx   xxx   xxxxx    xx!
    !xxx            xxxxxx   xxx xx x  x  x  xx   xxx    xxxx    xxxx!
    !       xxxxxxx       xxx  xx x x xx x  xx  xxx    xxx    xxxxx  !
    !  xxxxxxxxx    xxxxxxxx  xx x x    x xx  xx   xxxx    xxxxx     !
    !xxxx         xxxx       xxx x x x x x xx  xxxx    xxxxx     xxxx! 
    !---------x======================================x---------------!
    !.........|        \                    /        |...............!
    !.........| (^)_____\__________________/_____(^) |... [ENTER] ...!
    !.........|          \                /          |... [ PSW ] ...!
    !.........|           +--------------+           |...............!
    !.........|           |              |           |...  [ x ]  ...!
    !.........| (^)_______|____+====+____|_______(^) |...  [ x ]  ...!
    !.........|           |    |....| x  |           |...  [ x ]  ...!
    !.........|           |    |....|    |           |...  [ x ]  ...!
    !.........|           |    |....|    |           |...............!
    !.........| (^)_______/_-_-_-_-_-_-_-\_______(^) |...............!
    !.........|        /./                \.\        |...............!
    !.........|       /./  What year did   \.\       |...............!
    !.........|      /./    Kurt Cobain     \.\      |...............!
    !x........| (^)_/_/_________Die?_________\_\_(^) |..............x!
    !x........|    /./                        \.\    |..............x!
    !x........|___/./       GOOGLE KNOWS       \.\___|..............x!
    !----------------------------------------------------------------!\n\n'''

room_3_txt = '''
    !xxxxxxxxxxxx       xxxx    xxx    xxx    xxxx    xxxx     xxxxxx!
    !      xxxxxxxxxxxx    xxxx   xxxx   xxx    xxx    xxxx     xxxxx!
    !              xxxxxxx   xxxx   xxx   xxx   xxxx   xxxx    xxxxx !
    ! xxxxxxxx          xxxx   xxx  xxx   xxx   xxx    xxxx    xxxx  !
    !xxxxxxxxxxxxxxx      xxxx   xx  xxx  xxx   xxx   xxxx    xxxx   !
    !x            xxxxxxx   xxx   xx  xx  xxx   xxx   xxxx   xxxx    !
    !                  xxxx   xxx  x  xx  xxx  xxx   xxx    xxxx    x!
    !xxxxxxxxxxxxxxxxx    xxxx  xx  x  x  xx  xxx   xxx   xxxxx    xx!
    !xxx            xxxxxx   xxx xx x  x  x  xx   xxx    xxxx    xxxx!
    !       xxxxxxx       xxx  xx x x xx x  xx  xxx    xxx    xxxxx  !
    !  xxxxxxxxx    xxxxxxxx  xx x x    x xx  xx   xxxx    xxxxx     !
    !xxxx         xxxx       xxx x x x x x xx  xxxx    xxxxx     xxxx!
    !................................................................!
    !.................<o)))><........................................!
    !...><(((o>..........................<o)))><.....................!
    !................................................................!
    !................................................................!
    !.......................,---,....................................!
    !.....................,-'    `--,................................!
    !..............( `-,'            `\..............................!
    !...............\           ,    o \..........><(((o>............!
    !.............../   ,       ;       \............................!
    !...><(((o>....(_,-' \       `, _  ""/...........................!
    !.................... `-,___ =='__,-'............................!
    !........................................<o)))><.................!
    !................................................................!
    !x..............................................................x!
    !x..............><(((o>.........................................x!
    !x...............................................<o)))><........x!
    !----------------------------------------------------------------!\n\n'''

room_4_txt = '''
    !xxxxxxxxxxxx       xxxx    xxx    xxx    xxxx    xxxx     xxxxxx!
    !      xxxxxxxxxxxx    xxxx   xxxx   xxx    xxx    xxxx     xxxxx!
    !              xxxxxxx   xxxx   xxx   xxx   xxxx   xxxx    xxxxx !
    ! xxxxxxxx          xxxx   xxx  xxx   xxx   xxx    xxxx    xxxx  !
    !xxxxxxxxxxxxxxx      xxxx   xx  xxx  xxx   xxx   xxxx    xxxx   !
    !x            xxxxxxx   xxx   xx  xx  xxx   xxx   xxxx   xxxx    !
    !                  xxxx   xxx  x  xx  xxx  xxx   xxx    xxxx    x!
    !xxxxxxxxxxxxxxxxx    xxxx  xx  x  x  xx  xxx   xxx   xxxxx    xx!
    !xxx            xxxxxx   xxx xx x  x  x  xx   xxx    xxxx    xxxx!
    !       xxxxxxx       xxx  xx x x xx x  xx  xxx    xxx    xxxxx  !
    !  xxxxxxxxx    xxxxxxxx  xx x x    x xx  xx   xxxx    xxxxx     !
    !xxxx         xxxx       xxx x x x x x xx  xxxx    xxxxx     xxxx!
    !................................................................!
    !...........................{ }..................................!
    !...)......................{ @ }..................)..............!
    !..(...(....(.........)...{ @@ }......)...........(..............!
    !..)..(..)...)...(...(...{ @@@  }......( ...(....(...(......(....!
    !...(..(..)...(..)....).{  @@@@  }.....)...)..(..)..(...)..(..)..!
    !...)..(......(.)...(.{    @@@@@  }.....(...)..)..)..)...)..)....!
    !....).(..)...(..)..){  @  @@@@@@  }...(....(..)..(...)..(..)....!
    !....(..)..).)..)...{  @@  @@@@@@@   }..)....)..)..)...)..)..)...!
    !...)..)....)....).{  @@@@@@@@@##@@@@  } (....)..)...)..)..).....!
    !xxxxx%%%%%%%%%%%%{   @@@@@#@@@#####@@@  }%%%%%%%%%%%%%%%xxxxxxxx!
    !xxxx%%%%%%%%%%%%%%%  @@@@@#@@########@@  %%%%%%%%%%%%%%%%%xxxxxx!
    !xxx%%%%%%%%%%%%%%%%%  @@@@@@#########@@  %%%%%%%%%%%%%%%%%%%%xxx!
    !xxx%%%%%%%%%%%%%%%%%   @@@@@##########@  %%%%%%%%%%%%%%%%%%%%xxx!
    !xx%%%%%%%%%%%%%%%%%%%%  @@@@@@#######@  %%%%%%%%%%%%%%%%%%%%%%xx!
    !xx%%%%%%%%%%%%%%%%%%%%%                %%%%%%%%%%%%%%%%%%%%%%%xx!
    !xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx!
    !----------------------------------------------------------------!\n\n'''   

time_machine_txt = '''
                                       oo   
                                      oooo
                                     oooooo
                                    oooooooo
                                   oooooooooo
                                  oooooooooooo  
                              xxxxxxxxxxxxxxxxxxx
                         xxxxxxxxxxxxxxxxxxxxxxxxxxxx
                      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                  xxxxxxxx                            xxxxxxxx
               xxxxxx          ................             xxxxxx
             xxxxxx              ............                 xxxxxxx
           xxxxx                   ........                      xxxxxx
         xxxxx       """"""          ....           """"""         xxxxx
        xxxxx         """"            ..             """"           xxxxx
       xxxxx           ""           ......            ""             xxxxx
       xxxxx          """"        ..........         """"            xxxxx
        xxxxx        """"""      ............       """"""          xxxxx
         xxxxx      oo/         ...............          \oo     xxxxxx
          xxxxx   ooo/                                    \ooo xxxxxxx 
           xxxxx ooo/--------------------------------------\ooo xxxx
               oooo/ ...   ...   ...   ...   ...  ...  ...  \oooo
             ooooo/------------------------------------------\ooooo 
            ooooo/ ...  ...   ...   ...   ...   ...  ...  ... \ooooo
           ooooo/...  ...   ...   ...  ...  ...   ...  .... ...\ooooo
          ooooo/------------------------------------------------\oooooo
         ooooo/__________________________________________________\oooooo
        oooooo|A|n|d|y|-|L|a|s|h|a|r|n|-|S|a|i|h|a|r|-|M|i|c|h|a|l\oooooo\n\n'''

spider_small_txt = '''                     
                                         /\\\\_//\\
                                        // O O \\\\
                                       //  `"'  \\\\


                     /\('')/\\
                     \      /  \n\n'''

piranah_big_txt = ''' 
                                           o
                                          o 
                                ,---,      o
                             ,-'    `--, o  
                       ( `-,'            `\\
                        \           ,    @ \\
                        /   ,       ;       \\
                       (_,-' \       `, _  ""/
                              `-,___ =='__,-' \n\n'''

spider_mama_txt = '''
                          /\  .-"""-.  /\ 
                         //\\\\/  ,,,  \//\\\\
                         |/\| ,;;;;;, |/\|
                         //\\\\\;-"""-;///\\\\ 
                        //  \/   .   \/  \\\\
                       (| ,-_| \ | / |_-, |)
                         //`__\.-.-./__`\\\\
                        // /.-(() ())-.\ \\
                       (\ |)   '---'   (| /)
                        ` (|           |) `
                           \\)         (/  \n\n'''

kurt_txt = '''
         +++++++++++++++++=++=::::::.::-==++**+*+++=====++=+===++++++++++++++++=-=--==================++++++++
         +++++++++++++++++++=---:..::-+*#%@@@@@@@@@@%%#*+------:-----=======++++++++=----==-==-========+++++++
         ++++++++++++++=====-:-==:..+%@@@@@#*+======+*%@@@#+=+++=+=====--------==+=+++++==-:---=-==-===+++++++
         +++++++++==========-===-:.#@@@@%+.         .. .-*%@@%#%%%%%%%%##%#***#%%@@@@@@@%%#*=::--=--====++++++
         +++++++===========-+=--:.#@@@@*.       ...::----=*#%@@%##%%%%###%@@@%#*++######%@@@@@#=:---=++=++++++
         ++++++===========-===-: -@@@@#      ... :-=**#***#%#%@@%@%@@%%%@@#+--===+#%%%%%#*+*@@@@%+:=+++==+++++
         +++============-===--:  =@@@@-     .... -+#%%%%%%####@%@@@@@@@@%=-+*#%####%%%*%##*.:#@@@@#-==++=+++++
         ++============-=+==:..  :@@@@-     .... :==:::==--**#@@%%%%@@@@=:+##%%%%%####*##+:   #@@@@*==:-=+++++
         ============--=+=--:     *@@@#     .... .:.....:=*++@@####%%%@@..=-::=+::*##++=:.    -@@@@#-++:=+++++
         ==========----====:       +@@@*.            . .--:=%%#*#####%@@:.::....-+*+=-::      :@@%@#:=+=++++++
         ========-----=+===:.       :#@@%+:             .:*@#***#######@*....  :----:..       +@@@@+-===++++++
         ======-=-----+===:.       ..:-+#%@%*=-:....:-=+#%*+**#########*@*. .  ......        =@@@@+=-==+=+++++
         ======------=+==-:.       .:=+===++*##%%%%%##***+=+**#%%%%%###++%%+.              -#@@@%-==:++==+++++
         =====-------====-:.  ..   ::=++****+++=+++**###*+**=+*##%%####**=+#%%*=-:....:-=*%@@%*-.:+=-=++==++++
         ====-------=+====-: .-. ::--=+**###*######%%##*=+*-..-****=-=###%#+=++*#%%@@@@%%##*+- ..+=====+-=++++
         ===--------=====--: :=. .:-==+*###****###%%%##*==++=+=+++++-=+*#%%%%##**++++++++***+: :-+========++++
         ==---------++====--..:..:.-=++*###*+**##%%%#***++-=+**#***+*++*#%%%%%%%%%%%%%%##***+..-===-:=+===++++
         ==-------=+==--==--: ...-:-=++*##****####**+++=====+*+*=+*++=+*##%%%%%%%%%%%%%#*+**=.:-+==--+-+==++++
         ----------++-=-=---:  ..:.-=++**#**+**#*++++==-==++**+++##+++++**##%%%#%%##%###*+*+:..-++=.-=+==+++++
         ---------==+=------. .. ..-=++****+***===+++++++****##*#%###*++++**#####%##%%##***+..-++*-.=====+++++
         ---------+=+=-=--::. -.   -=+++***+++===+****#***+===+++++#%*##**+=+##*#######****-.-=++*.:=+=+++++++
         --------=+==+---::.. :..  :===++++=++++*****+=--====---===#+-**=**+=+#########***=:-=+=*+:-++==++++++
         -------:=+=-=---::.  :..  :-+==++===+++++*****###*****=-::=+==+**#*++#%######***+:=+=+:#-.--==+++++++
         ------:-++===---:..  .:....-==+===--==++***#******++=++++*######*##***#####**##+=++=+.:#-:====+++++++
         ------:-=-==-=--:.  .--::..-=++===---==++*******++==-===+**######**+++#####*##+++===. -+:-=-==+++++++
         ---::-:=====----:. ..+-+-: .-====-:.:--==+*****+==--::--=***####***+=+*******+=-=-:   --:-====+++++++
         ----:::==-==-=--...--+++=-  .--:-:...:===+=+====++++*+**++********++==+****+==-:...  .:::-==-++++++++
         --:::::====----:..=:=+**--....:.......--====+==++*=-==+*++++++++++==--=+*+++=:.::.    .::-+=-++++++++
         -::::::==-=-----.-:.==*+:-::....... ..:--==-==+=++=:--=+=+====+=++==::=+++++:::::     .-:=-+=++++++++
         ::::::-==-=-==-:.:.::==::-:.:::::......:---=---==+=:--+=++=========-:-+*++-.:--:.     .:-====++++++++
         ::::::===-=-=---...:-=:.:-..:-::--::....:::-------=---===========-:..-++-::==--...   ..:-===+++++++++
         ::::::-==-------..::-:.:-=..:--------:....:::-::--:::------===--:....-=-:=++=-:.:    .::-=-=+++++++++
         ::::::====-=---=...:::.:=:..--==--==-----::....:......:::-:-:...::-=++=-++*+=::-.   ...-====+++++++++
         ::::.--=-=-=---=-..:..:=:..:-========--------------:::::::::--==++++=-++**++-:-.    ...-+=-=+++++++++
         :::.:-=====----=-::-----:..-===+======---========+++=+++++********+==*****++:::    ...:=+==++++++++++
         :...-===-:-===-----=:::--::-=++++++===--===++++*********######***+==**###++=:-..   ...:==-+++++++++++\n\n'''

welcome_txt = "    Welcome to Time Hackers,\n\n    You are about to complete a series of challenges with your four friends:\n\n\n    Andy, Michal, Lasharn and Saihar.\n\n\n    Once you complete all the challenges you will reach a time machine.\n\n    You will be able to use the time machine to travel back in time\n    and save Kurt Cobain.\n\n    You find yourselves at the beginning of the corridor of doom. To reach\n    the time machine, you must pass through a swarm of deadly tarantulas, a\n    locked door with laser beams, a pool full of hungry piranhas and a\n    molten pit of lava.\n\n    Help your friends solve each challenge in order to save them from DEATH.\n"
challenge_1_txt = "    Challenge 1:\n\n    You encounter a swarm of deadly tarantulas.\n\n    Andy steps forward to answer the tarantula Queen's question.\n\n    Who is the best superhero?\n"
challenge_2_txt = "    Challenge 2:\n\n    You have reached a locked door with lasers and a giant keypad.\n\n    To unlock the door and safely get Michal through with you,\n    enter the correct code.\n\n    If you fail to unlock the door, it will activate the laser\n    beams which will destroy Michal.\n\n    There is a clue on the door which asks what year did\n    Kurt Cobain die?\n"
challenge_3_txt = "    Challenge 3:\n\n    You are now halfway through.\n\n    The next encounter is a pool of hungry piranhas.\n\n    Lasharn gets ready to answer a geographical question.\n"
challenge_4_txt = "    Challenge 4:\n\n    You’ve now reached the final challenge, a pit full\n    of molten lava.\n\n    There is an algebraic equation on a sign in front of you,\n    What is the value of X?\n\n    Saihar must answer the question correctly to proceed.\n"
challenge_5_txt = "    This is it!\n\n    You finally made it through all the challenges, and before you is\n    the time machine.\n\n    Awesome!\n"

challenge_1_quest = "    Enter \"A\" for Thor, \"B\" for Spiderman, \"C\" for Supergirl\n    or \"D\" for Batman:\n"
challenge_1_right = "\n    Correct! The tarantula Queen orders the other spiders back\n    into their webs.\n\n    You can all safely pass through.\n"
challenge_1_wrong = "\n    OH NO! That was the wrong answer. Andy is attacked by all\n    the tarantulas and didn’t survive.\n\n    Michal, Lasharn and Saihar will continue without him.\n"
challenge_2_quest = "    Type the code to pass?\n"
challenge_2_right = "\n    AWESOME! Michal entered the code correctly.\n\n    You wait for the door to slide open and continue on your quest.\n"
challenge_2_wrong = "\n    OH NO! Michal didn’t get the code correct and now he has been\n    vaprorised by laser beams!\n\n    The door slides open to allow the others through.\n"
challenge_3_quest = "    Mount Kilimanjaro is the highest mountain in the world.\n    True or False?\n"
challenge_3_right = "\n    CORRECT! The statement is false. It's actually Mount Everest.\n\n    A bridge rises out of the water and the group continue.\n"
challenge_3_wrong = "\n    OH NO! Wrong answer, the highest mountain is Mount Everest.\n\n    Lasharn is attacked and eaten by the piranhas.\n\n    A bridge rises out of the water and the group continue.\n"
challenge_4_quest = "    3x + 2 = 14\n"
challenge_4_right = "\n    WELL DONE! Saihar answered correctly.\n\n    Stepping stones appear and allow the group to cross\n    the lava lake together.\n"
challenge_4_wrong = "\n    OH NO! Incorrect answer. Saihar has been engulfed by the lava.\n\n    Stepping stones appear and you cross the lava lake.\n"
challenge_5_quest_a = "    You now have the option to travel back in time to save Kurt Cobain\n    or go back and save your friend.\n\n    Enter \"A\" if you wish to use the time machine to save Kurt or\n    enter \"B\" to go back and rescue your friend.\n"
challenge_5_quest_b = "    You now have the option to travel back in time to save Kurt Cobain\n    or go back and save your friends.\n\n    Enter \"A\" if you wish to use the time machine to save Kurt or\n    enter \"B\" to go back and rescue your friends.\n"

ending_1_txt = "    You go back in time and save Kurt Cobain\n\n    CONGRATS, YOU WIN THE GAME!"
ending_2_txt = "    CONGRATS, everyone survived!\n\n    You and your friends use the time machine to save\n    Kurt Cobain together.\n\n\n"

credits_1_txt = "                          C R E D I T S"
credits_2_txt = "                            ANDY JACKO"
credits_3_txt = "                           MICHAL WERNER"
credits_4_txt = "                            LASHARN F"
credits_5_txt = "                          SAIHAR SIDDIQUE"
credits_6_txt = "                           T H E  E N D"

new_line = "\n"
os.system('cls||clear')

def type_slow(print_this):
  for char in print_this:
    sleep(0.05)
    print(char, end="", flush=True)

def roll_credits():
  for i in range(100):
    sleep(0.25)
    print(new_line)
    if i == 10:
      print(credits_1_txt)
    if i == 15:
      print(credits_2_txt)
    if i == 45:
      print(credits_3_txt)
    if i == 25:
      print(credits_4_txt)
    if i == 35:
      print(credits_5_txt)
    if i == 30:  
      print(spider_small_txt)
    if i == 40:  
      print(piranah_big_txt)
    if i == 20:  
      print(spider_mama_txt)
    if i == 60:
      print(credits_6_txt)
    if i == 80:  
      print(kurt_txt)  

def start_game():
  global andy_alive
  andy_alive = 1
  global michal_alive
  michal_alive = 1
  global lasharn_alive
  lasharn_alive = 1
  global saihar_alive
  saihar_alive = 1

  os.system('cls||clear')
  print(intro_txt)
  type_slow(welcome_txt)
  
  sleep(pause_time * 3)
  room_1()

def room_1():
  os.system('cls||clear')
  print(room_1_txt)
  type_slow(challenge_1_txt + new_line + challenge_1_quest + new_line) 
  andy_question = input("    :- ")
  
  while andy_question.lower() != "a" and andy_question.lower() != "b" and andy_question.lower() != "c" and andy_question.lower() != "d": 
    os.system('cls||clear')
    print(room_1_txt)
    print(challenge_1_txt + new_line + challenge_1_quest) 
    andy_question = input("    :- ")
  
  if andy_question.lower() != "b":
    global andy_alive
    andy_alive = 0
    type_slow(challenge_1_wrong)
  else:
    type_slow(challenge_1_right)

  sleep(pause_time)
  room_2()

def room_2():  
  os.system('cls||clear')
  print(room_2_txt)
  type_slow(challenge_2_txt + new_line + challenge_2_quest + new_line)
  michal_question = input("    :- ")
  
  while michal_question == "":
    os.system('cls||clear')
    print(room_2_txt)
    print(challenge_2_txt + new_line + challenge_2_quest)
    michal_question = input("    :- ")
  
  if michal_question.lower() != "1994":
    global michal_alive
    michal_alive = 0
    type_slow(challenge_2_wrong)
  else:
    type_slow(challenge_2_right)

  sleep(pause_time)
  room_3()

def room_3():
  os.system('cls||clear')  
  print(room_3_txt)
  type_slow(challenge_3_txt + new_line + challenge_3_quest + new_line)
  lasharn_question = input("    :- ")
  
  while lasharn_question.lower() != "true" and lasharn_question.lower() != "false":
    os.system('cls||clear')
    print(room_3_txt)
    print(challenge_3_txt + new_line + challenge_3_quest)
    lasharn_question = input("    :- ")    
    
  if lasharn_question.lower() != "false":
    global lasharn_alive
    lasharn_alive = 0
    type_slow(challenge_3_wrong)
  else:
    type_slow(challenge_3_right)

  sleep(pause_time)
  room_4()
 
def room_4():
  os.system('cls||clear')
  print(room_4_txt)  
  type_slow(challenge_4_txt + new_line + challenge_4_quest + new_line)
  saihar_question = input("    :- ")
  
  while saihar_question == "":
    os.system('cls||clear')
    print(room_4_txt)   
    print(challenge_4_txt + new_line + challenge_4_quest)
    saihar_question = input("    :- ")
  
  if saihar_question.lower() != "4":
    global saihar_alive
    saihar_alive = 0
    type_slow(challenge_4_wrong)
  else:
    type_slow(challenge_4_right)

  sleep(pause_time)
  room_5()

def room_5():
  os.system('cls||clear') 
  print(time_machine_txt)
  type_slow(challenge_5_txt + new_line)
  
  if andy_alive == 0 or michal_alive == 0 or lasharn_alive == 0 or saihar_alive == 0 :
    dead_players = ["DEAD"]
    if andy_alive == 0:
      dead_players.append("Andy")
    if michal_alive == 0:
      dead_players.append("Michal")
    if lasharn_alive == 0:
      dead_players.append("Lasharn")
    if saihar_alive == 0:
      dead_players.append("Saihar")
    if len(dead_players) > 2:
      d_p = "    Your friends "
      who_to_save = challenge_5_quest_b
    else:
      d_p = "    Your friend " 
      who_to_save = challenge_5_quest_a
   
    if len(dead_players) > 1:
      for i in range(len(dead_players)):
        if i > 0:
          if i == (len(dead_players)-2) :
            d_p += dead_players[i] + " and "
          else:
            d_p += dead_players[i] + ", "

    d_p = d_p[:-2]
    d_p = d_p + " didn't make it.\n\n"
    type_slow(d_p + new_line + who_to_save + new_line)
    all_question = input("    :- ")

    while all_question.lower() != "a" and all_question.lower() != "b":
      os.system('cls||clear')
      print(time_machine_txt + new_line + challenge_5_txt + new_line + d_p + new_line + who_to_save)
      all_question = input("    :- ")    
    
    if all_question.lower() == "a":
      os.system('cls||clear')
      print(time_machine_txt)
      type_slow(ending_1_txt)
      roll_credits()
    else: 
      start_game()
  else:
    type_slow(ending_2_txt)
    roll_credits()

start_game()