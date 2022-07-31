from enum import Enum
import pandas as pd

class DIR(Enum):
    CPI = "common_player_info"
    PCS = "player_career_stats"

def gen_filename(dir, pair):
    root = "data"
    return "/".join([root, dir.value])
    