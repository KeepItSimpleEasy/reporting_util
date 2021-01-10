# reporting_util

Pre-requiste:

* Python3
* Create the config file and directories defined by you in the config
* Set the environment variable: EMAIL_SERVER=email server name

Usage:

pip install -e .

/usr/local/bin/python3.7 automated_report_tool.py "path of config file" >> /tmp/1.log

e.g. /usr/local/bin/python3.7 automated_report_tool.py config/sample.ini >> /tmp/1.log


This is utility tool which reads a config file and does the following for you:

* Runs a query in oracle database
* Create an excel file
* Zip the excel file
* Send an email with the attachment to configured reciepients
* archive the xlsx and zip file


Everything is configurable: database config, email config, Sql_query, report file name and zip file name, path to create the file and path to archive the file and zip. Please check the sample.ini for more details. 

The utility uses following python libraries:

* configparser
* cx_Oracle
* pandas
* smtplib
* os
* email import encoders
* email.mime.base import MIMEBase
* email.mime.multipart import MIMEMultipart
* email.mime.text import MIMEText
* datetime
* zipfile
* glob
