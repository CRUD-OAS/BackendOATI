import json
from flask import Blueprint, flash, request
from flaskr.db import get_db
from datetime import date
bp = Blueprint('votos', __name__, url_prefix='/votos')
def sqlite3_row_to_json(row):
  json_row = {}
  for column in row.keys():
    if column == 'fecha':
        json_row[column] = str(row[column])
    else:
        json_row[column] = row[column]
  return json_row

def sqlite3_rows_to_json(rows):
  json_rows = []
  for row in rows:
    json_rows.append(sqlite3_row_to_json(row))
  return json.dumps(json_rows,default=str)

@bp.route("/", methods=["GET", "POST"])
def votos():
    db = get_db()
    error = None
    print('Entra')
    registros = db.execute('SELECT * FROM votos').fetchall()
    print('Muere')
    flash(error)
    json_rows = sqlite3_rows_to_json(registros)
    return json_rows

@bp.route("/add", methods=["POST"])
def crear_votos():
    print(request.json)
    db = get_db()
    db.execute('INSERT INTO votos (candidato, partido, fecha) VALUES (?, ?, ?)', (request.json['candidato'], request.json['partido'], date.today()))
    db.commit()
    return {'message': 'Voto registrado exitosamente.'}

@bp.route("/<id>", methods=["DELETE"])
def delete_partido(id):
    db = get_db()
    db.execute('DELETE FROM votos WHERE id = ?', (id,))
    db.commit()
    return {'message': 'Partido eliminado exitosamente.'}
