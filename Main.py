# Sami Abu Rmaileh & Malak Raddad .
# ID : 1192325 & ID : 1192408.
# We certify that this submission is the original work of members of the group and meets.
# the Faculty's Expectations of Originality Expectations of Originality.
# we start the project in 12/5/2023 friday. 
import time
import winsound
sound_file1 = "sounds\Welcome_back.wav"
sound_file2 = "sounds\Hi.wav"
sound_file3 = "sounds\made.wav"
sound_file4 = "sounds\Ai.wav"
sound_file5 = "sounds\option.wav"
sound_file6 = "sounds\diff.wav"
sound_file7 = "sounds\op.wav"
sound_file8 = "sounds\Fullmark.wav"




# first welcome to our game 
def print_welcome():
    winsound.PlaySound(sound_file1, winsound.SND_FILENAME)
    time.sleep(1)
    print("Hi My Name is Malak Raddad \nMy partner is Sami Abu Rmaileh.")
    winsound.PlaySound(sound_file2, winsound.SND_FILENAME)
    time.sleep(1)
    print("We made this game as an AI course project.")
    winsound.PlaySound(sound_file3, winsound.SND_FILENAME)
    time.sleep(1)
    print("The AI in our game depends on Minimax algorithm.")
    winsound.PlaySound(sound_file4, winsound.SND_FILENAME)
    time.sleep(1)
    print("There is 3 option to play every option have 3 difficulty options\n Easy \n Normal \n Hard.")
    winsound.PlaySound(sound_file5, winsound.SND_FILENAME)
    time.sleep(1)
    print("The difficulty in our game depends on time\nThe Easy has no time to play.")
    print("The Normal every player have 5 secands to play every turn.")
    print("The hard one we reduction the time to 3 secands every turn.")
    winsound.PlaySound(sound_file6, winsound.SND_FILENAME)
    winsound.PlaySound(sound_file8, winsound.SND_FILENAME)
    # then choics what you want to play then the difficulty .
    print("Please choose an option:")
    print("1. Manual entry for both ■'s moves and □'s moves.")
    print("2. Manual entry for ■'s moves & automatic moves for □.")
    print("3. Manual entry for □'s moves & automatic moves for ■.")

def print_difficulty_options():
    print("Choose a difficulty level:")
    winsound.PlaySound(sound_file7, winsound.SND_FILENAME)
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")

print_welcome()
user_choice = input("Enter your choice (1, 2, or 3): ")

if user_choice == "1":
    print_difficulty_options()
    difficulty_choice = input("Enter your difficulty choice (1, 2, or 3): ")

    if difficulty_choice == "1":
        import FME as mode_module
    elif difficulty_choice == "2":
        import FMN as mode_module
    elif difficulty_choice == "3":
        import FMH as mode_module
    else:
        print("Invalid difficulty choice!")
        exit()

elif user_choice == "2":
    print_difficulty_options()
    difficulty_choice = input("Enter your difficulty choice (1, 2, or 3): ")

    if difficulty_choice == "1":
        import MAE as mode_module
    elif difficulty_choice == "2":
        import MAN as mode_module
    elif difficulty_choice == "3":
        import MAH as mode_module
    else:
        print("Invalid difficulty choice!")
        exit()

elif user_choice == "3":
    print_difficulty_options()
    difficulty_choice = input("Enter your difficulty choice (1, 2, or 3): ")

    if difficulty_choice == "1":
        import AME as mode_module
    elif difficulty_choice == "2":
        import AMN as mode_module
    elif difficulty_choice == "3":
        import AMH as mode_module
    else:
        print("Invalid difficulty choice!")
        exit()

else:
    print("Invalid choice!")
    exit()