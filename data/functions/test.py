from data.api import run_query
from data.queries import *
import filters
# 620030
# 23856

# ID Fetchers

def get_event_id(tournament_slug, event_slug):
    variables = {'slug' : tournament_slug}
    response = run_query(EVENT_ID_QUERY, variables)
    event_id = filters.event_id_filter(response, event_slug)

    return event_id

def get_player_id(event_id, player):
    variables = {'eventID' : event_id}
    response = run_query(PLAYER_ID_QUERY, variables)
    player_id = filters.player_id_filter(response, player)

    return player_id
    
# Fetch player's sets

def get_player_sets(event_id, player_id):
    variables = {'eventID' : event_id, 'player_id' : player_id}
    response = run_query(PLAYER_SETS_QUERY, variables)
    sets = filters.player_sets_filter(response)

    return sets

# Fetch specific set

def get_player_set(set_id):
    variables = {'setID' : set_id}
    response = run_query(PLAYER_SET_QUERY, variables)
    set = filters.player_set_filter(response)

    return set