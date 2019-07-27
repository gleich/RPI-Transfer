from util import commands
from json import load
import os


def main():
    """
    Runs the whole program
    :return: None
    """
    os.chdir("cd ~/../../pi")
    with open("settings.json") as settings_json:
        settings = load(settings_json)
    drive = settings["drive-name"]
    cards = settings["card-names"]
    if drive == "" or cards[0] == "":
        raise Exception("Please fill in settings.json")
    drives = os.listdir()
    if drive not in drive:
        raise Exception("Can't seem to find the drive: " + drive)
    file_paths = []
    for card in cards:
        if card not in drive:
            raise Exception("Can't seem to find the card: " + drive)
        card_content = os.listdir(card)
        for file in card_content:
            file_path = "/" + card + "/" + file
            file_paths.append(file_path)
    for path in file_path:
        os.system("mv " + path + " " + drive)


if __name__ == "__main__":
    main()
