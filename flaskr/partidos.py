import json
from flask import Blueprint, flash, request
from flaskr.db import get_db
bp = Blueprint('partidos', __name__, url_prefix='/partidos')
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
def partidos():
    db = get_db()
    error = None
    registros = db.execute('SELECT * FROM partidos').fetchall()
    flash(error)
    json_rows = sqlite3_rows_to_json(registros)
    return json_rows

@bp.route("/add", methods=["POST"])
def crear_partidos():
    print(request.json)
    db = get_db()
    db.execute('INSERT INTO partidos (nombre) VALUES (?)', (request.json['nombre'],))
    db.commit()
    return {'message': 'Partido creado exitosamente.'}

@bp.route("/<id>", methods=["GET"])
def get_partido(id):
    db = get_db()
    candidato = db.execute('SELECT * FROM partidos WHERE id = ?', (id)).fetchone()
    json_row = sqlite3_row_to_json(candidato)
    if not candidato:
        return {'error': 'Partido no encontrado.'}
    return json_row

@bp.route("/<id>", methods=["PUT"])
def update_partido(id):
    db = get_db()
    candidato = db.execute('SELECT * FROM partidos WHERE id = ?', (id)).fetchone()
    if not candidato:
        return {'error': 'Partido no encontrado.'}
    db.execute('UPDATE partidos SET nombre = ? WHERE id = ?', (request.json['nombre'], id))
    db.commit()
    return {'message': 'Partido actualizado exitosamente.'}

@bp.route("/<id>", methods=["DELETE"])
def delete_partido(id):
    db = get_db()
    partido = db.execute('SELECT * FROM partidos WHERE id = ?', (id,)).fetchone()
    if not partido:
        return {'error': 'Partido no encontrado.'}
    db.execute('DELETE FROM partidos WHERE id = ?', (id,))
    db.commit()
    return {'message': 'Partido eliminado exitosamente.'}