
import glob
from valve_keyvalues_python.keyvalues import KeyValues

from zplib import data_path

def get_players_keyvalues():
    player_list = []
    for i in glob.glob(data_path.player_format):
        kv = KeyValues(filename=i)["player_data"]
        player_list.append(kv)

    return player_list
