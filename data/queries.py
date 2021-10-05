EVENT_ID_QUERY = '''query EventIDQuery($slug: String!) {
    tournament(slug: $slug) {
        events {
            id
            slug
        }
    }
}
'''

PLAYER_ID_QUERY = '''query PlayerIDQuery($eventID: ID!) {
    event(id: $eventID) {
        entrants(query: {
            page: 1
            perPage: 32
        }) {
            nodes {
                participants {
                    gamerTag
                    player {
                        id
                    }
                }
            }
        }
    }
}
'''

PLAYER_SETS_QUERY = '''query PlayerSetsQuery($eventId: ID!, $playerId: ID!) {
    event(id: $eventId) {
        id
        name
        sets (
            page: 1
            perPage: 32
            sortType: STANDARD
            filters: {entrantIds: [$playerId]}
        ) {
            pageInfo {
                total
            }
            nodes {
                id
                slots {
                    id
                    entrant {
                        id
                        name
                    }
                }
            }
        }
    }
}
'''

PLAYER_SET_QUERY = '''query PlayerSetQuery($setId: ID!) {
    set(id: $setId) {
        state
        slots {
            entrant {
                id
                name
            }
            standing {
                placement
                stats {
                    score {
                        value
                    }
                }
            }
        }
    }
}
'''