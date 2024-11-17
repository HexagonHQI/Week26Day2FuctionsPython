#Exercise 1: What are you learning?

def display_message():
    print("I am learning functions in Python.")

#Function
#Exercise 2: What’s your favorite book?

def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Function with a book title
favorite_book("Alice in Wonderland")
#Exercise 3: Some Geography

def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Function with a city and its country
describe_city("Reykjavik")

# Call the function with a different city and country
describe_city("Paris", "France")

#Exercise 4: Random

import random

def random_number_comparison():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    
    if number1 == number2:
        print("Success! The numbers are the same:", number1)
    else:
        print(f"Fail! The numbers are {number1} and {number2}.")

# Function
random_number_comparison()

#Exercise 5: Let’s create some personalized shirts!

def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")


make_shirt()
make_shirt("medium", "Python is amazing!")
make_shirt("small", "Code more, worry less.")


#Exercise 6: Magicians

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magician_names):
    for i in range(len(magician_names)):
        magician_names[i] = f"{magician_names[i]} the Great"

# List of magician names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Make_great to modify the list
make_great(magician_names)

# Show_magicians to display the updated list
show_magicians(magician_names)