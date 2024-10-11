#modules
import hashlib  # for reg
import json
import os  # clear terminal
import pickle
import random  # pw generator
import string  # for pw generator
import subprocess
import sys  # for running end
import time  # timer
import turtle  # draw shape

from django.db.models.expressions import result
from googletrans import Translator


#<--- close here
#██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗░░░░░░░░░░░░░░░
#██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║░░░░░░░░░░██╗░░
#██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║░░░░░░░░██████╗
#██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║░░░░░░░░╚═██╔═╝
#██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║░░░░░░░░░░╚═╝░░
#╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░░░░░░░░░  v1.8
#         By: Masar

# link:
#   GitHub: https://github.com/MasarOfficial/Python-Plus-V-1.8.2---inf
#   discord: Soon

#   write your code after functions
# change log
# v 1.6
#added functions

# v 1.6.2
# added beta AI
#timer function

#1.7
# added functions

#1.8
# func meaning file and txt editor func

#1.8.2
#function added

#1.8.4.2
# new functions. bug fix

# Functions. if you want you can delete some func or add here

def add(*args):
    print(args)  # Print the args tuple
    result = 0
    for num in args:
        result += num
    return result

# adding numbers max to 26 numbers. type add(number+number) and its shows up

def running(trueorfalse):
    if trueorfalse:
        print('')
    else:
        sys.exit('')

#If running(True) program running. if running(False) program ends

def copypaste(txt):
    while True:
        print(txt)
# copy and pasting message. copypaste("yourself")

def log(message, level="info"):
    colors = {
        "info": "\033[94m",  # blue information messages
        "warning": "\033[93m",  # yellow warn
        "error": "\033[91m"  # red error
    }
    reset_color = "\033[0m"

    print(f"{colors.get(level, '')}{message}{reset_color}")


# using
#log("This is an info message.")
#log("This is a warning!", level="warning")
#log("This is an error!", level="error")

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        print(f"Data written to {filename}")
    except Exception as e:
        print(f"Failed to write to file: {e}")

# using
#write_to_file('example.txt', 'Hello, world!')

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# using
#print(generate_strong_password(16))

def filecreate(file_name, text):
    filename = f"{file_name}.txt"  # Specify the name of the file with the .txt extension
    with open(filename, 'w') as file:
        file.write(text)  # Write the provided text to the file
        print("")
#using
#filecreate("file", "This is the content of the file.")

def minus(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


#using
# minus(100, 1, 2, 3, 4)  # This would return 100 - 1 - 2 - 3 - 4 = 90

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

#using
#multiply(2, 3, 4)  #return 2 * 3 * 4 = 24

def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero!")
        result /= num
    return result

#using
#divide(100, 2, 5)  #return 100 / 2 / 5 = 10

def drawShape(shape):
    # Create a turtle object
    t = turtle.Turtle()
    t.speed(2)  # Set the drawing speed

    # Draw the specified shape
    if shape.lower() == 'circle':
        t.circle(50)  # Draw a circle with a radius of 50
    elif shape.lower() == 'square':
        for _ in range(4):
            t.forward(100)  # Draw a side of length 100
            t.right(90)     # Turn right by 90 degrees
    elif shape.lower() == 'triangle':
        for _ in range(3):
            t.forward(100)  # Draw a side of length 100
            t.left(120)     # Turn left by 120 degrees
    else:
        print("\033[91mShape not recognized. Please use 'circle', 'square', or 'triangle'.\033[0m")

    turtle.done()  # Finish drawing

# Example usage
# drawShape('circle')  # Change to 'square' or 'triangle' for other shapes

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage
#clearTerminal()

def connect(filesname):
    try:
        with open(filesname, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        with open(filesname, 'w') as file:
            file.write("")  # Create an empty file
        return ""

# Example usage
#file_name = "example.txt"
#result = connect(file_name)
#print(result)

def registration(nickname, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open("users.txt", "a") as file:
        file.write(f"{nickname}:{hashed_password}\n")
    print("Registration successful!") # note: you can delete this print if you don't want message to appear

#using
#registration("JohnDoe", "password123")

def login(nickname, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open("users.txt", "r") as file:
            for line in file:
                user, stored_password = line.strip().split(':')
                if user == nickname and stored_password == hashed_password:
                    print("Login successful!")
                    return True
        print("Login failed: Invalid credentials.")
        return False
    except FileNotFoundError:
        print("No users registered yet.")
        return False

#using
#login(Masar strong123)

def ai(task):
    task = task.lower()  # Convert the task to lowercase for easier comparison

    if task == "greet":
        return "Hello! How can I assist you today?"

    elif task == "joke":
        return "Why did the computer go to therapy? Because it had too many bugs!"

    elif task == "time":
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif task == "generate_password":
        return generate_strong_password()  # Assuming you have the `generate_strong_password` function defined

    elif task == "terminate":
        return "Shutting down..."

    else:
        return "I'm sorry, I don't understand that task."


# Example usage:
#print(ai("greet"))  # Output: "Hello! How can I assist you today?"
#print(ai("joke"))  # Output: "Why did the computer go to therapy? Because it had too many bugs!"
#print(ai("time"))  # Output: The current time is ...
#print(ai("generate_password"))  # Output: A randomly generated password
#print(ai("terminate"))  # Output: "Shutting down..."

def timer(Hours, Minutes, Seconds):
    total_seconds = Hours * 3600 + Minutes * 60 + Seconds

    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Display the timer in the format HH:MM:SS
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end='\r')
        time.sleep(1)
        total_seconds -= 1

    print("")
# Example usage:
# timer(0, 1, 30)  # A 1 minute and 30 seconds countdown timer
#timer(0, 0, 10)  # A 10-second countdown
#timer(0, 1, 30)  # A 1 minute and 30 seconds countdown
#timer(1, 0, 0)   # A 1-hour countdown



class Poll:
    def __init__(self, option1, option2, option3):
        self.options = {option1: 0, option2: 0, option3: 0}

    def display_poll(self, pollname):
        print(f"Poll: {pollname}")
        for index, option in enumerate(self.options.keys(), start=1):
            print(f"{index}. {option}")

    def vote(self, choice):
        option = list(self.options.keys())[choice - 1]
        self.options[option] += 1
        print(f"You voted for: {option}")

    def show_results(self):
        print("\nPoll Results:")
        for option, count in self.options.items():
            print(f"{option}: {count} votes")


def poll(option1, option2, option3):

    poll_instance = Poll(option1, option2, option3)

    poll_instance.display_poll()

    while True:
        try:
            choice = int(input("Enter the number of your choice (0 to quit): "))
            if choice == 0:
                break
            elif 1 <= choice <= 3:
                poll_instance.vote(choice)
            else:
                print("Invalid option. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    poll_instance.show_results()

def check_file(file_name_, directory):

    try:
        # Construct the full path to the file
        file_path = os.path.join(directory, file_name_)

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False

        # Check if the file is a regular file (not a directory)
        if not os.path.isfile(file_path):
            print(f"{file_path} is not a regular file")
            return False

        # Check if the file is readable
        if not os.access(file_path, os.R_OK):
            print(f"{file_path} is not readable")
            return False

        # Check if the file is writable
        if not os.access(file_path, os.W_OK):
            print(f"{file_path} is not writable")
            return False

        # If all checks pass, return True
        print(f"{file_path} is accessible")
        return True

    except Exception as e:
        print(f"Error checking file: {e}")
        return False

# Example usage:
#file_name = "example.txt"
#directory = "/path/to/directory"
#if check_file(file_name, directory):
#    print("File is accessible")
#else:
#    print("File is not accessible")

# Example usage:
#poll("Option 1", "Option 2", "Option 3")


def textedit(changedText):

    print("Current Text: ")
    print(changedText)

    # Get user input for modification
    new_text = input("Enter the new text (or press Enter to keep current text): ")

    # If new_text is empty, keep the original text
    if new_text:
        changedText = new_text

    return changedText


# Example usage
# if __name__ == "__main__":
#     original_text = "This is the original text."
#     modified_text = textedit(original_text)
#     print("\nModified Text:")
#     print(modified_text)


def pipmodule(namemodule):

    try:
        # Use subprocess to call pip install
        subprocess.check_call([sys.executable, "-m", "pip", "install", namemodule])
        print(f"Package '{namemodule}' installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package '{namemodule}'. Error: {e}")

#using
#pipmodule("pygame")


def translate(originaltext, language):

    translator = Translator()

    try:
        translated = translator.translate(originaltext, dest=language)
        return translated.text
    except Exception as e:
        return f"Error during translation: {str(e)}"


# Example usage
#text = "Hello, how are you?"
#target_language = 'es'  # Spanish

#translated_text = translate(text, target_language)
#print(f"Translated text: {translated_text}")



def data_save(save_file_name, data):

    try:
        # Check if the file name has an extension
        if not save_file_name.endswith(('.json', '.pickle')):
            raise ValueError("File name must have a .json or .pickle extension")

        # Save the data to a file
        if save_file_name.endswith('.json'):
            with open(save_file_name, 'w') as file:
                json.dump(data, file)
        elif save_file_name.endswith('.pickle'):
            with open(save_file_name, 'wb') as file:
                pickle.dump(data, file)

        print(f"Data saved to {save_file_name}")

    except Exception as e:
        print(f"Error saving data: {e}")

# Example usage:
#data = {"name": "John", "age": 30}
#data_save("data.json", data)

def load_safe(file_saves):

    try:
        with open(file_saves, 'r') as file:
            data = json.load(file)
            print("Game data loaded successfully.")
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_saves}' was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not in a valid JSON format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return {}  # Return an empty dictionary if loading fails

#Usage
#game_data = load_safe('path/to/save_file.json')

