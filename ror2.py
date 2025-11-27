"""
Generate a random loadout for a run of Risk of Rain 2
"""
import sys
import numpy as np

#For allowing character to be used as an argument on the command line
try:
    CHOSEN_SURVIVOR = sys.argv[1].lower()
    SURVIVOR_IS_CHOSEN = True
except IndexError:
    SURVIVOR_IS_CHOSEN = False

#Constants
RANDOMISE_SURVIVOR_SKILLS = True
RANDOMISE_FINALE = False
SUVIVOR_LIST: list = [
"commando",
"huntress",
"bandit",
"mul-t",
"engineer",
"artificer",
"mercenary",
"rex",
"loader",
"acrid",
"captain",
"railgunner",
"void fiend",
"seeker",
"false son",
"chef",
"operator",
"drifter"
]
HIGH_NUM: int = len(SUVIVOR_LIST) - 1

#Variables
rng = np.random.default_rng()

#Functions
def pick_skills(index: int) -> None:
    """For picking a random set of skills & a skin for a chosen survivor"""

    #Skill numbers for each character for each skill type
    #                    c, h, b, m, e, a, m, r, l, a, c, r, v, s, f, c, o ,d
    misc_list =         [0, 0, 0, 4, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 0, 0]
    primary_list =      [1, 2, 2, 4, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    secondary_list =    [2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2]
    utility_list =      [2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2]
    special_list =      [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2]
    other1_list =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0]
    other2_list =       other1_list
    skin_list =         [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 3, 3, 2, 2, 2, 2, 2]

    list_of_lists: list = [
        misc_list,
        primary_list,
        secondary_list,
        utility_list,
        special_list,
        other1_list,
        other2_list,
        skin_list
        ]

    print("Your skill build will be:")

    for cur_list in list_of_lists:

        selected_character_slice: int = cur_list[index]
        #need an exception case for if a skill doesn't exist on a survivor (parameterised by a 0)
        if selected_character_slice == 0:
            continue

        chosen_skill:int = rng.integers(1, selected_character_slice, endpoint= True)
        if cur_list == skin_list:
            print(f"The chosen skin is {chosen_skill}")
        else:
            print(chosen_skill)

def pick_finale() -> None:
    """For chosing a finale for the run"""

    finale_list: list = ["annihalate", "moon", "void", "seekers", "alloyed"]
    finale_index = rng.integers(0, len(finale_list))

    chosen_finale = finale_list[finale_index]
    print(f"You will try for the {chosen_finale} ending")

if SURVIVOR_IS_CHOSEN:
    survivor_index: int = SUVIVOR_LIST.index(CHOSEN_SURVIVOR)
else:
    survivor_index: int = rng.integers(0, HIGH_NUM, endpoint= True)

print(f"You will be playing {SUVIVOR_LIST[survivor_index]}")

if RANDOMISE_SURVIVOR_SKILLS:
    pick_skills(survivor_index)
if RANDOMISE_FINALE:
    pick_finale()

#EOC
