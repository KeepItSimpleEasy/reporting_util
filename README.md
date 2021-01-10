# reporting_util
Usage:

/usr/local/bin/python3.7 automated_report_tool.py <path of config file> >> /tmp/1.log
e.g. /usr/local/bin/python3.7 automated_report_tool.py config/sample.ini

Set the environment variable:

EMAIL_SERVER=email server name

This is utility tool which reads a config file and does the following for you:

* Runs a query in oracle database
* Create an excel file
* Zip the excel file
* Send an email with the attachment to configured reciepients
* archive the xlsx and zip file

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
