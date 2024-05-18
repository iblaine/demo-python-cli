import psutil
import time
import os

def get_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return uptime_seconds

def format_uptime(seconds):
    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{int(days)}d {int(hours)}h {int(minutes)}m"

def get_load_average():
    return os.getloadavg()

def get_users():
    return len(psutil.users())