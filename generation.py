import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import logging

logger = logging.getLogger()
logger.setLevel('INFO')


def gen_symmetric_key(len: int) -> bytes:
    """
    Функция генерации ключа для симметричного шифрования
    :param len: длина ключа
    :return: ключ
    """
    if len == 128 or len == 192 or len == 256:
        key = os.urandom(int(len/8))
        logging.info('Ключ для симметричного шифрования сгенерирован')
    else:
        logging.info('Длина ключа не равна 128, 192 или 256 бит')
    return key


def save_symmetric_key(key: bytes, file_name: str) -> None:
    """
    Функция сохранения ключа для симметричного шифрования
    :param key: ключ
    :param file_name: название файла
    :return: None
    """
    try:
        with open(file_name, 'wb') as key_file:
            key_file.write(key)
        logging.info(f'Симметричный ключ записан в {file_name}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи симметричного ключа в {file_name}!')


def gen_asymmetric_keys() -> tuple:
    """
    Функция генерирации ключей для асимметричного шифрования
    :return: закрытый ключ, открытый ключ
    """
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    logging.info('Ключ для асимметричного шифрования сгенерирован')
    return private_key, public_key


def save_asymmetric_keys(private_key, public_key, private_pem: str, public_pem: str) -> None:
    """
    Функция сохранения закрытого и открыторго ключей для ассиметричного шифрования
    :param private_key: закрытый ключ
    :param public_key: открытый ключ
    :param private_pem: название файла с закрытым ключом
    :param public_pem: название файла с открытым ключом
    :return: None
    """
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        logging.info(f'Закрытый ключ записан в {private_pem}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи закрытого ключа в {private_pem}!')
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logging.info(f'Открытый ключ записан в {public_pem}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи открытого ключа в {public_pem}!')
