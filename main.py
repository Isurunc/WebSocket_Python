import websocket
import json

#Got from deriv https://app.deriv.com/account/api-token
app_id = "LvopMSIoTVH6DfZ"

# Set the WebSocket URL with the APP_ID
ws_url = f"wss://ws.derivws.com/websockets/v3?app_id={app_id}"
#ws_url = "wss://ws.derivws.com/websockets/v3?app_id=" + app_id

# Define the states_list request body
request_body = {
    "states_list": "au"
}

# Create a WebSocket connection
ws = websocket.WebSocketApp(ws_url)

def on_open(ws):
    print("WebSocket connection opened")
    ws.send(json.dumps(request_body))

def on_message(ws, message):
    print(f"Received message: \"{message}\"")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_reason):
    print(f"WebSocket connection closed: {close_status_code} - {close_reason}")

# Register event callbacks
ws.on_open = on_open
ws.on_message = on_message
ws.on_error = on_error
ws.on_close = on_close

# Start the WebSocket connection
ws.run_forever()
