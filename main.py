import os
import random
import string
import paypalrestsdk
import requests
import time
import re
import sys
import shutil
import logging
from colorama import Fore, init, Back, Style
from flask import Flask, request, redirect, render_template, session, jsonify, url_for
from flask_socketio import SocketIO, emit, join_room
from pathlib import Path


app = Flask(__name__)
init(autoreset=True)
logging.basicConfig(filename='log.txt', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(message)s')

def start2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + ola)
    time.sleep(1)
    print(Back.CYAN + Fore.BLUE + "INFO" + Fore.BLUE + Back.MAGENTA + "SETUP" + Back.BLACK + Fore.RED +
          " > " + Back.BLACK + Fore.BLUE + f"Inicializating Setup...")
    time.sleep(2)
    print(Back.CYAN + Fore.BLUE + "INFO" + Fore.BLUE + Back.MAGENTA + "SETUP" + Back.BLACK + Fore.RED +
          " > " + Back.BLACK + Fore.BLUE + f"Loading Html Modules...")
    time.sleep(1)
    print(Back.CYAN + Fore.BLUE + "INFO" + Fore.BLUE + Back.MAGENTA + "SETUP" + Back.BLACK + Fore.RED +
          " > " + Back.BLACK + Fore.BLUE + f"Loading Python Modules...")
    time.sleep(3)
    print(Back.CYAN + Fore.BLUE + "INFO" + Fore.BLUE + Back.MAGENTA + "SETUP" + Back.BLACK + Fore.RED +
          " > " + Back.BLACK + Fore.BLUE + f"Loaded!")
    time.sleep(1)

ola = """
░██████╗░░█████╗░███╗░░░███╗██╗███╗░░██╗░██████╗░  ░██████╗██╗░░██╗░█████╗░██████╗░
██╔════╝░██╔══██╗████╗░████║██║████╗░██║██╔════╝░  ██╔════╝██║░░██║██╔══██╗██╔══██╗
██║░░██╗░███████║██╔████╔██║██║██╔██╗██║██║░░██╗░  ╚█████╗░███████║██║░░██║██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██║██║╚████║██║░░╚██╗  ░╚═══██╗██╔══██║██║░░██║██╔═══╝░
╚██████╔╝██║░░██║██║░╚═╝░██║██║██║░╚███║╚██████╔╝  ██████╔╝██║░░██║╚█████╔╝██║░░░░░
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░
░█████╗░░█████╗░███╗░░██╗░██████╗░█████╗░██╗░░░░░███████╗  ██╗░░░██╗░░███╗░░░░░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗██║░░░░░██╔════╝  ██║░░░██║░████║░░░░░██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░██║██║░░░░░█████╗░░  ╚██╗░██╔╝██╔██║░░░░░██║░░██║
██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░██║██║░░░░░██╔══╝░░  ░╚████╔╝░╚═╝██║░░░░░██║░░██║
╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚█████╔╝███████╗███████╗  ░░╚██╔╝░░███████╗██╗╚█████╔╝
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚════╝░╚══════╝╚══════╝  ░░░╚═╝░░░╚══════╝╚═╝░╚════╝░"""

start2()
# Imprimir el texto con fondo verde


paypalrestsdk.configure({
  "mode": "live",  # Cambia a "live" para producción
  "client_id": "AaYH-7diHTR49bzlIoy0OAkCaSTql9nhqNPQZJWbEJBEzp2zkG7-hME-YxAIQGx69vRtKg51wf0Uvn-Q",
  "client_secret": "EODZnEdy_JisCT98pXELOKmX5_5UD9ql-edsyMWRHFgwMrTgbiyfn_979e6yTJ5PrsJ-ECG5G9_MV3Kp"
})
app.secret_key = 'your_secret_key'  # Cambia esto por una clave secreta más segura.
socketio = SocketIO(app)  # Inicializa SocketIO
API_KEY = '8cf55d6c698ab7e227e32b4c8d67ea40'
test = "elpepe"
# Crear la carpeta de chats si no existe
if not os.path.exists('chats'):
    os.makedirs('chats')
    
@app.after_request
def after_request(response):
    # Obtener el código de estado de la respuesta
    status_code = response.status_code
    # Obtener el método y la ruta de la solicitud
    method = request.method
    path = request.path
    # Imprimir el log en la consola
    print(Back.CYAN + Fore.BLUE + "+" + Fore.BLUE + Back.MAGENTA + "LOG" + Back.BLACK + Fore.RED +
          " > " + Back.BLACK + Fore.BLUE + f"{method} request {path} :" + Back.GREEN + str(status_code))
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    # Registrar el error en log.txt
    logging.error("Error: %s", str(e))
    # Crear una respuesta de error
    response = jsonify({"message": "An error occurred", "error": str(e)})
    response.status_code = 500
    return response
    
@app.route('/xd')
def random_image(imagen):
    # Ruta de la carpeta donde están las imágenes
    image_folder = 'ruta/a/tu/carpeta/de/imagenes'
    
    # Obtener una lista de todos los archivos en la carpeta
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    
    # Seleccionar una imagen aleatoria
    random_image = random.choice(images)
    
    # Devolver la imagen seleccionada
    return send_file(os.path.join(image_folder, random_image))
    
@app.route('/products')
def products():
    if 'username' not in session:
        return redirect('/login')

    username = session['username']
    seller = session['seller']
    products = []

    # Cargar los productos creados por el usuario
    for product_name in os.listdir('products'):
        product_dir = os.path.join('products', product_name)
        seller_file_path = os.path.join(product_dir, 'seller.txt')
        if os.path.exists(seller_file_path):
            with open(seller_file_path, 'r') as seller_file:
                seller = seller_file.read().strip()
                if seller == username:
                    # Obtener el precio
                    price_file_path = os.path.join(product_dir, 'price.txt')
                    image_file_path = os.path.join(product_dir, 'image.txt')
                    name_file_path = os.path.join(product_dir, 'name.txt')
                    with open(name_file_path, 'r') as name_file:
                        name = name_file.read().strip()
                    with open(price_file_path, 'r') as price_file:
                        price = price_file.read().strip()
                    # Obtener la imagen (asumiendo que la imagen se llama 'imagen.jpg')
                    with open(image_file_path, 'r') as image_file:
                        image_path = image_file.read().strip()
                    products.append({
                        'name2': name,
                        'name': product_name,
                        'price': price,
                        'image': image_path  # Ruta de la imagen
                    })

    return render_template('products.html', username=username, products=products, is_seller=session['seller'])
    
    

    
@app.route('/catalog')
def product():
    
    if 'username' not in session:
        return redirect('/login')

    username = session['username']
    seller = session['seller']
    products = []

    # Cargar los productos creados por el usuario
    for product_name in os.listdir('products'):
        product_dir = os.path.join('products', product_name)

        # Obtener el precio
        price_file_path = os.path.join(product_dir, 'price.txt')
        image_file_path = os.path.join('products', product_name, 'image.txt')
        description_file_path = os.path.join('products', product_name, 'description.txt')
        seller_file_path = os.path.join('products', product_name, 'seller.txt')
        name_file_path = os.path.join('products', product_name, 'name.txt')

        with open(name_file_path, 'r') as name_file:
            name = name_file.read().strip()

        # Leer el precio
        with open(price_file_path, 'r') as price_file:
            price = price_file.read().strip()

        # Leer la imagen
        with open(image_file_path, 'r') as image_file:
            image_path = image_file.read().strip()

        with open(seller_file_path, 'r') as seller_file:
            seller_path = seller_file.read().strip()

        # Leer y procesar la descripción
        with open(description_file_path, 'r') as description_file:
            description = description_file.read().strip()
            # Procesar la descripción para evitar saltos de línea duplicados y espacios innecesarios
            description = re.sub(r'\n+', '\n', description)  # Eliminar saltos de línea duplicados
            description = re.sub(r'^\s*|\s*$', '', description)  # Eliminar espacios al inicio y al final
            description = re.sub(r'\s*\n\s*', '\n', description)  # Eliminar espacios alrededor de los saltos de línea

            # Solo agregar el producto si la descripción no está vacía
            if not description:
                continue  # Saltar este producto si la descripción está vacía

        # Agregar el producto a la lista
        products.append({
            'name2': name,
            'seller': seller_path,
            'name': product_name,
            'price': price,
            'description': description,
            'image': image_path  # Ruta de la imagen
        })
    return render_template('catalog.html', products=products, is_seller=seller, username=username)


@app.route('/buy/<product_name>')
def buy(product_name):
    quantity = int(request.args.get('quantity'))
    product_dir = os.path.join('products', product_name)
    price_file_path = os.path.join(product_dir, 'price.txt')
    seller_file_path = os.path.join(product_dir, 'seller.txt')
    name_file_path = os.path.join(product_dir, 'name.txt')
    mail_file_path = os.path.join(product_dir, 'mail.txt')
    with open(name_file_path, 'r') as name_file:
        name = name_file.read().strip()
    with open(seller_file_path, 'r') as seller_file:
        seller = seller_file.read().strip()
    with open(mail_file_path, 'r') as mail_file:
        mail = mail_file.read().strip()
    with open(price_file_path, 'r') as price_file:
        price = float(price_file.read().strip()) * quantity
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('payment_execute', mail=mail, price=price, product_name=product_name, name=name, quantity=quantity, _external=True),
            "cancel_url": url_for('product', _external=True)
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": product_name,
                    "sku": product_name,
                    "price": price / quantity,
                    "currency": "USD",
                    "quantity": quantity
                }]
            },
            "amount": {
                "total": price,
                "currency": "USD"
            },
            "description": f"Compra de {name} : seller {seller}"
        }]
    })
    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return str(payment.error)

@app.route('/payment/execute')
def payment_execute():
    product_name = request.args.get('product_name')
    price = float(request.args.get('price'))
    quantity = int(request.args.get('quantity', 1))  # Obtener la cantidad con un valor predeterminado de 1
    name = request.args.get('name')
    mail = request.args.get('mail')
    product_dir = os.path.join('products', product_name)
    seller_file_path = os.path.join(product_dir, 'seller.txt')

    with open(seller_file_path, 'r') as seller_file:
        seller = seller_file.read().strip()

    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    # Calcular el precio total en función de la cantidad
    total_price = round(price * quantity, 2)

    if payment.execute({"payer_id": payer_id}):
        print(Back.CYAN + Fore.BLUE + "+" + Fore.BLUE + Back.MAGENTA + "LOG" + Back.BLACK + Fore.RED +
              " > " + Back.BLACK + Fore.BLUE + f"{session['username']} + {seller} Payment Completed. > {product_name} or {name} for {total_price} | Quantity: {quantity}")
        text = f"{seller}: Your payment was successful. Please wait while we prepare everything. Item: {product_name} or {name}. Total Price: {total_price} | Quantity: {quantity}"
        create_chat_file2(session['username'], seller, text)

        # Calcular el monto para el payout (-10%)
        payout_amount = round(total_price * 0.9, 2)

        # Crear el payout
        payout = paypalrestsdk.Payout({
            "sender_batch_header": {
                "sender_batch_id": str(int(time.time())),
                "email_subject": f"Payment successfully: {name} from {session['username']}"
            },
            "items": [{
                "recipient_type": "EMAIL",
                "amount": {
                    "value": f"{payout_amount}",
                    "currency": "USD"
                },
                "receiver": mail,
                "note": f"Payment successfully: {name} from {session['username']} | Quantity: {quantity}",
                "sender_item_id": f"{product_name}"
            }]
        })

        # Ejecutar el payout
        if payout.create():
            print(f"Payout created successfully for {mail}. Amount: {payout_amount}")
            return render_template('success.html')
        else:
            print(payout.error)
    else:
        return str(payment.error)



import re  # Asegúrate de importar re al principio del archivo

@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        product_alias = request.form['product_alias']
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        product_description = request.form['product_description']
        paypal_email = request.form['paypal_email']
        image = request.files['image']

        product_dir = os.path.join('products', product_alias)
        os.makedirs(product_dir, exist_ok=True)

        if image and image.filename:
            image_path = os.path.join(product_dir, image.filename)
            image.save(image_path)
            with open(image_path, 'rb') as img_file:
                response = requests.post(
                    'https://api.imgbb.com/1/upload',
                    params={'key': API_KEY},
                    files={'image': img_file}
                )
            
            if response.status_code == 200:
                image_data = response.json()
                imagexd = image_data['data']['display_url']
            else:
                raise Exception('Error al subir la imagen a ImgBB')

        product_description = re.sub(r'\n+', '\n', product_description.strip())
        product_description = re.sub(r'\s*\n\s*', '\n', product_description)

        with open(os.path.join(product_dir, 'description.txt'), 'w') as desc_file:
            desc_file.write(product_description)

        with open(os.path.join(product_dir, 'price.txt'), 'w') as price_file:
            price_file.write(product_price)

        with open(os.path.join(product_dir, 'name.txt'), 'w') as name_file:
            name_file.write(product_name)

        with open(os.path.join(product_dir, 'seller.txt'), 'w') as seller_file:
            seller_file.write(session['username'])

        with open(os.path.join(product_dir, 'image.txt'), 'w') as image_file:
            image_file.write(imagexd)

        with open(os.path.join(product_dir, 'mail.txt'), 'w') as mail_file:
            mail_file.write(paypal_email)

        return redirect('/products')

    return render_template('sell.html', is_seller=session['seller'], username=session.get('username'))




@app.route('/delete/<product_name>', methods=['POST'])
def delete_product(product_name):
    if 'username' not in session:
        return redirect('/login')

    product_dir = os.path.join('products', product_name)

    if os.path.exists(product_dir):
        # Eliminar el directorio del producto
        shutil.rmtree(product_dir)
        return redirect('/products')

    return "Producto no encontrado", 404
    
@app.route('/<product_name>')
def product_detail(product_name):
    if 'username' not in session:
        return redirect('/login')

    product_dir = os.path.join('products', product_name)

    if not os.path.exists(product_dir):
        return "Producto no encontrado", 404

    # Cargar detalles del producto
    with open(os.path.join(product_dir, 'description.txt'), 'r') as desc_file:
        description = desc_file.read()

    with open(os.path.join(product_dir, 'name.txt'), 'r') as name_file:
        name = name_file.read()
    with open(os.path.join(product_dir, 'price.txt'), 'r') as price_file:
        price = price_file.read()

    # Obtener la imagen (asumiendo que la imagen se llama 'imagen.jpg')
    image_file_path = os.path.join(product_dir, 'image.txt')
    with open(image_file_path, 'r') as image_file:
                        image_path = image_file.read().strip()

    return render_template('product_detail.html', name2=name, name=product_name, price=price, description=description, image=image_path)


def read_users():
    users = {}
    if not os.path.exists('database.txt'):
        return users
    with open('database.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Verificar que la línea no esté vacía
                parts = line.split(':')

                username, password, seller = parts
                users[username] = password

               
    return users

def get_seller_by_username(username):
    if not os.path.exists('database.txt'):
        return None

    with open('database.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Verificar que la línea no esté vacía
                parts = line.split(':')
                if parts[0] == username:
                    return parts[2]  # Retornar el valor del seller

    return None  # Retornar None si no se encuentra el username

# Función para agregar un usuario al archivo
def add_user(username, password):
    users = read_users()  # Leer los usuarios existentes
    if username not in users:  # Solo agregar si no existe
        with open('database.txt', 'a') as f:
            f.write(f"\n{username}:{password},false")
    else:
        print(f"El usuario {username} ya existe.")  # Para depuración

# Función para generar un ID aleatorio para los chats
def generate_random_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Función para crear un archivo de chat
def create_chat_file(username1, username2):
        # Generar un ID aleatorio para el chat
        chat_id = generate_random_id()

        # Asegurarse de que username1 siempre sea menor alfabéticamente que username2
        if username1 > username2:
            username1, username2 = username2, username1  # Intercambiar para mantener un orden consistente

        # Crear el nombre del archivo de chat
        chat_filename = f"chats/{username1}-{username2}-{chat_id}.txt"

        # Crear el archivo vacío para el chat
        with open(chat_filename, 'w') as f:
            f.write("")  # Crear el archivo vacío

        return chat_filename
def create_chat_file2(username1, username2, text):
        # Generar un ID aleatorio para el chat
        chat_id = generate_random_id()

        # Asegurarse de que username1 siempre sea menor alfabéticamente que username2
        if username1 > username2:
            username1, username2 = username2, username1  # Intercambiar para mantener un orden consistente

        # Crear el nombre del archivo de chat
        chat_filename = f"chats/{username1}-{username2}-{chat_id}.txt"

        # Crear el archivo vacío para el chat
        with open(chat_filename, 'w') as f:
            f.write(text)  # Crear el archivo vacío

        return chat_filename
@app.route('/')
def index():
    return render_template(
        'index.html', 
        username=session.get('username'), 
        is_seller=session.get('seller', "false")
    )


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        if username in users:
            return "Usuario ya existe", 400  # Devuelve un código de estado 400
        add_user(username, password)
        trueor = get_seller_by_username(username)
        session['username'] = username
        session['password'] = password
        session['seller'] = trueor
        return redirect('/')
        print(Back.CYAN + Fore.BLUE + "+" + Fore.BLUE + Back.MAGENTA + "LOG" + Back.BLACK + Fore.RED +
              " > " + Back.BLACK + Fore.BLUE + f"Register succesfull :" + Back.GREEN + f" {username}:{password}")
    return render_template('register.html', username=session.get('username'), is_seller=session['seller'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'seller' not in session or not session['seller']:
        session['seller'] = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_users()
        if username in users and users[username] == password:
            trueor = get_seller_by_username(username)
            session['username'] = username
            session['password'] = password
            session['seller'] = trueor
            return redirect('/account')
            print(Back.CYAN + Fore.BLUE + "+" + Fore.BLUE + Back.MAGENTA + "LOG" + Back.BLACK + Fore.RED +
                  " > " + Back.BLACK + Fore.BLUE + f"Login succesfull :" + Back.GREEN + f" {username}:{password}")
        return "Usuario o contraseña incorrectos", 401  # Devuelve un código de estado 401
        
    # Solo pasa is_seller si session['seller'] existe
    return render_template('login.html', username=session.get('username'), is_seller=session.get('seller'))

@app.route('/account')
def account():
    if 'username' in session:
        return render_template('account.html', username=session['username'], is_seller=session.get('seller'))
    return redirect('/register')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session['seller'] = "false"
    time.sleep(2)
    return redirect('/')

@app.route('/chat')
def chat():
    if 'username' not in session:
        return redirect('/login')

    # Lista de chats que incluye los de ambos usuarios
    chats = [f for f in os.listdir('chats') if session['username'] in f]
    return render_template('chat.html', username=session['username'], chats=chats, is_seller=session['seller'])

@app.route('/create_chat', methods=['POST'])
def create_chat():
    if 'username' not in session:
        return redirect('/login')

    other_user = request.form['other_user']
    if other_user:  # Verifica que se ingresó un nombre de usuario
        create_chat_file(session['username'], other_user)
        print(Back.CYAN + Fore.BLUE + "+" + Fore.BLUE + Back.MAGENTA + "LOG" + Back.BLACK + Fore.RED +
              " > " + Back.BLACK + Fore.BLUE + f"New chat succesfully created:" + Back.GREEN + f"{session['username']} and {other_user}")
    return redirect('/chat')

@socketio.on('new_message')
def handle_new_message(data):
    # Aquí puedes manejar lo que quieras hacer con el nuevo mensaje
    # Por ejemplo, emitírselo a todos los usuarios conectados
    emit('new_message', data, broadcast=True)


@app.route('/chat/<chat_id>', methods=['GET', 'POST'])
def chat_with_user(chat_id):
    if 'username' not in session:
        return redirect('/login')

    chat_file_path = None
    for filename in os.listdir('chats'):
        if chat_id in filename:
            chat_file_path = os.path.join('chats', filename)
            break

    if chat_file_path is None:
        return "Chat no encontrado", 404

    messages = []
    if os.path.exists(chat_file_path):
        with open(chat_file_path, 'r') as f:
            messages = f.readlines()

    if request.method == 'POST':
        message = request.form['message']
        if message:
            with open(chat_file_path, 'a') as f:
                f.write(f"\n{session['username']}: {message}")
            socketio.emit('new_message', {'message': f"{session['username']}: {message}"}, room=chat_id)
            return redirect(f'/chat/{chat_id}')

    chat_usernames = chat_file_path.split('/')[-1].split('-')[:-1]
    other_user = [user for user in chat_usernames if user != session['username']][0]
    chatxd = chat_file_path.replace('chats', "").replace(chat_file_path.split('-')[2], "")

    return render_template('chat_detail.html', username=session['username'], other_username=chatxd, messages=messages, chat_id=chat_id, is_seller=session['seller'])

@socketio.on('join')
def on_join(data):
    chat_id = data['chat_id']
    join_room(chat_id)



if __name__ == '__main__':
        socketio.run(app, debug=False, port=3000, host='0.0.0.0')