def event_id_filter(response, slug):
    if response['data']['tournaments'] is None:
        return

    for event in response['data']['tournaments']['events']:
        if event['slug'].split('/')[-1] == slug:
            return event['id']

def player_id_filter(response, slug):
    if response['data']['event']['entrants']['nodes'] is None:
        return
    
    for node in response['data']['event']['entrants']['nodes']:
        if node['participants']['gamerTag'].lower() == slug.lower():
            return node['participants']['gamerTag']
        elif (node['participants']['gamerTag'].split("|")[-1]).lower() == slug.lower():
            return node['participants']['gamerTag']

def player_sets_filter(response):
    if response['data']['event']['sets']['nodes'] is None:
        return

    return response['data']['event']['sets']['nodes']

def player_set_filter(response):
    if response['set'] is None:
        return

    return response['set']