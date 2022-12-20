import sys
import time

class color:
 PURPLE = '\033[95m'
 CYAN = '\033[96m'
 DARKCYAN = '\033[36m'
 BLUE = '\033[94m'
 GREEN = '\033[92m'
 YELLOW = '\033[93m'
 RED = '\033[91m'
 BOLD = '\033[1m'
 UNDERLINE = '\033[4m'
 END = '\033[0m'
 
def print(str):
  str = color.BLUE + str + color.END   
  for char in str:
      time.sleep(0.05)
      sys.stdout.write(char)
      sys.stdout.flush()


def intro():
    print(
        "...You wake up in an empty, dark and ominous cave. A large endless lake is behind you. All you had with you was a one-handed sword. 3 orbs are levitating in front of you, between you and the only exit of the cave. The orb on the left was red, in the middle was blue and on the right was black. The exit was so dark that it was imposible to see what was awaiting for you outside of it. You walk over to the orbs, your steps loudly resonating accross the cave walls. You start to closely inspect the orbs but are careful to not touch them. They remind you of a myth of the 3 legendary power orbs. They could give powers to whoever absorbed them but it only happened once they were in sync. The red orb would give you the abilities over fire, the blue orb would give you powers over water while the black orb would give you power over shadows. You reach out and grab the...\n\nA. Red orb\nB. Blue orb\nC. Black orb"
    )

    orb = input(" \n>>> ")
  
    if orb == "A" or orb == "a":
        red()
    elif orb == "B" or orb == "b":
        blue()
    elif orb == "C" or orb == "c":
        blackOrb()
    else:
        print("Player tried to think outside of the box...lol")
        dead()


def dead():
    print("""\n\n  ------------------
  ------------------
  ---- You Died ----
  ------------------
  ------------------\n""")
    restart = input("\nDo you want to restart? (Y/N) ")
    if restart == "Y" or restart == "y":
      print("\n\n\n\n\n")
      intro()
    elif restart == "N" or restart == "n": 
        print("Goodbye...")


def red():
  print(
      "\nA briliant flash blinds you momentarily and you feel your body starts to heat up. When you start to see again, you see the imposible. Your body is covered in fire. You start to panic and feel light headed as you witness your skin burning right infront of your eyes.\n\nDo you...\nA. Jump into the lake\nB. Yell for help\nC.Stop, drop and roll on the cave ground"
  )

  fire = input(" \n>>> ")

  if fire == "A" or fire == "a":
    firelake()
  elif fire == "B" or fire == "b":
    leave()
  elif fire == "C" or fire == "c":
    print("\nYou drop onto the ground as fast as you can and start rolling. The fire doesn't seem to decrease at all and you are in immense pain from your skin boiling. You die and your whole body is burnt, not even sparing your bones as you turn into ashes.")
    dead()
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def blackOrb():
    print("\nDarkness overwhelmes your sight and you can't see anything. Then the cave starts to tremble and you hear the sound of thuds getting louder and clearer and your voice dies out. Then a large, looming figure, walks into the cave with steps that caused small tremors.\n\nDo you...\nA. Yell for help\nB. Stay calm and wait for your vision to clear again\nC. Try running towards where the exit was")
    
    blind = input("\n>>> ")

    if blind == "A" or blind == "a":
      print("\nThe troll hears your voice and charges towards you with a 4 feet long club. The troll smashes your head with the club and you die.")
      dead()

    elif blind == "B" or blind == "b":
      print("\nYou start to hear voices yelling at you to duck\n\n Do you...\nA. Listen to them\nB. Ignore them and try to find your way out")

      voices = input("\n>>> ")

      if voices == "A" or voices == "a":
        print("\nYou duck in time for a swosh to be heard where your head was moments ago. He head a growl coming from something right infront of you.")
        darkpower()

      elif voices == "B" or voices == "b":
        print("\nYou start walking into the general direction you remembered the exit was. As you walk towards the exit, still unable to see anything, something growls and the thuds get louder until you are hit by something really hard in your head, killing you.")
        dead() 

      else:
        print("\nPlayer tried to think outside of the box...lol")
        dead()

    elif blind == "C" or blind == "c":
      print("\nYou are burnt into a a crisp as you are running.")
      dead()

    else:
      print("\nPlayer tried to think outside of the box...lol")
      dead()


def firelake():
  print("\nYou jump into the lake and the cold water around you starts to instantaneously puts out the fire. You start to cool down but you see something move in the water. With the fire out, you start to swim to the to the surface but something hits you hard in your side. You lose you breath and you frantically try to swim to the surface. You gasp as you finally get air, looking under you and see something gigantic moving. It is getting bigger and bigger and you realize it is nearing you and you start swimming to the river bank but the thing was agile and slams into you again. You are almost at the lake's bank when you turn around to see the thing was a gigantic snake moving at you at imposible speed.\n\nDo you...\nA. Fight\nB. Try to swim out")
    
  lake = input("\n>>> ")

  if lake == "A" or lake == "a":
    print("\nYou try to bring out your sword but it isn't attached to your waste anymore. You realize that it probably fell to the bottom of the lake when you jamp in. The snake comes back and swallows you whole.")
    dead()

  elif lake == "B" or lake == "b":
    print("\nYou barely made it out of the lake as the snake tries to bite at you, instead it hits the rocky corner of the lake's bank. You stumble onto the ground, tired and heaving large breaths. You slowly get up.")
    stay()

  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def blue():
  print("\nThe water lights up and you go to investigate it but the cave starts to shake as if there is an earthquake boulders and spikes start to fall from the ceiling\n\nDo you...\nA. Jump into the lake\nB. Try to run to the exit\nC. Yell for help")

  cave_in = input("\n>>> ")

  if cave_in == "A" or cave_in == "a":
    print("\nYou jump into the lake as a boulder hits the water near you. You are scared an try to swim up to the surface. As you swim up, you feel as if there is something other than you in the lake. Just then you clearly see a giant glowing snake was coming at you very quickly\n\nDo you...\nA. Fight it\nB. Try to swim out")
    
    lake = input("\n>>> ")

    if lake == "A" or lake == "a":
      print("\nAs you try to grab the sword that was attached to your side, you find nothing. Looking down you see your sword was dropping to the bottom of the lake. You try to get your sword back but the snake swallows you whole.")
      dead()

    elif lake == "B" or lake == "b":
      print("\nYou barely made it out of the lake as the snake tries to bite you. You stumble onto the ground, tired and heaving large breaths. You open yours eyes and see a jagged spiked rock spike falling right at your head.")
      dead()
  
    else:
      print("\nPlayer tried to think outside of the box...lol")
      dead()

  elif cave_in == "B" or cave_in == "b":
    print("\nYou run as fast as you can but the exit gets covered by boulders right in front of you. You try to think of another exit bu you are hit by a boulder that fell from the ceiling and immediately die.")
    dead()

  elif cave_in == "C" or cave_in == "c":
    print("\nThe rocks are crashing as a troll enters because of your yelling. Just as the troll enters it is hit by a boulders and blood splatters all around the ground it was standing on. The exit is partially blocked\n\nDo you...\nA. Try to get out\nB. Give up")

    suicideTroll = input("\n>>> ")

    if suicideTroll == "A" or suicideTroll == "a":
      print("\nYou run but slip on the blood and fall, hit your head on the cold, hard ground and die")
      dead()

    elif suicideTroll == "B" or suicideTroll == "b":
      print("\nA spike hits you while you were standing still.")
      dead()
  
    else:
      print("\nPlayer tried to think outside of the box...lol")
      dead()

  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def stay():
  print("\nDo you...\nA. Yell for help\nB. Stay where you are")
  
  leaveCave = input("\n>>> ")

  if leaveCave == "A" or leaveCave == "a":
    leave()   

  elif leaveCave == "B" or leaveCave == "b":
    print("\nYou stay in the cave, not proceeding further into the cave. You stay in the cave for two full days, until you were getting very thirsty and hungery. You decide you have to get some  water from the lake or you will die. You go to the edge of the lake and crouch down to drink some water. Before you could even know what was happening, the snake came back and swallowed you whole and you died from the snake's venom burning through your body.")
    dead()  

  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def leave():
  print("\nThe cave starts to tremble and you hear the sound of thuds getting louder and clearer and your voice dies out in the middle of your scream of help. Then a large, looming figure appears infront of the exit of the cave, with steps that caused small tremors. It stops the in the middle of the cave and stares right at you. With a loud roar it charges at you while swinging his massive 4 foot club.\n\nDo you...\nA. Fight it\nB. Except your fate\nC. Run away")
  
  troll = input("\n>>> ")

  if troll == "A" or troll == "a":
    print("\nYou try to bring up your sword but it seems to be missing. You look down to try and find it, realization creeps into you that the sword probably was at the bottom of the lake. You look back up at the troll just to see a club headed at your face. Your head was smashed and you instantly die.")
    dead()

  elif troll == "B" or troll == "b":
    power()
  
  elif troll == "C" or troll == "c":
    print("\nYou run away from the troll to the only place you could, a boulder near the lake. As you were peaking around the boulder, you had your back turned to the lake. The snake emerges of the water and chomps your upper body at once.")
    dead()  

  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def darkpower():
  print("\nYour eyes are then suddenly able to see again. And what you see is a troll with a 4 feet long club growling in anger. You hear the voices from before telling you to strech out your hand. You slowly stretch out your hand and heavy black smoke starts to emmit from it. You and the troll both stand then, transfixed by the cold darkness comming from the smoke. The troll then shakes his head and anger is evident on his face. It raises the club, ready to smash your head.\n\nDo you...\nA. Fight it\nB. Run away\nC. Try to hide behind a boulder near the lake")
  
  troll = input("\n>>> ")

  if troll == "A" or troll == "a":
    print("\nYou get ready to fight the mad troll, when you feel something cold in your hand. You quicly look down to see it was a dagger made up of what seemed to be shadows. The troll bellows in rage as he is bringing down his club. You then move as fast as you can and cut down the club. The troll look even for enraged and was about to punch you but you where able to quickly decapitate it's head. The voices then told you how you where now able to summon him the troll to help you in battle. You then leave the cave and walk into what seems to be a corridor. You realize that you were able to see clearly in what should have been a dark corridor. In the end of the corrior, you see a sphinx guarding a pair of large golden doors.The sphinx tell you that your only chance at survival is if you can solve all 3 riddles that it tells you. You can't retreat or go forwards without solving all of the riddles, because it would kill you. The first riddle is...\nWhat is x if √x + 1 = 10\n\nIs it...\nA. 9\nB. -81\nC. 81\nD. None of the above")
  
    Q1 = input(">>> ")

    if Q1 == "A" or Q1 == "a":
      print("\nYou were wrong...")
      dead()

    elif Q1 == "B" or Q1 == "B":
      print("\nYou were wrong...")
      dead()

    elif Q1 == "C" or Q1 == "c":
      print("\nThe sphinx looks amused that you knew the answer. It then proceeds into asking the second question. \"What is x if x = log 10\" \n\nIs it...\nA. 10\nB. 0\nC. 5\nD. 1")

      Q2 = input(">>> ")

      if Q2 == "A" or Q2 == "a":
        print("\nYou were wrong...")
        dead()

      elif Q2 == "B" or Q2 == "B":
       print("\nYou were wrong...")
       dead()
        
      elif Q2 == "C" or Q2 == "c":
        print("\nYou were wrong...")
        dead()
      
      elif Q2 == "D" or Q2 == "d":
        
        print("\nThe sphinx seems impressed at your knowledge and it goes on to ask you the last riddle/ \"What does x^0 equal to?\" \n\nIs it...\nA. x\nB. 1\nC. 0\nD. I deserve to die for not knowing this")

        Q3 = input(">>> ")

        if Q3 == "A" or Q3 == "a":
          print("\nYou were wrong...")
          dead()

        elif Q3 == "B" or Q3 == "B":
          ending1()

        elif Q3 == "C" or Q3 == "c":
          print("\nYou were wrong...")
          dead()

        elif Q3 == "D" or Q3 == "d":
          print("\nYou were wrong...")
          dead()
        
        else:
          print("\nPlayer tried to think outside of the box...lol")
          dead()

    elif Q1 == "D" or Q1 == "d":
      print("\nYou were wrong...")
      dead()

    else:
      print("\nPlayer tried to think outside of the box...lol")
      dead()
    
  elif troll == "B" or troll == "b":
    print("\nAs you try to run away, the smake from your hand dissipates. You then realize you are cornered between the troll and the lake. As you stand there, contemplating if you should go in the lake. The troll charges at you and your decide to jump into the lake and swim around the troll and leave through the exit. As you jump into the lake, you don't notice te gigantic snake that awaited for the right moment to strike. The snake moved towards you at an unimaginable speed and swallows you whole.")
    dead()

  elif troll == "C" or troll == "c":
    print("\nYou run and hide behind a boulder with your back facing the lake. You peak around the boulder to see the troll when water started to drop at your head. You slowly look up to see a gigantic snake looming above you. The snake swallows you whole before you could move.")
    dead()  
  
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def power():
  a = "Take Control"
  a = color.BOLD + color.RED + a + color.END
  
  print("\nYou hear voices whisper while you stand still, while the troll charges at you. You class your mind and try to clear your thoughts, the voices get louder and clearer but you are unable to understand what they are saying. As you open your eyes, the troll was 5 feet away from you. Suddely what the voices were saying became crystal clear. They were telling you to telling you to \'" + a + "\' \n\nDo you...\nA. Listen to them\nB. Ignore them and fight")
  
  voices = input(">>> ")

  if voices == "A" or voices == "a":
    print("\nThe club is moments away from being acquainted with your head, when your whole body gets on fire again. You duck down to dodge the club and raise your arms as a red hilted sword made up of molten rock appears. You raise the sword with little effort and slice the club. The troll roars in anger but you quickly slice its head off. You walk over the body and exit the cave as fast as you can.")
    sphinx()

  elif voices == "B" or voices == "b":
    print("\nYou try to bring up your sword but it seems to be missing. You look down to try and find it, realization creeps into you that the sword probably was at the bottom of the lake. You look back up at the troll just to see a club headed at your face. Your head was smashed and you instantly die.")
    dead()
  
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()



def sphinx():
  print("\nIn the total darkness, you light a small fire in your hand. You slowly walk down the corridor, cautious of your where you were steping in case there were any traps. In the end you see a sphinx guarding a pair of large golden doors.The sphinx tell you that your only chance at survival is if you can solve all 3 riddles that it tells you. You can't retreat or go forwards before solving all of the riddles, because it would kill you. The first riddle is...\nWhat is x if √x + 1 = 10\n\nIs it...\nA. 9\nB. -81\nC. 81\nD. None of the above")
  
  q1 = input(">>> ")

  if q1 == "A" or q1 == "a":
    print("\nYou were wrong...")
    dead()
  
  elif q1 == "B" or q1 == "b":
    print("\nYou were wrong...")
    dead()
  
  elif q1 == "C" or q1 == "c":
    math2()
  
  elif q1 == "D" or q1 == "d":
    print("\nYou were wrong...")
    dead()
  
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()



def math2():
  
  print("\nThe sphinx looks amused that you knew the answer. It then proceeds into asking the second question. \"What is x if x = log 10\" \n\nIs it...\nA. 10\nB. 0\nC. 5\nD. 1")

  q2 = input(">>> ")

  if q2 == "A" or q2 == "a":
    print("\nYou were wrong...")
    dead()
  
  elif q2 == "B" or q2 == "b":
    print("\nYou were wrong...")
    dead()
  
  elif q2 == "C" or q2 == "c":
    print("\nYou were wrong...")
    dead()

  elif q2 == "D" or q2 == "d":
    math3()
  
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def math3():
  print("\nThe sphinx seems impressed at your knowledge and it goes on to ask you the last riddle/ \"What does x^0 equal to?\" \n\nIs it...\nA. 1\nB. x\nC. 0\nD. I deserve to die for not knowing this")

  q3 = input(">>> ")

  if q3 == "A" or q3 == "a":
    ending()

  elif q3 == "B" or q3 == "b":
    print("\nYou were wrong...")
    dead()

  elif q3 == "C" or q3 == "c":
    print("\nYou were wrong...")
    dead()

  elif q3 == "D" or q3 == "d":
    print("\nYou were wrong...")
    dead()
  
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def ending():

  print("\nYou pass by the sphinx as it congratulates you for your knowledge and wishes you good luck. You thank it as you open the giant double-doors and enter. The doors open up to show a magnificent large throne-room in the end of it. The throne was occupied by the Kronos, the king of titans. He then gives you the choice of either joining his army or forfeit your life\n\nDo you...\nA. Fight him\nB. Say you will join his army but try to backstab him to leave\nC. Try to find your way back home to your family")
  
  king = input(">>> ")

  if king == "A" or king == "a":

    print("\nYou create a fireball in each of your hands and smirk at the titan, who just laughs. You throw then both at the sitting titan. You watch in horror as the fireballs near the titan but they slow down and completely stop in the air infront the now smirking titan. He watches the 2 balls of fire in interest and tell you of how you are forgetting that he is the titan of time for a reason. He then distinguishes the fire with his thumb and index finger, like one would do to a candle. He then stand up and picks up his double axes that were laying against the throne. You growl and extend your hands out and a heavy double-handed sword appears in it. Kronos stood still waiting for you to make the first move. You charge straight at Kronos while raising the sword. As you got close to him, you brough your sword down in a deadly arch. You yelled a war cry as the sword was about to make contact with the unmoving titan. Just then, you slow do to a complete stop. Kronos just grinned maniacally as he raised a single axe and beheaded you.")
    dead()

  elif king == "B" or king == "b":

    print("\nYou bow before him stating that you would be honored to be part of his army and to serve him to your end. As you are facing the ground, you use you fire powers to make a dagger made of pure magma, behind your back in your right hand where he couldn't see it. Kronos laughs while getting up and turns around. You build a fire ball in your left hand and throw it straight at the titan's back. You are shocked as the fireball slows down to a complete stop right before it was about to hit him. He tell you of how you forgot that he is the titain of time. He turns around with an axe and in each of his hands. He brings them forth in an attempt to behead you. You try to move out of the way but are horrified when you realize you are unable to move. You look up to see Kronos smirk at you just as the axe reaches you.")
    dead()

  elif king == "C" or king == "c":

    print("\nYou try to leave through the doors but they are locked and won't budge. The titan laughs as a dozen trolls enter throug a side oor and surround you. You did not have a chance and where quickly overwhelmed.")
    dead()
  
  else:

    print("\nPlayer tried to think outside of the box...lol")
    dead()


def ending1():

  print("\nYou pass by the sphinx as it congratulates you for your knowledge and wishes you good luck. You thank it as you open the giant double-doors and enter. The doors open up to show a magnificent large throne-room in the end of it. The throne was occupied by the Kronos, the king of titans. He then gives you the choice of either joining his army or forfeit your life\n\nDo you...\nA. Fight him\nB. Say you will join his army but try to backstab him to leave\nC. Try to find your way back home to your family")
  
  king = input("\n>>> ")

  if king == "A" or king == "a":

    print("\nYou create a ball of pure black energy with both of your hands and smirk at the titan, who just laughs. You throw the ball right at the Kronos, who seems impressed. He complements the power you have over shadows and tries to push the ball away with the back of his hand. Instead, the ball exploded in his face making him incapable of seeing you. You then bring back the dagger that was made of darkness and try to summon the troll like the voices told you. When Kronos is able to see again, he stands up and grabs two axes that were leaning against the throne. He then bellows a war cry as he swings both of the axes at the same time but dodge the attack moving towards the door. The titan keeps pushing you forwards, trying to corner you. When your back touches the giant doors, Kronos grins as he swings his axes once more. You then quickly jump up over the titan and land behind him. You summon the troll and you both corner the titan. The troll was swinging his club and distracting the titan while you decapitated the titan's head. You stood there, over the body of Kronos when the troll drops on one knee and hails you as the new king. You smirk and make your way to the your throne.")
    win()

  elif king == "B" or king == "b":
    print("\nYou bow before him stating that you would be honored to be part of his army and serve him to your end. As you are facing the ground, you use your powers over darkness to bring back the shadow dagger behind your back, so that Kronos could not see it. Kronos laughs while getting up and turns around. You build a ball black energy in your left hand and throw it straight at the titan's back. You are shocked as the ball slows down to a complete stop right before it was about to hit him. Kronos tells you of how you forget that he is the titan of time for a reason. He turns around with an axe in each hand . He brings them forth in a deadly arch, aiming straight for your head. You try to move out of the way but are horrified when you realize you are moving too slowly, as if you were trying to run in jello. You look up to see Kronos smirk at you just as the axes reaches you and you meet your bloody end.")
    dead()

  elif king == "C" or king == "c":
    print("\nYou try to leave through the doors but they are locked and won't budge. The titan then stands up and sighs as he gathers his twin axes. You where about to bring forwards your shadow knife, when the titan appears in front of your face with both axes imbedded into your body.")
    dead()
  
  else:
    print("\nPlayer tried to think outside of the box...lol")
    dead()


def win():
    print("""\n\n  ------------------
  ------------------
  ---- You Won -----
  ------------------
  ------------------""")

intro()