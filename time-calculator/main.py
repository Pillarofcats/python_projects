# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from clock import start_clock
# from unittest import main


add_time("8:55 PM", "1:12", "Saturday")

start_clock()

# Run unit tests automatically
# main(module='test_module', exit=False) 