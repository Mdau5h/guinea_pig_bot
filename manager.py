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
        rows = db.fetchall(self.table_name, ['*'])
        # хуйня, надо править, тут идет запрос всей базы, кто знает сколько там будет записей
        message_date = rows[-1][1]
        message_body = rows[-1][2]
        return message_date, message_body


    @staticmethod
    def _get_now_formatted() -> str:
        """Возвращает сегодняшнюю дату строкой"""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# manager = DBManager()
# print(manager.last_message())
