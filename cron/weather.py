import click
import json
import os
import requests

SETTINGS_FILE = 'settings.json'
URL_WEATHER = "https://lit-plateau-35814.herokuapp.com/weather"


@click.command("weather")
def main():
    file_path = os.path.join(
        '/'.join(os.path.abspath(__file__).split('/')[:-2]),
        SETTINGS_FILE
    )
    print(f"Settings file: {file_path}")
    with open(f"{file_path}") as fh:
        settings = json.load(fh)
    city = settings.get("city")
    print(f"Get weather for '{city}'")
    resp = requests.post(url=f"{URL_WEATHER}", data=f"{city}")
    if resp.status_code == requests.codes.ok:
        print(resp.json())
        return resp.json()
    print({"city": {"name": f"{city}"}})
    return {"city": {"name": f"{city}"}}


if __name__ == "__main__":
    main()
