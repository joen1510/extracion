from selenium.webdriver.common.by import By
from selenium import webdriver
import Basedd as dbase
import Prodsave as ps
import time
db=dbase.dbConnection()
consulta = input("Ingrese el nombre del artículo: ")#Nombre del producto que se va a buscar
driver = webdriver.Chrome()
driver.get("https://ec.ebay.com/")
cuadro_busqueda=driver.find_element(by=By.CSS_SELECTOR, value="#gh-ac")
cuadro_busqueda.send_keys(consulta)
time.sleep(2)#Esperamos un momento ya que depende de la velocidad del internet
boton_busqueda=driver.find_element(by=By.CSS_SELECTOR, value="#gh-btn")
boton_busqueda.click()
fila_p=driver.find_elements(by=By.CSS_SELECTOR, value="#srp-river-results > ul>li")
g=driver.find_elements(by=By.CSS_SELECTOR, value="#cityPoisTable > div > div > table > tbody > tr>td.wind")
time.sleep(2)
#Recorremos todos los productos de la busqueda
for pro in fila_p:
    try:
        precio=pro.find_element(By.CSS_SELECTOR, value="#srp-river-results > ul > li >div > div > div > div > span.s-item__price").text
        estado = pro.find_element(By.CSS_SELECTOR, value="#srp-river-results > ul > li >div > div > div > span.SECONDARY_INFO").text
        nombre=pro.find_element(By.CSS_SELECTOR, value="#srp-river-results > ul > li >div > div > a > div > span").text
        print("Nombre: ",nombre)
        print("Estado: ",estado)
        print("Precio",precio)
        ps.guardar(consulta,nombre,estado,precio)#Llamamos a la función que guarda los datos en MongoDB
        print("************************************")
    except Exception as e:
        print("Falla al extraer",e)
        print("eeeeeeeeeeeerroooooooooooooorrrrrrrrrrrrrrrrrrr")
driver.close()
print("Información almacenada con exito en la Base de Datos")