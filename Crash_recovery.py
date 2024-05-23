import subprocess
import time


def check_service(service_name):
    cmd = f'systemctl is-active {service_name}'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    status = proc.communicate()[0].decode('utf-8').strip()
    return status == 'active'

def restart_service(service_name):
    cmd = f'sudo systemctl restart {service_name}'
    subprocess.call(cmd, shell=True)

def auto_recovery(service_name, sleep_time=60):
    while True:
        if not check_service(service_name):
            print(f'The service {service_name} is not working. Restart...')
            restart_service(service_name)
        time.sleep(sleep_time)

service_name = input('Enter the name of the service: ')
auto_recovery(service_name)
