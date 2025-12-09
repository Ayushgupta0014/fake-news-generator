#1 - import the random module
import random
#2 - create subjects
subjects = [
    "Sharukhan",
    "A group of buffaloes",
    "Auto rikshaw driver from Delhi",
    "Virat Kohli",
    "Nirmala sitaraman",
    "Prime Minister Modi"
]

actions = [
    "Launches",
    "cancels",
    "dance with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plote of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

#3 - start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do You Want another headline? (yes/no)").strip()  #stip removes space
    if user_input == "no":
        break

#print goodbye  message
print("\nThanks for using the Fake News Headline Generator.Have a fun Day")
