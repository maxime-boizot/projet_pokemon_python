import time
from lore.cynthiaLines import *
from lore.interactionsLines import *
from lore.lore import *
from functions.prompting import *


print(pokemon_logo)
time.sleep(3)
clear_screen()

time.sleep(0.5)
prompting(lore1)
time.sleep(1)
prompting(lore2)

time.sleep(2)
clear_screen()
prompting(lore3)

time.sleep(1)
clear_screen()
print("Cynthia :")
prompting(startDial)