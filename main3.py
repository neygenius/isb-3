import argparse
import settings
from generation import gen_symmetric_key, gen_asymmetric_keys, save_symmetric_key, save_asymmetric_keys
from encryption import symmetric_encrypt, asymmetric_encrypt
from decryption import asymmetric_decrypt, load_symmetric_key, load_private_key
from extras import read_text, write_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-gen', '--generation', nargs="?", const=256, type=int,
                        help='Запускает режим генерации ключей')
    parser.add_argument('-enc', '--encryption', nargs="?", const=256, type=int,
                        help='Запускает режим шифрования')
    parser.add_argument('-dec', '--decryption', nargs="?", const=256, type=int,
                        help='Запускает режим дешифрования')

    args = parser.parse_args()
    if args.generation is not None:
        symmetric_key = gen_symmetric_key(args.generation)
        private_key, public_key = gen_asymmetric_keys()
        save_asymmetric_keys(private_key, public_key,
                             settings['secret_key'], settings['public_key'])
        cipher_symmetric_key = asymmetric_encrypt(public_key, symmetric_key)
        save_symmetric_key(cipher_symmetric_key, settings['symmetric_key'])
    elif args.encryption is not None:
        private_key = load_private_key(settings['secret_key'])
        cipher_key = load_symmetric_key(settings['symmetric_key'])
        symmetric_key = asymmetric_decrypt(private_key, cipher_key)
        text = read_text(settings['initial_file'])
        cipher_text = symmetric_encrypt(symmetric_key, text, args.encryption)
        write_text(cipher_text, settings['encrypted_file'])
    else:
        print(' ')
