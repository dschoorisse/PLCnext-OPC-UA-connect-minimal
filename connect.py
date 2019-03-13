from opcua import ua, Client
import time
import logging
import sys

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('opcua')

if __name__ == "__main__":
    client = Client("opc.tcp://192.168.1.10:4840")
    client.set_user('admin')
    client.set_password('3127fb3a')
    client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate-example.der,private-key-example.pem")

    try:
        client.connect()
        root = client.get_root_node()
        _logger.info('Objects node is: %r', root)

        objects = client.get_objects_node()
        node = client.get_node("ns=5;s=Arp.Plc.Eclr/NewProgram1.INPUT")
        
        print(node.get_value())

    finally:
        client.disconnect()
