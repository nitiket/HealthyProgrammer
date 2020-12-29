from pygame import mixer
from datetime import datetime
from time import time
c = 0

def music(file):
    mixer.init()  # Starting the mixer
    mixer.music.load(file)  # Loading the song
    mixer.music.set_volume(1)  # Setting the volume
    mixer.music.play()  # Start playing the song
    q = input("\nEnter 'Done' to stop music and 'exit' to exit the program : ")
    q.lower()
    if q == "done":
        mixer.music.stop()
    elif q == "exit":
        print("Thank You !!! , See you next time !")
        exit()

def log(w):
    f = open("log.txt", "a")
    f.writelines(w)
    f.close()

if __name__ == '__main__':
    print("\n ++++++++++ : HEALTHY PROGRAMMER : ++++++++++")
    print("( We care for your thirst, eyes and physical health ... )")
    print("\n *MENU*")
    print("\n1.Set drinking timer\n2.Set eye timer\n3.Set exercise timer\n")

    d = int(input("\nIn how many minutes you want to drink water ?\n"))
    local_timed = float(d)
    local_timed = local_timed * 60

    d = int(input("\nIn how many minutes you want to blink eyes ?\n"))
    local_timee = float(d)
    local_timee = local_timee * 60

    d = int(input("\nIn how many minutes you want to do exercise ?\n"))
    local_timep = float(d)
    local_timep = local_timep * 60

    timed, timee, timep = time(), time(), time()

    while True:
        if time() - timed > local_timed:
            music("drink.mp3")
            w = "\n Water level covered at [ ", str(datetime.now()), " ]"
            log(w)
            timed = time()

        if time() - timee > local_timee:
            music("eyes.mp3")
            w = "\n Eyes Blinked at [ ", str(datetime.now()), " ]"
            log(w)
            timee = time()

        if time() - timep > local_timep:
            music("exercise.mp3")
            w = "\n Exercise done at [ ", str(datetime.now()), " ]"
            log(w)
            timep = time()