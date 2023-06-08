from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding as aspadding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import logging


def load_private_key(private_pem: str):
    """
    Функция десериализации закрытого ключа
    :param private_pem: название файла
    :return: закрытый ключ
    """
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        logging.info(f'Закрытый ключ десериализован из {private_pem}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при десериализации закрытого ключа из {private_pem}')
    return private_key


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


def asymmetric_decrypt(private_key, cipher_text: bytes) -> bytes:
    """
    Функция расшифровки асимметрично зашифрованного текста при помощи закрытого ключа
    :param text: зашифрованный текст
    :param private_key: закрытый ключ
    :return: расшифрованный текст
    """
    try:
        decrypted_text = private_key.decrypt(cipher_text,
                                             aspadding.OAEP(mgf=aspadding.MGF1(algorithm=hashes.SHA256()),
                                                          algorithm=hashes.SHA256(), label=None))
        logging.info(f'Асимметрично зашифрованный текст расшифрован')
    except OSError as err:
        logging.warning(f'{err} Ошибка при асимметричном дешифровании!')
    return decrypted_text
