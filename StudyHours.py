import tkinter
import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    start_time = datetime.datetime.now()
    start_date = start_time.date()
    start_date_str = start_date.strftime('%Y-%m-%d')
    weekday = dayofweek_map[start_time.weekday()]
    
    # make a daily index consisting of the last 12 weeks
    last12 = pd.date_range(start=start_date - datetime.timedelta(days=12), end=start_date)
    # make a daily index of the last year
    last52 = pd.date_range(start=start_date - datetime.timedelta(days=52), end=start_date)
    # columns we will use
    columns = ['Weekday', 'Hours_Studied', 'Seconds_Studied']

    global studyhours_df
    try: # if the file already exists, open it
        studyhours_df = pd.read_csv('data\\studyhours.csv', index_col=0)
    except Exception as e: # else create the file new
        print(e)
        index = last12
        studyhours_df = pd.DataFrame(index=index, columns=columns)

    # add empty days to the csv file (for visualization)
    for day in last52:
        day_str = day.strftime('%Y-%m-%d')
        if day_str not in studyhours_df.index:
            if day > pd.to_datetime(studyhours_df.index[0]):
                studyhours_df.loc[day_str] = [np.nan, np.nan, np.nan] # add empty row
    
    # # # # # # # # # # # # # # # # # # # # # # # # #
    # Program waits here until user stops studying  #
    open_window()                                   #
    # # # # # # # # # # # # # # # # # # # # # # # # #

    # measure the time spent studying
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    duration_seconds = duration.total_seconds()
    duration_hours = round(duration_seconds/3600, 2)

    # write the value to the dataframe
    if studyhours_df.loc[start_date_str].isnull().any() == True: # if it is the first time the program has been opened today
        studyhours_df.loc[start_date_str] = [weekday, duration_hours, duration_seconds]
    else: # if the tracker has already been opened today, then add the hours to the existing value
        duration_seconds += studyhours_df['Seconds_Studied'].loc[start_date_str]        
        duration_hours = round(duration_seconds/3600, 2)
        studyhours_df.loc[start_date_str] = [weekday, duration_hours, duration_seconds]

    studyhours_df.to_csv('data\\studyhours.csv')

def showHistory():
    plt.figure(figsize=(10,6), num='Hours/days')

    global studyhours_df
    plt.bar(studyhours_df.index,
            studyhours_df['Hours_Studied'],
            align='edge',
            )
    
    plt.xlabel('Day')
    plt.title('Avg Hours Studied')
    plt.ylabel('Avg Hours Studied')
    plt.xticks(rotation=30, ha="right")


    plt.figure(figsize=(7,5), num='Hours/weekday')
    plt.bar(studyhours_df.groupby(['Weekday']).groups.keys(), 
            studyhours_df.groupby(['Weekday'])['Hours_Studied'].agg('sum'),
            align='center',
            color='rgbkymc',
            )
    plt.xlabel('Day of Week')
    plt.title('Avg Hours Studied per Weekday')
    plt.ylabel('Avg Hours Studied')
    
    plt.show()

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
    stopBttn.pack(side="left", padx=10, pady=10)
    stopBttn.pack()

    reportsBttn = tkinter.Button(window, text="Show History", command=showHistory)
    reportsBttn.pack(side="right", padx=10, pady=10)
    reportsBttn.pack()

    # open the window
    window.mainloop()

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

if __name__ == '__main__':
    main()