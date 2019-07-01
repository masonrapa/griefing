import nmap
import tkinter
import socket
import time
from tkinter import *
def main():
	option = (var.get())
	if option == "PORT SCANNER":
		escaner()
	if option == "SUBDOMAIN SCANNER":
		subd()
	if option == "SET AN OPTION":
		banner = Label(ventana, text="Please, Set any option", bg="black")
		banner.pack(fill=X)

def subd():
	seti = (setinput.get())
	subdomains = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "node 4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "render"]
	for execute in subdomains:
		try:
			iphost = str(execute)+"."+str(seti)
			check = socket.gethostbyname(str(iphost))
			final = "IP >> "+str(iphost)+" Resolved >> "+str(check)		
			banner = Label(ventana, text=str(final), bg="black", fg="white")
			banner.pack(fill=X)
		except:
			pass

def escaner():
	seti = (setinput.get())
	setip = socket.gethostbyname(str(seti))
	scanner = nmap.PortScanner()
	scanner.scan(setip, '1-20,23-79,81-3305,3307-8079,8081-10000,10100-10500,20000-27000,29000-30000,65000-65535', '-v -A -Pn')
	printear = (scanner[setip]['tcp'].keys())
	ip = str(printear)
	ip = ip.replace ('dict_keys([', "")
	ip = ip.replace ("])", "")
	banner = Label(ventana, text=str(ip), bg="black", fg="white")
	banner.pack(fill=X)

ventana = Tk()
Button(ventana, text='SCAN IP', command=main).pack()
space = Label(ventana, text="", bg="black")
space.pack(fill=X)
hour = time.strftime("%H:%M")
banner = Label(ventana, text="ACTUAL TIME >>  	["+str(hour)+"]", bg="black", fg="white")
banner.pack(fill=X)
ventana.configure(background="black")
ventana.geometry("500x700")
ventana.title ("Scanner By zMasonrapa")
var = StringVar(ventana)
var.set("SET AN OPTION")
opciones = ["PORT SCANNER", "-------", "SUBDOMAIN SCANNER"]
opcion = OptionMenu(ventana,var, *opciones)
opcion.pack(padx=30, pady=30)
opcion.config(width=20)
setinput = Entry(ventana)
setinput.pack(fill=X)
select = Label(ventana, textvariable=var, width=999, height=3)
mainloop()
