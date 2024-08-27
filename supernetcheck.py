import ipaddress

def checkSubnets(subnet_list):
    subnets = [ipaddress.ip_network(subnet) for subnet in subnet_list]
    subnets.sort(key=lambda x: (x.prefixlen, x.network_address))
    
    result = []
    for subnet in subnets:
        if not any(subnet.supernet_of(existing_subnet) for existing_subnet in result):
            result.append(subnet)
    
    return [str(subnet) for subnet in result]

def readSubnets(file_path):
    with open(file_path, 'r') as file:
        subnets = file.read().splitlines()
    return subnets

def writeSubnets(subnets, file_path):
    with open(file_path, 'w') as file:
        for subnet in subnets:
            file.write(subnet + '\n')

input_file = 'input_subnets.txt'
output_file = 'output_subnets.txt'

subnets = readSubnets(input_file)
deduplicated_subnets = checkSubnets(subnets)
writeSubnets(deduplicated_subnets, output_file)
