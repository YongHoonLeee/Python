"""Using yaml file
"""
import yaml

# TODO make yaml file
with open('ConfigAndLogging/config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 80
        }
    }, yaml_file)
