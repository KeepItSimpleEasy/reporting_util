class MailConfig:
    def __init__(self, email_to='', email_from='', subject='', body='', cc=''):
        self.__email_to = email_to
        self.__email_from = email_from
        self.__subject = subject
        self.__body = body
        self.__cc = cc

    def get_email_to(self):
        email_to = self.__email_to
        return email_to

    def set_email_to(self, email_to):
        self.__email_to = email_to

    def get_email_from(self):
        email_from = self.__email_from
        return email_from

    def set_email_from(self, email_from):
        self.__email_from = email_from

    def get_subject(self):
        subject = self.__subject
        return subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_body(self):
        body = self.__body
        return body

    def set_body(self, body):
        self.__body = body

    def get_cc(self):
        cc = self.__cc
        return cc

    def set_cc(self, cc):
        self.__cc = cc
