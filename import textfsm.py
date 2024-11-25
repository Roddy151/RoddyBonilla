import textfsm
from netmiko import ConnectHandler

# Conexión SSH con Netmiko
device = {
    'device_type': 'cisco_xr',
    'host': '10.0.0.1',
    'username': 'user',
    'password': 'password',
}

connection = ConnectHandler(**device)
output_summary = connection.send_command('show bgp summary')
output_run_bgp = connection.send_command('sh run router bgp')
output_advertised = connection.send_command('sh bgp advertised summary')
output_routes = connection.send_command('sh route ipv4 bgp | utility wc lines')

# Parseo con TextFSM
with open('show_bgp_summary.textfsm') as template:
    fsm_summary = textfsm.TextFSM(template)
    result_summary = fsm_summary.ParseText(output_summary)

with open('sh_run_router_bgp.textfsm') as template:
    fsm_run_bgp = textfsm.TextFSM(template)
    result_run_bgp = fsm_run_bgp.ParseText(output_run_bgp)

with open('sh_bgp_advertised_summary.textfsm') as template:
    fsm_advertised = textfsm.TextFSM(template)
    result_advertised = fsm_advertised.ParseText(output_advertised)

with open('sh_route_ipv4_bgp.textfsm') as template:
    fsm_routes = textfsm.TextFSM(template)
    result_routes = fsm_routes.ParseText(output_routes)

# Mostrar resultados
print("Resumen BGP:", result_summary)
print("Configuración BGP:", result_run_bgp)
print("Rutas Anunciadas:", result_advertised)
print("Total de Rutas IPv4:", result_routes)

connection.disconnect()