import psutil, os, sys, time, keyboard
from colorama import Fore, Style, init
init()

total = 30

os.system('cls')

print(Fore.CYAN + '================================')
print( '       Monitor de Sistema       ')
print( '================================')

time.sleep(3)

os.system('cls')

print('Inicializando Monitor de sistemas!')

time.sleep(2)

os.system('cls')

dots = ['', '.', '..', '...']

for i in range(20):
    sys.stdout.write( Fore.CYAN + '\rCarregando' + dots[i % len(dots)] + '   '  + Style.RESET_ALL)
    sys.stdout.flush()
    time.sleep(0.4)

os.system('cls')

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('C:\\').percent

if cpu <= 60:
    print(Fore.GREEN + 'Uso de CPU dentro do esperado: ' + str(cpu) + '%' + Style.RESET_ALL)

elif cpu <= 80:
    print(Fore.YELLOW + 'Uso de CPU elevado: ' + str(cpu) + '%' + Style.RESET_ALL)

else:
    print(Fore.RED + 'Uso Crítico de CPU detectado: ' + str(cpu) + '%' + Style.RESET_ALL)

time.sleep(2)

if ram <= 60:
    print(Fore.GREEN + 'Uso de memória dentro do esperado: ' + str(ram) + '%' + Style.RESET_ALL)

elif ram <= 80:
    print(Fore.YELLOW + 'Uso de memória elevado: ' + str(ram) + '%' + Style.RESET_ALL)

else:
    print(Fore.RED + 'Consumo crítico de memória: ' + str(ram) + '%' + Style.RESET_ALL)

time.sleep(2)

if disk <= 70:
    print(Fore.GREEN + 'Espaço em disco adequado: ' + str(disk) + '%')

elif disk <= 85:
    print(Fore.YELLOW + 'Espaço em disco acima do recomendado: ' + str(disk) + '%')

else:
    print(Fore.RED + 'Armazenamento crítico: ' + str(disk) + '%')

time.sleep(2)

os.system('cls')

dots = ['', '.', '..', '...']

for i in range(20):
    sys.stdout.write('\r' + dots[i % len(dots)] + '   '  + Style.RESET_ALL)
    sys.stdout.flush()
    time.sleep(0.4)

os.system('cls')

print(Fore.CYAN + '================================')
print( '         Módulo de Rede       ')
print( '================================')

time.sleep(3)
os.system('cls')

print('Inicializando Módulo de Rede!')

time.sleep(2)

os.system('cls')

dots = ['', '.', '..', '...']

for i in range(20):
    sys.stdout.write( Fore.CYAN + '\rCarregando' + dots[i % len(dots)] + '   '  + Style.RESET_ALL)
    sys.stdout.flush()
    time.sleep(0.4)

os.system('cls')

print(Fore.GREEN + 'Aperte Q para encerrar o módulo.')

time.sleep(2)

def bytes_para_mbps(bytes_por_segundo: float) -> float:
    return (bytes_por_segundo * 8) / (1024 * 1024)

io_antes = psutil.net_io_counters()
sent_antes = io_antes.bytes_sent
recv_antes = io_antes.bytes_recv
pico_down = 0
pico_up = 0

try:
    while True:
        if keyboard.is_pressed('q'):
            print(Fore.RED + "\nEncerrando módulo...")
            break

        time.sleep(1)  

        io_agora = psutil.net_io_counters()
        sent_agora = io_agora.bytes_sent
        recv_agora = io_agora.bytes_recv

        up_bps = sent_agora - sent_antes
        down_bps = recv_agora - recv_antes

        sent_antes = sent_agora
        recv_antes = recv_agora

        up_mbps = bytes_para_mbps(up_bps)
        down_mbps = bytes_para_mbps(down_bps)

        if down_mbps > pico_down:
            pico_down = down_mbps

        if up_mbps > pico_up:
            pico_up = up_mbps


        if down_mbps < 1:
            cor = Fore.GREEN
            status = "OK"
        elif down_mbps < 10:
            cor = Fore.YELLOW
            status = "ATENÇÃO"
        else:
            cor = Fore.RED
            status = "ALTO"

        print(
            cor + f"[{status}] Down: {down_mbps:6.2f} Mbps | Up: {up_mbps:6.2f} Mbps"
            + Style.RESET_ALL,
            end="\r"
        )

except KeyboardInterrupt:
    print("\rMódulo encerrado (Ctrl+C).")

time.sleep(3)
os.system('cls')

print("\n")
print(Fore.CYAN + "================================" + Style.RESET_ALL)
print(Fore.CYAN + "      RESUMO DO SISTEMA          " + Style.RESET_ALL)
print(Fore.CYAN + "================================" + Style.RESET_ALL)

print(Fore.BLUE + f"CPU Final:   {cpu}%")
print(f"RAM Final:   {ram}%")
print(f"Disco Final: {disk}%")

print("--------------------------------")
print(f"Pico Download: {pico_down:.2f} Mbps")
print(f"Pico Upload:   {pico_up:.2f} Mbps" + Style.RESET_ALL)

print(Fore.CYAN + "================================" + Style.RESET_ALL)

