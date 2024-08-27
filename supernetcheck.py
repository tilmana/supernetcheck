import ipaddress

inputFile = 'input_subnets.txt'
outputFile = 'output_subnets.txt'

def checkSubnets(subnet_list):
    newSubnets = []
    for subnet in subnets:
        if "/" not in subnet:
            subnet = subnet + "/32"
            newSubnets.append(subnet)
        else:
            newSubnets.append(subnet)
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

subnets = readSubnets(inputFile)
uniqueSubnets = checkSubnets(subnets)
writeSubnets(uniqueSubnets, outputFile)
