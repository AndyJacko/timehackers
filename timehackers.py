from time import sleep

pause_time = 2
andy_alive = 1 
michal_alive = 1
lasharn_alive = 1
saihar_alive = 1

intro_txt = '''
 ::::::::::: ::::::::::: ::::    ::::  ::::::::::   :::    :::     :::      ::::::::  :::    ::: :::::::::: :::::::::   ::::::::
     :+:         :+:     +:+:+: :+:+:+ :+:          :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  :+:        :+:    :+: :+:    :+:
     +:+         +:+     +:+ +:+:+ +:+ +:+          +:+    +:+  +:+   +:+  +:+        +:+  +:+   +:+        +:+    +:+ +:+
     +#+         +#+     +#+  +:+  +#+ +#++:++#     +#++:++#++ +#++:++#++: +#+        +#++:++    +#++:++#   +#++:++#:  +#++:++#++
     +#+         +#+     +#+       +#+ +#+          +#+    +#+ +#+     +#+ +#+        +#+  +#+   +#+        +#+    +#+        +#+
     #+#         #+#     #+#       #+# #+#          #+#    #+# #+#     #+# #+#    #+# #+#   #+#  #+#        #+#    #+# #+#    #+#
     ###     ########### ###       ### ##########   ###    ### ###     ###  ########  ###    ### ########## ###    ###  ########\n\n'''

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
      +++++++++++++++++++++++++++++++++++++=++=::::::.::-==++**+*+++=====++=+===++++++++++++++++=-=--==================++++++++
      +++++++++++++++++++++++++++++++++++++++=---:..::-+*#%@@@@@@@@@@%%#*+------:-----=======++++++++=----==-==-========+++++++
      ++++++++++++++++++++++++++++++++++=====-:-==:..+%@@@@@#*+======+*%@@@#+=+++=+=====--------==+=+++++==-:---=-==-===+++++++
      +++++++++++++++++++++++++++++==========-===-:.#@@@@%+.         .. .-*%@@%#%%%%%%%%##%#***#%%@@@@@@@%%#*=::--=--====++++++
      +++++++++++++++++++++++++++===========-+=--:.#@@@@*.       ...::----=*#%@@%##%%%%###%@@@%#*++######%@@@@@#=:---=++=++++++
      ++++++++++++++++++++++++++===========-===-: -@@@@#      ... :-=**#***#%#%@@%@%@@%%%@@#+--===+#%%%%%#*+*@@@@%+:=+++==+++++
      +++++++++++++++++++++++============-===--:  =@@@@-     .... -+#%%%%%%####@%@@@@@@@@%=-+*#%####%%%*%##*.:#@@@@#-==++=+++++
      ++++++++++++++++++++++============-=+==:..  :@@@@-     .... :==:::==--**#@@%%%%@@@@=:+##%%%%%####*##+:   #@@@@*==:-=+++++
      ++++++++++++++++++++============--=+=--:     *@@@#     .... .:.....:=*++@@####%%%@@..=-::=+::*##++=:.    -@@@@#-++:=+++++
      +++++++++++++++++++===========----====:       +@@@*.            . .--:=%%#*#####%@@:.::....-+*+=-::      :@@%@#:=+=++++++
      ++++++++++++++++++==========-----=+===:.       :#@@%+:             .:*@#***#######@*....  :----:..       +@@@@+-===++++++
      ++++++++++++++++==========-=-----+===:.       ..:-+#%@%*=-:....:-=+#%*+**#########*@*. .  ......        =@@@@+=-==+=+++++
      +++++++++++++++===========------=+==-:.       .:=+===++*##%%%%%##***+=+**#%%%%%###++%%+.              -#@@@%-==:++==+++++
      +++++++++++++++==========-------====-:.  ..   ::=++****+++=+++**###*+**=+*##%%####**=+#%%*=-:....:-=*%@@%*-.:+=-=++==++++
      ++++++++++++++==========-------=+====-: .-. ::--=+**###*######%%##*=+*-..-****=-=###%#+=++*#%%@@@@%%##*+- ..+=====+-=++++
      +++++++++++++==========--------=====--: :=. .:-==+*###****###%%%##*==++=+=+++++-=+*#%%%%##**++++++++***+: :-+========++++
      +++++++++++===========---------++====--..:..:.-=++*###*+**##%%%#***++-=+**#***+*++*#%%%%%%%%%%%%%%##***+..-===-:=+===++++
      ++++++++++============-------=+==--==--: ...-:-=++*##****####**+++=====+*+*=+*++=+*##%%%%%%%%%%%%%#*+**=.:-+==--+-+==++++
      +++++++++===========----------++-=-=---:  ..:.-=++**#**+**#*++++==-==++**+++##+++++**##%%%#%%##%###*+*+:..-++=.-=+==+++++
      ++++++++++==========---------==+=------. .. ..-=++****+***===+++++++****##*#%###*++++**#####%##%%##***+..-++*-.=====+++++
      ++++++++===========----------+=+=-=--::. -.   -=+++***+++===+****#***+===+++++#%*##**+=+##*#######****-.-=++*.:=+=+++++++
      +++++++===========----------=+==+---::.. :..  :===++++=++++*****+=--====---===#+-**=**+=+#########***=:-=+=*+:-++==++++++
      +++++============----------:=+=-=---::.  :..  :-+==++===+++++*****###*****=-::=+==+**#*++#%######***+:=+=+:#-.--==+++++++
      ++++============----------:-++===---:..  .:....-==+===--==++***#******++=++++*######*##***#####**##+=++=+.:#-:====+++++++
      ++++============----------:-=-==-=--:.  .--::..-=++===---==++*******++==-===+**######**+++#####*##+++===. -+:-=-==+++++++
      +++============--------::-:=====----:. ..+-+-: .-====-:.:--==+*****+==--::--=***####***+=+*******+=-=-:   --:-====+++++++
      ++============----------:::==-==-=--...--+++=-  .--:-:...:===+=+====++++*+**++********++==+****+==-:...  .:::-==-++++++++
      =============---------:::::====----:..=:=+**--....:.......--====+==++*=-==+*++++++++++==--=+*+++=:.::.    .::-+=-++++++++
      ============---------::::::==-=-----.-:.==*+:-::....... ..:--==-==+=++=:--=+=+====+=++==::=+++++:::::     .-:=-+=++++++++
      =========----------:::::::-==-=-==-:.:.::==::-:.:::::......:---=---==+=:--+=++=========-:-+*++-.:--:.     .:-====++++++++
      ========----------::::::::===-=-=---...:-=:.:-..:-::--::....:::-------=---===========-:..-++-::==--...   ..:-===+++++++++
      ======----------::::::::::-==-------..::-:.:-=..:--------:....:::-::--:::------===--:....-=-:=++=-:.:    .::-=-=+++++++++
      ====------------::::::::::====-=---=...:::.:=:..--==--==-----::....:......:::-:-:...::-=++=-++*+=::-.   ...-====+++++++++
      ===-----------::::::::::.--=-=-=---=-..:..:=:..:-========--------------:::::::::--==++++=-++**++-:-.    ...-+=-=+++++++++
      ==-----------::::::::::.:-=====----=-::-----:..-===+======---========+++=+++++********+==*****++:::    ...:=+==++++++++++
      ------------:::::::::...-===-:-===-----=:::--::-=++++++===--===++++*********######***+==**###++=:-..   ...:==-+++++++++++\n\n'''

welcome_txt = "Welcome to Time Hackers,\nYou are about to complete a series of challenges with your four friends: Andy, Michal, Lasharn and Saihar.\n\nOnce you complete all the challenges you will reach a time machine. You will be able to travel back in time and save Kurt Cobain.\n\nYou now find yourselves at the beginning of the corridor of doom. To reach the time machine, you must pass through a swarm of tarantulas, a locked door with laser beams, a pool of piranhas and a pit of lava.\nHelp your friends answer each challenge question in order to save them from death.\n"
challenge_1_txt = "Challenge 1:\nYou encounter a swarm of deadly tarantulas,\nAndy steps forward to answer the following question.\nWho is the best superhero?.\n"
challenge_2_txt = "Challenge 2:\nYou have reached a locked door with a giant keypad.\nTo unlock the door and safely get Michal through with you, enter the correct code.\nIf you fail to unlock the door, it will activate the laser beams which will destroy Michal.\nThere is a clue on the door which asks what year did Kurt Cobain die?\n"
challenge_3_txt = "Challenge 3:\nYou are now halfway through.\nThe next encounter is a pool of piranhas,\nLasharn must get ready to answer this next geographical question.\n"
challenge_4_txt = "Challenge 4:\nYou’ve now reached the final challenge, a pit full of molten lava.\nYou have an algebraic equation on a sign in front of you, What is the value of X?\nSaihar must answer the question correctly to proceed.\n"
challenge_5_txt = "This is it!\nYou finally made it through all the challenges, and before you is the time machine.\nAwesome!\n"

challenge_1_quest = "Type \"A\" for Thor, \"B\" for Spiderman, \"C\" for Supergirl or \"D\" for Batman:\n"
challenge_1_right = "\nRIGHT – GREAT! The tarantulas have all climbed back into their webs, allowing you to safely pass through.\n"
challenge_1_wrong = "\nWRONG – OH NO! That was the wrong answer. Andy didn’t survive, but Michal, Lasharn and Saihar will continue.\n"
challenge_2_quest = "Type the code to pass?\n"
challenge_2_right = "\nRIGHT – AWESOME! Michal entered the code correctly. You wait for the door to slide open and continue on your quest.\n"
challenge_2_wrong = "\nWRONG – OH NO! Michal didn’t get the code correct and now he vaprorised by laser beams! The door slides open to allow the others through.\n"
challenge_3_quest = "Mount Kilimanjaro is the highest mountain in the world. True or False?\n"
challenge_3_right = "\nRIGHT – CORRECT! The statement is false. It's Mount Everest. A bridge rises out of the water so that the group can continue.\n"
challenge_3_wrong = "\nWRONG – OH NO! Wrong answer, the highest mountain is actually Mount Everest. Lasharn is attacked and eaten by the piranhas. A bridge rises out of the water so that the group can continue..\n"
challenge_4_quest = "3x + 2 = 14\n"
challenge_4_right = "\nRIGHT – WELL DONE! Saihar answered correctly. Stepping stones appear and allow the group to cross the lava lake together.\n"
challenge_4_wrong = "\nWRONG – OH NO! Incorrect answer. Saihar has been engulfed by the lava. Stepping stones appear and you cross the lava lake.\n"
challenge_5_quest = "You now have the option to travel back in time to save Kurt Cobain or go back and save your friend/s.\n\nEnter \"A\" if you wish to use the time machine to save Kurt or enter \"B\" to go back and rescue your friend/s\n"

ending_1_txt = "You go back in time and save Kurt Cobain\nCONGRATS, YOU WIN THE GAME!"
ending_2_txt = "CONGRATS, everyone survived! You and your friends use the time machine to save Kurt Cobain together.\n\n\n"

credits_1_txt = "                                                C R E D I T S"
credits_2_txt = "                                                  ANDY JACKO"
credits_3_txt = "                                                MICHAL WERNER"
credits_4_txt = "                                                  LASHARN F"
credits_5_txt = "                                                SAIHAR SIDDIQUE"
credits_6_txt = "                                                 T H E  E N D"

new_line = "\n"
clear_screen = "\033[H\033[J"

def type_slow(print_this):
  for char in print_this:
    sleep(0.03)
    print(char, end="", flush=True)

def roll_credits():
  for i in range(80):
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
    if i == 70:  
      print(kurt_txt)
    if i == 60:
      print(credits_6_txt)

def start_game():
  global andy_alive
  andy_alive = 1
  global michal_alive
  michal_alive = 1
  global lasharn_alive
  lasharn_alive = 1
  global saihar_alive
  saihar_alive = 1

  print(clear_screen)
  print(intro_txt)
  type_slow(welcome_txt)
  
  sleep(pause_time * 2)
  room_1()

def room_1():
  print(clear_screen)
  print(room_1_txt)
  type_slow(challenge_1_txt + new_line)
  andy_question = input(challenge_1_quest)
  
  while andy_question.lower() != "a" and andy_question.lower() != "b" and andy_question.lower() != "c" and andy_question.lower() != "d": 
    print(clear_screen)    
    print(room_1_txt)
    print(challenge_1_txt)
    andy_question = input(challenge_1_quest)
  
  if andy_question.lower() != "b":
    global andy_alive
    andy_alive = 0
    type_slow(challenge_1_wrong)
  else:
    type_slow(challenge_1_right)

  sleep(pause_time)
  room_2()

def room_2():  
  print(clear_screen)
  print(room_2_txt)
  type_slow(challenge_2_txt + new_line)
  michal_question = input(challenge_2_quest)
  
  while michal_question == "":
    print(clear_screen)
    print(room_2_txt)
    print(challenge_2_txt)
    michal_question = input(challenge_2_quest)
  
  if michal_question.lower() != "1994":
    global michal_alive
    michal_alive = 0
    type_slow(challenge_2_wrong)
  else:
    type_slow(challenge_2_right)

  sleep(pause_time)
  room_3()

def room_3():
  print(clear_screen)  
  print(room_3_txt)
  type_slow(challenge_3_txt + new_line)
  lasharn_question = input(challenge_3_quest)
  
  while lasharn_question.lower() != "true" and lasharn_question.lower() != "false":
    print(clear_screen)
    print(room_3_txt)
    print(challenge_3_txt)
    lasharn_question = input(challenge_3_quest)    
    
  if lasharn_question.lower() != "false":
    global lasharn_alive
    lasharn_alive = 0
    type_slow(challenge_3_wrong)
  else:
    type_slow(challenge_3_right)

  sleep(pause_time)
  room_4()
 
def room_4():
  print(clear_screen)
  print(room_4_txt)  
  type_slow(challenge_4_txt + new_line)
  saihar_question = input(challenge_4_quest)
  
  while saihar_question == "":
    print(clear_screen)
    print(room_4_txt)   
    print(challenge_4_txt)
    saihar_question = input(challenge_4_quest)
  
  if saihar_question.lower() != "4":
    global saihar_alive
    saihar_alive = 0
    type_slow(challenge_4_wrong)
  else:
    type_slow(challenge_4_right)

  sleep(pause_time)
  room_5()

def room_5():
  print(clear_screen)  
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
      d_p = "Your friends "
    else:
      d_p = "Your friend "    
    
    if len(dead_players) > 1:
      for i in range(len(dead_players)):
        if i > 0:
          d_p += dead_players[i] + ", "
          
    d_p = d_p[:-2]
    d_p = d_p + " died."
    print(d_p)
    all_question = input(challenge_5_quest)

    while all_question.lower() != "a" and all_question.lower() != "b":
      print(clear_screen)
      print(time_machine_txt)
      print(challenge_5_txt)
      print(d_p)
      all_question = input(challenge_5_quest)    
    
    if all_question.lower() == "a":
      print(clear_screen)
      print(time_machine_txt)
      type_slow(ending_1_txt)
      roll_credits()
    else: 
      start_game()
  else:
    type_slow(ending_2_txt)
    roll_credits()

start_game()