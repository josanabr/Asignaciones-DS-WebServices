#!/usr/bin/env python
#
# El siguiente programa permite obtener algunos valores referentes al estado de un 
# sistema operativo Linux.
#  
# El proposito es que usted haga una especie de "llene los espacios en blanco" 
# para que se vaya familiarizando con la forma como se desarrollan los Web 
# Services.
#  
# Author: 
# Date:
#

# Librerias que se requieren para correr la aplicacion
from flask import Flask, jsonify, make_response
import subprocess

# Se crea un objeto de tipo Flask llamado 'app'
app = Flask(__name__)

#
# Modifique este metodo de modo que cuando el usuario acceda a cualquiera de 
# las rutas aqui definidas le aparezca un mensaje donde se indica los posibles
# servicios que puede consumir
#
@app.route('/')
@app.route('/index.htm')
@app.route('/index.html')
def index():
	#
	# Almacene en una variable llamada 'output' un mensaje que describa 
        # todos los web services definidos en este programa
	#
	return output

#
# Este metodo se usa para determinar que personas estan conectadas usando el 
# comando 'who'. Si usted no sabe como funciona el comando 'who', por favor
# abra una terminal y ejecute 'who'.
#
# Este codigo muestra como en Python se puede acceder al resultado de ejecutar
# el comando 'who' y presentar el resultado en formato 'json'.
#
# Observe, sin embargo, que este comando es mucho mas que solo correr el comando
# 'who', lo que se esta ejecutando realmente es:
#
# 'who | cut -d ' ' -f 1 | uniq'
#
# Ahora, ejecute el comando anterior en una terminal.
#
# La forma como debe consumirse este servicio desde terminal es:
#
# curl http://localhost:5000/who
#
@app.route('/who',methods = ['GET'])
def who():
	who = subprocess.Popen(['who'], stdout = subprocess.PIPE)
	cut = subprocess.Popen(['cut', '-d', ' ', '-f', '1'], stdin = who.stdout, stdout = subprocess.PIPE)
	output = subprocess.check_output(('uniq'), stdin = cut.stdout)
	return jsonify({'users': output})

#
# Este metodo permite determinar si un usuario en particular esta conectado. 
# El comando usado en el shell para esta tarea es:
#
# 'who | cut -d ' ' -f 1 | grep ${USERNAME} | uniq'
#
# Vale la pena recalcar que el nombre del usuario que se desea validar si esta o
# no conectado es 'user', el 'user' que se pasa como argumento al metodo 'who'
#
# La forma como debe consumirse este servicio desde terminal es:
#
# curl http://localhost:5000/who/john
#
@app.route('/who/<string:user>',methods = ['GET'])
def whou(user):
	#
	# Escriba aqui su codigo. El nombre del usuario que desea buscar se
	# encuentra definido en la variable 'user'.
	#
	# Tenga en cuenta que el resultado de la ejecucion del comando debe 
	# quedar en la variable 'output'
	#
	return jsonify({'loggedin': output})

#
# Este metodo es usado para determinar el uso de la CPU. Para ello se utiliza 
# el comando 'vmstat'. Abra una terminal y ejecute dicho comando.
#
# Si quiere saber mas detalles de este comando, desde la terminal, ejecute el
# comando 'man vmstat' o visite https://linux.die.net/man/8/vmstat 
#
# Una vez se ejecuta el comando, este arroja varios valores que segun su 
# posicion representan porcentajes del total del tiempo de la CPU:
#
# 14: tiempo invertido en la ejecucion de codigo que no es del kernel
# 15: tiempo invertido en la ejecucion de codigo del kernel
# 16: tiempo inactivo 
# 17: tiempo invertido en la espera de operaciones de IO
# 18: tiempo que se toma desde una maquina virtual
#
# El comando que se usa aqui para sacar los valores es
#
# vmstat | tail -n +3 | tr -s ' ' | cut -d ' ' -f n
#
# donde n puede ser: 14, 15, 16, 17 o 18
#
# La forma como se invoca este web service puede ser
#
# curl http://localhost:5000/cpu/us (valor 14)
# curl http://localhost:5000/cpu/sy (valor 15)
# curl http://localhost:5000/cpu/id (valor 16)
# curl http://localhost:5000/cpu/wa (valor 17)
# curl http://localhost:5000/cpu/st (valor 18)
#
# Entones, la variable 'param' puede tener el valor 'us', 'sy', 'id', 'wa' o 'st'
#
@app.route('/cpu/<string:param>', methods = ['GET'])
def cpuwa(param):
	#
	# Escriba aqui su codigo. El tipo de valor de la CPU se encuentra 
	# definido en la variable 'param'.
	#
	# Tenga en cuenta que el resultado de la ejecucion del comando debe 
	# quedar en la variable 'output'
	#
	return jsonify({'cpu %s' % param: output})

#
# Otros web services ya implementados
#
# Web service que entrega informacion relativa a esta maquina
#
# Metodo de acceso 
#
# curl http://localhost:5000/os
#
@app.route('/os',methods=['GET'])
def os():
	kernel = subprocess.check_output(['uname','-s'])
	release = subprocess.check_output(['uname','-r'])
	nodename = subprocess.check_output(['uname','-n'])
	kernelv = subprocess.check_output(['uname','-v'])
	machine = subprocess.check_output(['uname','-m'])
	processor = subprocess.check_output(['uname','-p'])
	os = subprocess.check_output(['uname','-o'])
	hardware = subprocess.check_output(['uname','-i'])
	return jsonify({'kernel': kernel, 
			'release': release,
			'node_name': nodename,
			'kernel_version': kernelv,
			'machine': machine,
			'processor': processor,
			'operating_system': os,
			'hardware_platform': hardware})

#
# Funcion que recupera informacion relativa a un parametro especifico del host
#
# Posibles valores
#
# - kernel
# - release
# - nodename
# - kernelversion
# - machine
# - processor
# - operatingsystem
# - hardware
#
# Metodo de acceso
# curl http://localhost:5000/os/kernel
# curl http://localhost:5000/os/release
# curl http://localhost:5000/os/nodename
# curl http://localhost:5000/os/kernelversion
# curl http://localhost:5000/os/machine
# curl http://localhost:5000/os/processor
# curl http://localhost:5000/os/operatingsystem
# curl http://localhost:5000/os/hardware
#
@app.route('/os/<string:param>',methods=['GET'])
def osp(param):
	key = param
	value = ""
	if (param == "kernel"):
		value = subprocess.check_output(['uname','-s']) 
	elif (param == "release"):
		value = subprocess.check_output(['uname','-r']) 
	elif (param == "nodename"):
		value = subprocess.check_output(['uname','-n']) 
	elif (param == "kernelversion"):
		value = subprocess.check_output(['uname','-v']) 
	elif (param == "machine"):
		value = subprocess.check_output(['uname','-m']) 
	elif (param == "processor"):
		value = subprocess.check_output(['uname','-p']) 
	elif (param == "operatingsystem"):
		value = subprocess.check_output(['uname','-o']) 
	elif (param == "hardware"):
		value = subprocess.check_output(['uname','-i']) 
	else:
		return make_response(jsonify({'error': 'Bad parameter. Valid parameters: \'kernel\', \'release\' \'nodename\' \'kernelversion\' \'machine\' \'processor\' \'operatingsystem\' \'hardware\''}), 404)

	return jsonify({key: value})

#
# Metodo usado para determinar el uso de memoria. 
#
# Posibles metodos de acceso
#
# curl http://localhost:5000/mem/swpd
# curl http://localhost:5000/mem/free
# curl http://localhost:5000/mem/buff
# curl http://localhost:5000/mem/cache
#
@app.route('/mem/<string:param>', methods = ['GET'])
def mem(param):
	vmstat = subprocess.Popen(['vmstat'], stdout = subprocess.PIPE)
	tail = subprocess.Popen(['tail','-n','+3'], stdin = vmstat.stdout, stdout = subprocess.PIPE)
	tr = subprocess.Popen(['tr', '-s', ' '], stdin = tail.stdout, stdout = subprocess.PIPE)
	if (param == "swpd"):
		value = "4"
	elif (param == "free"):
		value = "5"
	elif (param == "buff"):
		value = "6"
	elif (param == "cache"):
		value = "7"
	else:
		return make_response(jsonify({'error': 'Possible values swpd, free, buff, cache'}), 404)

	output = subprocess.check_output(['cut', '-d', ' ', '-f', value], stdin = tr.stdout)
	return jsonify({'mem %s' % param: output})


#
# Este es el punto donde arranca la ejecucion del programa
#
if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0')
