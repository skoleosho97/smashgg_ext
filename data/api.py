import requests, constants

# Helper function; runs all query requests
def run_query(query, variables):
    json_request = {'query' : query, 'variables' : variables}

    try:
        request = requests.post(
            url='https://api.smash.gg/gql/alpha',
            json=json_request,
            headers=constants.header
        )
        #Error handling
        response = request.json()
        return response
    except:
        #more error handling
        return