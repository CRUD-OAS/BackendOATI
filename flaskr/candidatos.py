import json
from flask import Blueprint, flash, request
from flaskr.db import get_db
bp = Blueprint('candidatos', __name__, url_prefix='/candidatos')
def sqlite3_row_to_json(row):
  json_row = {}
  for column in row.keys():
    json_row[column] = row[column]
  return json_row

def sqlite3_rows_to_json(rows):
  json_rows = []
  for row in rows:
    json_rows.append(sqlite3_row_to_json(row))
  return json.dumps(json_rows)

@bp.route("/", methods=["GET", "POST"])
def candidatos():
    db = get_db()
    error = None
    registros = db.execute('SELECT * FROM candidatos').fetchall()
    flash(error)
    json_rows = sqlite3_rows_to_json(registros)
    return json_rows

@bp.route("/add", methods=["POST"])
def crear_candidato():
    print(request.json)
    db = get_db()
    db.execute('INSERT INTO candidatos (nombre, partido) VALUES (?, ?)', (request.json['nombre'], request.json['partido']))
    db.commit()
    return {'message': 'Candidato creado exitosamente.'}

@bp.route("/<id>", methods=["GET"])
def get_candidato(id):
    db = get_db()
    candidato = db.execute('SELECT * FROM candidatos WHERE id = ?', (id)).fetchone()
    json_row = sqlite3_row_to_json(candidato)
    if not candidato:
        return {'error': 'Candidato no encontrado.'}
    return json_row

@bp.route("/<id>", methods=["PUT"])
def update_candidato(id):
    db = get_db()
    candidato = db.execute('SELECT * FROM candidatos WHERE id = ?', (id)).fetchone()
    if not candidato:
        return {'error': 'Candidato no encontrado.'}
    db.execute('UPDATE candidatos SET nombre = ? WHERE id = ?', (request.json['nombre'], id))
    db.commit()
    return {'message': 'Candidato actualizado exitosamente.'}

@bp.route("/<id>", methods=["DELETE"])
def delete_candidato(id):
    db = get_db()
    candidato = db.execute('SELECT * FROM candidatos WHERE id = ?', (id,)).fetchone()
    if not candidato:
        return {'error': 'Candidato no encontrado.'}
    db.execute('DELETE FROM candidatos WHERE id = ?', (id,))
    db.commit()
    return {'message': 'Candidato eliminado exitosamente.'}