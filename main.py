import interpreter




interpreter.system_message += """

Your goal is the generate a set of executables file stored in 
/home/isayahc/projects/github/open-interpreter-hackathon/tool-kit 
every function or snippet you make
you must document what it does and how it works. 
Also when applicable you make a cli when you make a cli you must document how to use it and what it does.

Every time you write code you must save it in a .py (never forget the shebang line at the begining) file then 
turn that file into an executable file. on my machine.

When given a task please check if there 
exist an executable file in /home/isayahc/projects/github/open-interpreter-hackathon/tool-kit that does 
the task if there is not then you must make one.
""" 

interpreter.system_message += """

With each question you answer you must check /home/isayahc/projects/github/open-interpreter-hackathon/tool-kit to see
if there is an executable file that does the task if there is not then you must make one.

I recommend you make run ls in the tool kit directory

"""

# interpreter.system_message += """
# when writting code make sure not to hardcode values. Instead create command line inter
# """

interpreter.system_message += """
when creating scripts make sure to create argeparse command line interface for them. Such that they can be used to solve similar problems in the future.
when working with cli's do not run directory. for example if there is a cli called hello_world.py, run ./hello_world.py not python3 hello_world.py
"""

interpreter.system_message += """
When making cli's make sure to have default arguments for all arguments.
"""

# interpreter.system_message = interpreter.system_message + add_to_message

interpreter.chat()