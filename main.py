import stat_cal as stat
import ev_calc as ev


def stat_calc(stat_data): 
    
    total_hp = stat.compute.hp(stat_data)
    print("The total hp is ")
    print(total_hp)

    
    other_stat = stat.compute.other_stat(stat_data)
    print("The other stat is ")
    print(other_stat)

    option(stat_data)


def ev_calc(stat_data): 
    print("You are about to compute the ev's needed to increase stat")
    print("please enter your desired stat increase")    
    stat = int(input())
    stat_data["stat"] = stat

    eve_needed = ev.compute.ev_needed(stat_data)
    print("The ev needed is: ")
    print(eve_needed)

    option(stat_data)



def computation_type(data):
    print("Please choose type of calculation")
    print("-Stat calculation")
    print("-Ev calculation")

    opt = int(input())

    if(opt == 1):
        stat_calc(data)

    elif(opt == 2):
        ev_calc(data)
    else:
        print("Invalid input") 


def start():

    print("I need some information to proceed on calculation")
    print("Please enter the following input")

    print("please enter the base hp")
    base = int(input())

    flag = 1
    while flag == 1:
        print("Please enter the IV between 0-31")
        iv = int(input())
        if(iv >= 0 and iv <= 31):
            flag = 2


    flag2 = 1
    while flag2 == 1:
        print("Please enter the EV between 0-255")
        ev = int(input())
        if(ev >= 0 and ev <= 255):
            flag2 = 2

    print("please enter the level")
    level = int(input())


    print("pleease type of nature")
    print("1. Benificial")
    print("2. Hindering")
    natureInput = int(input())

    if natureInput == 1:
        nature = 1.1
    elif natureInput == 2:
        nature = 0.9
    else: 
        nature = 1.1


    stat_data = {
        "base": base,
        "iv": iv,
        "ev": ev,
        "level": level,
        "nature": nature
    }

    computation_type(stat_data)




def option(data): 
    print("1. To choose other computation")
    print("2. To start again")

    x = int(input())

    if( x == 1): 
        computation_type(data)
    elif( x == 2):
        start()
    else:
        start()


start()
