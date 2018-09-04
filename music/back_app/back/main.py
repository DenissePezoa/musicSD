from flask import Flask,request,render_template, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

mysql = MySQL()
app = Flask(__name__)
CORS(app)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'sddb'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = 'db'
mysql.init_app(app)


@app.route("/")
def home():
	return 'HELLO WORLD! '

@app.route("/dejavu")
def dejaVu():
	return 'I\'ve just been in this place before...'

#----------------------------------------------#
# LOS SERVICIOS GET DEL SISTEMA                #
#----------------------------------------------#

@app.route("/cancion", methods=['GET'])
def getCancion():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from cancion")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'canciones' : data})

@app.route("/autor", methods=['GET'])
def getAutor():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from autor")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'autores' : data})

@app.route("/genero", methods=['GET'])
def getGenero():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from genero")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'generos' : data})

@app.route("/getIdCancion", methods=['GET'])
def getIdCancion():
    nameCan = request.args.get('nameCan')
    albumCan = request.args.get('albumCan')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT idcancion FROM cancion WHERE nombrecancion = '"+nameCan+"' AND albumcancion = '"+albumCan+"'")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'cancionId' : data})

@app.route("/getIdAutor", methods=['GET'])
def getIdAutor():
    nameAutor = request.args.get('nameAutor')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT idautor FROM autor WHERE nombreautor = '"+nameAutor+"'")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'autorId' : data})

@app.route("/getIdGenero", methods=['GET'])
def getIdGenero():
    nameGenero = request.args.get('nameGenero')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT idgenero FROM genero WHERE nombregenero = '"+nameGenero+"'")
    data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
    return jsonify({'generoId' : data})


#-------------------------------------------------------#
# Busqueda por nombre cancion
@app.route("/busquedaNC", methods=['GET'])
def getBusquedaCancion():
    textoBusqueda = request.args.get('cancion')

    if textoBusqueda is None or textoBusqueda is "":
    	return "No hay filtro de busqueda!"
    textoBusqueda = textoBusqueda.strip()

    cursor = mysql.connection.cursor()

    if textoBusqueda is None or textoBusqueda is "":
    	return "No hay filtro de busqueda!"

    else:
	    cursor.execute("SELECT * FROM cancion WHERE nombrecancion LIKE '%"+textoBusqueda+"%' OR albumcancion LIKE '%"+textoBusqueda+"%'")
	    data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]

	   

	    
	    if data is None :
	    	return "Data not valid"
	    else:
	    	return jsonify({'resultados' : data})


# Busqueda por autor cancion
@app.route("/busquedaAC", methods=['GET'])
def getBusquedaAutor():
    textoBusqueda = request.args.get('autor')

    if textoBusqueda is None or textoBusqueda is "":
    	return "No hay filtro de busqueda!"
    textoBusqueda = textoBusqueda.strip()

    cursor = mysql.connection.cursor()

    if textoBusqueda is None or textoBusqueda is "":
    	return "No hay filtro de busqueda!"

    else:
                cursor.execute("SELECT * FROM cancion WHERE idcancion IN (SELECT cancion_idcancion FROM cancion_autor WHERE autor_idautor IN (SELECT idautor FROM autor WHERE nombreautor LIKE '%"+textoBusqueda+"%'))")
                data = [dict((cursor.description[i][0], value)
                for i, value in enumerate(row)) for row in cursor.fetchall()]
                if data is None :
                        return "Data not valid"
                else:
                        return jsonify({'resultados' : data})

# Busqueda por genero
@app.route("/busquedaGC", methods=['GET'])
def getBusquedaGenero():
    textoBusqueda = request.args.get('genero')

    if textoBusqueda is None or textoBusqueda is "":
    	return "No hay filtro de busqueda!"
    textoBusqueda = textoBusqueda.strip()

    cursor = mysql.connection.cursor()

    if textoBusqueda is None or textoBusqueda is "":
    	return "No hay filtro de busqueda!"

    else:
                        cursor.execute("SELECT * FROM cancion WHERE idcancion in (SELECT cancion_idcancion FROM cancion_genero WHERE genero_idgenero IN (SELECT idgenero FROM genero WHERE nombregenero LIKE '"+textoBusqueda+"'))")
                        data = [dict((cursor.description[i][0], value)
			for i, value in enumerate(row)) for row in cursor.fetchall()]
                        if data is None:
                                return "Data not valid"
                        else:
                                return jsonify({'resultados' : data})

#----------------------------------------------#
# LOS SERVICIOS DE INSERT DEL SISTEMA          #
#----------------------------------------------#

@app.route("/newCancion", methods=['POST'])
def newCancion():
	if request.method == 'POST':
		#idcancion = request.json['cancionid']
		nombrecancion = request.json['cancionnombre']
		albumcancion = request.json['cancionalbum']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idcancion) FROM cancion")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idcancion)')
		print(maxID)

		cursor.execute("INSERT INTO cancion (idcancion,nombrecancion,albumcancion) VALUES (%s,%s,%s)",(maxID+1,nombrecancion,albumcancion))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."

@app.route("/newAutor", methods=['POST'])
def newAutor():
	if request.method == 'POST':
		#idautor = request.json['autorid']
		nombreautor = request.json['autornombre']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idautor) FROM autor")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idautor)')
		print(maxID)


		cursor.execute("INSERT INTO autor (idautor,nombreautor) VALUES (%s,%s)",(maxID+1,nombreautor))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."

@app.route("/newGenero", methods=['POST'])
def newGenero():
	if request.method == 'POST':
		#idgenero = request.json['generoid']
		nombregenero = request.json['generonombre']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idgenero) FROM genero")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idgenero)')
		print(maxID)

		cursor.execute("INSERT INTO genero (idgenero,nombregenero) VALUES (%s,%s)",(maxID+1,nombregenero))
		mysql.connection.commit()
		return "LOCKED AND LOADED"

	else:
		return "But nothing happens..."


#-------------------------------------------------#
# LOS SERVICIOS DE INSERT INTERMEDIOS DEL SISTEMA #
#-------------------------------------------------#

@app.route("/newCancionGenero", methods=['POST'])
def newCanGen():
	if request.method == 'POST':
		#idcancion_genero = request.json['canciongeneroid']
		cancionid = request.json['cancionid']
		generoid = request.json['generoid']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idcancion_genero) FROM cancion_genero")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idcancion_genero)')
		print(maxID)

		cursor.execute("INSERT INTO cancion_genero (idcancion_genero,cancion_idcancion,genero_idgenero) VALUES (%s,%s,%s)",(maxID+1,cancionid,generoid))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."

@app.route("/newCancionAutor", methods=['POST'])
def newCanAut():
	if request.method == 'POST':
		#idcancion_autor = request.json['cancionautorid']
		cancionid = request.json['cancionid']
		autorid = request.json['autorid']
		cursor = mysql.connection.cursor()

		cursor.execute("SELECT MAX(idcancion_autor) FROM cancion_autor")
		data= [dict((cursor.description[i][0], value)
         for i, value in enumerate(row)) for row in cursor.fetchall()]
		maxID = data[0].get('MAX(idcancion_autor)')
		print(maxID)

		cursor.execute("INSERT INTO cancion_autor (idcancion_autor,cancion_idcancion,autor_idautor) VALUES (%s,%s,%s)",(maxID+1,cancionid,autorid))
		mysql.connection.commit()
		return "LOCKED AND LOADED"
	else:
		return "But nothing happens..."


if __name__ == "__main__":
	app.run(host='0.0.0.0')
