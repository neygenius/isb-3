import argparse
import settings
from generation import gen_symmetric_key, gen_asymmetric_keys, save_asymmetric_keys
#import logging


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
    elif args.encryption is not None:
        print(' ')
    else:
        print(' ')
