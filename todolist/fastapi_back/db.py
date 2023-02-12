import psycopg2


class RestApiDataBase:
    def __init__(self):
        self.database = 'fastapi_todo'
        self.user = 'nick'
        self.password = '1234'
        self.host = 'localhost'
        self.port = '5432'
        self.cursor = self.connect_db().cursor()

    def connect_db(self):
        try:
            conn = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return conn
        except psycopg2.DatabaseError:
            print('Database error!')

    def make_query(self, query: str):
        try:
            with self.cursor:
                self.cursor.execute(query)
            self.connect_db().close()
        except psycopg2.DatabaseError:
            return 'Database error!'

    def create_table(self):
        self.make_query(
            """
                CREATE TABLE public.todolist
                (
                    id serial NOT NULL,
                    title character varying(128) NOT NULL,
                    description text NOT NULL,
                    PRIMARY KEY (id)
                );

                ALTER TABLE IF EXISTS public.todolist
                    OWNER to nick;
                COMMIT;
        """
        )

    def truncate_db(self):
        self.make_query(
            """
                TRUNCATE todolist RESTART IDENTITY;
                COMMIT;
        """
        )

    def get_all_rows(self):
        try:
            with self.cursor:
                self.cursor.execute(
                    """
                        SELECT * FROM public.todolist
                            ORDER BY id ASC
                """
                )
                self.connect_db().close()
                data = self.cursor.fetchall()
                return data

        except psycopg2.DatabaseError:
            return 'Database error!'

    def get_one_row(self, id_: int):
        try:
            with self.cursor:
                self.cursor.execute(f"SELECT * FROM todolist WHERE id = {id_}")
                self.connect_db().close()
                data = self.cursor.fetchone()
                return data

        except psycopg2.DatabaseError:
            return "Database error!"

    def create(self, title: str, description: str):
        self.make_query(
           f"INSERT INTO todolist(title, description)"
           f"VALUES ('{title}', '{description}');"
           "COMMIT;"
        )

    def update(self, id_: int, title: str, description: str):
        self.make_query(
            f"UPDATE todolist SET title = '{title}', description = '{description}' WHERE id = {id_}; COMMIT;"
        )

    def delete(self, id_):
        self.make_query(
            f"DELETE FROM todolist WHERE id = {id_}; COMMIT;"
        )

