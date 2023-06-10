import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import logging


logger = logging.getLogger()
logger.setLevel('INFO')


def symmetric_encrypt(key: bytes, text: bytes, len: int) -> bytes:
    """
    Функция шифрования текста алгоритмом симметричного шифрования Camellia
    :param len: длина ключа
    :param text: шифруемый текст
    :param key: ключ
    :return: зашифрованный текст
    """
    try:
        padder = padding.ANSIX923(len).padder()
        padded_text = padder.update(text) + padder.finalize()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        logging.info(f'Текст зашифрован алгоритмом Camellia')
    except OSError as err:
        logging.warning(f'{err} Ошибка при симметричном шифровании!')
    return iv + encrypted_text


def load_symmetric_key(file_name: str) -> bytes:
    """
    Функция десериализации ключа симметричного шифрования
    :param file_name: название файла
    :return: ключ
    """
    try:
        with open(file_name, mode='rb') as key_file:
            key = key_file.read()
        logging.info(f'Симметричный ключ десериализован из {file_name}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при десериализации симметричного ключа из {file_name}')
    return key


def symmetric_decrypt(key: bytes, cipher_text: bytes, len: int) -> bytes:
    """
    Функция расшифровки симметрично зашифрованного текста
    :param len: длина ключа
    :param cipher_text: зашифрованный текст
    :param key: ключ
    :return: расшифрованный текст
    """
    try:
        cipher_text, iv = cipher_text[16:], cipher_text[:16]
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        text = decryptor.update(cipher_text) + decryptor.finalize()
        unpadder = padding.ANSIX923(len).unpadder()
        unpadded_text = unpadder.update(text) + unpadder.finalize()
        logging.info(f'Симметрично зашифрованный (алгоритмом Camellia) текст расшифрован')
    except OSError as err:
        logging.warning(f'{err} Ошибка при симметричном дешифровании!')
    return unpadded_text
