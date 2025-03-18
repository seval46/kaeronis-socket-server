

import os
import socketio
import eventlet

# Crée un serveur Socket.IO avec autorisation CORS pour tous les clients
sio = socketio.Server(cors_allowed_origins='*')

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

    # Réemission du message à tous les autres clients sauf celui qui envoie
    sio.emit('message', data, skip_sid=sid)
    print(f"📤 Message réémis à tous les clients sauf {sid}")

# Point d'entrée du serveur
if __name__ == '__main__':
    # Utilise le port dynamique donné par Render ou 5000 en local
    PORT = int(os.environ.get("PORT", 5000))

    print(f"🚀 Socket.IO Server lancé sur 0.0.0.0:{PORT}")
    print(f"🌐 Accède à ton service via Render : https://kaeronis-socket-server.onrender.com")

    # Lance le serveur Eventlet WSGI
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', PORT)), app)

