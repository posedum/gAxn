import os
import requests


def get_weather(city):
    return requests.post(
        url="https://lit-plateau-35814.herokuapp.com/weather",
        data=f"{city}"
    )


def main():
    print("in main")
    weather = get_weather("Cape Town")
    print(weather)


if __name__ == "__main__":
    main()

