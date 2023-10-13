import interpreter




add_to_message = """

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

interpreter.system_message = interpreter.system_message + add_to_message

interpreter.chat()