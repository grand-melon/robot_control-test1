import sys
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket manager for broadcasting logs
class LogWebSocketManager:
    def __init__(self):
        self.active_connections: set[WebSocket] = set()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.discard(websocket)

    async def broadcast(self, message: str):
        to_remove = set()
        for ws in self.active_connections:
            try:
                await ws.send_text(message)
            except Exception:
                to_remove.add(ws)
        for ws in to_remove:
            self.disconnect(ws)

log_ws_manager = LogWebSocketManager()

# Custom stdout to broadcast logs
class BroadcastStdout:
    def __init__(self, real_stdout, ws_manager):
        self.real_stdout = real_stdout
        self.ws_manager = ws_manager
        self.loop = asyncio.get_event_loop()

    def write(self, data):
        if data.strip() != "":
            # Schedule broadcast in event loop
            self.loop.call_soon_threadsafe(
                asyncio.create_task, self.ws_manager.broadcast(data.rstrip())
            )
        self.real_stdout.write(data)
        self.real_stdout.flush()

    def flush(self):
        self.real_stdout.flush()

# Replace sys.stdout with our broadcaster
sys.stdout = BroadcastStdout(sys.stdout, log_ws_manager)

@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await log_ws_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive, ignore input
    except WebSocketDisconnect:
        log_ws_manager.disconnect(websocket)

@app.post("/button/{num}")
async def button_click(num: int):
    if num not in [1, 2, 3]:
        return JSONResponse(status_code=400, content={"error": "Invalid button"})
    print(f"[버튼 {num} 클릭됨]\n")
    return {"result": f"Button {num} clicked"}

# Example: print a startup message
print("[서버 시작됨] FastAPI log streaming backend ready.")
