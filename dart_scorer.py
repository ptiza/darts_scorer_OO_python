#!/usr/bin/python3

from viewer import Viewer
from match import Match


viewer = Viewer()
playernames = list(range(viewer.get_player_number()))
for playernum in playernames:
    playernames[playernum] = viewer.get_player_name(playernum+1)
sets = viewer.get_number_of_sets()
legs_per_set = viewer.get_number_of_legs_per_set()
start_score = viewer.get_start_score()

match = Match(playernames, sets, legs_per_set, start_score)

match.play_match()
