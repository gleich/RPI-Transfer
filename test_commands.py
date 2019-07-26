import unittest

from src.util import commands

class TestCommands(unittest.TestCase):
    """
    Will test all the functions inside the file /src/util/commands.py
    """ 

    def test_run_command(self):
        """
        Tests the run_command function
        """
        result = commands.run_command("echo 'Hello World'", True)
        result2 = commands.run_command("echo 'Hello World'", False)
        self.assertEqual('Hello World\n', result)
        self.assertEqual(result2, None)


if __name__ == "__main__":
    unittest.main()
