import cx_Oracle
import pandas as pd


class DBUtil:

    @staticmethod
    def create_report(db_config, sql_query, file_name, dir_out):
        conn = cx_Oracle.connect(db_config.get_username(), db_config.get_password(), db_config.get_db())
        df = pd.read_sql(sql_query, conn)
        df.to_excel(dir_out + file_name)
        conn.close()

