import websocket


# For connecting to web sockets
# Must be on python 3.10 to use websocket module


def on_message(ws, message):
    print("Server response:", message)


def on_error(ws, error):
    print("WebSocket error:", error)


def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed.")


def on_open(ws):
    print("Connection established. Sending 'key'.")
    ws.send("key")


url = "ws://ptl-52e1d8dc-f6f179b8.libcurl.so/pentesterlab" # Example of a url just edit to whatever url you desire
ws = websocket.WebSocketApp(
    url, on_message=on_message, on_error=on_error, on_close=on_close
)
ws.on_open = on_open
ws.run_forever()