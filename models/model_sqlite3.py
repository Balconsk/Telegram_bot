import sqlite3


class DataBase:
    __instance = None
<<<<<<< HEAD
    __connect = sqlite3.connect("this_database.db")
    __cursor = __connect.cursor()
    __cursor.execute("CREATE TABLE IF NOT EXISTS openai_logs \
            (user_id INTEGER, product TEXT, prompt TEXT, answer TEXT, tokens INTEGER, status INTEGER);")
    __cursor.execute("CREATE TABLE IF NOT EXISTS admins_id (user_id INTEGER)")
    __cursor.execute("CREATE TABLE IF NOT EXISTS allowed_users (user_id INTEGER, token INTEGER)")
    __connect.commit()
=======
>>>>>>> 96c23cf (add readme and create funk create_database)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
<<<<<<< HEAD
=======
            cls.__connect = sqlite3.connect("this_database.db")
            cls.__cursor = cls.__connect.cursor()
>>>>>>> 96c23cf (add readme and create funk create_database)
        return cls.__instance

    def __del__(self):
        self.__connect.close()

<<<<<<< HEAD
=======
    def create_database(self):
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS openai_logs \
                    (user_id INTEGER, product TEXT, prompt TEXT, answer TEXT, tokens INTEGER, status INTEGER);")
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS admins_id (user_id INTEGER)")
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS allowed_users (user_id INTEGER, token INTEGER)")

>>>>>>> 96c23cf (add readme and create funk create_database)
    def checking_user_in_table(self, user_id: int, table="allowed_users") -> bool:
        """Checking the availability of the user in the database"""
        sql = "SELECT user_id FROM table WHERE user_id == ?;"
        if table == "allowed_users":
            sql = sql.replace("table", "allowed_users")
        elif table == "admins_id":
            sql = sql.replace("table", "admins_id")
        self.__cursor.execute(sql, (user_id,))
        if len(self.__cursor.fetchall()) == 0:
            return False
        return True

    def get_admin_list(self):
        """Returns the list of admin IDs"""
        self.__cursor.execute("SELECT user_id FROM admins_id;")
        return [int(i[0]) for i in self.__cursor.fetchall()]

    def add_admin(self, admin_id):
        """Adds admin id to the table admins_id"""
        # Need each id admins be unique
        if not self.checking_user_in_table(admin_id):
            self.__cursor.execute("INSERT INTO admins_id (user_id) VALUES(?);", (admin_id,))
            self.__connect.commit()
            return True
        return False

    def get_allowed_users_list(self):
        """Returns the list of allowed users IDs"""
        self.__cursor.execute("SELECT user_id FROM allowed_users;")
        return [int(i[0]) for i in self.__cursor.fetchall()]

    def add_allowed_user(self, user_id, tokens=5000):
        """Adds user id to the table allowed_users"""
        # Need each id admins be unique
        if not self.checking_user_in_table(user_id):
            self.__cursor.execute("INSERT INTO allowed_users (user_id, token) VALUES(?, ?);", (user_id, tokens))
            self.__connect.commit()
            return True
        else:
            return False

    def remove_allowed_user(self, user_id: int) -> bool:
        """Remove user ID from the allowed_users table"""
        if self.checking_user_in_table(user_id):
            self.__cursor.execute("DELETE FROM allowed_users WHERE user_id == ?;", (user_id,))
            self.__connect.commit()
            return True
        else:
            return False

    def get_user_token(self, user_id: int) -> int:
        """Returns the number of tokens the user has"""
        if self.checking_user_in_table(user_id):
            self.__cursor.execute("SELECT token FROM allowed_users WHERE user_id==?;", [user_id, ])
            return self.__cursor.fetchall()[0][0]
        else:
            return False

    def change_token(self, user_id: int, token_count: str) -> bool:
        """This function will change the number of tokens in the allowed_user table"""
        if self.checking_user_in_table(user_id):
            sql = "UPDATE allowed_users SET token = {} WHERE user_id==?;"
            token_count = str(token_count)
            # write the or because (token - -arg) == (token + arg)
            if token_count.startswith('+') or token_count.startswith('-'):
                sql = sql.format('token + ?')
            else:
                sql = sql.format('?')
            self.__cursor.execute(sql, (token_count, user_id))
            self.__connect.commit()
            return True
        else:
            return False

    def write_log_openai(self, user_id, prompt, product="unknown", answer="", token=0, status="2"):
        """
        This function writes logs to the database.
        Status 0 - ok, 1 - bad, 2 - unknown
        """
        self.__cursor.execute("INSERT INTO openai_logs VALUES(?,?,?,?,?,?)",
                              (user_id, product, prompt, answer, token, status))
        self.__connect.commit()
<<<<<<< HEAD
=======

>>>>>>> 96c23cf (add readme and create funk create_database)
