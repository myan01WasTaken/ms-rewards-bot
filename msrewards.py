#---------------------------------------
#ms rewards bot by myan01
howManySearches = 35
minSearchDelay = 7
maxSearchDelay = 10
#customize these however you'd like
#---------------------------------------
import pyautogui
import time
import tkinter
import random
from tkinter import messagebox
words = [
    "apple", "river", "mountain", "galaxy", "whisper", "freedom", "lantern", "breeze", "horizon", "thunder",
    "crystal", "shadow", "echo", "journey", "silence", "flame", "compass", "emerald", "meadow", "harmony",
    "frost", "tide", "canyon", "sapphire", "mirror", "storm", "desert", "melody", "vine", "autumn",
    "star", "dream", "stone", "lighthouse", "forest", "riverbank", "sky", "glow", "pearl", "dawn",
    "ocean", "sand", "twilight", "cave", "feather", "flame", "stream", "dusk", "leaf", "hill",
    "village", "city", "cloud", "flamewood", "labyrinth", "bridge", "moss", "cliff", "gate", "echoing",
    "lanterns", "valley", "canyoning", "ripple", "prism", "frostbite", "moonlight", "spark", "ember", "silence",
    "glimmer", "meadowland", "thicket", "grove", "canyonfall", "glacier", "iceberg", "reef", "island", "voyage",
    "compassrose", "current", "waterfall", "spring", "pond", "rain", "monsoon", "season", "harvest", "orchard",
    "blossom", "petal", "root", "branch", "bark", "soil", "seed", "sprout", "bloom", "fruit"
]
totaltime = 0
wait = 0

messagebox.showinfo("a", "after you click ok move your mouse to where we should clikc to search (you have 5 seconds)")
time.sleep(5)
pyautogui.click()

for i in range(howManySearches):
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(random.choice(words), interval=0.05)
    pyautogui.press("Enter")
    wait = random.randint(minSearchDelay, maxSearchDelay)
    print(f"waiting {wait} seconds")
    time.sleep(wait)
    pyautogui.click()
    print(f"{(i + 1)} searches complete out of {howManySearches}")
    totaltime += wait
    print(f"{totaltime // 60}:{(totaltime % 60):02d} elapsed")
    print(f"estimated time remaining: {(minSearchDelay*((howManySearches - 1)-i)) // 60}:{((minSearchDelay*((howManySearches - 1)-i)) % 60):02d} - {(maxSearchDelay*((howManySearches - 1)-i)) // 60}:{((maxSearchDelay*((howManySearches - 1)-i)) % 60):02d}")
    print("-----------------------------")


# print(pyautogui.position())