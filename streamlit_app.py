import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="POD Clone 1:1 Studio",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Tự động lấy API Key từ mục Secrets của Streamlit (nếu bạn đã cài ở bước 4)
secret_api_key = ""
try:
    secret_api_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    secret_api_key = ""

# Ẩn các thanh mặc định của Streamlit để giao diện giống app độc lập 100%
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

html_code = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {{
            background-color: #070810;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 16px;
        }}
        .checkerboard {{
            background-image: 
                linear-gradient(45deg, #161829 25%, transparent 25%), 
                linear-gradient(-45deg, #161829 25%, transparent 25%), 
                linear-gradient(45deg, transparent 75%, #161829 75%), 
                linear-gradient(-45deg, transparent 75%, #161829 75%);
            background-size: 20px 20px;
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        }}
    </style>
</head>
<body>
    <div class="max-w-7xl mx-auto">
        <!-- Thanh nhập API Key nhanh nếu chưa cài trong Secrets -->
        <div class="mb-4 bg-[#0d0f1a] border border-[#1d2038] rounded-xl p-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2 text-xs text-slate-300">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                <span class="font-bold tracking-wider uppercase">POD CLONE 1:1 STUDIO (GEMINI AI)</span>
            </div>
            <div class="flex items-center gap-2 flex-1 max-w-md">
                <input id="apiKeyInput" type="password" value="{secret_api_key}" placeholder="Dán Gemini API Key (AIzaSy...) vào đây..." 
                    class="w-full bg-[#131626] border border-[#252a47] rounded-lg px-3 py-1.5 text-xs text-white focus:outline-none focus:border-[#5340ff]">
                <a href="https://aistudio.google.com/apikey" target="_blank" class="text-[11px] bg-[#1e223a] hover:bg-[#2a2f52] text-indigo-300 px-3 py-1.5 rounded-lg whitespace-nowrap">Lấy Key Free</a>
            </div>
        </div>

        <!-- Bố cục 2 cột chuẩn 1:1 theo hình mẫu -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            
            <!-- CỘT TRÁI: THIẾT LẬP CLONE 1:1 -->
            <div class="bg-[#0c0e1a] border border-[#1c2038] rounded-3xl p-6 flex flex-col justify-between shadow-2xl">
                <div>
                    <div class="flex items-center gap-2.5 mb-5">
                        <span class="w-2.5 h-2.5 rounded-full bg-[#5b4eff]"></span>
                        <h2 class="text-xs font-bold tracking-widest text-slate-300 uppercase">THIẾT LẬP CLONE 1:1</h2>
                    </div>

                    <!-- Bộ chọn Model: GEMINI 3.8 FLASH & GEMINI 3 PRO -->
                    <div class="grid grid-cols-2 gap-3.5 mb-6">
                        <div id="modelFlash" onclick="selectModel('flash')" class="cursor-pointer rounded-2xl p-4 border border-[#232742] bg-[#111322] transition-all">
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-xs font-extrabold text-white">GEMINI 3.8 FLASH</span>
                                <span class="text-[9px] font-bold px-2 py-0.5 rounded bg-[#232742] text-slate-300">FREE TIER</span>
                            </div>
                            <p class="text-[11px] text-slate-400 leading-relaxed">Tốc độ cao, tiết kiệm. Phù hợp phác thảo.</p>
                        </div>

                        <div id="modelPro" onclick="selectModel('pro')" class="cursor-pointer rounded-2xl p-4 border-2 border-[#5b4eff] bg-[#141530] transition-all">
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-xs font-extrabold text-white">GEMINI 3 PRO</span>
                                <span class="text-[9px] font-bold px-2 py-0.5 rounded bg-[#5b4eff] text-white">PREMIUM</span>
                            </div>
                            <p class="text-[11px] text-slate-300 leading-relaxed">Chất lượng tối đa, sắc nét chuẩn in ấn thương mại.</p>
                        </div>
                    </div>

                    <!-- Độ phân giải: 1K / 2K / 4K -->
                    <div class="mb-5">
                        <label class="block text-[10px] font-bold tracking-widest text-slate-400 uppercase mb-2.5">CHẤT LƯỢNG VẼ (RESOLUTION)</label>
                        <div class="grid grid-cols-3 gap-3">
                            <button id="res1K" onclick="selectRes('1K')" class="py-2.5 rounded-xl border border-[#222640] bg-[#111322] text-center transition">
                                <div class="text-xs font-bold text-slate-300">1K</div>
                                <div class="text-[9px] text-slate-500">TIẾT KIỆM</div>
                            </button>
                            <button id="res2K" onclick="selectRes('2K')" class="py-2.5 rounded-xl border border-[#222640] bg-[#111322] text-center transition">
                                <div class="text-xs font-bold text-slate-300">2K</div>
                                <div class="text-[9px] text-slate-500">CÂN BẰNG</div>
                            </button>
                            <button id="res4K" onclick="selectRes('4K')" class="py-2.5 rounded-xl border border-[#5b4eff] bg-[#5b4eff] text-center transition shadow-lg shadow-indigo-600/30">
                                <div class="text-xs font-bold text-white">4K</div>
                                <div class="text-[9px] text-indigo-100">CHUẨN IN</div>
                            </button>
                        </div>
                    </div>

                    <!-- Dán link ảnh hoặc tải file -->
                    <div class="flex gap-2 mb-5">
                        <input id="imgUrlInput" type="text" placeholder="Dán link ảnh (Etsy, Google...) vào đây" 
                            class="flex-1 bg-[#111322] border border-[#222640] rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-[#5b4eff]">
                        <button onclick="loadFromUrl()" class="bg-[#5b4eff] hover:bg-[#4a3de6] text-white text-xs font-bold px-5 py-2.5 rounded-xl transition">TẢI</button>
                        <label class="bg-[#1b1f38] hover:bg-[#252b4d] text-slate-200 text-xs font-bold px-3.5 py-2.5 rounded-xl cursor-pointer flex items-center">
                            📁 Tệp
                            <input id="fileInput" type="file" accept="image/*" class="hidden" onchange="loadFromFile(event)">
                        </label>
                    </div>

                    <!-- Khung hiển thị ảnh áo mẫu -->
                    <div class="border border-dashed border-[#2c3258] rounded-2xl p-3 bg-[#090b14] flex items-center justify-center min-h-[380px] relative overflow-hidden">
                        <img id="sourcePreview" src="
