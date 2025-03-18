import socketio

# Crée un client Socket.IO
sio = socketio.Client()

@sio.event
def connect():
    print('✅ Connecté au serveur')

@sio.event
def disconnect():
    print('🚪 Déconnecté du serveur')

@sio.on('message')
def on_message(data):
    print(f'💬 Nouveau message reçu : {data}')

# Connecte le client au serveur Render
sio.connect('https://kaeronis-socket-server.onrender.com', transports=['websocket'])

# Envoie un message de test
sio.emit('message', {'user': 'Sébastien', 'text': 'Hello depuis mon client test !'})

# Boucle d'attente pour garder la connexion ouverte
sio.wait()

