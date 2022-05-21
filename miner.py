import string
import colorama
from colorama import *
import random
import time

init()
def main():
    address=input("Enter your ETH address: ")
    print("OK")
    characters=string.ascii_lowercase+string.digits
    for _ in range(100000):
        print(Fore.RED + "> %s | 0.00000 ETH" % "".join(random.sample(characters,32)))
    time.sleep(0.5)
    print(Fore.GREEN + "> %s | 1.23838 ETH" % "".join(random.sample(characters,32)))
    time.sleep(0.5)
    print(Fore.WHITE + "> Attempting to transfer to your wallet...")
    time.sleep(3)
    print(Fore.WHITE + "> Done transfering ETH to wallet!")
main()
