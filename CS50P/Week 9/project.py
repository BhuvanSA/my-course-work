from jokeapi import Jokes  # To get jokes from JokeAPI
import asyncio  # For async
import argparse  # To ease CLI
import pyttsx3  # For Telling the Joke
from playsound import playsound  # To play laugh and quack sound effects


def main():
    parser = argparse.ArgumentParser(description="Get a joke")
    parser.add_argument("-n", default=1, help="Number of jokes", type=int)
    parser.add_argument("-t", default="python",
                        help="Topic of jokes", type=str)
    args = parser.parse_args()
    jokes = asyncio.run(get_joke(args.n, args.t))
    print_jokes(jokes)


def print_jokes(jokes):
    for joke in jokes:
        for i, line in enumerate(joke.split('\n')):
            print(line)
            sayer(line, joke, i)
        playsound('./laughs.mp3')
        print()


def sayer(line, joke, i):
    engine = pyttsx3.init()
    engine.say(line)
    engine.runAndWait()
    if i != len(joke.split('\n'))-1:
        playsound("./quack.mp3")


async def get_joke(amount=1, topic="python"):
    j = await Jokes()  # Initialise the class

    # Will return a joke that fits in programming category.
    joke = await j.get_joke(category=['programming', 'dark', 'spooky'], amount=amount, blacklist=['nsfw', 'racist'], response_format="json", search_string=topic)

    # A list to store jokes
    jokes = []

    # Single Joke
    if amount == 1:
        if joke["type"] == "twopart":
            jokes.append(f"{joke['setup']}\n{joke['delivery']}")
        else:
            jokes.append(f"{joke['joke']}")

    # Multiple Jokes
    else:
        for every_joke in joke['jokes']:
            if every_joke["type"] == "twopart":
                jokes.append(
                    f"{every_joke['setup']}\n{every_joke['delivery']}")
            else:
                jokes.append(f"{every_joke['joke']}")

    return jokes

if __name__ == "__main__":
    main()
