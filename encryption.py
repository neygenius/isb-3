import os
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding as aspadding
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


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    """
    Функция асимметричного шифрования по открытому ключу
    :param text: шифруемый текст
    :param public_key: открытый ключ
    :return: зашифрованный текст
    """
    try:
        encrypted_text = public_key.encrypt(text, aspadding.OAEP(mgf=aspadding.MGF1(algorithm=hashes.SHA256()),
                                                               algorithm=hashes.SHA256(), label=None))
        logging.info(f'Текст зашифрован алгоритмом асимметричного шифрования')
    except OSError as err:
        logging.warning(f'{err} Ошибка при асимметричном шифровании!')
    return encrypted_text
