"""
Ward Anderson
CS 111
Dr. Kelley
CS Final Project Code: Basketball Game
5/2/18
"""

import random
import image
import pylab #from stack (https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible)
import matplotlib.pyplot
import numpy #with help of dr. kelley
shot_list = ["left corner 3-point shot", "left wing 3-point shot", "straight up 3-point shot", "right wing 3-point shot", "right corner 3-point shot", "left baseline 2-point shot", "left wing 2-point shot", "straight up 2-point shot", "right wing 2-point shot", "right baseline 2-point shot",  "left High Paint 2-point shot", "right High Paint 2-point shot", "left Low Paint 2-point shot", "right Low Paint 2-point shot"]
strength_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
defensive_list = ["Defensive Pressure", "No Defensive Pressure", "Shot is Blocked"] #three options for defensive pressure 
user_point_tally = 0
user_FGA = []
user_FGM =[]
user_FGpercent = []

def rules_of_game():
    """
    Purpose:
        Prints rules of the Basketball Game 
    Parameters:
        None
    Return Value:
        None
    """
    #parameters of game
    print("\n")
    print("Welcome to Python's Basketball Shooting Game.\n")

    print("Before playing, you should be aware of the following parameters: \n")

    print("\t #1: In basketball, a 'field goal' is a shot attempted from the court \n")

    print("\t #2: In this game you will be prompted to select from a shot form the 14")
    print("\t different shots below: (visualized on actual court to your left)")
    print("\t \t 1 = left corner 3-point shot (yellow)")
    print("\t \t 2 = right corner 3-point shot (yellow)")
    print("\t \t 3 = left wing 3-point shot (yellow)")
    print("\t \t 4 = straight up 3-point shot (yellow)")
    print("\t \t 5 = right wing 3-point shot (yellow)")
    print("\t \t 6 = left baseline 2-point shot (red)")
    print("\t \t 7 = left wing 2-point shot (red)")
    print("\t \t 8 = straight up 2-point shot (red)")
    print("\t \t 9 = right wing 2-point shot (red)")
    print("\t \t 10 = right baseline 2-point shot (red)")
    print("\t \t 11 = left high paint 2-point shot (green)")
    print("\t \t 12 = right high paint 2-point shot (green)")
    print("\t \t 13 = left low paint 2-point shot (green)")
    print("\t \t 14 = right low paint 2-point shot (green)\n")

    print("\t#4: Each shot from the floor requires a certain level of strength in")
    print("\t order to make the shot:")
    print("\t\ta. The strength scale is between 1 (low strength) and 10")
    print("\t\t (high strength)")
    print("\t\tb. The further the shot is from the basket,")
    print("\t\tthe more difficult the shot is to make.")
    print("\t\t\t i. ex: 3-point shot is further than low-paint)\n")

    print("\t#5: This game will track the amount of points you score and update after")
    print("\teach shot:")
    print("\t\t a. If you make a 3-point shot, 3 points will be added to your")
    print("\t\tscore")
    print("\t\t b. If you make a 2-point shot, 2 points will be added to your")
    print("\t\tscore")
    print("\t\t c. If you miss a shot, either due to the incorrect strength or")
    print("\t\tthe defender blocked your shot, 0 points will be added to your")
    print("\t\tscore\n")

    print("\t6: Additionally this game will calculate your Field Goal Percentage")
    print("\t(FG%)")
    print("\t\tand update after each shot:")
    print("\t\ta. FG% is calculated by dividing the total number of Field Goals")
    print("\t\t(shots) made by the total number of Field Goals (shots)")
    print("\t\tattempted")
    print("\t\tb. If your FG% > 40%, than you will be considered an 'effective")
    print("\t\tbasketball shooter'")
    print("\t\tc. If your FG% < 40% than you will be considered an 'ineffective")
    print("\t\tbasketball shooter'\n")


    print("\t#7: Lastly, if you make a certain shot you cannot choose the same shot")
    print("\tagain\n")
        
def user_walkup_story(user_name):
    """
    Purpose:
        Create fun story using user's inputted user_name before they take shot
    Parameters:
        user_name: user's inputted name for game
    Return value:
        None
    """

    #fun background story
    print("\t***GET HYPED!!!***")
    print("\t"+user_name+"'s heart is beating fast as", user_name)
    print("\twalks down the tunnel and feels an adrenline rush.\n")
    print("\tCapital One Arena's lights turn on with a FLASH and the crowd goes")
    print("\tWILD as", user_name, "walks onto the court! The crowd chants, 'We want",user_name.upper()+"'")
    print("\tand again, 'we want", user_name.upper()+"'\n")
    print("\tWill", user_name, "perform under the big lights and pressure of the NBA?\n")
    print("\tWill a defender block", user_name+"'s shot?\n")
    print("\tDoes", user_name, "have what it takes to be part of the Washington Wizards?\n")
    print("\n")

def fgPercentage_linePlot(user_FGM, user_FGA): 
    """
    Purpose:
        Plot fluctuation in user's Field Goal Percentage (FG%) based on their selected number of shots
    Parameters:
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA) 
    Return value:
        line plot that represents fluctuation in user's Field Goal Percentage (FG%) based on their selected number of shots (FG% vs. FGA)
    Citations:
        pylab module and more specifically pylab.legend(loc = "upper right") used from stack query in order to get legend and position
        pylab.plot(range(1, len(user_FGA)+1), user_FGpercent, label = "FG%") created with help of Dr. Kelley
        pylab.xticks(numpy.arange(1, len(user_FGA)+1), range(1, len(user_FGA)+1)) created with help of Dr. kelley and matplotlib.pyplot function documentation online 
    """
    
    pylab.plot(range(1, len(user_FGA)+1), user_FGpercent, label = "FG%") #with help of Dr. Kelley
    pylab.legend(loc = "upper right") #from stack (https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible)
    pylab.ylabel("Field Goal Percentage (FG%)")
    pylab.xlabel("Number of shots")
    pylab.ylim(0, 100)
    pylab.xticks(numpy.arange(1, len(user_FGA)+1), range(1, len(user_FGA)+1)) #with help of Dr. kelley
    pylab.title("Field Goal Percentage (FG%) vs. Number of Shots")
    pylab.show()


#3's outcome
def made3ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '1' to indicate made shot
            -appends user_FGA list with '1' to indicate shot attempt
            -appends user_FGpercent list with FG% after made shot
            -adds 3 points to their point tally
            -tells the user they made the shot, as there was no defender and the corect strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
        
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(1)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=3
    print(user_name, "MADE a 3 point shot! No defensive pressure and correct strength value was selected. NICE JOB :)\n")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

def miss3ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '0' to indicate missed shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after made shot
            -adds 0 points to their point tally
            -tells the user they missed the shot, as there was no defender, but the incorect strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(0)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=0
    print(user_name, "MISSED a 3 point shot! Although there was no defensive pressure, your strength value was INCORRECT. Better luck next time :(")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

def miss3ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '0' to indicate missed shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after made shot
            -adds 0 points their point tally
            -tells the user they missed a 3-point shot, as the defender blocked their shot, although the correct strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(0)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=0
    print(user_name, "MISSED a 3 point shot! Eventhough you iputted the correct strength value, the defender BLOCKED your shot! Better luck next time :(")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

def miss3ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '0' to indicate missed shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after made shot
            -adds 0 points their point tally
            -tells the user they missed a 3-point shot, as the defender blocked their shot, and the incorrect strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(0)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=0
    print(user_name, " MISSED a 3 point shot! Unfortunately, you inputted the incorrect strength value and the defender BLOCKED your shot! Better luck next time :( \n")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

#2's outcome
def made2ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '1' to indicate made shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after made shot
            -adds 2 points their point tally
            -tells the user they made a 2-point shot, as no defensive pressure, and the correct strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(1)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=2
    print(user_name, "MADE a 2 point shot! No defensive pressure and correct strength value was selected. NICE JOB :)\n")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

def miss2ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '0' to indicate missed shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after missed shot
            -adds 0 points their point tally
            -tells the user they missed a 2-point shot, as no defensive pressure, but the incorrect strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(0)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=0
    print(user_name, "MISSED a 2 point shot! Although there was no defensive pressure, your strength value was INCORRECT. Better luck next time :(")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

def miss2ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '0' to indicate missed shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after missed shot
            -adds 0 points their point tally
            -tells the user they missed a 2-point shot, as the defender blocked their shot, although the correct strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(0)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=0
    print(user_name, "MISSED a 2 point shot! Eventhough you iputted the correct strength value, the defender BLOCKED your shot! Better luck next time :(")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA

def miss2ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -appends user_FGM list with '0' to indicate missed shot
            -appends user_FGA list with '1' to indicate attempt shot
            -appends user_FGpercent list with FG% after missed shot
            -adds 0 points their point tally
            -tells the user they missed a 2-point shot, as the defender blocked their shot, and the incorrect strength value was inputted
            -tells the user their point tally
            -tells the user their FG%
    Parameters:
        user_name: user's inputted name for game
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    user_FGM.append(0)
    user_FGA.append(1)
    user_FGpercent.append((sum(user_FGM)/len(user_FGA) * 100)) #calculating field goal percentage and appending to user_FGpercent list after shot
    user_point_tally +=0
    print(user_name, " MISSED a 2 point shot! Unfortunately, you inputted the incorrect strength value and the defender BLOCKED your shot! Better luck next time :( \n")
    print(user_name, "has a point tally of:", user_point_tally, "\n")
    print(user_name, "has a Field Goal Percentage (FG%):", str((sum(user_FGM)/len(user_FGM)) * 100),"%", "\n")
    return user_FGM, user_FGA
    
#shot function
def shot(user_point_tally, user_FGM, user_FGA):
    """
    Purpose:
        Multiple:
            -prompts the user how many shots they want to take
            -prompts the user for their user_name for the game
            -determines if the user is excited to play the game
            -asks the user to select one shot (from 14 shown on image)
            -asks the user to select strength for selected shot (1-10)
            -chooses randomly from list of defensive pressure if defender will block shot
            -determines if user will make or miss their shot
            -uses 2pt or 3pt helper functions (8 functions above) to tell user if they made or missed the shot, their point tally, and field goal percentage based on their inputted shot and strength values            
    Parameters:
        user_point_tally: user's total points after each shot
        user_FGM: list that contains '0' to indicate a missed shot and '1' to indicate a made shot
        user_FGA: list that contains (n) amount of '1's to represent the user's Field Goal's Attempted (FGA)
    Return value:
        user_FGM (number of field goals (shots) user has made succesfully)
        user_FGA (number of field goals (shots) user has attempted)
    """
    print("***Please READ the game guidelines ABOVE so you can have FUN!***")
    print("\n")
    shot_number = int(input("\tHow many shots would you like to take? "))
    print("\n")
    user_name = str(input("\tWhat is your 'baller's name' for this AWESOME game? ")) #prompting user to enter their user_name for game
    print("\n")
    excited = input("\tAre you excited to play? Please type '1' for yes and '2' for no: ")
    print("\n")
    if excited == "1":
        print("\t\tAWESOME! It's time to test your basketball shooting abilities!")
    else:
        print("\t\tThat's unfortunate. Get EXCITED to test your basketball shooting")
        print("\t\tabilities!")
    print("\n")
    user_walkup_story(user_name)
    made_shots = []
    for i in range(shot_number):
        print("\t***SHOT:***")
        player_shot_1 = int(input("\tPlease type an integer from the IMAGE on the LEFT to select a shot: "))
        while player_shot_1 in made_shots: #preventing user from taking same shot in same spot if already made (ex: cannot take shot number 2 again if already have made)
            player_shot_1 = int(input("\tSorry you cannot take the same shot if you already made it :( . Please choose another shot: "))
        print("\n")
        shot_1_strength = int(input("\tType an integer (1-10) to guess the strength needed for your shot: "))
        print("\n")
        defensive_press_1 = random.choice(defensive_list) #randomly choosing from defensive_list at beginning (["Defensive Pressure", "No Defensive Pressure", "Shot is Blocked"] ) to determine if "Shot is Blocked"

        #***CORNER 3's***
        #a. if left corner 3  or right corner 3 are selected, no defensive pressure, and correct strength
        if (player_shot_1 == 1 or player_shot_1 == 5) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength == 9 or shot_1_strength == 10): 
            made3ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)
            made_shots.append(player_shot_1)
            
        #b. if left corner 3 or right corner 3 are selected, no defensive pressure, and incorrect strength
        elif (player_shot_1 == 1 or player_shot_1 == 5) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength != 9 and shot_1_strength != 10):
            miss3ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)


        #c. if left corner 3 or right corner 3 are selected, defensive pressure, and correct strength       
        elif (player_shot_1 == 1 or player_shot_1 == 5) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength == 9 or shot_1_strength == 10):
            miss3ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #d. if left corner 3 or right corner 3 are selected, defensive pressure, and incorrect strength
        elif (player_shot_1 == 1 or player_shot_1 == 5) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength != 9 and shot_1_strength != 10):
            miss3ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #***TOP 3's***
        #a. if left wing 3, straight up 3, or right wing 3 are selected, no defensive pressure, and correct strength
        elif (player_shot_1 == 2 or player_shot_1 == 3 or player_shot_1 == 4) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength == 7 or shot_1_strength == 8):
            made3ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)
            made_shots.append(player_shot_1)
            

        #b. if left wing 3, straight up 3, or right wing 3 are selected, no defensive pressure, and incorrect strength
        elif (player_shot_1 == 2 or player_shot_1 == 3 or player_shot_1 == 4) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength != 7 and shot_1_strength != 8):
            miss3ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)
            
        #c. if left wing 3, straight up 3, or right wing 3 are selected, defensive pressure, and correct strength
        elif (player_shot_1 == 2 or player_shot_1 == 3 or player_shot_1 == 4) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength == 7 or shot_1_strength == 8):
            miss3ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)
            
        #d. if left wing 3, straight up 3, or right wing 3 are selected, defensive pressure, and incorrect strength
        elif (player_shot_1 == 2 or player_shot_1 == 3 or player_shot_1 == 4) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength != 7 and shot_1_strength != 8):
            miss3ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #***regular 2's***
        #a. if left baseline 2-point shot, left wing 2-point shot, straight up 2-point shot, right wing 2-point shot, or right baseline 2-point shot, no defensive pressure, and correct strength
        elif (player_shot_1 == 6 or player_shot_1 == 7 or player_shot_1 == 8 or player_shot_1 == 9 or player_shot_1 == 10) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength == 5 or shot_1_strength == 6):
            made2ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)
            made_shots.append(player_shot_1)

        #b. if left baseline 2-point shot, left wing 2-point shot, straight up 2-point shot, right wing 2-point shot, or right baseline 2-point shot, no defensive pressure, and incorrect strength
        elif (player_shot_1 == 6 or player_shot_1 == 7 or player_shot_1 == 8 or player_shot_1 == 9 or player_shot_1 == 10) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength != 5 and shot_1_strength != 6):
            miss2ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #c. if left baseline 2-point shot, left wing 2-point shot, straight up 2-point shot, right wing 2-point shot, or right baseline 2-point shot, defensive pressure, and correct strength
        elif (player_shot_1 == 6 or player_shot_1 == 7 or player_shot_1 == 8 or player_shot_1 == 9 or player_shot_1 == 10) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength == 5 or shot_1_strength == 6):
            miss2ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #d. if left baseline 2-point shot, left wing 2-point shot, straight up 2-point shot, right wing 2-point shot, or right baseline 2-point shot, defensive pressure, and incorrect strength
        elif (player_shot_1 == 6 or player_shot_1 == 7 or player_shot_1 == 8 or player_shot_1 == 9 or player_shot_1 == 10) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength != 5 and shot_1_strength != 6):
            miss2ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #***high paint 2's***
        #a. if left high paint 2-point shot or right high paint 2-point shot, no defensive pressure, and correct strength
        elif (player_shot_1 == 11 or player_shot_1 == 12) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength == 3 or shot_1_strength == 4):
            made2ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)
            made_shots.append(player_shot_1)

        #b. if left high paint 2-point shot or right high paint 2-point shot, no defensive pressure, and incorrect strength
        elif (player_shot_1 == 11 or player_shot_1 == 12) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength != 3 and shot_1_strength != 4):
            miss2ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #c. if left high paint 2-point shot or right high paint 2-point shot, defensive pressure, and correct strength
        elif (player_shot_1 == 11 or player_shot_1 == 12) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength == 3 or shot_1_strength == 4):
            miss2ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #d. if left high paint 2-point shot or right high paint 2-point shot, defensive pressure, and incorrect strength
        elif (player_shot_1 == 11 or player_shot_1 == 12) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength != 3 and shot_1_strength != 4):
            miss2ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)
                
        #***low paint 2's***
        #a. if left low paint 2-point shot or right low paint 2-point shot, no defensive pressure, and correct strength
        elif (player_shot_1 == 13 or player_shot_1 == 14) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength == 1 or shot_1_strength == 2):
            made2ptShot_noDef_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)
            made_shots.append(player_shot_1)

        #b. if left low paint 2-point shot or right low paint 2-point shot, no defensive pressure, and incorrect strength
        elif (player_shot_1 == 13 or player_shot_1 == 14) and (defensive_press_1 != "Shot is Blocked") and (shot_1_strength != 1 and shot_1_strength != 2):
            miss2ptShot_noDef_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #c. if left low paint 2-point shot or right low paint 2-point shot, defensive pressure, and correct strength
        elif (player_shot_1 == 13 or player_shot_1 == 14) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength == 1 or shot_1_strength == 2):
            miss2ptShot_Def_correctStrength(user_name, user_point_tally, user_FGM, user_FGA)

        #d. if left low paint 2-point shot or right low paint 2-point shot, defensive pressure, and incorrect strength
        elif (player_shot_1 == 13 or player_shot_1 == 14) and (defensive_press_1 == "Shot is Blocked") and (shot_1_strength != 1 and shot_1_strength != 2):
            miss2ptShot_Def_incorrectStrength(user_name, user_point_tally, user_FGM, user_FGA)

    return user_FGM, user_FGA

#calling main
def main():
    """
    Purpose:
        Multiple:
            -calls rules_of_game() helper function to display rules of the game
            -uploads image that contains 14 shots user can select
            -calls shot() helper function to play game
            -calls fgPercentage_linePlot() helper function show how the user's field goal percentage fluctuates over time
    Parameters:
        None
    Return value:
        None
    """
    rules_of_game()
    penguin = image.Image(file = "WIZNICEGIF.gif", title = "List of 14 shots") #importing GIF (image with 14 shot choices) to help user select shot
    penguin.show()
    shot(user_point_tally, user_FGM, user_FGA) 
    if user_FGpercent[-1] >= 40.0: #determining if user is effective basketball shooter
        print("Congrats! You are an effective basketball shooter, based on the high FG% (by NBA standards) of: ", user_FGpercent[-1],"%") 
    else:
        print("Unfortunately, you are not an effective basketball shooter, based on the low FG% (by NBA standards) of: "+ str(user_FGpercent[-1])+"%") 
    fgPercentage_linePlot(user_FGM, user_FGA)
    #not calling image.mainloop() like we went over in office hours, but still running for some reason and not ending like it should
    
main() 
