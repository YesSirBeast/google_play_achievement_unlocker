import sys
import argparse
from gpau_objects.structure import Dummy
from gpau_objects.gpau import GooglePlayAchievementUnlocker
from typing import Union

DEBUG = False

args: Union[argparse.Namespace, Dummy] = Dummy()

parser = argparse.ArgumentParser(epilog="By @TheNoiselessNoise")
if not DEBUG:
    parser.add_argument('-i', dest='input', metavar='input', help='path to the .db file')
    parser.add_argument('--readme', dest='readme', action='store_true', help='How to use this?')
    
    # Pending Ops Yönetimi (Başarımlar ve Liderlik Tabloları)
    parser.add_argument('--auto-inc-achs', dest='auto_inc_achs', action='store_true', help='Automatically set the incremental achievements to max')
    parser.add_argument('--rem-dup-ops', dest='rem_dup_ops', action='store_true', help='Remove duplicate achievement pending ops')
    parser.add_argument('--rem-all-ops', dest='rem_all_ops', action='store_true', help='Remove all achievement pending ops')
    parser.add_argument('--rem-dup-lb-ops', dest='rem_dup_lb_ops', action='store_true', help='Remove duplicate leaderboard pending ops')
    parser.add_argument('--rem-all-lb-ops', dest='rem_all_lb_ops', action='store_true', help='Remove all leaderboard pending ops')
    
    package_group = parser.add_mutually_exclusive_group()
    package_group.add_argument('-a', dest='app', metavar='app_name', help='app name')
    package_group.add_argument('-aid', dest='app_id', metavar='app_id', help='app id')
    
    player_group = parser.add_mutually_exclusive_group()
    player_group.add_argument('-p', dest='player', metavar='#', help='player # in --list-players')
    
    list_group = parser.add_mutually_exclusive_group()
    list_group.add_argument('--list-cc', action='store_true', help='list all client contexts')
    list_group.add_argument('--list-games', action='store_true', help='list all games')
    list_group.add_argument('--list-players', action='store_true', help='list all players')
    list_group.add_argument('--list-ops', action='store_true', help='list all achievement pending ops')
    list_group.add_argument('--list-lb-ops', action='store_true', help='list all leaderboard pending ops')
    
    package_list_group = parser.add_mutually_exclusive_group()
    package_list_group.add_argument('--list-achs', action='store_true', help='list all achievements')
    package_list_group.add_argument('--list-u-achs', action='store_true', help='list all unlocked achievements')
    package_list_group.add_argument('--list-nu-achs', action='store_true', help='list all not unlocked achievements')
    package_list_group.add_argument('--list-nor-achs', action='store_true', help='list all normal achievements')
    package_list_group.add_argument('--list-inc-achs', action='store_true', help='list all incremental achievements')
    package_list_group.add_argument('--list-sec-achs', action='store_true', help='list all secret achievements')
    package_list_group.add_argument('--list-lbs', action='store_true', help='list all leaderboards for given package')
    
    search_group = parser.add_argument_group()
    search_group.add_argument('--search-games', metavar='search', nargs=1, type=str, help='search for a game by input')
    search_group.add_argument('--search-achs', metavar='search', nargs=1, type=str, help='search for an achievement by input')
    search_group.add_argument('--search-u-achs', metavar='search', nargs=1, type=str, help='search for unlocked achievements by input')
    search_group.add_argument('--search-nu-achs', metavar='search', nargs=1, type=str, help='search for not unlocked achievements by input')
    search_group.add_argument('--search-nor-achs', metavar='search', nargs=1, type=str, help='search for normal achievements by input')
    search_group.add_argument('--search-inc-achs', metavar='search', nargs=1, type=str, help='search for incremental achievements by input')
    search_group.add_argument('--search-sec-achs', metavar='search', nargs=1, type=str, help='search for secret achievements by input')
    search_group.add_argument('--search-lbs', metavar='search', nargs=1, type=str, help='search for a leaderboard by input')
    
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument('--unlock-id', dest='unlock_id', metavar='external_id', nargs=1, type=str, help='unlocks an achievement by its external id')
    action_group.add_argument('--unlock-all', dest='unlock_all', action='store_true', help='unlocks all achievements in given package')
    action_group.add_argument('--unlock-listed', dest='unlock_listed', action='store_true', help='unlocks all listed achievements')
    action_group.add_argument('--submit-score', dest='submit_score', metavar=('lb_id', 'score'), nargs=2, type=str, help='submit score to a leaderboard (e.g. --submit-score CgkI... 1500)')
    
    args = parser.parse_args()
else:
    args.input = "dbs\\games_2db19fbf.db"

if __name__ == "__main__":
    if not DEBUG:
        if len(sys.argv[1:]) == 0:
            parser.print_help()
            exit(1)

    GooglePlayAchievementUnlocker(args).run()
