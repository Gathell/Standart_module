import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
        os.getenv('HOMEPATH'), \
            'test.log')

else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('сохраняем в лог в', logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename= logging_file,
    filemode= 'w',
)

logging.debug("начало программы")
logging.info('какие-то действия')
logging.warning('программа умирает')