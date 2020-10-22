import json

import gspread
from flask import Flask, request, render_template
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__, template_folder="templates")

@app.route('/get', methods=["GET"])
def get(img=None):
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive',
             'https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    worksheet = client.open("PIZZERIA_CANCIANI").sheet1
    #obtiene la primera fila del archivo
    values_list = worksheet.row_values(1)
    #obtiene todos los valores del archivo en forma de diccionario
    list_of_hashes = worksheet .get_all_records()
    datos = json.dumps(list_of_hashes, indent=4, separators=(',', ': '),ensure_ascii=False)
    print(datos)

    return datos

if __name__ == '__main__':
    app.run(debug=True, port=5002)