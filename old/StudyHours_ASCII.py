import matplotlib.pyplot as pyplot
import datetime
import time
import sys
import threading


# for now just a series of moving dots
# TO DO: Something like a book flipping pages? ASCII Art?
def studying_art():

    n_dots = 5

    print('Counting....')
    dots = '.' * n_dots
    
    # prints the amount of n_dots and then rewrites that line
    while(studying == True):
        for dot in dots:        
            print(dot, end='')
            time.sleep(0.8)
        
        print('\r', end='')
        print(' '*n_dots + '\r', end='')

def waiter():
    print('Press any key to stop studying')
    global studying
    studying == False

as

def main():
    time1 = datetime.datetime.now()
    print('\n' + '-'*40)
    print('Hi! Counting your study hours... Starting now!\n')
    
    t_input = threading.Thread(target=waiter())
    t_art = threading.Thread(target=studying_art())
    
    t_input.start()
    t_art.start()


    input('Press any key to stop studying')
    studying == False

    

    time2 = datetime.datetime.now()
    a = datetime.datetime.today().weekday()
    b = datetime.datetime.now().weekday()
    print(a,b)

    time_diff =  time2 - time1
    print(time1.weekday(), time1, time2, time_diff)


available_studyhours = {
    'monday' : 3,
    'tuesday' : 5,
    'wednesday': 3,
    'thursday' : 5,
    'friday' : 3,
    'saturday' : 10,
    'sunday' : 10,
}

dayofweek_map = {
    'monday' : 0,
    'tuesday' : 1,
    'wednesday': 2,
    'thursday' : 3,
    'friday' : 4,
    'saturday' : 5,
    'sunday' : 6,
}

if __name__ == '__main__':
    studying = True
    main()