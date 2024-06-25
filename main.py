import random

happy = ("ELO - Mr. Blue Sky", "Chuu - Underwater", "Chuu - Hitchhiker")
sad   = ("$uicideBoy$ - Antartica", "SadSvit - Небо", "Molchat Doma - Sudno")
angry = ("Jasiah - Lockdown", "Pouya - Vengeance", "Yakui the Maid - All about your fears")
calm  = ("Tears For Fears - Everybody Wants to Rule the World", "DVRST - Close Eyes", "DVRST - My Toy")
def vibe_check():
    print("Como você está se sentindo hoje? ")
    print("1 - Feliz")
    print("2 - Triste")
    print("3 - Irritado")
    print("4 - Calmo")
    response = int(input())

    match response:
        case 1:
            index = random.randint(0,2)
            print(happy[index])
        case 2:
            index = random.randint(0,2)
            print(sad[index])
        case 3:
            index = random.randint(0,2)
            print(angry[index])
        case 4:
            index = random.randint(0,2)
            print(calm[index])

vibe_check()
            

