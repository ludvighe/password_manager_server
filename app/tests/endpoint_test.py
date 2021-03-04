import requests

base_url = 'http://127.0.0.1:5000'
register_url = base_url + '/register'
key = '?key=key-0'

def __response_check(response, verbose):
    if response.status_code != 200:
        raise Exception(f'Endpoint failure: Status code [{response.status_code}]')
    if verbose: print('Status: ' + str(response.status_code))
    if 'error' in response.json():
        if response.json()['error']['error_code'] == 1:
            if verbose: print(f'{response.json()}\nPlease delete user or switch test user to complete test.\n')
        else:
            raise Exception(f'Endpoint failure: {response.json()}')
    if verbose: print('Response (JSON): ' + str(response.json()))

def user_endpoint(verbose):
    print('\nTESTING: User endpoint:')

    url = base_url + '/register'
    headers = {'Content-type': 'application/json'}

    if verbose: print('\n- register/create user')

    user_data = {
        "name": "name-1",
        "email": "email-1"
    }
    if verbose: print(f'Url: {url}')
    response = requests.post(url, json=user_data, headers=headers)
    __response_check(response, verbose)

    if 'error' not in response.json(): 
        key = response.json()['message']
    url = base_url + '/user?key=' + key
    if verbose: print('passed')

    if verbose: print('\n- get user')
    if verbose: print(f'Url: {url}')
    response = requests.get(url)
    __response_check(response, verbose)
    if verbose: print('passed')

    if verbose: print('\n- update user')

    user_data_updated = {
        "name": "name-1-updated",
        "email": "email-1"
    }
    if verbose: print(f'Url: {url}')
    response = requests.put(url, json=user_data_updated, headers=headers)
    __response_check(response, verbose)
    response = response = requests.get(url)
    if response.json()['name'] != 'name-1-updated': raise Exception('Endpoint failure: User was not updated.')
    if verbose: print('passed')

    if verbose: print('\n- delete user')
    if verbose: print(f'Url: {url}')
    response = requests.delete(url)
    __response_check(response, verbose)
    response = response = requests.get(url)
    if 'error' not in response.json(): raise Exception('Endpoint failure: User was not deleted.')
    if verbose: print('passed')

    print('\nUser endpoint PASSED')


def password_data_endpoint(verbose):
    print('\nTESTING: Password Data endpoint:')

    headers = {'Content-type': 'application/json'}

    if verbose: print('\nCreating temporary user')
    user_data = {
        "name": "name-1",
        "email": "email-1"
    }
    response = requests.post(register_url, json=user_data, headers=headers)
    key = response.json()['message']
    url = base_url + '/pwdata?key=' + key

    if verbose: print('\n- create password data')
    if verbose: print(f'Url: {url}')
    response = requests.post(url, json={
        "title": "title-1",
        "salt": "salt-1",
        "count": 16,
        "length": 16,
        "created": "created-1",
        "last_used": "last_used-1"
    }, headers=headers)
    __response_check(response, verbose)
    pwdata_id = response.json()['message']
    if verbose: print('passed')

    if verbose: print('\n- get password data')
    url = url + '&id=' + pwdata_id
    if verbose: print(f'Url: {url}')
    response = requests.get(url)
    __response_check(response, verbose)

    if verbose: print('\n- update password data')
    if verbose: print(f'Url: {url}')
    response = requests.put(url, json={
        "id": pwdata_id,
        "usr_id": "usr_id-1",
        "title": "title-1-updated",
        "salt": "salt-1",
        "count": 16,
        "length": 16,
        "created": "created-1",
        "last_used": "last_used-1"
    }, headers=headers)
    __response_check(response, verbose)
    response = response = requests.get(url)
    if response.json()['title'] != 'title-1-updated': raise Exception('Endpoint failure: Password was not updated.')

    if verbose: print('\n- delete password data')
    if verbose: print(f'Url: {url}')
    response = requests.delete(url)
    __response_check(response, verbose)
    response = response = requests.get(url)
    if 'error' not in response.json(): raise Exception('Endpoint failure: User was not deleted.')
    if verbose: print('passed')

    if verbose: print('\nDeleting temporary user')
    response = requests.delete(base_url + '/user?key=' + key)


    print('\nUser endpoint PASSED')


# user_endpoint(verbose=True)
password_data_endpoint(verbose=True)