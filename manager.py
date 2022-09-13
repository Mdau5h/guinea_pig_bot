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
        row = db.fetch_with_pagination(self.table_name, ['*'], 1)
        message_date = row[0][1]
        message_body = row[0][2]
        return message_date, message_body

    def get_message_by_id(self, record_id):
        row = db.fetch_by_id(self.table_name, ['*'], record_id)
        message_date = row[0][1]
        message_body = row[0][2]
        return message_date, message_body

    def get_message_list(self):
        rows = db.fetch_with_pagination(self.table_name, ['*'], 5)
        return [row[:-1] for row in rows]

    @staticmethod
    def _get_now_formatted() -> str:
        """Возвращает сегодняшнюю дату строкой"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    manager = DBManager()
    print(manager.get_message_list())
