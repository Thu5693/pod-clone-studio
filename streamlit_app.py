import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="POD Clone 1:1 Studio",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

secret_api_key = ""
try:
    secret_api_key = st.secrets.get("GEMINI_API_KEY", "")
except Exception:
    secret_api_key = ""

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

html_code = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #070810;
            color: #ffffff;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 16px;
        }
        .checkerboard {
            background-image: 
                linear-gradient(45deg, #161829 25%, transparent 25%), 
                linear-gradient(-45deg, #161829 25%, transparent 25%), 
                linear-gradient(45deg, transparent 75%, #161829 75%), 
                linear-gradient(-45deg, transparent 75%, #161829 75%);
            background-size: 20px 20px;
            background-position: 0 0, 0 10px, 10px -10px, -10px 0px;
        }
    </style>
</head>
<body>
    <div class="max-w-7xl mx-auto">
        <!-- Thanh trạng thái & API Key -->
        <div class="mb-4 bg-[#0d0f1a] border border-[#1d2038] rounded-xl p-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2 text-xs text-slate-300">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                <span class="font-bold tracking-wider uppercase">POD PRO CLONE 1:1 (STABLE ENGINE)</span>
            </div>
            <div class="flex items-center gap-2 flex-1 max-w-md">
                <input id="apiKeyInput" type="password" value="SECRET_KEY_PLACEHOLDER" placeholder="Dán Gemini API Key (AIzaSy...) vào đây..." 
                    class="w-full bg-[#131626] border border-[#252a47] rounded-lg px-3 py-1.5 text-xs text-white focus:outline-none focus:border-[#5340ff]">
                <a href="https://aistudio.google.com/apikey" target="_blank" class="text-[11px] bg-[#1e223a] hover:bg-[#2a2f52] text-indigo-300 px-3 py-1.5 rounded-lg whitespace-nowrap">Lấy Key Free</a>
            </div>
        </div>

        <!-- Bố cục 2 cột chuẩn POD -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            
            <!-- CỘT TRÁI: THIẾT LẬP & MẪU -->
            <div class="bg-[#0c0e1a] border border-[#1c2038] rounded-3xl p-6 flex flex-col justify-between shadow-2xl">
                <div>
                    <div class="flex items-center gap-2.5 mb-5">
                        <span class="w-2.5 h-2.5 rounded-full bg-[#5b4eff]"></span>
                        <h2 class="text-xs font-bold tracking-widest text-slate-300 uppercase">THIẾT LẬP CLONE 1:1</h2>
                    </div>

                    <!-- Bộ chọn Model Gemini -->
                    <div class="grid grid-cols-2 gap-3.5 mb-6">
                        <div id="modelFlash" onclick="selectModel('flash')" class="cursor-pointer rounded-2xl p-4 border border-[#232742] bg-[#111322] transition-all">
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-xs font-extrabold text-white">GEMINI 3.8 FLASH</span>
                                <span class="text-[9px] font-bold px-2 py-0.5 rounded bg-[#232742] text-slate-300">FREE TIER</span>
                            </div>
                            <p class="text-[11px] text-slate-400 leading-relaxed">Tốc độ cao, tối ưu phân tích chi tiết.</p>
                        </div>

                        <div id="modelPro" onclick="selectModel('pro')" class="cursor-pointer rounded-2xl p-4 border-2 border-[#5b4eff] bg-[#141530] transition-all">
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-xs font-extrabold text-white">GEMINI 3 PRO</span>
                                <span class="text-[9px] font-bold px-2 py-0.5 rounded bg-[#5b4eff] text-white">PREMIUM</span>
                            </div>
                            <p class="text-[11px] text-slate-300 leading-relaxed">Độ sắc nét tối đa, chuyên sâu thương mại.</p>
                        </div>
                    </div>

                    <!-- Chất lượng vẽ & Kích thước Pixel chuẩn in -->
                    <div class="mb-5">
                        <label class="block text-[10px] font-bold tracking-widest text-slate-400 uppercase mb-2.5">CHẤT LƯỢNG VẼ & KÍCH THƯỚC XUẤT FILE</label>
                        <div class="grid grid-cols-3 gap-3">
                            <button id="res1K" onclick="selectRes('1K')" class="py-2.5 rounded-xl border border-[#222640] bg-[#111322] text-center transition">
                                <div class="text-xs font-bold text-slate-300">1K</div>
                                <div class="text-[9px] text-slate-500">2100x2400px</div>
                            </button>
                            <button id="res2K" onclick="selectRes('2K')" class="py-2.5 rounded-xl border border-[#222640] bg-[#111322] text-center transition">
                                <div class="text-xs font-bold text-slate-300">2K</div>
                                <div class="text-[9px] text-slate-500">3150x3600px</div>
                            </button>
                            <button id="res4K" onclick="selectRes('4K')" class="py-2.5 rounded-xl border border-[#5b4eff] bg-[#5b4eff] text-center transition shadow-lg shadow-indigo-600/30">
                                <div class="text-xs font-bold text-white">4K (Chuẩn in)</div>
                                <div class="text-[9px] text-indigo-100">4200x4800px 300DPI</div>
                            </button>
                        </div>
                    </div>

                    <!-- Tải link hoặc file -->
                    <div class="flex gap-2 mb-5">
                        <input id="imgUrlInput" type="text" placeholder="Dán link ảnh (Etsy, Google...) vào đây" 
                            class="flex-1 bg-[#111322] border border-[#222640] rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-[#5b4eff]">
                        <button onclick="loadFromUrl()" class="bg-[#5b4eff] hover:bg-[#4a3de6] text-white text-xs font-bold px-5 py-2.5 rounded-xl transition">TẢI</button>
                        <label class="bg-[#1b1f38] hover:bg-[#252b4d] text-slate-200 text-xs font-bold px-3.5 py-2.5 rounded-xl cursor-pointer flex items-center">
                            📁 Tệp
                            <input id="fileInput" type="file" accept="image/*" class="hidden" onchange="loadFromFile(event)">
                        </label>
                    </div>

                    <!-- Khung xem trước mockup -->
                    <div class="border border-dashed border-[#2c3258] rounded-2xl p-3 bg-[#090b14] flex items-center justify-center min-h-[360px] relative overflow-hidden">
                        <img id="sourcePreview" src="https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800&q=80" 
                            crossorigin="anonymous" class="max-h-[340px] rounded-xl object-contain" alt="Mockup Preview">
                    </div>
                </div>
            </div>

            <!-- CỘT PHẢI: KẾT QUẢ 2D GRAPHIC & XỬ LÝ -->
            <div class="bg-[#0c0e1a] border border-[#1c2038] rounded-3xl p-6 flex flex-col justify-between shadow-2xl">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center gap-2.5">
                            <span class="w-2.5 h-2.5 rounded-full bg-[#10b981]"></span>
                            <h2 class="text-xs font-bold tracking-widest text-slate-300 uppercase">KẾT QUẢ 2D GRAPHIC (CHUẨN TÁCH NỀN)</h2>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="knockoutBlack()" class="text-[11px] bg-[#161a30] hover:bg-[#22284a] text-indigo-300 border border-[#2b325c] px-3 py-1 rounded-lg font-medium">✨ Khử viền đen</button>
                            <button onclick="downloadResult()" class="text-[11px] bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1 rounded-lg font-bold">⬇ Tải PNG Chuẩn In</button>
                        </div>
                    </div>

                    <!-- Khung Canvas hiển thị kết quả -->
                    <div id="resultContainer" class="rounded-2xl bg-black border border-[#1e223d] flex items-center justify-center min-h-[440px] p-4 relative overflow-hidden">
                        <canvas id="resultCanvas" class="max-h-[420px] max-w-full object-contain rounded-lg"></canvas>
                        <div id="loadingOverlay" class="hidden absolute inset-0 bg-black/80 flex flex-col items-center justify-center gap-3">
                            <div class="w-9 h-9 border-4 border-[#5b4eff] border-t-transparent rounded-full animate-spin"></div>
                            <p id="loadingText" class="text-xs text-indigo-300 font-semibold">Gemini đang phân tích bóc tách & duỗi thẳng chữ...</p>
                        </div>
                    </div>

                    <!-- Thanh trượt điều chỉnh Knock-out -->
                    <div class="mt-3 flex items-center justify-between bg-[#101324] px-3.5 py-2 rounded-xl border border-[#1d2240]">
                        <span class="text-[11px] text-slate-400">Ngưỡng khử nền đen (Knock-out Threshold):</span>
                        <input id="thresholdSlider" type="range" min="0" max="90" value="0" oninput="applyThreshold(this.value)" class="w-40 accent-[#5b4eff]">
                    </div>
                </div>

                <!-- Nút thực thi tự động gọn gàng -->
                <div class="mt-5">
                    <button onclick="runCloneProcess()" class="w-full py-4 rounded-xl bg-gradient-to-r from-[#4e3eff] to-[#6352ff] hover:opacity-95 text-white font-extrabold text-xs tracking-wider uppercase shadow-lg shadow-indigo-600/30 transition">
                        ✨ TIẾN HÀNH CLONE 1:1 & CHUẨN HÓA NỀN IN
                    </button>
                </div>
            </div>

        </div>
    </div>

    <script>
        let currentModel = 'pro';
        let currentRes = '4K';
        let originalImageData = null;

        const canvas = document.getElementById('resultCanvas');
        const ctx = canvas.getContext('2d');
        const sourceImg = document.getElementById('sourcePreview');

        sourceImg.onload = () => {
            drawToCanvas(sourceImg);
        };

        function drawToCanvas(img) {
            canvas.width = img.naturalWidth || 800;
            canvas.height = img.naturalHeight || 800;
            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            originalImageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        }

        function selectModel(m) {
            currentModel = m;
            document.getElementById('modelFlash').className = m === 'flash'
                ? 'cursor-pointer rounded-2xl p-4 border-2 border-[#5b4eff] bg-[#141530] transition-all'
                : 'cursor-pointer rounded-2xl p-4 border border-[#232742] bg-[#111322] transition-all';
            document.getElementById('modelPro').className = m === 'pro'
                ? 'cursor-pointer rounded-2xl p-4 border-2 border-[#5b4eff] bg-[#141530] transition-all'
                : 'cursor-pointer rounded-2xl p-4 border border-[#232742] bg-[#111322] transition-all';
        }

        function selectRes(r) {
            currentRes = r;
            ['1K', '2K', '4K'].forEach(res => {
                const btn = document.getElementById('res' + res);
                if (res === r) {
                    btn.className = 'py-2.5 rounded-xl border border-[#5b4eff] bg-[#5b4eff] text-center transition shadow-lg shadow-indigo-600/30';
                } else {
                    btn.className = 'py-2.5 rounded-xl border border-[#222640] bg-[#111322] text-center transition';
                }
            });
        }

        function loadFromUrl() {
            const url = document.getElementById('imgUrlInput').value.trim();
            if (!url) return alert('Vui lòng dán link ảnh!');
            sourceImg.src = 'https://images.weserv.nl/?url=' + encodeURIComponent(url);
        }

        function loadFromFile(e) {
            const file = e.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = (ev) => { sourceImg.src = ev.target.result; };
            reader.readAsDataURL(file);
        }

        function applyThreshold(val) {
            if (!originalImageData) return;
            const t = parseInt(val);
            const imgData = new ImageData(
                new Uint8ClampedArray(originalImageData.data),
                originalImageData.width,
                originalImageData.height
            );
            const d = imgData.data;
            for (let i = 0; i < d.length; i += 4) {
                const brightness = (d[i] + d[i+1] + d[i+2]) / 3;
                if (brightness <= t) {
                    d[i+3] = 0;
                }
            }
            ctx.putImageData(imgData, 0, 0);
            document.getElementById('resultContainer').classList.toggle('checkerboard', t > 0);
        }

        function knockoutBlack() {
            const slider = document.getElementById('thresholdSlider');
            slider.value = 28;
            applyThreshold(28);
        }

        function downloadResult() {
            const link = document.createElement('a');
            let w = 4200, h = 4800;
            if (currentRes === '1K') { w = 2100; h = 2400; }
            if (currentRes === '2K') { w = 3150; h = 3600; }
            
            const exportCanvas = document.createElement('canvas');
            exportCanvas.width = w;
            exportCanvas.height = h;
            const eCtx = exportCanvas.getContext('2d');
            eCtx.drawImage(canvas, 0, 0, w, h);

            link.download = 'pod-graphic-' + currentRes + '-' + w + 'x' + h + '-300dpi.png';
            link.href = exportCanvas.toDataURL('image/png');
            link.click();
        }

        async function runCloneProcess() {
            const apiKey = document.getElementById('apiKeyInput').value.trim();
            if (!apiKey) {
                alert('Vui lòng dán Gemini API Key ở thanh trên cùng trước khi chạy!');
                return;
            }

            const overlay = document.getElementById('loadingOverlay');
            const loadingText = document.getElementById('loadingText');
            overlay.classList.remove('hidden');

            try {
                const tempCanvas = document.createElement('canvas');
                tempCanvas.width = sourceImg.naturalWidth || 800;
                tempCanvas.height = sourceImg.naturalHeight || 800;
                tempCanvas.getContext('2d').drawImage(sourceImg, 0, 0);
                const base64Data = tempCanvas.toDataURL('image/jpeg', 0.9).split(',')[1];

                loadingText.innerText = 'Bước 1/2: Gemini Vision đang bóc tách chi tiết & khử bỏ nếp nhăn mockup...';

                const visionRes = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=' + apiKey, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{
                            parts: [
                                { text: 'Analyze this t-shirt mockup graphic in extreme detail. Strictly identify and extract the core 2D print artwork and typography. MANDATORY RULES: Remove all shirt wrinkles, fabric textures, stray hairs, and mockup noise. Automatically detect any warped or curved text caused by mockup folds and straighten/normalize them into crisp, flat horizontal typography layouts. Isolate everything on a uniform solid absolute black background #000000.' },
                                { inlineData: { mimeType: 'image/jpeg', data: base64Data } }
                            ]
                        }]
                    })
                });

                const visionJson = await visionRes.json();
                const detailedPrompt = visionJson?.candidates?.[0]?.content?.parts?.[0]?.text || 'exact 1:1 flat 2D graphic clone';

                loadingText.innerText = 'Bước 2/2: Đang tổng hợp file 2D Graphic chuẩn in...';

                let targetWidth = 4200, targetHeight = 4800;
                if (currentRes === '1K') { targetWidth = 2100; targetHeight = 2400; }
                if (currentRes === '2K') { targetWidth = 3150; targetHeight = 3600; }

                const finalPrompt = 'flat 2D t-shirt print graphic, strict 1:1 precise clone, pure solid uniform absolute black background #000000, zero mockup wrinkles, zero stray hair, zero fabric texture noise, all warped or curved text automatically straightened and corrected into clean flat horizontal typography layouts, crisp screenprint vector art, commercial print ready. Details: ' + detailedPrompt;
                const encodedPrompt = encodeURIComponent(finalPrompt);

                const seed = Math.floor(Math.random() * 100000);
                const imageUrls = [
                    'https://image.pollinations.ai/prompt/' + encodedPrompt + '?width=' + targetWidth + '&height=' + targetHeight + '&nologo=true&seed=' + seed,
                    'https://pollinations.ai/p/' + encodedPrompt + '?width=' + targetWidth + '&height=' + targetHeight + '&nologo=true&seed=' + seed
                ];

                let loaded = false;
                for (let url of imageUrls) {
                    try {
                        await new Promise((resolve, reject) => {
                            const newImg = new Image();
                            newImg.crossOrigin = 'anonymous';
                            newImg.onload = () => {
                                canvas.width = targetWidth;
                                canvas.height = targetHeight;
                                ctx.drawImage(newImg, 0, 0, targetWidth, targetHeight);
                                originalImageData = ctx.getImageData(0, 0, targetWidth, targetHeight);
                                loaded = true;
                                resolve();
                            };
                            newImg.onerror = reject;
                            newImg.src = url;
                        });
                        if
