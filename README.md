## Toinish - A todo list in Python
Toinish *(to-i-nish)* is a todo list made purely of a single Python file.

### Documentation
To create a new task:

    todo c {task_name}

To remove a task:

    todo r {task_name}

### Installation
To run Toinish, you need to have Python 3 installed

On Unix-based systems, run

    touch ~/.config
    cd ~/.config
    git clone https://github.com/empty-blip/Toinish.git toinish

and then add

    alias todo=python3\ ~/.config/toinish/todo.py

or

    alias {command_name}=python3\ ~/.config/toinish/todo.py

to your .zshrc or .bashrc. Make sure you change *{command_name}* to the command name of your choice.
