from datetime import datetime
from aiogram.dispatcher.filters.state import State, StatesGroup
import db


class FSM(StatesGroup):
    new_msg = State()


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

    # todo
    def last_message(self):
        pass

    @staticmethod
    def _get_now_formatted() -> str:
        """Возвращает сегодняшнюю дату строкой"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


