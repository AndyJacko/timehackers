#import sleep function from time library
from time import sleep

#Declare Global variables
pause_time = 2
andy_alive = 1 
michal_alive = 1
lasharn_alive = 1
saihar_alive = 1

#Declare text variables used throughout game as graphics and storyline
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
 !.........|        \  code_nation_co.   /        |...............!
 !.........| (^)_____\__________________/_____(^) |..[ENTER]......!
 !.........|          \                /          |..[ PSW ]......!
 !.........|           +--------------+           |..       ......!
 !.........|           |              |           |.. [ x ] ......!
 !.........| (^)_______|____+====+____|_______(^) |.. [ x ] ......!
 !.........|           |    |....| x  |           |.. [ x ] ......!
 !.........|           |    |....|    |           |.. [ x ] ......!
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

welcome_txt = "Welcome to Time Hackers,\nWhere you’ll complete a series of missions with your 4 friends, Andy, Michal, Lasharn and Saihar.\n\nOnce you reach the time machine at the end, this means you have won the game and will be able to travel back in time to save Kurt Cobain.\n\nNow that you’ve arrived at the corridor of doom, you must get past the swarm of tarantulas, the laser beams, the pool of piranhas and the pit of lava to succeed.\nHelp your friends answer each question in order to carry them along with you."
challenge_1_txt = "Challenge 1:\nTo escape the pit of deadly tarantulas,\nAndy must step forward and give the answer to the following question.\nWho is the best superhero?.\n"
challenge_2_txt = "Challenge 2:\nYou have reached a bolted door with a giant keypad.\nTo unlock the door and safely get Michal through with you, get ready to input the correct code.\nIf you fail to unlock the door, it will activate the laser beams which will destroy Michal.\nThere is a clue on the door which asks what year did Kurt Cobain die?\n"
challenge_3_txt = "Challenge 3:\nYou are now halfway through.\nThe next encounter is a pool of piranhas,\nLasharn must get ready to answer this next geographical question.\n"
challenge_4_txt = "Challenge 4:\nYou’ve now reached the final mission, a pit full of molten lava.\nYou have an algebraic equation on the sign in front of you, What is the value of X?\nSaihar must answer the question correctly to proceed.\n"
challenge_5_txt = "This is it!\nYou tried your best and made it to the time machine.\nAwesome!\n"

#All the text for right/wrong answers used throughout the game
challenge_1_right = "RIGHT – GREAT! The tarantulas have climbed back into their webs, allowing you to safely pass through."
challenge_1_wrong = "WRONG – OH NO! That was the wrong answer. Andy didn’t survive, but Michal, Lasharn and Saihar will continue."
challenge_2_right = "RIGHT – AWESOME! Michal entered the code in time. Wait for the door to slide open and continue on your quest."
challenge_2_wrong = "WRONG – OH NO! Michal didn’t get the code correct and now he is no more! The door will slide open to allow the others through."
challenge_3_right = "RIGHT – CORRECT! The statement is false. A bridge rises out of the water so that the group can continue on."
challenge_3_wrong = "WRONG – OH NO! Wrong answer, the highest mountain is actually Mount Everest. Lasharn has been attacked by the piranhas, the group continue on for the next stage."
challenge_4_right = "RIGHT – WELL DONE! Saihar answered correctly. Wait for the stepping stones to appear and cross the lava lake together."
challenge_4_wrong = "WRONG – OH NO! Incorrect answer. Saihar has been engulfed by the lava. Wait for the stepping stones to appear and cross the lava lake."

#Clear screen by printing it full of blank characters
clear_screen = "\033[H\033[J"

#Create function to print text 1 char at a time...
def type_slow(print_this):
  for char in print_this:              #For every character in string 
    sleep(0.03)                        #Pause for a little bit
    print(char, end='', flush=True)    #Print character then flush the i/o buffer so it can print the next character

#Function to loop through credits line by line displaying names and ASCII art. Not very well, but you know, we didnt have a Lucasfilm budget.
def roll_credits():
  for i in range(80):
    sleep(0.25)
    print(" \n")
    if i == 10:
      print("                                                C R E D I T S")
    if i == 15:
      print("                                                  ANDY JACKO")
    if i == 45:
      print("                                                MICHAL WERNER")
    if i == 25:
      print("                                                  LASHARN F")
    if i == 35:
      print("                                                SAIHAR SIDDIQUE")
    if i == 30:  
      print(spider_small_txt)
    if i == 40:  
      print(piranah_big_txt)
    if i == 20:  
      print(spider_mama_txt)
    if i == 70:  
      print(kurt_txt)
    if i == 60:
      print("                                                 T H E  E N D")

#Function to start and restart the game resetting global variables back to being alive on restart
def start_game():
  print(clear_screen)
  print(intro_txt)
  type_slow(welcome_txt)
  print("\n")
  #Make everyone alive incase game has been restarted
  global andy_alive
  andy_alive = 1
  global michal_alive
  michal_alive = 1
  global lasharn_alive
  lasharn_alive = 1
  global saihar_alive
  saihar_alive = 1

  sleep(pause_time)  #Pause for a little bit
  room_1() #Move to room 1

#Function for the first challenge room
def room_1():
  print(clear_screen)
  print(room_1_txt)
  type_slow(challenge_1_txt)
  andy_question = input("\nType A for Thor, B for Spiderman, C for Supergirl or D for Batman:\n")
  
  while andy_question.lower() != "a" and andy_question.lower() != "b" and andy_question.lower() != "c" and andy_question.lower() != "d": 
    print(clear_screen)    
    print(room_1_txt)                #Keep asking unless a, b, c or d entered
    print(challenge_1_txt)
    andy_question = input("Type A for Thor, B for Spiderman, C for Supergirl or D for Batman:\n")
  
  if andy_question.lower() != "b":
    global andy_alive
    andy_alive = 0
    print("\n")
    type_slow(challenge_1_wrong)
    print("\n")
  else:
    print("\n")
    type_slow(challenge_1_right)
    print("\n")

  sleep(pause_time)  #Pause for a little bit
  room_2() #Move to room 2

#Function for the second challenge room
def room_2():  
  print(clear_screen)
  print(room_2_txt)
  type_slow(challenge_2_txt)
  michal_question = input("\nType the code to pass? \n")
  
  while michal_question == "": #Keep asking if nothing is entered but return pressed
    print(clear_screen)
    print(room_2_txt)
    print(challenge_2_txt)
    michal_question = input("Type the code to pass? \n")
  
  if michal_question.lower() != "1994":
    global michal_alive
    michal_alive = 0
    print("\n")
    type_slow(challenge_2_wrong)
    print("\n")
  else:
    print("\n")
    type_slow(challenge_2_right)
    print("\n")

  sleep(pause_time)  #Pause for a little bit
  room_3() #Move to room 3

#Function for the third challenge room
def room_3():
  print(clear_screen)  
  print(room_3_txt)
  type_slow(challenge_3_txt)
  lasharn_question = input("\nMount Kilimanjaro is the highest mountain in the world. True or False? \n")
  
  while lasharn_question.lower() != "true" and lasharn_question.lower() != "false": #Keep asking until either true or false entered
    print(clear_screen)
    print(room_3_txt)
    print(challenge_3_txt)
    lasharn_question = input("Mount Kilimanjaro is the highest mountain in the world. True or False? \n")    
    
  if lasharn_question.lower() != "false":
    global lasharn_alive
    lasharn_alive = 0
    print("\n")
    type_slow(challenge_3_wrong)
    print("\n")
  else:
    print("\n")
    type_slow(challenge_3_right)
    print("\n")

  sleep(pause_time) #Pause for a little bit
  room_4() #Move to room 4
 
#Function for the fourth challenge room
def room_4():
  print(clear_screen)
  print(room_4_txt)  
  type_slow(challenge_4_txt)
  saihar_question = input("\n3x + 2 = 14\n")
  
  while saihar_question == "": #Keep asking if nothing is entered but return pressed
    print(clear_screen)
    print(room_4_txt)   
    print(challenge_4_txt)
    saihar_question = input("3x + 2 = 14 \n")
  
  if saihar_question.lower() != "4":
    global saihar_alive
    saihar_alive = 0
    print("\n")
    type_slow(challenge_4_wrong)
    print("\n")
  else:
    print("\n")
    type_slow(challenge_4_right)
    print("\n")

  sleep(pause_time)  #Pause for a little bit
  room_5() #Move to final room

#Function for the final room
def room_5():
  print(clear_screen)  
  print(time_machine_txt)
  type_slow(challenge_5_txt)
  print("\n")
  #Check if any players died. If they did you get 1 ending if they didnt you get a completely different ending. WOW!
  if andy_alive == 0 or michal_alive == 0 or lasharn_alive == 0 or saihar_alive == 0 :
    dead_players = ["DEAD"] #Create list of dead playser entering a word to take up index 0
    if andy_alive == 0:
      dead_players.append("Andy")
    if michal_alive == 0:
      dead_players.append("Michal")                   #If anyone died add to the list
    if lasharn_alive == 0:
      dead_players.append("Lasharn")
    if saihar_alive == 0:
      dead_players.append("Saihar")
    if len(dead_players) > 2: #If greater than 2 means more than 1 person died so use plural
      d_p = "Your friends "
    else:
      d_p = "Your friend "    
    
    if len(dead_players) > 1:
      for i in range(len(dead_players)):   #Loop through dead list putting name comma and space (, )in the string
        if i > 0:
          d_p += dead_players[i] + ", "
          
    d_p = d_p[:-2] #Remove the ", " from the end of the string
    d_p = d_p + " died." #Add to end of string forming full sentence
    print(d_p)
    all_question = input("\nYou have the option to travel back in time to save Kurt Cobain or restart the mission and revive your friend/s.\n\nEnter A if you wish to use the time machine to save Kurt or enter B to go back and rescue your friend/s\n")

    while all_question.lower() != "a" and all_question.lower() != "b": #Keep asking unless the answer is a or b
      print(clear_screen)
      print(time_machine_txt)
      print(challenge_5_txt)
      print(d_p)
      all_question = input("You have the option to travel back in time to save Kurt Cobain or restart the mission and revive your friend/s.\n\nEnter A if you wish to use the time machine to save Kurt or enter B to go back and rescue your friend/s\n")    
    
    if all_question.lower() == "a": #If answer is a go and save Kurt
      print(clear_screen)
      print(time_machine_txt)
      type_slow("You go back in time and save Kurt Cobain\nCONGRATS, YOU WIN THE GAME!")
      roll_credits() #Does what it says on the tin
    else: 
      start_game() #This 1 resets the game if you choose to save your friends
  else:
    type_slow("CONGRATS, everyone survived! You and your friends can use the time machine to save Kurt Cobain together.\n\n\n")
    roll_credits() #Does what it says on the tin

start_game() #This 1 line right here starts the whole thing going