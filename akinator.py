import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

features = [
    {"name": "Shahruk Khan", "human": True, "Female": False, "youtuber": False, "movie": True , "fictional": False, "inventor": False, "indian": True},

    {"name": "Priyanka chopra", "human": True, "Female": True, "youtuber": False, "movie": True , "fictional": False, "inventor": False, "indian": True},

    {"name": "Chris Hemsworth", "human": True, "Female": False, "youtuber": False, "movie": True , "fictional": False, "inventor": False, "indian": False},

    {"name": "Ariana Grande", "human": True, "Female": True, "youtuber": False, "movie": True , "fictional": False, "inventor": False, "indian": False},

    {"name": "CV Raman", "human": True, "Female": False, "youtuber": False, "movie": False, "fictional": False, "inventor": True, "indian": True},

    {"name": "Janaki Ammal", "human": True, "Female": True, "youtuber": False, "movie": False, "fictional": False, "inventor": True, "indian": True},

    {"name": "Isaac Newton", "human": True, "Female": False, "youtuber": False, "movie": False, "fictional": False, "inventor": True, "indian": False},

    {"name": "Marie Curie", "human": True, "Female": True, "youtuber": False, "movie": False, "fictional": False,"inventor": True, "indian": False},

    {"name": "Carry Minati (Ajey Nagar)", "human": True, "Female": False, "youtuber": True, "movie": False, "fictional": False, "inventor": False, "indian": True},

    {"name": "Mostly Sane (Prajakta Koli)", "human": True, "Female": True, "youtuber": True, "movie": False, "fictional": False, "inventor": False, "indian": True},

    {"name": "PewDiePie", "human": True, "Female": False, "youtuber": True, "movie": False, "fictional": False, "inventor": False, "indian": False},

    {"name": "JENNA MARBLES ", "human": True, "Female": True, "youtuber": True, "movie": False, "fictional": False, "inventor": False, "indian": False},

    {"name": "Mogli", "human": False, "Female": False, "youtuber": False, "movie": True, "fictional": True, "inventor": False, "indian": True},

    {"name": "Jasmin", "human": False, "Female": True, "youtuber": False, "movie": True, "fictional": True, "inventor": False, "indian": True},

    {"name": "Hiccup Horrendous Haddock", "human": False, "Female": False, "youtuber": False, "movie": True, "fictional": True, "inventor": False, "indian": False},

    {"name": "Ariel", "human": False, "Female": True, "youtuber": False, "movie": True, "fictional": True, "inventor": False, "indian": False},

    {"name": "Lal Bahadur Shastri", "human": True, "Female": False, "youtuber": False, "movie": False, "fictional": False, "inventor": False, "indian": True},

    {"name": "Indira Gandhi", "human": True, "Female": True, "youtuber": False, "movie": False, "fictional": False, "inventor": False, "indian": True},

    {"name": "Barack Obama", "human": True, "Female": False, "youtuber": False, "movie": False, "fictional": False, "inventor": False, "indian": False},

    {"name": "Angela Merkel", "human": True, "Female": True, "youtuber": False, "movie": False, "fictional": False, "inventor": False, "indian": False},
]


def guess_my_character(answer, key):
    if answer == "y":
        response = True
    else:
        response = False

    filter = []

    for j in features:
        if j[key] != response:
            filter.append(j)

    for i in filter:
        features.remove(i)

    if len(features) == 1:
        print("\n\nYour character is " +features[0]["name"])
        speak("Your character is " +features[0]["name"])
        quit()



print("Hello World, Welcome to the Akinator i will try to read your mind")
speak("Hello World, Welcome to the Akinator i will try to read your mind")

print("Please guess any character from the list given below")
speak("Please guess any character from the list given below")

for i in range(len(features)):
    print(f"{i+1}). ", features[i]["name"])

speak("Press enter when you are ready")
input("\n\nPress enter when you are ready..")

print("Please answer the questions and i will try to guess your character")
speak("Please answer the questions and i will try to guess your character")

speak("is your character human")
response = input("\n\nIs your character human(y/n): ")
guess_my_character(response, "human")

speak("is your character female")
response = input("\n\nIs your character female(y/n): ")
guess_my_character(response, "Female")


speak("is your character Youtuber")
response = input("\n\nIs your character Youtuber(y/n): ")
guess_my_character(response, "youtuber")

speak("is your character movie")
response = input("\n\nIs your character in a movie(y/n): ")
guess_my_character(response,"movie")

speak("is your character fictional")
response = input("\n\nIs your character fictional(y/n): ")
guess_my_character(response,"fictional")

speak("is your character Inventor")
response = input("\n\nIs your character Inventor(y/n): ")
guess_my_character(response,"inventor")

speak("is your character Indian")
response = input("\n\nIs your character Indian(y/n): ")
guess_my_character(response,"indian")


