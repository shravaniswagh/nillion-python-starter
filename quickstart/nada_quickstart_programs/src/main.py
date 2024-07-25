from nada_dsl import *
import random

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Define a list of quotes or jokes
    quotes_or_jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "To be or not to be, that is the question.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you get if you cross a snowman and a vampire? Frostbite.",
        "Why don’t some couples go to the gym? Because some relationships don’t work out.",
        "I would avoid the sushi if I was you. It’s a little fishy.",
        "Want to hear a joke about construction? I’m still working on it.",
        "I used to play piano by ear, but now I use my hands.",
        "Why can’t you give Elsa a balloon? Because she will let it go.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why do cows wear bells? Because their horns don’t work.",
        "What do you call fake spaghetti? An impasta.",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "I’m reading a book on anti-gravity. It’s impossible to put down.",
        "Why was the math book sad? Because it had too many problems.",
        "How does a penguin build its house? Igloos it together.",
        "Why don’t programmers like nature? It has too many bugs."
    ]

    # Generate a random index to select a quote or joke
    random_index = random.randint(0, len(quotes_or_jokes) - 1)
    selected_quote_or_joke = quotes_or_jokes[random_index]

    # Define a Secret input to hold the selected quote or joke
    quote_or_joke = Secret(Input(name="quote_or_joke", party=party1))

    # Assign the selected quote or joke to the input
    quote_or_joke.set_value(selected_quote_or_joke)

    return [Output(quote_or_joke, "my_output", party3)]
