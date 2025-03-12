################################################################FORMATTING##########################################################
# todo -> outputs all tasks
# todo c {task-name} -> creates task with task-name
# todo r {task-name} -> removes task with task-name
# todo h -> prints toinish help page
# Includes when task was added
#####################################################################################################################################

import sys
from datetime import datetime
import os

class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Todo:

    def __init__(self):

        self.home = os.getcwd().split('/')

        self.run()
        self.quit()

    def run(self):
        
        arg = len(sys.argv)
        if arg == 1:
            self.todo()
        else:
            if sys.argv[1][0] == 'c':
                self.todo_c()
            elif sys.argv[1][0] == 'r':
                self.todo_r()
            elif sys.argv[1][0] == 'h':
                self.todo_h()
            else:
                print('todo: please provide valid arguments')
                print('todo: use the -h option to see help')

    def todo(self):

        self.open('r')
        print('Toinish v0.1')
        print(self.f.read())
        self.close()

    def todo_c(self):

        self.open('r')
        if self.f.read() == '\n':
            self.close()
            self.open('a')
            self.f.write(sys.argv[2] + '    ' + datetime.today().strftime('%Y-%m-%d'))
        else:
            self.open('a')
            self.f.write('\n' + sys.argv[2] + '    ' + datetime.today().strftime('%Y-%m-%d'))
        self.close()
        self.todo()

    def todo_r(self):
        
        with open('/' + self.home[1]+'/' + self.home[2]+'/' + ".config/toinish/todo", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if not sys.argv[2] + '    ' in i:
                    f.write(i)
                '''
                if i != sys.argv[2]:
                    f.write(i)
                '''
            f.truncate()
        self.todo()

    def todo_h(self):

        print(color.BOLD + 'Toinish v0.1' + color.END)
        print('https://github.com/empty-blip/Toinish')
        print('\nA simple todo app for the terminal\n')

        print(color.BOLD + color.UNDERLINE + 'Usage:' + color.END)
        print(color.BOLD + '  todo ' + color.END + '<OPTION>\n')

        print(color.BOLD + color.UNDERLINE + 'Options' + color.END)
        print(color.BOLD + 'c' + color.END + '  creates a new task')
        print(color.BOLD + 'r' + color.END + '  removes a new task')
        print(color.BOLD + 'h' + color.END + '  prints this help page')

    def open(self, type):
        self.f = open('/' + self.home[1]+'/' + self.home[2]+'/' + '.config/toinish/todo', type)

    def close(self):
        self.f.close()

    def quit(self):
        sys.exit()

todo = Todo()
