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
        config['File_path'] = {'recording_path': 'recording',
                            'report_path': 'report'}
        config['Camera'] = {'black_list': '1'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
    #read config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    #check if config file is valid
    if not config.has_section('BE_Network'):
        raise ValueError('Invalid config file')
    
    return config

def check_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def test():
    conf = config_reader()
    check_directory(conf['File_path']['recording_path'])
    check_directory(conf['File_path']['report_path'])
    from src.video_controller import video_controller
    vc = video_controller(conf['File_path']['report_path'], conf['File_path']['recording_path'])
    vc.init_camera()
    vc.start_Recording()

if __name__ == '__main__':
    # test()
    conf = config_reader()
    check_directory(conf['File_path']['recording_path'])
    check_directory(conf['File_path']['report_path'])
    program = ui_main_page(conf)
    program.run()