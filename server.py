import os
import socketio
import eventlet

# Crée un serveur Socket.IO avec autorisation CORS pour tous les clients
sio = socketio.Server(cors_allowed_origins='*')  # CORS * : tous les domaines peuvent se connecter

# Application WSGI à lancer avec eventlet
app = socketio.WSGIApp(sio)

# Fonction appelée à chaque nouvelle connexion d'un client
@sio.event
def connect(sid, environ):
    print(f"✅ Client connecté : {sid}")

# Fonction appelée à chaque déconnexion d'un client
@sio.event
def disconnect(sid):
    print(f"🚪 Client déconnecté : {sid}")

# Fonction appelée à chaque réception de message d'un client
@sio.event
def message(sid, data):
    print(f"💬 Message reçu de {sid}: {data}")

    # Réemission du message à tous les clients sauf l'émetteur
    sio.emit('message', data, skip_sid=sid)

# Point d'entrée du serveur
if __name__ == '__main__':
    # On récupère le port dynamique assigné par Render ou on utilise 5000 en local
    PORT = int(os.environ.get("PORT", 5000))

    print(f"🚀 Socket.IO Server lancé sur 0.0.0.0:{PORT}")

    # Lance le serveur Eventlet WSGI sur le port récupéré
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', PORT)), app)


