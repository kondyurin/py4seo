# Создать парсер с использованием классов, который будет писать данные в базу.
# Можете переписать парсер с предыдущего ДЗ, или написать любой другой.
# Модуль для работы с базой должен быть отдельным, т.е. у вас должно получиться
# минимум два файла.
# Еще обязательно задайте уникальные имена своим таблицам в базе и пришлите их
# вместе с ДЗ.


import sqlalchemy as sa


class Database:
    def __init__(self):
        self.TABLE_NAME = 'kondyurin_crawler'
        self.connection = {'user': 'py4seo', 'database': 'library', 'host': '46.30.164.249', 'password': 'PY1111forSEO'}
        self.dsn = 'postgresql://{user}:{password}@{host}/{database}'.format(**self.connection)
        self.engine = sa.create_engine(self.dsn)
        self.metadata = sa.MetaData()
        self.metadata.bind = self.engine
        self.domain = sa.Table(
            self.TABLE_NAME, self.metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('domain', sa.String(255)),
            sa.Column('url', sa.Text),
            sa.Column('title', sa.Text),
            sa.Column('description', sa.Text),
            sa.Column('h1', sa.Text)
        )

    def create_db(self):
        return self.metadata.create_all()

    def write_to_db(self, item_values):
        conn = self.engine.connect()
        query = self.domain.insert().values(**item_values)
        conn.execute(query)

if __name__ == '__main__':
    # Database().create_db()
    # dct = {'domain': 'asdasd.ru'}
    # res = Database().write_to_db(dct)
    print("DB successfully created!")
