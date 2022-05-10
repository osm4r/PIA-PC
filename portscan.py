# This script runs on Python 3
import os
import socket
import threading
import logging

if not os.path.exists('logs'):
  os.makedirs('logs')
logging.basicConfig(filename="logs/reporte.log", filemode="a",
                    format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',
                    level= logging.INFO)

def TCP_connect(ip, port_number, delay, output):
    """
        Funcion para realizar coneccion TCP.
        
        :Ejemplo:

        >>> TCP_connect('192.168.1.1', 542, 15, 'Listening')        
        
        :param ip: primer argumento
        :type ip: string
        :param port_number: segundo argumento
        :type port_number: int
        :param delay: tercer argumento
        :type delay: int
        :param output: cuarto argumento
        :type output: string
        """
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''


def scan_ports(Host_ip, delay):
    """
        Funcion para escanear puertos.
        
        :Ejemplo:

        >>> scan_ports('192.168.1.1', 15)        
        
        :param Host_ip: primer argumento
        :type Host_ip: string
        :param delay: segundo argumento
        :type delay: int
        """
    
    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(Host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(10000):
        threads[i].start()

    # Locking the main thread until all threads complete
    for i in range(10000):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ' : ' + output[i])
            logging.info(str(i) + ' : ' + output[i])


def ShootYourShot(Host_ip):
    """
        Funcion de redireccion.
        
        :Ejemplo:

        >>> ShootYourShot('192.168.1.1')        
        
        :param Host_ip: primer argumento
        :type Host_ip: string
        """

    # delay = int(input("How many seconds the socket is going to wait until timeout: "))
    logging.info("Escaneando...")
    try:
        scan_ports(Host_ip, delay=15)
    except Exception as e:
        logging.error(e)
