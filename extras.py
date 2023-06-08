import logging
import json

def load_settings(file_name: str) -> dict:
    """
    Функция загрузки файла настроек
    :param file_name: название файла
    :return: настройки
    """
    try:
        with open(file_name) as json_file:
            settings = json.load(json_file)
        logging.info(f'Настройки загружены из {file_name}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при загрузке настроек из {file_name}')
    return settings


def read_text(file_name: str) -> bytes:
    """
    Функция чтения текста из файла
    :param file_name: название файла
    :return: текст
    """
    try:
        with open(file_name, 'rb') as text_file:
            text = text_file.read()
        logging.info(f'{file_name} прочитан')
    except OSError as err:
        logging.warning(f'{err} Ошибка при чтении {file_name}!')
    return text


def write_text(text: bytes, file_name: str) -> None:
    """
    Функция записи текста в файл
    :param text: текст
    :param file_name: название файла
    :return: None
    """
    try:
        with open(file_name, 'wb') as text_file:
            text_file.write(text)
        logging.info(f'Текст записан в {file_name}')
    except OSError as err:
        logging.warning(f'{err} Ошибка записи в {file_name}!')
