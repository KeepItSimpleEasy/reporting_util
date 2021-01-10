from enum import Enum


class Config(Enum):
    DB = "DB"
    USER = "USER"
    PASSWORD = "PASSWORD"
    SQL_QUERY = "SQL_QUERY"
    EMAIL_TO = "EMAIL_TO"
    EMAIL_FROM = "EMAIL_FROM"
    EMAIL_CC = "EMAIL_CC"
    SUBJECT = "SUBJECT"
    BODY = "BODY"
    EMAIL_SERVER = "EMAIL_SERVER"
    DIR_DATA_OUT = "DIR_DATA_OUT"
    FILE_NAME = "FILE_NAME"
    DIR_ARCHIVE = "DIR_ARCHIVE"
    LOG_FILE = "LOG_FILE"
    DATA_OUT_FILE_PATTERN = "DATA_OUT_FILE_PATTERN"
    ZIP_FILE_NAME = "ZIP_FILE_NAME"
    OUTPUT_SUCCESS = "OUTPUT_SUCCESS"
