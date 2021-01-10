import os

from dbutil import DBUtil


class ReportService:

    def __init__(self, db_config, sql_query, file_name, dir_data_out):
        self.__db_config = db_config
        self.__sql_query = sql_query
        self.__file_name = file_name
        self.__dir_data_out = dir_data_out

    def execute_reports(self):
        DBUtil.create_report(self.__db_config, self.__sql_query, self.__file_name, self.__dir_data_out)

