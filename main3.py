import argparse

from menu import menu_gen, menu_enc, menu_dec
from extras import load_settings


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str, help='Позволяет использовать собственный json-файл с путями')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', nargs="?", const=256, type=int, help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', nargs="?", const=256, type=int, help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', nargs="?", const=256, type=int, help='Запускает режим дешифрования')
    args = parser.parse_args()
    if args.settings is not None:
        settings = load_settings(args.settings)
    else:
        settings = load_settings('settings.json')
    if args.generation is not None:
        menu_gen(args.generation, settings['secret_key'], settings['public_key'], settings['symmetric_key'])
    elif args.encryption is not None:
        menu_enc(args.encryption, settings['secret_key'], settings['symmetric_key'], settings['initial_file'],
                 settings['encrypted_file'])
    else:
        menu_dec(args.encryption, settings['secret_key'], settings['symmetric_key'], settings['encrypted_file'],
                 settings['decrypted_file'])
