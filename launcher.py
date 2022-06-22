import logging
import argparse
import psutil
import time

# logging.basicConfig(filename='log_file.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--seconds", help="launch the program every N seconds", type=int)
args = parser.parse_args()
print("number passed as argument for seconds")
print(args.seconds)
logging.basicConfig(filename='log_file.log', encoding='utf-8', level=logging.DEBUG)

tasks_to_execute = [psutil.cpu_times(percpu=False), psutil.cpu_times(),
psutil.cpu_times_percent(interval=None, percpu=False), psutil.cpu_count(logical=True), 'INFO Sojhgiufhcvbis', psutil.virtual_memory(), psutil.swap_memory(), psutil.disk_partitions(all=False),
                     psutil.disk_usage("/System/Volumes/Data")]

#tasks_to_execute = ["Début", "Milieu", "Fin"]


def log_info_to_file():
    while True:
        for task in tasks_to_execute:
            logging.debug(task)
        time.sleep(args.seconds)


log_info_to_file()

# logging.info('INFO Sojhgiufhcvbis')
# logging.warning('warning A;jhkgcfvbn,too')
# logging.error('error And non-ASCII stuff, too, like Øresund and Malmö')
