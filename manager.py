from datetime import datetime
from aiogram.dispatcher.filters.state import State, StatesGroup
import db


class FSM(StatesGroup):
    new_msg = State()
    msg_list = State()


class DBManager:

    table_name = 'diary'

    def add_message(self, raw_message: str):
        """Добавляет новое сообщение.
        Принимает на вход текст сообщения, пришедшего в бот."""
        message = {
            'created': f'{self._get_now_formatted()}',
            'message': f'{raw_message}'
        }
        db.insert(self.table_name, message)

    def delete_message(self, row_id: int) -> None:
        """Удаляет сообщение по его идентификатору"""
        db.delete(self.table_name, row_id)

    def get_last_message(self):
        """Возвращает последнее записанное сообщение"""
        return db.fetch_with_pagination(self.table_name, ['created', 'message'], 1)[0]

    # todo отрефакторить как get_last_message
    def get_message_by_id(self, record_id):
        """Возвращает сообщение по его идентификатору"""
        row = db.fetch_by_id(self.table_name, ['*'], record_id)
        message_date = row[0][1]
        message_body = row[0][2]
        return message_date, message_body

    def get_message_list(self):
        """Возвращает список сообщений"""
        return db.fetch_with_pagination(self.table_name, ['id', 'created'], 5)

    # todo Переделать в db.py под нормальный запрос
    def get_messages_count(self):
        """Возвращает количество записей"""
        rows = db.fetchall(self.table_name, ['*'])
        return len(rows)

    @staticmethod
    def _get_now_formatted() -> str:
        """Возвращает сегодняшнюю дату строкой"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    manager = DBManager()
    print(manager.get_last_message())
