import json

settings = {
    'initial_file': 'data/initial_file.txt',
    'encrypted_file': 'data/encrypted_file.txt',
    'decrypted_file': 'data/decrypted_file.txt',
    'symmetric_key': 'data/symmetric_key.txt',
    'public_key': 'data/public_key.pem',
    'secret_key': 'data/secret_key.pem'
}

if __name__ == '__main__':
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)
