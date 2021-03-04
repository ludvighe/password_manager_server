# Message responses for various functions and errors
# NOTE: Error numbering will not be changed and and i meant to be relied on in client

# Json Message Responses
message = lambda a: {'message': a} 

success_message = {'message': 'success'}


# Json Error Responses

test_null_error = {'error': {'error_code': 0, 'message': 'null - test'}}

# General error message
error = lambda a: {'error': {'error_code': 1 , 'message': a}}

# Request based
invalid_request_error = {'error': {'error_code': 10, 'message': 'invalid request'}}
missing_params_error = {'error': {'error_code': 11, 'message': 'missing parameters'}}
not_found_error = lambda a: {'error': {'error_code': 12, 'message': f'{a} not found'}}

# Client/Database based (denials)
key_verification_error = {'error': {'error_code': 100, 'message': 'invalid key'}}
already_exists_error = lambda a: {'error': {'error_code': 101, 'message': f'{f} already exists'}}