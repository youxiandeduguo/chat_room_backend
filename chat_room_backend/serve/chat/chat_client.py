import socket
import tkinter
import tkinter.messagebox
import threading
import json
import tkinter.filedialog
from tkinter.scrolledtext import ScrolledText

IP = ''
PORT = ''
user=''

users = [] 
chat = 'Group'






class ChatUser:
	
	def __init__(self,IP,PORT,username):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((IP, int(PORT)))
		self.user=username
		self.s.send(user.encode())
		r = threading.Thread(target=self.receive,daemon=True)
		r.start()

	
	def send(self,message):
		message = message + '~' + self.user + '~' + chat
		self.s.send(message.encode())


	def receive(self):
		global usesr
		while True:
			data = self.s.recv(1024)
			data = data.decode()
			print(data)
			try:
				users = json.loads(data)
				# listbox1.delete(0, tkinter.END)
				# listbox1.insert(tkinter.END, "当前在线用户")
				# listbox1.insert(tkinter.END, "------Group chat-------")
				# for x in range(len(uses)):
				# 	listbox1.insert(tkinter.END, uses[x])
				users.append('------Group chat-------')
			except:
				data = data.split('~')
				message = data[0]
				userName = data[1]
				chatwith = data[2]
				message = '\n' + message
				# if chatwith == '------Group chat-------':   # 群聊
				# 	if userName == user:
				# 		listbox.insert(tkinter.END, message)
				# 	else:
				# 		listbox.insert(tkinter.END, message)
				# elif userName == user or chatwith == user:  # 私聊
				# 	if userName == user:
				# 		listbox.tag_config('tag2', foreground='red')
				# 		listbox.insert(tkinter.END, message, 'tag2')
				# 	else:
				# 		listbox.tag_config('tag3', foreground='green')
				# 		listbox.insert(tkinter.END, message,'tag3')

				# listbox.see(tkinter.END)


