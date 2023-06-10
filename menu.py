from generation import gen_symmetric_key, gen_asymmetric_keys, save_symmetric_key, save_asymmetric_keys
from symmetric import symmetric_encrypt, symmetric_decrypt, load_symmetric_key
from asymmetric import asymmetric_encrypt, asymmetric_decrypt, load_private_key
from extras import read_text, write_text


def menu_gen(len: int, secret_key_file: str, public_key_file: str, symmetric_key_file: str) -> None:
    """
        Функция вызова генератора ключей из командной строки
        :param len: длина ключа симметричного шифрования
        :param secret_key_file: имя файла с закрытым ключом
        :param public_key_file: имя файла с открытым ключом
        :param symmetric_key_file: имя файла с симметричным ключом
        :return: None
    """
    symmetric_key = gen_symmetric_key(len)
    private_key, public_key = gen_asymmetric_keys()
    save_asymmetric_keys(private_key, public_key, secret_key_file, public_key_file)
    cipher_symmetric_key = asymmetric_encrypt(public_key, symmetric_key)
    save_symmetric_key(cipher_symmetric_key, symmetric_key_file)


def menu_enc(len: int, secret_key_file: str, symmetric_key_file: str, initial_file: str, encrypted_file: str) -> None:
    """
        Функция вызова шифратора из командной строки
        :param len: длина ключа симметричного шифрования
        :param secret_key_file: имя файл с закрытым ключом
        :param symmetric_key_file: имя файл с симметричным ключом
        :param initial_file: имя файла с исходным текстом
        :param encrypted_file: имя файла с зашифрованным текстом
        :return: None
    """
    private_key = load_private_key(secret_key_file)
    cipher_key = load_symmetric_key(symmetric_key_file)
    symmetric_key = asymmetric_decrypt(private_key, cipher_key)
    text = read_text(initial_file)
    cipher_text = symmetric_encrypt(symmetric_key, text, len)
    write_text(cipher_text, encrypted_file)


def menu_dec(len: int, secret_key_file: str, symmetric_key_file: str, encrypted_file: str, decrypted_file: str) -> None:
    """
        Функция вызова дешифратора из командной строки
        :param len: длина ключа симметричного шифрования
        :param secret_key_file: имя файл с закрытым ключом
        :param symmetric_key_file: имя файл с симметричным ключом
        :param encrypted_file: имя файла с зашифрованным текстом
        :param decrypted_file: имя файла с расшифрованным текстом
        :return: None
    """
    private_key = load_private_key(secret_key_file)
    cipher_key = load_symmetric_key(symmetric_key_file)
    symmetric_key = asymmetric_decrypt(private_key, cipher_key)
    cipher_text = read_text(encrypted_file)
    text = symmetric_decrypt(symmetric_key, cipher_text, len)
    write_text(text, decrypted_file)
