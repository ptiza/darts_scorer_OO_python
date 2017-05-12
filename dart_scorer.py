from viewer import Viewer
from match import Match

viewer = Viewer()
player_1_name = viewer.get_player_name(1)
player_2_name = viewer.get_player_name(2)
sets = viewer.get_number_of_sets()
legs_per_set = viewer.get_number_of_legs_per_set()
start_score = viewer.get_start_score()

match = Match(player_1_name, player_2_name, sets, legs_per_set, start_score)
match.play_match()