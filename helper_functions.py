from nba_api.stats.static import players

def strip(x):
    if x is None:
        return 0
    else: 
        return x

def get_player_id_from_pair(pair): 
    name = pair[0]
    player_list = players.find_players_by_full_name(name)
    if(len(player_list)==1):
        return player_list[0]['id']
    else:
        return player_list

def gen_pairs(frame):
    return list(zip(frame['namePlayer'].tolist(), frame['yearDraft'].tolist()))

def get_career_per_game_stat(pdf, cat):
    return round(sum(list(map(strip, pdf[cat].tolist())))/sum(pdf['GP']), 1)

def get_player_id_from_ids(ids, year):
    for p in ids:
        pyear = p['id']
        print(pyear)

def gen_filename(dir, pair):
    root = "data"
    return "/".join([root, dir.value])
