import sys
from mail_util import MailUtil
from util import Util
from report_service import ReportService
from config_parser import LocalConfigParser
from db_config import DBConfig
from config_enum import Config
from mail_config import MailConfig


class AutomatedReportTool:

    zip_file_pattern = ".zip"

    def __init__(self, arg, period):
        self.__local_config_parser = ""
        self.__reporting_period = ""
        if len(arg) > 1:
            self.__local_config_parser = LocalConfigParser(arg)

        if len(period) > 1:
            self.__reporting_period = period

    def __get_db_config(self):
        db = self.__local_config_parser.get_config(Config.DB.value)
        username = self.__local_config_parser.get_config(Config.USER.value)
        password = self.__local_config_parser.get_config(Config.PASSWORD.value)
        db_config = DBConfig(db, username, password)
        return db_config

    def __get_mail_config(self):
        email_to = self.__local_config_parser.get_config(Config.EMAIL_TO.value)
        email_from = self.__local_config_parser.get_config(Config.EMAIL_FROM.value)
        email_cc = self.__local_config_parser.get_config(Config.EMAIL_CC.value)
        subject = self.__local_config_parser.get_config(Config.SUBJECT.value)
        body = self.__local_config_parser.get_config(Config.BODY.value)
        mail_config = MailConfig(email_to, email_from, subject, body, email_cc)
        return mail_config

    @staticmethod
    def main(path, period):
        art = AutomatedReportTool(path, period)
        db_config = art.__get_db_config()
        archive_dir = art.__local_config_parser.get_config(Config.DIR_ARCHIVE.value)
        sql_query = art.__local_config_parser.get_config(Config.SQL_QUERY.value)
        file_name = art.__local_config_parser.get_config(Config.FILE_NAME.value)
        dir_data_out = art.__local_config_parser.get_config(Config.DIR_DATA_OUT.value)
        report_service = ReportService(db_config, sql_query, file_name, dir_data_out)
        report_service.execute_reports()
        zip_file_name = art.__local_config_parser.get_config(Config.ZIP_FILE_NAME.value)
        Util.zip_files(dir_data_out, dir_data_out, "xlsx", zip_file_name)
        zip_file = Util.get_list_of_files(dir_data_out, art.zip_file_pattern)
        mail_config = art.__get_mail_config()
        email_server = Util.get_environment_property(Config.EMAIL_SERVER.value)
        subject = mail_config.get_subject()
        if len(art.__reporting_period) > 1:
            subject = mail_config.get_subject() + " " + art.__reporting_period
        MailUtil.send_mail(mail_config.get_email_from(), mail_config.get_email_to(), mail_config.get_cc(),
                           subject, mail_config.get_body(), zip_file, email_server)
        Util.move_list_of_files(dir_data_out, archive_dir, "xlsx")
        Util.move_list_of_files(dir_data_out, archive_dir, art.zip_file_pattern)


if __name__ == '__main__':
    try:
        args = sys.argv
        if len(args) == 1:
            print("Please add config file to the argument list - see the sample config file in hte repo")
            exit()

        if len(args) >= 3:
            AutomatedReportTool.main(args[1], args[2])
        else:
            AutomatedReportTool.main(args[1], "")
    except Exception as e:
        print(str(e))
        MailUtil.send_mail("youremailid", "youremailid", "youremailid",
                           "Error processing " + sys.argv[1], str(e), '',
                           Util.get_environment_property(Config.EMAIL_SERVER.value))
