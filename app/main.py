from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
import secrets

app = FastAPI(title="🚀 SuperApp Cotonou - Dashboard PRO")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === JWT + RÔLES ===
SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str

class User(BaseModel):
    username: str
    role: str

# FAKE USERS (remplace par DB après)
USERS_DB = {
    "client": {"password": "123456", "role": "client"},
    "driver": {"password": "driver123", "role": "driver"},
    "admin": {"password": "admin123", "role": "admin"},
    "superadmin": {"password": "super123", "role": "superadmin"}
}

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        role: str = payload.get("role")
        if username is None or role is None:
            raise credentials_exception
        return User(username=username, role=role)
    except JWTError:
        raise credentials_exception

def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):
        role_order = ["client", "driver", "admin", "superadmin"]
        if role_order.index(current_user.role) < role_order.index(required_role):
            raise HTTPException(403, f"Role {required_role} required")
        return current_user
    return role_checker

# === ROUTES AUTH ===
@app.post("/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = USERS_DB.get(form_data.username)
    if not user_dict or user_dict["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    access_token = create_access_token(
        data={"sub": form_data.username, "role": user_dict["role"]}
    )
    return {"access_token": access_token, "token_type": "bearer", "role": user_dict["role"]}

# === DASHBOARD PAGES ===
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return """
    <!DOCTYPE html>
    <html class="h-full">
    <head>
        <title>🚀 SuperApp Cotonou - Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <script>
            tailwind.config = { theme: { extend: { animation: { 'pulse-fast': 'pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite' } } } }
        </script>
        <style>
            .gradient-1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .gradient-2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
            .gradient-3 { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        </style>
    </head>
    <body class="bg-gradient-to-br from-slate-50 to-blue-50 min-h-screen">
    
    <!-- Loading -->
    <div id="loading" class="fixed inset-0 bg-white flex items-center justify-center z-50">
        <div class="text-center">
            <div class="w-16 h-16 border-4 border-blue-200 border-t-blue-500 rounded-full animate-spin mx-auto mb-4"></div>
            <p class="text-lg font-semibold text-gray-600">Connexion...</p>
        </div>
    </div>
    
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md shadow-sm border-b border-gray-100 sticky top-0 z-40">
        <div class="max-w-7xl mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 gradient-1 rounded-2xl flex items-center justify-center shadow-lg">
                        <i class="fas fa-rocket text-white text-xl"></i>
                    </div>
                    <div>
                        <h1 class="text-2xl font-black bg-gradient-to-r from-gray-900 to-gray-700 bg-clip-text text-transparent">SuperApp Cotonou</h1>
                        <p class="text-sm text-gray-500" id="user-role">-</p>
                    </div>
                </div>
                <div class="flex items-center space-x-4">
                    <span id="user-name" class="font-semibold text-gray-700">-</span>
                    <button onclick="logout()" class="px-4 py-2 bg-red-500 text-white rounded-xl hover:bg-red-600 transition-all font-medium shadow-md">
                        <i class="fas fa-sign-out-alt mr-2"></i>Déconnexion
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-6 py-12">
        <!-- Stats Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
            <div class="gradient-1 text-white p-8 rounded-3xl shadow-2xl hover:shadow-3xl transition-all group cursor-pointer" onclick="goToGozem()">
                <div class="flex items-center justify-between">
                    <div class="p-3 bg-white/20 rounded-2xl">
                        <i class="fas fa-motorcycle text-2xl"></i>
                    </div>
                    <div class="text-right">
                        <p class="text-blue-100 font-medium" id="rides-count">0</p>
                        <p class="text-3xl font-black" id="rides-today">0</p>
                    </div>
                </div>
                <p class="mt-4 font-semibold opacity-90">Courses Gozem</p>
            </div>
            
            <div class="gradient-2 text-white p-8 rounded-3xl shadow-2xl hover:shadow-3xl transition-all group cursor-pointer" onclick="goToHousing()">
                <div class="flex items-center justify-between">
                    <div class="p-3 bg-white/20 rounded-2xl">
                        <i class="fas fa-home text-2xl"></i>
                    </div>
                    <div class="text-right">
                        <p class="text-blue-100 font-medium" id="housing-count">0</p>
                        <p class="text-3xl font-black" id="housing-active">0</p>
                    </div>
                </div>
                <p class="mt-4 font-semibold opacity-90">Appartements</p>
            </div>
            
            <div class="gradient-3 text-white p-8 rounded-3xl shadow-2xl hover:shadow-3xl
