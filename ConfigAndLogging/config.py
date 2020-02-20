"""ConfigParser init
"""
import configparser


# TODO config.ini 만들때
# config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug': True
# }
# config['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
# config['db_server'] = {
#     'host': '127.0.0.1',
#     'port': 3306
# }

# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

# TODO 읽을때

config = configparser.ConfigParser()
config.read('ConfigAndLogging/config.ini')
print(config['DEFAULT'], ['debug'])
print(config['db_server']['host'])
print(config['web_server'], ['port'])
