import os
import csv
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import plot_utilities as pu


# UI stuff.
### Take input from user regarding their season of interest.
year = input("\n Make sure you have a stable internet connection first.\n Data collection began after the year 2000. \n Enter the season you'd like data for.\n Eg: '2012' for the 2012-13 season; '2004' for the 2004-05 season.\n ")
year = int(year)

# Prepare season 'string' to display in the graphs. Eg: Season 2008-09, 2013-14, etc.
if(int(str(year)[2:]) + 1 < 10):
    year_str = str(year) + "-" + "0" + str((int(str(year)[2:]) + 1))
else:
    year_str = str(year) + "-" + str((int(str(year)[2:]) + 1))


# Functions to scrape data from SkySports and return a DataFrame of relevant data with necessary columns.
def read_data_epl():
    # Scraping.
    f = open('dataset_epl_sky.csv', 'w', newline = '')
    writer = csv.writer(f)
    soup = BeautifulSoup(urllib.request.urlopen("https://www.skysports.com/premier-league-table/{}".format(year)).read(), 'lxml')
    tbody = soup('tbody')[0].find_all('tr')
    
    for row in tbody:
        cols = row.findChildren(recursive = False)
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)
        print(cols)
    
    f.close()
    
    # Data reading.
    df = pd.read_csv("dataset_epl_sky.csv", header = None)
    df = pd.read_csv("dataset_epl_sky.csv", names = ["PositionPos", "Club", "PlayedPl", "WonW","DrawnD","LostL","GF","GA","GD","PointsPts"])
    df = pd.read_csv("dataset_epl_sky.csv", names = ["Club", "PlayedPl", "WonW","DrawnD","LostL","GF","GA","GD","PointsPts", "Nothing"])
    df.drop("Nothing", axis = 1, inplace = True)
    return df


def read_data_bundesliga():
    try:
        # Scraping
        f = open('bundesliga_table.csv', 'w', newline = '')
        writer = csv.writer(f)
        soup = BeautifulSoup(urllib.request.urlopen("https://www.skysports.com/bundesliga-table/{}".format(year)).read(), 'lxml')
        tbody = soup('tbody')[0].find_all('tr')
        
        for row in tbody:
            cols = row.findChildren(recursive = False)
            cols = [ele.text.strip() for ele in cols]
            writer.writerow(cols)
            print(cols)
            
        f.close()
        
        # Data reading.
        df = pd.read_csv("bundesliga_table.csv", header = None)
        df = pd.read_csv("bundesliga_table.csv", names = ["PositionPos", "Club", "PlayedPl", "WonW","DrawnD","LostL","GF","GA","GD","PointsPts"])
        if(df["PositionPos"][1] == 2) is False:
            df = pd.read_csv("bundesliga_table.csv", names = ["Club", "PlayedPl", "WonW","DrawnD","LostL","GF","GA","GD","PointsPts", "Nothing"])
            df = df.drop("Nothing", axis = 1)
            df["PositionPos"] = np.arange(1, 19)
            print("Dataset reading with additional changes done.")    
        else:
            print("Dataset reading done.")
        return df
    
    except IndexError:
        # Printing a formatted string.
        return (f"\n We're sorry; no data available for the {year - 1}-{year} Bundesliga season.")


def read_data_laliga():
    # Scraping.
    f = open('la_liga_table.csv', 'w', newline = '')
    writer = csv.writer(f)
    soup = BeautifulSoup(urllib.request.urlopen("https://www.skysports.com/la-liga-table/{}".format(year)).read(), 'lxml')
    tbody = soup('tbody')[0].find_all('tr')
    
    for row in tbody:
        cols = row.findChildren(recursive = False)
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)
        print(cols)
    
    f.close()
    
    # Data reading.
    df = pd.read_csv("la_liga_table.csv", header = None)
    df = pd.read_csv("la_liga_table.csv", names = ["PositionPos", "Club", "PlayedPl", "WonW","DrawnD","LostL","GF","GA","GD","PointsPts"])
    df = pd.read_csv("la_liga_table.csv", names = ["Club", "PlayedPl", "WonW","DrawnD","LostL","GF","GA","GD","PointsPts", "Nothing"])
    df.drop("Nothing", axis = 1, inplace=True)
    return df


### ============================================================================================

# UI stuff.
print("\n\n\n\n")
print(40 * "_")
print("\n Bundesliga, EPL, LaLiga stats & visualizations. \n")
print(40 * "_")
print("\n Please ensure you have a stable internet connection before entering your choice. ")
choice = input("\n Enter your choice:\n\n 1. Bundesliga\n 2. EPL\n 3. La Liga\n\n ")
choice = int(choice)

if(choice == 1):
    print("\n You have chosen 1) Bundesliga.\n Make sure you're connected to the internet. \n Processing... \n ")
    league = "Bundesliga"
    df = read_data_bundesliga()

elif(choice == 2):
    print("\n You have chosen 2) EPL.\n Make sure you're connected to the internet. \n Processing... \n ")
    league = "EPL"
    df = read_data_epl()

elif(choice == 3):
    print("\n You have chosen 3) La Liga.\n Make sure you're connected to the internet. \n Processing... \n ")
    league = "La Liga"
    df = read_data_laliga()

elif((choice != 1) or (choice != 2) or (choice != 3)):
    print("Wrong choice.")

### ============================================================================================

# 8 colors for 8 PNG plots.
colors = ['#0000CD', '#10F85B', '#006400', 'red', '#8B6565', '#7CFC00', '#FF8C00', '#AF9F00']
number_of_teams = int(len(df))
print("Number of teams in the {}: {}".format(league, number_of_teams))

# Lists containing various data values that will be fed into utility functions.
wins = list(df['WonW'])[::-1]
losses = list(df['LostL'])[::-1]
draws = list(df['DrawnD'])[::-1]
gf = list(df['GF'])[::-1]
ga = list(df['GA'])[::-1]
gd = list(df['GD'])[::-1]
gp = list(df['PlayedPl'])[::-1]
points = list(df['PointsPts'])[::-1]
clubs = list(df['Club'])[::-1]

wins_pygal = list(df['WonW'])
losses_pygal = list(df['LostL'])
draws_pygal = list(df['DrawnD'])
gf_pygal = list(df['GF'])
ga_pygal = list(df['GA'])
gd_pygal = list(df['GD'])
gp_pygal = list(df['PlayedPl'])
points_pygal = list(df['PointsPts'])
clubs_pygal = list(df['Club'])

# Plotting - Function calls.
folder_png = "plots_png"
os.mkdir(folder_png)
pu.plot_points(league = league, team_names = clubs, values = points, color = colors[0], year_str = year_str, folder_png = folder_png)
pu.plot_gd(league = league, team_names = clubs, values = gd, color = colors[1], year_str = year_str, folder_png = folder_png)
pu.plot_wins(league = league, team_names = clubs, values = wins, color = colors[2], year_str = year_str, folder_png = folder_png)
pu.plot_losses(league = league, team_names = clubs, values = losses, color = colors[3], year_str = year_str, folder_png = folder_png)
pu.plot_draws(league = league, team_names = clubs, values = draws, color = colors[4], year_str = year_str, folder_png = folder_png)
pu.plot_gf(league = league, team_names = clubs, values = gf, color = colors[5], year_str = year_str, folder_png = folder_png)
pu.plot_ga(league = league, team_names = clubs, values = ga, color = colors[6], year_str = year_str, folder_png = folder_png)
pu.plot_gp(league = league, team_names = clubs, values = gp, color = colors[7], year_str = year_str, folder_png = folder_png)

folder_svg = "plots_svg"
os.mkdir(folder_svg)
pu.plot_pygal_all(year_str, folder_svg, number_of_teams, clubs_pygal, points_pygal, gd_pygal, gf_pygal, ga_pygal, wins_pygal, losses_pygal, draws_pygal, gp_pygal, league = league)

sorted_plots_folder_name = "plots_sorted"
os.mkdir(sorted_plots_folder_name)
df_sorted_by = df.set_index(keys = ['Club'])
pu.plot_sorted_all(df_sorted_by = df_sorted_by, year_str = year_str, sorted_plots_folder_name = sorted_plots_folder_name, league = league)
print("Done.")