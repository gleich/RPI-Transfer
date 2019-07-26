from util import commands
from json import load

def main():
    """
    Runs the whole program
    :return: None
    """
    commands.run_command("cd ~/../..", False)
    with open("settings.json") as settings_json:
        settings = load(settings_json)
    if settings["drive-name"] == "" or settings["card-names"][0] == "":
        raise Exception("Please fill in settings.json")


if __name__ == "__main__":
    main()
