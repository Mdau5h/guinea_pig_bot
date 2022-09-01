from datetime import datetime
import db


table_name = 'diary'


def add_expense(raw_message: str):
    """Добавляет новое сообщение.
    Принимает на вход текст сообщения, пришедшего в бот."""
    message = {
        'created': f'{_get_now_formatted()}',
        'message': f'{raw_message}'
    }
    db.insert(table_name, message)


def delete_expense(row_id: int) -> None:
    """Удаляет сообщение по его идентификатору"""
    db.delete(table_name, row_id)


def _get_now_formatted() -> str:
    """Возвращает сегодняшнюю дату строкой"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


print(_get_now_formatted())
