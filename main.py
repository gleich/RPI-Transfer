from json import load
import os


def main():
    """
    Runs the whole program
    :return: None
    """
    os.system("cd ~/../../media/pi")
    print(os.popen("pwd").read())
    with open("settings.json") as settings_json:
        settings = load(settings_json)
    drive = settings["drive-name"]
    cards = settings["card-names"]
    if drive == "" or cards[0] == "":
        raise Exception("Please fill in settings.json")
    drives = os.listdir(".")
    file_paths = []
    for card in cards:
        card_content = os.listdir(card)
        for file in card_content:
            file_path = "/" + card + "/" + file
            file_paths.append(file_path)
    for path in file_path:
        os.system("cp " + path + " " + drive)


if __name__ == "__main__":
    main()
