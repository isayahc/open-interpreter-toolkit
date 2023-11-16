import os
import dotenv
from typing import List

import interpreter

#import dotenv variables
dotenv.load_dotenv()



TOOL_KIT_DIR = os.getenv("TOOL_KIT_DIR")

# Function to add system message
def add_system_message(interpreter, messages: List[str]) -> None:
    for message in messages:
        interpreter.system_message += f"\n{message}"

#To modift the behavior of the interpreter you can add to the system message


# List of guidelines and instructions for the interpreter
guidelines = [
    f"""

Your goal is the generate a set of executables file stored in 
{TOOL_KIT_DIR} 
every function or snippet you make
you must document what it does and how it works. 
Also when applicable you make a cli when you make a cli you must document how to use it and what it does.

Every time you write code you must save it in a .py (never forget the shebang line at the begining) file then 
turn that file into an executable file. on my machine.

When given a task please check if there 
exist an executable file in {TOOL_KIT_DIR} that does 
the task if there is not then you must make one.
""" ,
f"""

With each question you answer you must check {TOOL_KIT_DIR} to see
if there is an executable file that does the task if there is not then you must make one.

I recommend you make run ls in the tool kit directory

""",
f"""
when creating scripts make sure to create argeparse command line interface for them. Such that they can be used to solve similar problems in the future.
when working with cli's do not run directory. for example if there is a cli called hello_world.py, run ./hello_world.py not python3 hello_world.py
""",
f"""
When making cli's make sure to have default arguments for all arguments. Else the this interpreter will break. So please give each
argument a default value.
"""



]




# Add guidelines to the system message
add_system_message(interpreter, guidelines)

interpreter.chat()
