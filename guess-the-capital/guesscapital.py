import random
import Tkinter

### Variables

country_capital_dict = {
        "Slovenia": "Ljubljana",
        "Croatia": "Zagreb",
        "Serbia": "Belgrade",
        "Austria": "Vienna",
        "Germany": "Berlin",
        "France": "Paris",
        "United Kingdom": "London",
        "Russia": "Moscow",
        "Japan": "Tokyo",
        "Italy": "Rome",
        "Turkey": "Istanbul"
    }

random_country = ""



####  Functions

def choose_random_country():
    random_number = random.randint(0, len(country_capital_dict) - 1)
    random_country = country_capital_dict.keys()[random_number]
    return random_country


def check_guess():
    global random_country
    if input_field.get().lower() == country_capital_dict[random_country].lower():
        random_country = choose_random_country()
        question.config(text = "What is the capital of " + random_country)
        feedback.config(text = "You are correct!")
        image_path = "img/" + country_capital_dict[random_country] + ".gif"
        image.config(file = image_path)
    else:
        feedback.config(text="You are wrong! Try again.")



### Program

random_country = choose_random_country()


#### GUI

window = Tkinter.Tk()
window.minsize(300,100)

question = Tkinter.Label(window, text = "What is the capital of " + random_country)
question.pack(pady=10)

input_field = Tkinter.Entry(window)
input_field.pack()

submit_button = Tkinter.Button(window, text = "Submit", command = check_guess)
submit_button.pack(pady=10)

image_path = "img/" + country_capital_dict[random_country] + ".gif"
image = Tkinter.PhotoImage(file=image_path)

feedback = Tkinter.Label(window, text="")
feedback.pack()

image_label = Tkinter.Label(image=image)
image_label.image = image
image_label.pack()

window.mainloop()




