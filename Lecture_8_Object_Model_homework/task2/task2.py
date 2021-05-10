import sqlite3


class TableData:
    __slots__ = ["database_name", "table_name"]

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def __len__(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT count(*) from {self.table_name}")
        return cursor.fetchone()[0]

    def __iter__(self):
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = TableData.dict_factory
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from {self.table_name}")
        while True:
            row = cursor.fetchone()
            if row:
                yield row
            else:
                break

    def __contains__(self, item):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT count(*) from {self.table_name} where name='{item}'")
        count = cursor.fetchone()[0]
        return count > 0

    def __getitem__(self, item):
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = TableData.dict_factory
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from {self.table_name} where name='{item}'")
        return cursor.fetchone()

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
