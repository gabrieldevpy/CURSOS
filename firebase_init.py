import os
import json
import firebase_admin
from firebase_admin import credentials, db

firebase_config = os.getenv("FIREBASE_CONFIG")
if not firebase_config:
    raise Exception("Variável de ambiente FIREBASE_CONFIG não configurada!")
try:
    firebase_config_json = json.loads(firebase_config)
except json.JSONDecodeError as e:
    raise Exception(f"Erro ao decodificar o JSON de FIREBASE_CONFIG: {e}")

cred = credentials.Certificate(firebase_config_json)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bottelegram-6937f-default-rtdb.firebaseio.com'
})
print("Firebase inicializado com sucesso!")
