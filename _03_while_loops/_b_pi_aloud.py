"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math

from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi_str = '3.1415926535897932384'
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

        # TODO) Use a while loop to keep asking for the next digit of pi
    incorrect = 0
    index = 0
    while incorrect<1:
        save = simpledialog.askstring(None, prompt = 'whats the next digit of pi?')

        if save == pi_str[index]:
            print('correct')
        else:

            print('incorrect')
            incorrect = 1
            print(index)
        index = index+1


        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
