import tkinter
import time
import datetime
import pandas as pd

# Value initializations
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
    0 : 'monday',
    1 : 'tuesday',
    2 : 'wednesday',
    3 : 'thursday',
    4 : 'friday',
    5 : 'saturday',
    6 : 'sunday',
}

def stopStudying():
    window.destroy()

def open_window():
    global window
    window = tkinter.Tk()

    # Title of TKinter window
    window.title("StudyHours")

    # put a fun background
    from PIL import Image, ImageTk

    image = Image.open("img\\onestone_smol2.jpg")
    onestone = ImageTk.PhotoImage(image)

    tkinter.Label(window, image=onestone).pack()
    window.iconbitmap(r'img\\book-32.ico')
    # stop button to stop the program
    stopBttn = tkinter.Button(window, text="Stop Studying", command=stopStudying)
    stopBttn.pack()
    
    # open the window
    window.mainloop()

def main():

    start_time = datetime.datetime.now()
    start_date = start_time.date()
    weekday = dayofweek_map[start_time.weekday()]
    

    last12 = pd.date_range(start=start_date - datetime.timedelta(days=12), end=start_date)
    columns = ['Weekday', 'Hours_Studied']

    try:
        studyhours_df = pd.read_csv('data\\studyhours.csv', index_col=0)
    except Exception as e:
        print(e)
        index = last12
        studyhours_df = pd.DataFrame(index=index, columns=columns)
    
    # # # # # # # # # # # # # # # # # # # # # # # # #
    # Program waits here until user stops studying  #
    open_window()                                   #
    # # # # # # # # # # # # # # # # # # # # # # # # #

    # measure the time spent studying
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    duration_seconds = duration.total_seconds()
    duration_seconds = duration_seconds * 7200
    duration_hours = round(duration_seconds/3600, 2)
    print(duration, duration_hours, duration_seconds)

    # write the value to the dataframe
    studyhours_df.loc[start_date] = {'Weekday':weekday, 'Hours_Studied':duration_hours}

    studyhours_df.to_csv('data\\studyhours.csv')
    

if __name__ == '__main__':
    main()