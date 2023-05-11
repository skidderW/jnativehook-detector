import subprocess
import re
import psutil
import datetime
import colorama
from colorama import Fore

colorama.init()

print("Scanning...")

def get_user_logon_time():
    boot_time = psutil.boot_time()
    elapsed_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(boot_time)
    return datetime.datetime.now() - elapsed_time

user_logon_time = get_user_logon_time()

command = 'fsutil usn readjournal C: csv'
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

filtered_output = [line for line in output.decode('cp1252').split('\n') if '.dll' in line and '0x00000100' in line and 'JNativeHook' in line]
filtered_output_str = '\n'.join(filtered_output)

if not filtered_output_str.strip():
    clean = Fore.GREEN + r"""No cheats found."""
    print("")
    print("")
    print("")
    print("")
    print("Results:")
    print (clean)

else:
    lines = filtered_output_str.split('\n')
    for line in lines:
        if line.strip() == "":
            continue
        fields = line.split(',')
        file_name = fields[3]
        file_create_time = datetime.datetime.strptime(fields[5], '"%m/%d/%Y %H:%M:%S"')
        if file_create_time > user_logon_time:
            detected = Fore.LIGHTRED_EX + r"""Java Clicker in instance."""
            print("")
            print("")
            print("")
            print("")
            print("Results:")
            print (detected)