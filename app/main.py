from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
app = FastAPI(title="GoZem SuperApp Cotonou")

class RideRequest(BaseModel):
    pickup: str
    destination: str
    ride_type: str = 'zem'

@app.get("/", response_class=HTMLResponse)
async def gozem_clone():
    html = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GoZem Bénin - SuperApp Cotonou</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="font-inter bg-gray-50 overflow-x-hidden">

<!-- HEADER EXACT GoZem -->
<header class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-xl border-b border-gray-100 shadow-sm">
    <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
            
            <!-- Logo GoZem GAUCHE -->
            <div class="flex items-center space-x-4">
                <a href="/" class="flex items-center space-x-3 group">
                    <div class="w-12 h-12 bg-gradient-to-br from-orange-500 to-orange-600 rounded-2xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-all">
                        <i class="fas fa-motorcycle text-white text-xl"></i>
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold bg-gradient-to-r from-orange-600 to-orange-400 bg-clip-text text-transparent">gozem</h1>
                        <p class="text-xs text-gray-500 font-medium">SuperApp</p>
                    </div>
                </a>
            </div>

            <!-- Navbar CENTRE -->
            <nav class="hidden md:flex items-center space-x-8">
                <a href="#" class="text-gray-700 hover:text-orange-600 font-medium px-3 py-2 rounded-lg transition-all hover:bg-orange-50">Partenaires</a>
                <a href="#" class="text-gray-700 hover:text-orange-600 font-medium px-3 py-2 rounded-lg transition-all hover:bg-orange-50">Carrières</a>
                <a href="#" class="text-gray-700 hover:text-orange-600 font-medium px-3 py-2 rounded-lg transition-all hover:bg-orange-50">Centre d'aide</a>
            </nav>

            <!-- DROITE: Pays + Langue -->
            <div class="flex items-center space-x-4">
                <!-- Toggle Pays -->
                <div class="relative">
                    <select id="countrySelect" class="text-sm font-medium text-gray-700 bg-white border border-gray-200 rounded-xl px-4 py-2 pr-10 appearance-none focus:outline-none focus:ring-2 focus:ring-orange-500">
                        <option value="bj">🇧🇯 Bénin</option>
                        <option value="tg">🇹🇬 Togo</option>
                        <option value="ml">🇲🇱 Mali</option>
                        <option value="ci">🇨🇮 Côte d'Ivoire</option>
                    </select>
                </div>

                <!-- Toggle Langue -->
                <div class="relative">
                    <button id="langToggle" class="flex items-center space-x-2 text-sm font-medium text-gray-700 bg-white border border-gray-200 rounded-xl px-4 py-2 hover:bg-gray-50 transition-all">
                        <span>FR</span>
                        <i class="fas fa-chevron-down text-xs"></i>
                    </button>
                </div>

                <!-- CTA -->
                <a href="/client/123456" class="bg-gradient-to-r from-orange-500 to-orange-600 text-white font-semibold px-6 py-3 rounded-xl hover:shadow-lg hover:-translate-y-0.5 transition-all shadow-md">
                    Ouvrir l'app
                </a>
            </div>
        </div>
    </div>
</header>

<!-- CARROUSEL Hero (EXACT GoZem) -->
<section class="pt-24 pb-32 relative overflow-hidden">
    <!-- Background Gradient -->
    <div class="absolute inset-0 bg-gradient-to-br from-orange-400/20 via-transparent to-transparent"></div>
    
    <!-- Carrousel Images + Texte Animé -->
    <div class="max-w-7xl mx-auto px-6 relative z-10">
        <div class="grid lg:grid-cols-2 gap-12 items-center h-[70vh] min-h-[600px]">
            
            <!-- Colonne TEXTE ANIMÉ -->
            <div class="animate-fade-in-up">
                <div class="space-y-6 max-w-lg">
                    <h1 class="text-5xl lg:text-7xl font-black leading-tight bg-gradient-to-r from-gray-900 via-gray-800 to-orange-600 bg-clip-text text-transparent">
                        Ta SuperApp
                        <span class="block text-4xl lg:text-6xl text-orange-500 drop-shadow-lg">Cotonou</span>
                    </h1>
                    <p class="text-xl text-gray-700 leading-relaxed max-w-md">
                        Course Zem, Taxi, Tricycle • Courses • Livraisons • Paiements Mobile Money
                    </p>
                    
                    <!-- Cards Services -->
                    <div class="grid grid-cols-3 gap-4 pt-8">
                        <div class="bg-white/70 backdrop-blur-sm p-4 rounded-2xl shadow-lg border border-white/50 hover:scale-105 transition-all">
                            <div class="text-2xl mb-2">🏍️</div>
                            <div class="text-sm font-bold text-gray-800">Zem</div>
                            <div class="text-xs text-gray-600">Dès 1 500 FCFA</div>
                        </div>
                        <div class="bg-white/70 backdrop-blur-sm p-4 rounded-2xl shadow-lg border border-white/50 hover:scale-105 transition-all">
                            <div class="text-2xl mb-2">🛒</div>
                            <div class="text-sm font-bold text-gray-800">Courses</div>
                            <div class="text-xs text-gray-600">30min garanti</div>
                        </div>
                        <div class="bg-white/70 backdrop-blur-sm p-4 rounded-2xl shadow-lg border border-white/50 hover:scale-105 transition-all">
                            <div class="text-2xl mb-2">💳</div>
                            <div class="text-sm font-bold text-gray-800">Paiements</div>
                            <div class="text-xs text-gray-600">Moov Money</div>
                        </div>
                    </div>
                    
                    <div class="pt-8">
                        <a href="#" class="inline-flex items-center bg-gradient-to-r from-orange-500 to-orange-600 text-white font-bold px-8 py-4 rounded-2xl text-lg shadow-2xl hover:shadow-3xl hover:-translate-y-1 transition-all">
                            <i class="fas fa-download mr-3"></i>
                            Télécharger l'app
                        </a>
                    </div>
                </div>
            </div>

            <!-- Colonne CARROUSEL Images -->
            <div class="relative h-full animate-slide-in-right">
                <div id="heroCarousel" class="h-full rounded-3xl shadow-2xl overflow-hidden">
                    <!-- Image 1 -->
                    <div class="carousel-slide absolute inset-0 bg-gradient-to-br from-orange-400 to-yellow-500 flex items-center justify-center">
                        <div class="text-white text-center p-12">
                            <i class="fas fa-motorcycle text-6xl mb-6 animate-bounce"></i>
                            <h3 class="text-3xl font-bold mb-4">Zem Express</h3>
                            <p class="opacity-90">Cotonou → Bohicon en 45min</p>
                        </div>
                    </div>
                    <!-- Image 2 -->
                    <div class="carousel-slide absolute inset-0 bg-gradient-to-br from-green-400 to-emerald-500 flex items-center justify-center opacity-0">
                        <div class="text-white text-center p-12">
                            <i class="fas fa-shopping-bag text-6xl mb-6 animate-pulse"></i>
                            <h3 class="text-3xl font-bold mb-4">Courses Rapides</h3>
                            <p class="opacity-90">Riz, huile, gaz en 30min</p>
                        </div>
                    </div>
                </div>
                
                <!-- Dots Carrousel -->
                <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 flex space-x-2">
                    <div class="carousel-dot w-3 h-3 bg-white/50 rounded-full cursor-pointer hover:bg-white transition-all"></div>
                    <div class="carousel-dot w-3 h-3 bg-orange-400 rounded-full cursor-pointer transition-all"></div>
                    <div class="carousel-dot w-3 h-3 bg-white/50 rounded-full cursor-pointer hover:bg-white transition-all"></div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Barre Commande Fixe Mobile -->
<div class="md:hidden fixed bottom-6 left-4 right-4 z-40">
    <div class="bg-white/95 backdrop-blur-xl rounded-3xl p-6 shadow-2xl border border-white/50">
        <div class="space-y-4">
            <input id="pickup" placeholder="Départ: Route des Pêches" class="w-full p-4 border-2 border-gray-200 rounded-2xl text-lg focus:border-orange-500">
            <input id="destination" placeholder="Destination: Bohicon Centre" class="w-full p-4 border-2 border-gray-200 rounded-2xl text-lg focus:border-orange-500">
            <button onclick="bookRide()" class="w-full bg-gradient-to-r from-orange-500 to-orange-600 text-white py-5 px-6 rounded-2xl text-xl font-bold shadow-xl hover:shadow-2xl transform hover:-translate-y-1 transition-all">
                <i class="fas fa-search mr-2"></i>Commander Zem (1 500 FCFA)
            </button>
        </div>
    </div>
</div>

<script>
let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.carousel-dot');

function nextSlide() {
    slides[currentSlide].classList.remove('opacity-0');
    slides[currentSlide].style.opacity = '0';
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].style.opacity = '1';
    
    dots.forEach((dot, index) => {
        dot.classList.toggle('bg-orange-400', index === currentSlide);
        dot.classList.toggle('bg-white/50', index !== currentSlide);
    });
}

setInterval(nextSlide, 4000);

// Toggle Langue
document.getElementById('langToggle').onclick = () => {
    const btn = document.getElementById('langToggle');
    btn.innerHTML = btn.innerHTML.includes('FR') ? '<span>EN</span><i class="fas fa-chevron-down text-xs"></i>' : '<span>FR</span><i class="fas fa-chevron-down text-xs"></i>';
}

// Commande Ride
function bookRide() {
    const pickup = document.getElementById('pickup').value;
    const destination = document.getElementById('destination').value;
    alert(✅ Course Zem confirmée !\\n → \\nPrix: 1 500 FCFA | ETA: 8min);
}
</script>

<style>
.carousel-slide { transition: opacity 1s ease-in-out; }
.animate-fade-in-up { animation: fadeInUp 1s ease-out; }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
.font-inter { font-family: 'Inter', sans-serif; }
</style>
</body>
</html>'''
    return HTMLResponse(content=html)

@app.post("/api/gozem/rides")
async def create_ride(request: RideRequest):
    return {"success": True, "ride_id": "GOZEM_123456", "price": 1500, "eta": "8min"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
