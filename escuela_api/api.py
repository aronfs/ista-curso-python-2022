from email import message
from hashlib import new
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def leer_archivo():
    archivo = None
    data = {"lista":[]}
    with open(r'C:\Users\arons\OneDrive\Escritorio\EscuelaApi\ista-python-curso-2022\baseDatos\asistencia.csv') as a: 
       archivo = a.readlines()  
    for row1 in archivo:
        partes = row1.split(',')
        data['lista'].append({
            "cedula": partes[0], "materia":partes[1], "fecha_año":partes[2], "fecha_mes":partes[3], "fecha_dia":partes[4]
        })       
    return data




@app.route('/obtenerDatosAsistencia')
def mostrarDatos():
    contenido = leer_archivo()
    return jsonify(contenido)

@app.route('/obtenerDatosBuscar/<string:cedula>')
def getDataFind(cedula):
    contenido = leer_archivo()
    itemFound = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(itemFound)>0:
        return jsonify({
            "message":"Encontrado",
            "Data": itemFound[0]
        })
    return jsonify({
        "message": "Estudiante no Encontrado"
    })

@app.route('/crearAsistencias', methods=['POST'])
def addAsistence():
    new_asistence = {
        "cedula": request.json['cedula'],
        "materia": request.json['materia'],
        "fecha_anio": request.json['fecha_anio'],
        "fecha_mes": request.json['fecha_mes'],
        "fecha_dia": request.json['fecha_dia']
    }
    contenido = leer_archivo()
    contenido["lista"].append(new_asistence)
    return jsonify({
        "message": "Agregado satisfactoriamente",
        "lista": contenido
    })

@app.route('/actualizarAsistencia/<string:cedula>', methods=['PUT'])
def editAsistence(cedula):
    contenido = leer_archivo()  
    itemFound = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(itemFound)>0:
        itemFound[0]['cedula'] = request.json['cedula']
        itemFound[0]['materia'] = request.json['materia']
        itemFound[0]['fecha_anio'] = request.json['fecha_anio']
        itemFound[0]['fecha_mes'] = request.json['fecha_mes']
        itemFound[0]['fecha_dia'] = request.json['fecha_dia']
        return jsonify({
             "message": "Actualizado Correctamente",
             "lista": contenido 
        })

@app.route('/eliminarAsistencia/<string:cedula>', methods=['DELETE'])
def eliminarAsistencia(cedula):
    contenido = leer_archivo()
    itemFound = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(itemFound)>0:
        contenido['lista'].remove(itemFound[0])
        return jsonify({
            "message": "Eliminado Correctamente",
            "Lista": contenido
        })
    return jsonify({
        "message": "Asistencia no encontrado"
    })

#--------------------------------------------Estudiante API CRUD-------------------------------------------------


def leer_estudiantearchivo():
    archivo = None
    data = {"lista":[]}
    with open(r'C:\Users\arons\OneDrive\Escritorio\EscuelaApi\ista-python-curso-2022\baseDatos\estudiante.csv') as a: 
       archivo = a.readlines()  
    for row1 in archivo:
        partes = row1.split(',')
        data['lista'].append({
            "cedula": partes[0], "materia":partes[1], "fecha_año":partes[2], "fecha_mes":partes[3], "fecha_dia":partes[4]
        })       
    return data


@app.route('/obtenerDatosEstudiante')
def mostrarDatosEstudiante():
    contenido = leer_estudiantearchivo()
    return jsonify(contenido)

@app.route('/obtenerDatosBuscarEstudiante/<string:cedula>')
def getDataFindEstudiante(cedula):
    contenido = leer_estudiantearchivo()
    itemFound = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(itemFound)>0:
        return jsonify({
            "message":"Estudiante Encontrado :)",
            "Data": itemFound[0]
        })
    return jsonify({
        "message": "Estudiante no encontrado"
    })

@app.route('/crearEstudiante', methods=['POST'])
def addEstudiante():
    new_asistence = {
        "cedula": request.json['cedula'],
        "primer_apellido": request.json['primer_apellido'],
        "segundo_apellido": request.json['segundo_apellido'],
        "primer_nombre": request.json['primer_nombre'],
        "segundo_nombre": request.json['segundo_nombre']
    }
    contenido = leer_estudiantearchivo()
    contenido["lista"].append(new_asistence)
    return jsonify({
        "message": "Agregado satisfactoriamente",
        "lista": contenido
    })

@app.route('/actualizarEstudiante/<string:cedula>', methods=['PUT'])
def editEstudiante(cedula):
    contenido = leer_estudiantearchivo()  
    itemFound = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(itemFound)>0:
        itemFound[0]['cedula'] = request.json['cedula']
        itemFound[0]['primer_apellido'] = request.json['primer_apellido']
        itemFound[0]['segundo_apellido'] = request.json['segundo_apellido']
        itemFound[0]['primer_nombre'] = request.json['primer_nombre']
        itemFound[0]['segundo_nombre'] = request.json['segundo_nombre']
        return jsonify({
             "message": "Actualizado Correctamente",
             "lista": contenido 
        })

@app.route('/eliminarAsistencia/<string:cedula>', methods=['DELETE'])
def eliminarEstudiante(cedula):
    contenido = leer_estudiantearchivo()
    itemFound = [objeto for objeto in contenido['lista'] if objeto['cedula'] == cedula]
    if len(itemFound)>0:
        contenido['lista'].remove(itemFound[0])
        return jsonify({
            "message": "Eliminado Correctamente",
            "Lista": contenido
        })
    return jsonify({
        "message": "Estudiante no encontrado"
    })

if __name__ == '__main__':
     app.run(debug=True, port=4000)