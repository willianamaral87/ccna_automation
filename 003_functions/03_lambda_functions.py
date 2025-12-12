# Sort interfaces by port number
interfaces = ['Gi0/12', 'Gi0/1', 'Gi0/2', 'Gi0/11']
interfaces.sort(key=lambda x: int(x.split('/')[-1]))
print(interfaces)