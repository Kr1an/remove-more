import os


def run_tests():
    """Tests runner function"""
    os.system("python -m unittest discover -v -s './tests'")
