import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(f"✅ Client connecté : {sid}")

@sio.event
def disconnect(sid):
    print(f"🚪 Client déconnecté : {sid}")

@sio.event
def message(sid, data):
    print(f"💬 Message reçu de {sid}: {data}")
    sio.emit('message', data, skip_sid=sid)

if __name__ == '__main__':
    print("🚀 Socket.IO Server lancé sur 0.0.0.0:5000")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)

