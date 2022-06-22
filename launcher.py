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

tasks_to_execute_macOS = ["CPU",
                          psutil.cpu_times(percpu=False),
                          psutil.cpu_times(),
                          psutil.cpu_times_percent(interval=None, percpu=False),
                          psutil.cpu_count(logical=True),
                          psutil.cpu_stats(),
                          psutil.cpu_freq(percpu=False),
                          psutil.getloadavg(),
                          "MEMORY",
                          psutil.virtual_memory(),
                          psutil.swap_memory(),
                          psutil.disk_partitions(all=False),
                          "DISK",
                          psutil.disk_partitions(all=False),
                          psutil.disk_usage("/System/Volumes/Data"),
                          psutil.disk_io_counters(perdisk=False, nowrap=True),
                          "FUNCTIONS",
                          psutil.pids(),
                          psutil.process_iter(attrs=None, ad_value=None),
                          "OPERATING SYSTEM CONSTANTS",
                          psutil.POSIX,
                          psutil.LINUX,
                          psutil.WINDOWS,
                          psutil.MACOS,
                          psutil.FREEBSD,
                          psutil.NETBSD,
                          psutil.OPENBSD,
                          psutil.BSD,
                          psutil.SUNOS,
                          psutil.AIX,
                          psutil.OSX,
                          #psutil.PROCFS_PATH,
                          "PROCESS STATUS CONSTANTS",
                          psutil.STATUS_RUNNING,
                          psutil.STATUS_SLEEPING,
                          psutil.STATUS_DISK_SLEEP,
                          psutil.STATUS_STOPPED,
                          psutil.STATUS_TRACING_STOP,
                          psutil.STATUS_ZOMBIE,
                          psutil.STATUS_DEAD,
                          #psutil.STATUS_WAKE_KILL,
                          psutil.STATUS_WAKING,
                          "PROCESS PRIORITY CONSTANTS",
                          #psutil.REALTIME_PRIORITY_CLASS(),
                          #psutil.HIGH_PRIORITY_CLASS,
                          #psutil.ABOVE_NORMAL_PRIORITY_CLASS,
                          #psutil.NORMAL_PRIORITY_CLASS,
                          #psutil.IDLE_PRIORITY_CLASS,
                          #psutil.BELOW_NORMAL_PRIORITY_CLASS,
                          #psutil.IOPRIO_CLASS_NONE,
                          #psutil.IOPRIO_CLASS_RT,
                          #psutil.IOPRIO_CLASS_BE,
                          #psutil.IOPRIO_CLASS_IDLE,
                          #psutil.IOPRIO_VERYLOW,
                          #psutil.IOPRIO_LOW,
                          #psutil.IOPRIO_NORMAL,
                          #psutil.IOPRIO_HIGH,
                          "PROCESS RESOURCES CONSTANTS",
                          #psutil.RLIM_INFINITY,
                          # psutil.RLIMIT_AS,
                          # psutil.RLIMIT_CORE,
                          # psutil.RLIMIT_CPU,
                          # psutil.RLIMIT_DATA,
                          # psutil.RLIMIT_FSIZE,
                          # psutil.RLIMIT_MEMLOCK,
                          # psutil.RLIMIT_NOFILE,
                          # psutil.RLIMIT_NPROC,
                          # psutil.RLIMIT_RSS,
                          # psutil.RLIMIT_STACK,
                          # psutil.RLIMIT_LOCKS,
                          # psutil.RLIMIT_MSGQUEUE,
                          # psutil.RLIMIT_NICE,
                          # psutil.RLIMIT_RTPRIO,
                          # psutil.RLIMIT_RTTIME,
                          # psutil.RLIMIT_SIGPENDING,
                          "CONNECTION CONSTANTS",
                          psutil.CONN_ESTABLISHED,
                          psutil.CONN_SYN_SENT,
                          psutil.CONN_SYN_RECV,
                          psutil.CONN_FIN_WAIT1,
                          psutil.CONN_FIN_WAIT2,
                          psutil.CONN_TIME_WAIT,
                          psutil.CONN_CLOSE,
                          psutil.CONN_CLOSE_WAIT,
                          psutil.CONN_LAST_ACK,
                          psutil.CONN_LISTEN,
                          psutil.CONN_CLOSING,
                          psutil.CONN_NONE,
                          "HARDWARE CONSTANTS",
                          psutil.AF_LINK,
                          psutil.NIC_DUPLEX_FULL,
                          psutil.NIC_DUPLEX_HALF,
                          psutil.NIC_DUPLEX_UNKNOWN,
                          psutil.POWER_TIME_UNKNOWN,
                          psutil.POWER_TIME_UNLIMITED,
                          psutil.version_info,
                          ]


def log_info_to_file():
    while True:
        for task in tasks_to_execute_macOS:
            logging.debug(task)
        time.sleep(args.seconds)


log_info_to_file()
