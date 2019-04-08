import jwt


def read_file(file_path, mode='r', max_len=None):
    with open(file_path, mode=mode) as file:
        data = file.read(max_len)
    return data


# PEM key=pair paths
private_key_path = 'C:/dev/keys/rsa/private.pem'
public_key_path = 'C:/dev/keys/rsa/pub.pem'

# Load PEM key-pair from files paths
private_key = file_data = read_file(private_key_path, 'rb')
public_key = file_data = read_file(public_key_path, 'rb')

# payload example
payload = {"iss": "it",
           "sub": "user",
           "user_id": "0164884b696f0a002700001100000002",
           "exp": 1747295000,
           "account_id": "0164884b696f0a002700001100000000",
           "request_id": "0164884b696f0a002700001100000001",
           "roles": ["User"]}
# headers = {
#   "alg": "RS256"
# }

encoded = jwt.encode(payload, private_key, algorithm='RS256')
print(encoded)
# decoded = jwt.decode(encoded, public_key, algorithms='RS256')
# print(decoded)