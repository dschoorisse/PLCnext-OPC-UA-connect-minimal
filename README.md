# PLCnext-OPC-UA-connect-minimal
This is a minimal example to connect to a Phoenix Contact AXC F 2152 PLCnext enabled PLC. 

To familiarize myself with the OPC-UA protocol (and server in the PLC) I tried to connect to the PLC usings (almost) its default settings. The exact security string took me some time to get right; maybe this is useful for someone else.

*Use with python3 and be sure python-opcua is installed ("pip3 install opcua")
*The included certificates are provided as example or for testing purposes only, generate your own for real-world use!
*Configure the visibilty of variables of the OPC UA server to either 'Marked'
*This application reads the variable named 'INPUT' of 'NewProgram1':
![alt text](https://raw.githubusercontent.com/dschoorisse/PLCnext-OPC-UA-connect-minimal/master/screen_opc_variable.PNG)



 Based on example code from https://github.com/FreeOpcUa/python-opcua/tree/master/examples

