import matplotlib.pyplot as pyplot
import datetime
import time
import sys

def main():
    time1 = datetime.datetime.now()
    print('\n' + '--'*40 + '\n')
    print('Hi! Counting your study hours... Starting now!\n')

    print('Counting....')
    dots = '.'*5
    while(1):
        # time.sleep(0.1)
        # print('.', end='')
        # time.sleep(0.1)
        # print('.', end='')
        # print('\b\b', end='')

        for i, dot in enumerate(dots):
        
            sys.stdout.write(dot)
            print('', end='', flush=True)
            # sys.stdout.flush()
            time.sleep(1)


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
    main()