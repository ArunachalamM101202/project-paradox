from fastapi import FastAPI
from routes import router
from ws_router import socket_app

app = FastAPI()
app.include_router(router)

import uvicorn

if __name__ == "__main__":
    import threading
    def run_ws():
        uvicorn.run(socket_app, host="0.0.0.0", port=8001)

    threading.Thread(target=run_ws).start()
    uvicorn.run(app, host="0.0.0.0", port=8000)


