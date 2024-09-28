import json

import psycopg2

with open('config.json', 'r') as cfg:
  data = json.load(cfg)

BDD      = data["BDD_PGSQL"]
USER     = data["USER_PGSQL"]
PASSWORD = data["PSW_PGSQL"]
HOST     = data["HOST_PGSQL"]

#Etablir la connection:
conn = psycopg2.connect(
   database=BDD, user=USER, password=PASSWORD, host=HOST, port= PORT
)

#Creation du curseur pour requeter:
cursor = conn.cursor()

#Requete SQL:
request = """ SELECT * FROM "Table"  WHERE colonne = 'info'"""
cursor.execute(request)

#Requetage (fetchall/fetchone/fetchmany(n))
data = cursor.fetchall()
print("Données récupérées :",data)

#Closing the connection
conn.close()