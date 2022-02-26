import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig:
    
    @staticmethod
    def get_base_url():
        url = config.get('common info', 'base_url')
        return url
    
    @staticmethod
    def get_user_email():
        user_email = config.get('common info', 'user_email')
        return user_email
    
    @staticmethod
    def get_user_password():
        user_password = config.get('common info', 'user_password')
        return user_password