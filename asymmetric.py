from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as aspadding
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import logging


logger = logging.getLogger()
logger.setLevel('INFO')


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
