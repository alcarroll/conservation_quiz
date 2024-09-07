import random
import csv

class Game_speices:
    """Class to generate species for gameplay"""
    def __init__(self, banding_code_4, common_name, scientific_name, banding_code_6):
        # Initialize attributes
        self.banding_code_4 = banding_code_4
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.banding_code_6 = banding_code_6

def game_mode(answer_species_1, answer_species_2, answer_species_3, answer_species_4, full_species_data):
    """Specifications for each type of game mode"""
    # Configure modes
    common_name_mode = {'mode_name' : 'common', 'mode_description' : 'common name from its sceintific name.',
                      'correct_answer' : answer_species_1.common_name,
                      'possible_answers' : [answer_species_1.common_name, answer_species_2.common_name,
                                            answer_species_3.common_name, answer_species_4.common_name],
                       'question' : f"What is the common name for the species " + answer_species_1.scientific_name}

    scientific_name_mode = {'mode_name' : 'scientific', 'mode_description' : 'scientific name from its common name.',
                            'correct_answer' : answer_species_1.scientific_name,
                            'possible_answers' : [answer_species_1.scientific_name, answer_species_2.scientific_name,
                                                  answer_species_3.scientific_name, answer_species_4.scientific_name],
                            'question' : f"What is the scientific name for the species " + answer_species_1.common_name}

    banding_code_four_mode = {'mode_name' : 'banding_four', 'mode_description' : 'four letter banding code from its common name.',
                            'correct_answer': answer_species_1.banding_code_4,
                            'possible_answers': [answer_species_1.banding_code_4, answer_species_2.banding_code_4,
                                                 answer_species_3.banding_code_4, answer_species_4.banding_code_4],
                            'question': f"What is the 4 letter banding code for the species " + answer_species_1.common_name}

    banding_code_six_mode = {'mode_name' : 'banding_six', 'mode_description' : 'six letting banding code from its common name.',
                            'correct_answer': answer_species_1.banding_code_6,
                            'possible_answers': [answer_species_1.banding_code_6, answer_species_2.banding_code_6,
                                                 answer_species_3.banding_code_6, answer_species_4.banding_code_6],
                            'question': f"What is the six letter banding code for the species " + answer_species_1.common_name}

    # Prompt for gameplay type and accept input
    print("\n\n\nWelcome to the Conservation Quiz!\nPlease select how you would like play: \n ")
    mode_menu_selection_count = 1
    # note - figure out a way to populate this dynamically so additional modes can be added later without recoding
    modes = [common_name_mode, scientific_name_mode, banding_code_four_mode, banding_code_six_mode]
    for mode in modes:
        print(str(mode_menu_selection_count) + f": Guess a species\' {mode['mode_description']}")
        mode_menu_selection_count +=1
    game_mode_selection = int(input("Gameplay selection: "))
    game_mode = modes[game_mode_selection - 1]
    print(game_mode)

    # Format variables for passing to answer_prompt function (find clener way to do this?)
    correct_answer = (game_mode['correct_answer'])
    possible_answers = (game_mode['possible_answers'])
    random.shuffle(possible_answers)
    game_mode_setting = (f"{game_mode['mode_name']}")
    print(f"{game_mode['question']}")
    answer_prompt(correct_answer, possible_answers, game_mode_setting,full_species_data)

def answer_prompt(correct_answer, possible_answers, game_mode_setting,full_species_data):
    """Give users answer options and prompt for answer choice"""
    # Display answers
    answer_count = 1
    for name in possible_answers:
        print( f" " + str(answer_count) + ": " + name )
        answer_count += 1
    # Accept player input and check to see if it's correct then output result
    player_answer = input("\nAnswer Selection (1-4): ")
    player_answer = int(player_answer) - 1
    correct_guess = int(possible_answers.index(correct_answer))
    if player_answer == correct_guess:
        print("That's correct!")
    else:
        print(f"Nope! The correct answer was " + correct_answer )
    # Ask to play again
    play_again_prompt(game_mode_setting,full_species_data)

def play_again_prompt(game_mode_setting,full_species_data):
    """Prompt to play again. Used as a separate function to allow for error handling"""
    print("\n\nWould you like to play again?")
    play_again = input("y = yes\nn = no\nc = change mode\n:")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        generate_species(game_mode_setting,full_species_data)
    elif play_again.lower() == "c" or play_again.lower() == "change":
        start_game()
    elif play_again.lower() == "n" or play_again.lower() == "no":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid selection, please try again.")
        play_again_prompt()

def generate_species(game_mode_setting,full_species_data):
    """Generate speices class instances for game play"""
    new_species = random.choice(full_species_data)
    # Rewrite as a loop?
    answer_species_1 = Game_speices(new_species[0], new_species[1], new_species[2], new_species[3])
    new_species = random.choice(full_species_data)
    answer_species_2 = Game_speices(new_species[0], new_species[1], new_species[2], new_species[3])
    new_species = random.choice(full_species_data)
    answer_species_3 = Game_speices(new_species[0], new_species[1], new_species[2], new_species[3])
    new_species = random.choice(full_species_data)
    answer_species_4 = Game_speices(new_species[0], new_species[1], new_species[2], new_species[3])

    game_mode(answer_species_1, answer_species_2, answer_species_3, answer_species_4, full_species_data)

def start_game():
    # Set default game mode to common
    game_mode_setting = "common"
    generate_species(game_mode_setting, full_species_data)

# Populate full_species_data list with data from bird_info.csv file then start game
file = open("bird_info.csv", "r")
full_species_data = list(csv.reader(file, delimiter=","))
file.close()
start_game()