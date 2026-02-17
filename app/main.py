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
    <title>APPZem Bénin - SuperApp Cotonou</title>
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
            
            <!-- Logo APPZem GAUCHE -->
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
@app.get("/partenaires", response_class=HTMLResponse)
async def partenaires_page():
    html = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Partenaires - SuperApp Cotonou</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-gray-50 font-sans">

<!-- HEADER IDENTIQUE -->
<header class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur-xl border-b border-gray-100 shadow-sm">
    <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
            <a href="/" class="flex items-center space-x-3">
                <div class="w-12 h-12 bg-gradient-to-br from-orange-500 to-orange-600 rounded-2xl flex items-center justify-center shadow-lg">
                    <i class="fas fa-motorcycle text-white text-xl"></i>
                </div>
                <div>
                    <h1 class="text-2xl font-bold bg-gradient-to-r from-orange-600 to-orange-400 bg-clip-text text-transparent">gozem</h1>
                    <p class="text-xs text-gray-500 font-medium">SuperApp</p>
                </div>
            </a>
            <nav class="hidden md:flex items-center space-x-8">
                <a href="/" class="text-gray-700 hover:text-orange-600 font-medium px-3 py-2 rounded-lg transition-all hover:bg-orange-50">Accueil</a>
                <a href="/partenaires" class="text-orange-600 font-bold px-3 py-2 rounded-lg bg-orange-50 border-b-2 border-orange-500">Partenaires</a>
                <a href="#" class="text-gray-700 hover:text-orange-600 font-medium px-3 py-2 rounded-lg transition-all hover:bg-orange-50">Carrières</a>
                <a href="#" class="text-gray-700 hover:text-orange-600 font-medium px-3 py-2 rounded-lg transition-all hover:bg-orange-50">Centre d'aide</a>
            </nav>
            <div class="flex items-center space-x-4">
                <select class="text-sm font-medium text-gray-700 bg-white border border-gray-200 rounded-xl px-4 py-2 pr-10">
                    <option>🇧🇯 Bénin</option>
                </select>
                <button class="flex items-center space-x-2 text-sm font-medium text-gray-700 bg-white border border-gray-200 rounded-xl px-4 py-2">FR ▼</button>
                <a href="/client/123456" class="bg-gradient-to-r from-orange-500 to-orange-600 text-white font-semibold px-6 py-3 rounded-xl hover:shadow-lg">Ouvrir l'app</a>
            </div>
        </div>
    </div>
</header>

<!-- Hero Partenaires -->
<section class="pt-32 pb-20 bg-gradient-to-br from-orange-500/10 to-orange-100">
    <div class="max-w-7xl mx-auto px-6 text-center">
        <h1 class="text-5xl lg:text-6xl font-black bg-gradient-to-r from-gray-900 to-orange-600 bg-clip-text text-transparent mb-6">
            Devenir Partenaire
        </h1>
        <p class="text-xl text-gray-700 max-w-3xl mx-auto leading-relaxed">
            Intégrez la plus grande plateforme de mobilité et livraison du Bénin. 
            <strong class="text-orange-600 font-bold">+500 entreprises</strong> nous font déjà confiance.
        </p>
    </div>
</section>

<!-- Stats -->
<section class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-6">
        <div class="grid md:grid-cols-4 gap-8 text-center">
            <div>
                <div class="text-4xl font-black text-orange-600 mb-2">500+</div>
                <div class="text-gray-600 font-semibold">Partenaires actifs</div>
            </div>
            <div>
                <div class="text-4xl font-black text-orange-600 mb-2">50k+</div>
                <div class="text-gray-600 font-semibold">Livraisons/mois</div>
            </div>
            <div>
                <div class="text-4xl font-black text-orange-600 mb-2">98%</div>
                <div class="text-gray-600 font-semibold">Satisfaction</div>
            </div>
            <div>
                <div class="text-4xl font-black text-orange-600 mb-2">24h</div>
                <div class="text-gray-600 font-semibold">Délai moyen</div>
            </div>
        </div>
    </div>
</section>

<!-- Formulaire Inscription Partenaire (EXACT Gozem Partners) -->
<section class="py-32 bg-gray-50">
    <div class="max-w-4xl mx-auto px-6">
        <div class="bg-white rounded-3xl shadow-2xl border border-gray-100 overflow-hidden">
            <div class="grid lg:grid-cols-2 gap-0">
                <!-- Left: Benefits -->
                <div class="bg-gradient-to-br from-orange-500 to-orange-600 p-12 text-white">
                    <h2 class="text-3xl font-bold mb-8">Pourquoi nous rejoindre ?</h2>
                    <div class="space-y-6">
                        <div class="flex items-start space-x-4">
                            <div class="w-8 h-8 bg-white/20 rounded-xl flex items-center justify-center mt-1">
                                <i class="fas fa-truck text-xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-xl mb-2">Livraisons ultra-rapides</h3>
                                <p class="opacity-90">30min en moyenne à Cotonou</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-4">
                            <div class="w-8 h-8 bg-white/20 rounded-xl flex items-center justify-center mt-1">
                                <i class="fas fa-chart-line text-xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-xl mb-2">Tarifs compétitifs</h3>
                                <p class="opacity-90">Jusqu'à -40% vs logistique traditionnelle</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-4">
                            <div class="w-8 h-8 bg-white/20 rounded-xl flex items-center justify-center mt-1">
                                <i class="fas fa-mobile-alt text-xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-xl mb-2">Tableau de bord</h3>
                                <p class="opacity-90">Suivi en temps réel 24/7</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-4">
                            <div class="w-8 h-8 bg-white/20 rounded-xl flex items-center justify-center mt-1">
                                <i class="fas fa-users text-xl"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-xl mb-2">Support dédié</h3>
                                <p class="opacity-90">Account Manager + hotline 24/7</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Right: Formulaire -->
                <div class="p-12">
                    <h3 class="text-2xl font-bold text-gray-900 mb-8">Devenez partenaire dès aujourd'hui</h3>
                    <form id="partnerForm" class="space-y-6">
                        <div>
                            <label class="block text-sm font-semibold text-gray-700 mb-2">Nom de l'entreprise *</label>
                            <input type="text" required class="w-full p-4 border-2 border-gray-200 rounded-2xl focus:border-orange-500 focus:outline-none focus:ring-2 focus:ring-orange-100 text-lg" placeholder="Ex: Restaurant Le Nokoué">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-gray-700 mb-2">Email professionnel *</label>
                            <input type="email" required class="w-full p-4 border-2 border-gray-200 rounded-2xl focus:border-orange-500 focus:outline-none focus:ring-2 focus:ring-orange-100 text-lg" placeholder="contact@monentreprise.com">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-gray-700 mb-2">Téléphone *</label>
                            <input type="tel" required class="w-full p-4 border-2 border-gray-200 rounded-2xl focus:border-orange-500 focus:outline-none focus:ring-2 focus:ring-orange-100 text-lg" placeholder="+229 62 37 49 49">
                        </div>
                        <div>
                            <label class="block text-sm font-semibold text-gray-700 mb-2">Type d'activité</label>
                            <select class="w-full p-4 border-2 border-gray-200 rounded-2xl focus:border-orange-500 text-lg">
                                <option>Restaurant</option>
                                <option>Supermarché</option>
                                <option>Pharmacie</option>
                                <option>Commerce général</option>
                                <option>Autre</option>
                            </select>
                        </div>
                        <button type="submit" class="w-full bg-gradient-to-r from-orange-500 to-orange-600 text-white font-bold py-5 px-6 rounded-2xl text-xl shadow-xl hover:shadow-2xl hover:-translate-y-1 transition-all">
                            <i class="fas fa-paper-plane mr-2"></i>Envoyer ma demande
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Témoignages -->
<section class="py-32 bg-white">
    <div class="max-w-4xl mx-auto px-6">
        <h2 class="text-4xl font-black text-center text-gray-900 mb-20">Ils nous font confiance</h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-gray-50 p-8 rounded-3xl border border-gray-100 hover:shadow-xl transition-all">
                <div class="flex items-center mb-6">
                    <img src="https://via.placeholder.com/60x60/FF6B35/FFFFFF?text=RB" class="w-16 h-16 rounded-2xl mr-4">
                    <div>
                        <h4 class="font-bold text-xl text-gray-900">Restaurant Bohicon</h4>
                        <div class="flex items-center text-orange-600">
                            <i class="fas fa-star mr-1"></i>
                            <i class="fas fa-star mr-1"></i>
                            <i class="fas fa-star mr-1"></i>
                            <i class="fas fa-star mr-1"></i>
                            <i class="fas fa-star mr-1"></i>
                        </div>
                    </div>
                </div>
                <p class="text-gray-700 italic">"Livraisons en 25min pile ! Nos clients adorent."</p>
            </div>
            <div class="bg-gray-50 p-8 rounded-3xl border border-gray-100 hover:shadow-xl transition-all">
                <div class="flex items-center mb-6">
                    <img src="https://via.placeholder.com/60x60/4F46E5/FFFFFF?text=PH" class="w-16 h-16 rounded-2xl mr-4">
                    <div>
                        <h4 class="font-bold text-xl text-gray-900">Pharmacie du Centre</h4>
                        <div class="flex items-center text-orange-600">
                            <i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i>
                        </div>
                    </div>
                </div>
                <p class="text-gray-700 italic">"Service fiable 24/7, même le dimanche."</p>
            </div>
            <div class="bg-gray-50 p-8 rounded-3xl border border-gray-100 hover:shadow-xl transition-all">
                <div class="flex items-center mb-6">
                    <img src="https://via.placeholder.com/60x60/10B981/FFFFFF?text=SM" class="w-16 h-16 rounded-2xl mr-4">
                    <div>
                        <h4 class="font-bold text-xl text-gray-900">SuperMarché Nokoué</h4>
                        <div class="flex items-center text-orange-600">
                            <i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i><i class="fas fa-star mr-1"></i>
                        </div>
                    </div>
                </div>
                <p class="text-gray-700 italic">"Économies de 35% sur nos livraisons."</p>
            </div>
        </div>
    </div>
</section>

<script>
document.getElementById('partnerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    // Animation succès
    const btn = this.querySelector('button');
    btn.innerHTML = '<i class="fas fa-check mr-2"></i>Demandé envoyée !';
    btn.classList.add('bg-green-500');
    setTimeout(() => {
        alert('✅ Votre demande a été envoyée !\\nNous vous contactons sous 24h.');
    }, 1000);
});
</script>

</body>
</html>'''
    return HTMLResponse(content=html)

@app.post("/api/gozem/rides")
async def create_ride(request: RideRequest):
    return {"success": True, "ride_id": "GOZEM_123456", "price": 1500, "eta": "8min"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
