from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
app = FastAPI(title="SuperApp Cotonou 🚀")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    html = '''
    <!DOCTYPE html>
    <html>
    <head><title>SuperApp Cotonou</title></head>
    <body>
        <h1>🚀 SuperApp Cotonou LIVE !</h1>
        <p>✅ FastAPI + TailwindCSS Dashboard</p>
        <a href="/client/123456">🔐 Login Client</a> | 
        <a href="/docs">📚 API Docs</a>
    </body>
    </html>
    '''
    return HTMLResponse(content=html)

@app.get("/client/{user_id}", response_class=HTMLResponse)
async def client_dashboard(user_id: str):
    html = f'''
    <!DOCTYPE html>
    <html>
    <head><title>Client {user_id}</title></head>
    <body>
        <h1>👤 Client Dashboard</h1>
        <p>ID: {user_id}</p>
        <p>🚗 Gozem Rides | 🏠 Appartements</p>
        <a href="/">🏠 Accueil</a>
    </body>
    </html>
    '''
    return HTMLResponse(content=html)

@app.get("/docs")
async def docs():
    return {"message": "Swagger UI: http://127.0.0.1:3000/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
