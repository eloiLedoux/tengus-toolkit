import psycopg2

#Etablir la connection:
conn = psycopg2.connect(
   database="bdd", user='postgres', password='psswrd!', host='127.0.0.1', port= '5432'
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