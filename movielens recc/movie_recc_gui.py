import pandas as pd
import warnings
warnings.filterwarnings('ignore')
## import os
## print(os.getcwd())

import tkinter as ttk
app = ttk.Tk()
app.title('Movie Reccomendor System')
app.geometry("900x900")

#Reading the Data Files
cols = ['user_id', 'movie_id', 'rating', 'ts']
df = pd.read_csv('u.data', sep = '\t', names = cols).drop('ts', axis = 1)
item_cols = ['movie_id', 'title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep = '|', names = item_cols, encoding = "ISO-8859-1")[['movie_id', 'title']]
    
#Merging the two Data Frames
movie = pd.merge(df, df1, on = 'movie_id')

result = ttk.Variable(app)
box = ttk.Listbox(app, height=10)
for rows, val in movie.iterrows():
    box.insert(rows+1, val('title'))

box.place(x=10, y=10)

def get_movie():
    pass

ttk.Button(app, text="Find Reccomendations", font= ('Arial',22), command = get_movie).place(x=200, y=50)


ttk.Label(app, textvariable=result, font=('Arial',22)).place(x=200, y=100)






app.mainloop()