import xmlrpc.client

with xmlrpc.client.ServerProxy(('127.0.0.1', 8000)) as proxy:
    print(proxy.add_num(10, 20))
