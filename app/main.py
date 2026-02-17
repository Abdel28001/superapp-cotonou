from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI(title="SuperApp Cotonou 🚀")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    html = '''
<!DOCTYPE html>
<html class="dark">
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <title>SuperApp Cotonou</title>
</head>
<body class="bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900 min-h-screen">
    <div class="container mx-auto px-6 py-8">
        <div class="text-center mb-12">
            <h1 class="text-6xl font-black text-white mb-4 animate-pulse">🚀 SuperApp</h1>
            <p class="text-xl text-blue-100">Gozem Rides + Appartements Cotonou</p>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-white/10 backdrop-blur-xl rounded-3xl p-8 text-center hover:scale-105 transition-all">
                <div class="text-4xl mb-4">🚗</div>
                <h2 class="text-2xl font-bold text-white mb-2">Gozem Rides</h2>
                <a href="/client/123456" class="bg-green-500 text-white px-8 py-3 rounded-2xl font-bold hover:bg-green-600 block">Commander</a>
            </div>
            <div class="bg-white/10 backdrop-blur-xl rounded-3xl p-8 text-center hover:scale-105 transition-all">
                <div class="text-4xl mb-4">🏠</div>
                <h2 class="text-2xl font-bold text-white mb-2">Appartements</h2>
                <a href="/api/apartments" class="bg-blue-500 text-white px-8 py-3 rounded-2xl font-bold hover:bg-blue-600 block">Trouver</a>
            </div>
            <div class="bg-white/10 backdrop-blur-xl rounded-3xl p-8 text-center hover:scale-105 transition-all">
                <div class="text-4xl mb-4">👑</div>
                <h2 class="text-2xl font-bold text-white mb-2">Admin</h2>
                <a href="/docs" class="bg-purple-500 text-white px-8 py-3 rounded-2xl font-bold hover:bg-purple-600 block">APIs</a>
            </div>
        </div>
    </div>
</body>
</html>'''
    return HTMLResponse(content=html)

@app.get("/client/{user_id}", response_class=HTMLResponse)
async def client_dashboard(user_id: str):
    html = f'''
<!DOCTYPE html>
<html><head><title>Client {user_id}</title>
<script src="https://cdn.tailwindcss.com"></script></head>
<body class="bg-gray-100 p-8">
    <div class="max-w-4xl mx-auto">
        <h1 class="text-4xl font-bold text-gray-800 mb-8">👤 Client {user_id}</h1>
        <div class="grid md:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-xl shadow-lg">
                <h2 class="text-2xl font-bold mb-4">🚗 Gozem Rides</h2>
                <button class="w-full bg-green-500 text-white py-3 px-6 rounded-xl font-bold hover:bg-green-600">Commander Course</button>
            </div>
            <div class="bg-white p-6 rounded-xl shadow-lg">
                <h2 class="text-2xl font-bold mb-4">🏠 Appartements</h2>
                <button class="w-full bg-blue-500 text-white py-3 px-6 rounded-xl font-bold hover:bg-blue-600">Réserver</button>
            </div>
        </div>
        <a href="/" class="mt-8 inline-block bg-gray-500 text-white py-2 px-6 rounded-xl hover:bg-gray-600">🏠 Accueil</a>
    </div>
</body></html>'''
    return HTMLResponse(content=html)

@app.get("/api/apartments")
async def get_apartments():
    return [{"id": 1, "title": "Appart Bohicon Centre", "price": "150k FCFA", "city": "Cotonou"}]

@app.post("/api/gozem/rides")
async def create_ride():
    return {"success": True, "ride_id": "GOZEM_123456", "price": 2500, "eta": "8min"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
