import socket
import re
import common_ports


def get_open_ports(target, port_range, verbose_mode=False):
    #Socket scanning port and append into list
    ip = ""
    open_ports = []
    hostnamenotfound = False
    try:
      ip = socket.gethostbyname(target)
      for port in range(port_range[0], port_range[1]+1):
        #Initialize socket to connect
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((ip, port))
        if result == 0:
          open_ports.append(port)
        s.close()
    
    except KeyboardInterrupt:
      return "Exiting program"
    except socket.gaierror:
      if(re.search("[a-zA-Z]", target)):
        return "Error: Invalid hostname"
      return "Error: Invalid IP address"
    except socket.error:
      return "Error: Invalid IP address"
    #Connect socket to get hostname/IPAddress
    host = None
    try:
      host = socket.gethostbyaddr(ip)[0]
    except socket.herror:
      host = None
      hostnamenotfound = True
  
    #Returned verbose mode
    if not verbose_mode:
      print(open_ports)
      return (open_ports)
    else:
      returned_string = ""
      returned_string += f"Open ports for {host} ({ip})\n"
      #If hostname not found, use IP adress as name
      if hostnamenotfound : 
        returned_string = f"Open ports for {ip}\n"
      returned_string += "PORT     SERVICE\n"
    
      for port in open_ports:
        spacing = "".center(9-len(str(port)))
        returned_string += f'{port}{spacing}{common_ports.ports_and_services[port]}\n'
  
      return returned_string.rstrip("\n")
  
    #return (open_ports)
  