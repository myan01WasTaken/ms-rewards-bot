#---------------------------------------
#ms rewards bot by myan01
howManySearches = 35
minSearchDelay = 7
maxSearchDelay = 10
minKeystrokeDelay = 0.05
maxKeystrokeDelay = 0.15
#customize these however you'd like
#---------------------------------------
import pyautogui
import time
import tkinter
import random
from tkinter import messagebox
words = [
    "apple","river","mountain","galaxy","whisper","freedom","lantern","breeze","horizon","thunder",
    "crystal","shadow","echo","journey","silence","flame","compass","emerald","meadow","harmony",
    "frost","tide","canyon","sapphire","mirror","storm","desert","melody","vine","autumn",
    "star","dream","stone","lighthouse","forest","riverbank","sky","glow","pearl","dawn",
    "ocean","sand","twilight","cave","feather","stream","dusk","leaf","hill","village",
    "city","cloud","flamewood","labyrinth","bridge","moss","cliff","gate","echoing",
    "lanterns","valley","ripple","prism","moonlight","spark","ember","glimmer","thicket","grove",
    "glacier","iceberg","reef","island","voyage","current","waterfall","spring","pond","rain",
    "season","harvest","orchard","blossom","petal","root","branch","bark","soil","seed",
    "sprout","bloom","fruit","riverstone","meadowlark","pine","cedar","willow","maple","oak",
    "ash","elm","cypress","birch","fern","ivy","rose","daisy","tulip","orchid",
    "sunflower","violet","lily","poppy","iris","lavender","sage","mint","thyme","basil",
    "pepper","ginger","cinnamon","nutmeg","clove","honey","amber","pearlite","opal","topaz",
    "diamond","ruby","emeraldine","sapphireblue","garnet","onyx","quartz","agate","jade","turquoise",
    "silver","gold","copper","bronze","iron","steel","nickel","zinc","tin","platinum",
    "cloudburst","raindrop","snowflake","hailstone","sunbeam","moonbeam","starlight","comet","meteor","planet",
    "asteroid","nebula","universe","cosmos","orbit","gravity","eclipse","solstice","equinox","aurora",
    "breezelet","gust","zephyr","hurricane","cyclone","tornado","monsoon","typhoon","stormcloud","rainbow",
    "mist","fog","dew","frostbite","icicle","hail","sleet","blizzard","avalanche","glowworm",
    "firefly","beetle","dragonfly","butterfly","moth","ant","bee","wasp","hornet","ladybug",
    "spider","cricket","grasshopper","locust","termite","aphid","mosquito","gnat","fly","caterpillar",
    "worm","snail","slug","clam","mussel","oyster","shrimp","lobster","crab","scallop",
    "salmon","trout","bass","perch","pike","cod","herring","sardine","anchovy","mackerel",
    "dolphin","whale","shark","seal","otter","penguin","albatross","gull","pelican","heron",
    "stork","flamingo","swan","goose","duck","eagle","hawk","falcon","owl","crow",
    "raven","magpie","jay","sparrow","finch","wren","robin","lark","canary","parrot",
    "macaw","cockatoo","toucan","peacock","pheasant","quail","turkey","chicken","rooster","hen",
    "pigeon","dove","partridge","woodpecker","kingfisher","hummingbird","oriole","blackbird","goldfinch","nightingale",
    "wolf","fox","coyote","jackal","dog","cat","lion","tiger","leopard","cheetah",
    "jaguar","panther","lynx","bobcat","bear","panda","koala","kangaroo","wallaby","opossum",
    "raccoon","weasel","badger","otterhound","mongoose","ferret","skunk","wolverine","marten","ermine",
    "deer","elk","moose","caribou","antelope","gazelle","giraffe","zebra","horse","donkey",
    "mule","camel","llama","alpaca","goat","sheep","cow","bull","bison","buffalo",
    "pig","boar","hippopotamus","rhinoceros","elephant","tapir","manatee","dugong","orangutan","chimpanzee",
    "gorilla","baboon","monkey","lemur","gibbon","tamarin","marmoset","sloth","anteater","armadillo",
    "pangolin","hedgehog","porcupine","rabbit","hare","squirrel","chipmunk","beaver","rat","mouse",
    "vole","lemming","hamster","gerbil","guinea","capybara","platypus","echidna","bat","mole",
    "shrew","opossumrat","wildcat","lynxcat","fisher","pinecat","crowbird","stormpetrel","sunbird","mooncat",
    "starlark","windrose","earthling","skylark","dreamer","wanderer","traveler","thinker","builder","seeker",
    "keeper","runner","flyer","diver","singer","dancer","painter","writer","reader","player",
    "friend","neighbor","helper","leader","teacher","student","parent","child","artist","maker",
    "crafter","designer","inventor","thinkerling","adventurer","explorer","captain","pilot","sailor","farmer",
    "gardener","baker","cook","chef","driver","rider","walker","climber","hiker","swimmer",
    "runnerup","sprinter","jumper","thrower","catcher","pitcher","builderman","dreamcatcher","pathfinder","starfinder",
    "moonwalker","sunseeker","cloudchaser","rainmaker","stormbreaker","winddancer","earthshaper","firesinger","watershaper","lightkeeper",
    "darkhunter","brightseer","soundweaver","wordsmith","mindcrafter","soulsearcher","heartkeeper","timewalker","spacefarer","galefinder",
    "wavebreaker","stonecarver","woodworker","ironmonger","steelmaker","glassblower","potter","weaver","spinner","knitter",
    "tailor","mason","carpenter","smith","miner","fisherman","hunter","gatherer","trader","merchant",
    "sailmaker","shipwright","navigator","astronomer","philosopher","scientist","engineer","inventor","teacherling","learner",
    "thinkermind","dreamweave","stargazer","moonwatcher","sunwatcher","cloudwatcher","stormwatcher","windwatcher","earthwatcher","firewatcher",
    "waterwatcher","lightwatcher","shadowwatcher","timewatcher","spacewatcher","pathwatcher","mindwatcher","soulwatcher","heartwatcher","worldwatcher"
]

totaltime = 0

messagebox.showinfo("a", "after you click ok move your mouse to where we should clikc to search (you have 5 seconds)")
time.sleep(5)
pyautogui.click()

for x in range(howManySearches):
    pyautogui.hotkey("ctrl", "a")

    word = random.choice(words)
    print(f"typing {word}")

    keystrokeDelayList = [
        random.uniform(minKeystrokeDelay, maxKeystrokeDelay)
        for _ in word
    ]
    print(f"typing with {keystrokeDelayList} keystroke delays")

    for i, letter in enumerate(word):
        pyautogui.typewrite(letter)
        time.sleep(keystrokeDelayList[i])

    pyautogui.press("Enter")

    wait = random.randint(minSearchDelay, maxSearchDelay)
    print(f"waiting {wait} seconds")
    time.sleep(wait)

    pyautogui.click()

    print(f"{(x + 1)} searches complete out of {howManySearches}")
    totaltime += wait
    print(f"{totaltime // 60}:{(totaltime % 60):02d} elapsed")
    print(f"estimated time remaining: {(minSearchDelay*((howManySearches - 1)-x)) // 60}:{((minSearchDelay*((howManySearches - 1)-x)) % 60):02d} - {(maxSearchDelay*((howManySearches - 1)-x)) // 60}:{((maxSearchDelay*((howManySearches - 1)-x)) % 60):02d}")
        
    print("-----------------------------")


# print(pyautogui.position())
