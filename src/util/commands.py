import os

def run_command(command, capture_output):
    """
    Run a command using python. Purely exists to make commands cleaner.
    :param command: command to run (str)
    :param capture_output: capture the output and return it (bool)
    :return: None
    """
    if capture_output:
        return os.popen(command).read()
    else:
        os.system(command)
