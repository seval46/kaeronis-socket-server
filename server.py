import os
import socketio
import eventlet

# Création de l'instance Socket.IO Server
sio = socketio.Server(cors_allowed_origins='*')  # Autorise tous les domaines (CORS)

# Création de l'application WSGI
app = socketio.WSGIApp(sio)

# Événement de connexion
@sio.event
def connect(sid, environ):
    print(f"✅ Client connecté : {sid}")

# Événement de déconnexion
@sio.event
def disconnect(sid):
    print(f"🚪 Client déconnecté : {sid}")

# Événement pour transmettre des messages (signalisation WebRTC par exemple)
@sio.event
def message(sid, data):
    print(f"💬 Message reçu de {sid}: {data}")
    # On émet à tous les autres clients sauf celui qui envoie
    sio.emit('message', data, skip_sid=sid)

# Point d'entrée principal
if __name__ == '__main__':
    # Utilisation du port donné par Render, ou 5000 en local
    PORT = int(os.environ.get("PORT", 5000))
    
    print(f"🚀 Socket.IO Server lancé sur 0.0.0.0:{PORT}")
    
    # Lancement du serveur Eventlet sur le port dynamique
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', PORT)), app)

