
import statistics
import pandas as pd
import plotly.express as px

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from data_reader import *

#Load data
df = pd.read_csv("lotto.csv")

firsts = pd.read_csv("lebrons.csv")
seconds = pd.read_csv("durants.csv")
thirds = pd.read_csv("jordans.csv")
fourths = pd.read_csv("pauls.csv")


def get_from_year_from_id(id):
    return commonplayerinfo.CommonPlayerInfo(player_id=id).get_data_frames()[0]['FROM_YEAR']

#print(first_rounders['namePlayer'].tolist())
    
def career_stuff_downloader(pairs):
    for pair in pairs:
        p = int(get_player_id_from_pair(pair))
        filename = "data/"+pair[0].replace(" ", "")+'.csv'
        if(p != 0):
            career = playercareerstats.PlayerCareerStats(player_id=p)
            pdf = career.get_data_frames()[0]
            pdf.to_csv(filename)
            print()
 

