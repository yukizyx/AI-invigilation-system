from gui_src.gui import *
from gui_src.gui_status import *
import configparser
import os
def config_reader():
    #if config file does not exist, create one
    if not os.path.exists('config.ini'):
        config = configparser.ConfigParser()
        config['BE_Network'] = {'host': 'localhost', 
                            'port': '8765'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    #read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

if __name__ == '__main__':
    conf = config_reader()
    program = ui_main_page(conf)
    program.run()