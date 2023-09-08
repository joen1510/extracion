import Basedd as dbase
db=dbase.dbConnection()
def guardar(nom_ar,nom_pro,est_pro,pre_pro):
    try:
        articulo = {
            "Nom_pro": nom_pro.upper(),
            "Est_pro": est_pro.upper(),
            "Pre_pro": pre_pro
        }
        collection = db.get_collection(nom_ar.upper())
        collection.insert_one(articulo)
    except ConnectionError:
        print('Error Al guardar en la BDD')