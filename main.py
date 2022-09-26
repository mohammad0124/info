import os, platform, time, sys
import cowsay
from colorama import Fore

name = platform.uname()


def Ok():
    os.system("clear" or "cls")

    a = int(input("Hello enter the platform:\n1)System\n2)node\n3)release\n4)version\n5)machine\n6)developer"
                  "\n7)exit "
                  "\nchoose:"))
    if a == 1:
        name.system == "Linux"
        print(cowsay.tux(Fore.GREEN + "Hello your system is Linux"))

        print(Fore.LIGHTBLUE_EX + f"Hello your system is {name.system}")
    elif a == 1:
        name.system == "Windows"

        print(cowsay.dragon(Fore.RED + "Hello your System is Windows"))

        print(Fore.LIGHTBLUE_EX + f"Hello your system is {name.system}")

    elif a == 2:
        print(Fore.LIGHTBLUE_EX + f"Hello your node is {name.node}")

    elif a == 3:
        print(Fore.LIGHTBLUE_EX + f"Hello your release is {name.release}")

    elif a == 4:
        print(Fore.LIGHTBLUE_EX + f"Hello your version is {name.version}")

    elif a == 5:
        print(Fore.LIGHTBLUE_EX + f"Hello your TypeSystem is {name.machine}")

    elif a == 6:
        print(Fore.LIGHTBLUE_EX + "Hello my name is Mohammad :)")

    elif a == 7:
        sys.exit("Hello exit")

    else:
        print("try agin")

        time.sleep(2)
        return Ok()


Ok()
