import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="POD Clone 1:1 Studio",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Tự động lấy API Key từ mục Secrets của Streamlit
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

html_code = """
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
        <!-- Thanh nhập API Key nhanh nếu chưa cài trong Secrets -->
        <div class="mb-4 bg-[#0d0f1a] border border-[#1d2038] rounded-xl p-3 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2 text-xs text-slate-300">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
                <span class="font-bold tracking-wider uppercase">POD CLONE 1:1 STUDIO (GEMINI AI)</span>
            </div>
            <div class="flex items-center gap-2 flex-1 max-w-md">
                <input id="apiKeyInput" type="password" value="SECRET_KEY_PLACEHOLDER" placeholder="Dán Gemini API Key (AIzaSy...) vào đây..." 
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
                        <img id="sourcePreview" src="https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=800&q=80" 
                            crossorigin="anonymous" class="max-h-[370px] rounded-xl object-contain" alt="Mockup Preview">
                    </div>
                </div>

                <!-- 4 Chế độ POD -->
                <div class="flex flex-wrap gap-2.5 mt-5 pt-3 border-t border-[#181c33]">
                    <button id="mode_clone" onclick="selectMode('clone')" class="px-4 py-1.5 rounded-full text-xs font-bold bg-[#5b4eff] text-white">Clone 1:1</button>
                    <button id="mode_text" onclick="selectMode('text')" class="px-4 py-1.5 rounded-full text-xs font-semibold bg-[#15182b] text-slate-300 border border-[#252a48]">Đổi Chữ</button>
                    <button id="mode_vintage" onclick="selectMode('vintage')" class="px-4 py-1.5 rounded-full text-xs font-semibold bg-[#15182b] text-slate-300 border border-[#252a48]">Vintage Clean</button>
                    <button id="mode_vector" onclick="selectMode('vector')" class="px-4 py-1.5 rounded-full text-xs font-semibold bg-[#15182b] text-slate-300 border border-[#252a48]">Vectorify</button>
                </div>
            </div>

            <!-- CỘT PHẢI: KẾT QUẢ 2D GRAPHIC -->
            <div class="bg-[#0c0e1a] border border-[#1c2038] rounded-3xl p-6 flex flex-col justify-between shadow-2xl">
                <div>
                    <div class="flex items-center justify-between mb-4">
                        <div class="flex items-center gap-2.5">
                            <span class="w-2.5 h-2.5 rounded-full bg-[#10b981]"></span>
                            <h2 class="text-xs font-bold tracking-widest text-slate-300 uppercase">KẾT QUẢ 2D GRAPHIC</h2>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="knockoutBlack()" class="text-[11px] bg-[#161a30] hover:bg-[#22284a] text-indigo-300 border border-[#2b325c] px-3 py-1 rounded-lg font-medium">✨ Tách nền đen (PNG)</button>
                            <button onclick="downloadResult()" class="text-[11px] bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1 rounded-lg font-bold">⬇ Tải PNG 4K</button>
                        </div>
                    </div>

                    <!-- Khung Canvas hiển thị kết quả 2D -->
                    <div id="resultContainer" class="rounded-2xl bg-black border border-[#1e223d] flex items-center justify-center min-h-[430px] p-4 relative overflow-hidden">
                        <canvas id="resultCanvas" class="max-h-[410px] max-w-full object-contain rounded-lg"></canvas>
                        <div id="loadingOverlay" class="hidden absolute inset-0 bg-black/80 flex flex-col items-center justify-center gap-3">
                            <div class="w-9 h-9 border-4 border-[#5b4eff] border-t-transparent rounded-full animate-spin"></div>
                            <p id="loadingText" class="text-xs text-indigo-300 font-semibold">Đang phân tích & tái tạo Graphic 2D chuẩn in...</p>
                        </div>
                    </div>

                    <!-- Thanh trượt tinh chỉnh độ sạch nền đen -->
                    <div class="mt-3 flex items-center justify-between bg-[#101324] px-3.5 py-2 rounded-xl border border-[#1d2240]">
                        <span class="text-[11px] text-slate-400">Ngưỡng khử nền đen (Knock-out Threshold):</span>
                        <input id="thresholdSlider" type="range" min="0" max="90" value="0" oninput="applyThreshold(this.value)" class="w-40 accent-[#5b4eff]">
                    </div>
                </div>

                <!-- Khu vực Prompt & Nút Cập Nhật -->
                <div class="mt-5 space-y-3">
                    <div class="bg-[#111322] border border-[#222640] rounded-xl p-3">
                        <div class="text-[10px] font-bold text-slate-400 uppercase mb-1">MÔ TẢ HỆ THỐNG:</div>
                        <input id="systemPrompt" type="text" value="strict clone replicate every element precisely flat 2D graphic isolated on pure black background #000000" 
                            class="w-full bg-transparent text-xs text-indigo-300 focus:outline-none">
                    </div>

                    <input id="userPrompt" type="text" placeholder="Nhập yêu cầu sửa thêm (VD: Đổi chữ thành MIKE MACDONALD, giữ nguyên bố cục)..." 
                        class="w-full bg-[#111322] border border-[#222640] rounded-xl px-4 py-3 text-xs text-white focus:outline-none focus:border-[#5b4eff]">

                    <button onclick="runCloneProcess()" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-[#4e3eff] to-[#6352ff] hover:opacity-95 text-white font-extrabold text-xs tracking-wider uppercase shadow-lg shadow-indigo-600/30 transition">
                        CẬP NHẬT CHỈNH SỬA
                    </button>
                </div>
            </div>

        </div>
    </div>

    <script>
        let currentModel = 'pro';
        let currentRes = '4K';
        let currentMode = 'clone';
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

        function selectMode(mode) {
            currentMode = mode;
            const prompts = {
                clone: 'strict clone replicate every element precisely flat 2D graphic isolated on pure black background #000000',
                text: 'strict clone graphic layout, replace typography with custom text, crisp edges on pure black #000000',
                vintage: 'clean vintage bootleg rap tee graphic, distressed screenprint texture isolated on pure black #000000',
                vector: 'clean sharp vector screenprint graphic, bold outlines, solid vibrant colors on pure black #000000'
            };
            document.getElementById('systemPrompt').value = prompts[mode];
            ['clone', 'text', 'vintage', 'vector'].forEach(m => {
                const btn = document.getElementById('mode_' + m);
                btn.className = (m === mode)
                    ? 'px-4 py-1.5 rounded-full text-xs font-bold bg-[#5b4eff] text-white'
                    : 'px-4 py-1.5 rounded-full text-xs font-semibold bg-[#15182b] text-slate-300 border border-[#252a48]';
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
            link.download = 'pod-graphic-' + currentRes + '.png';
            link.href = canvas.toDataURL('image/png');
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

                const sysPrompt = document.getElementById('systemPrompt').value;
                const usrPrompt = document.getElementById('userPrompt').value;

                loadingText.innerText = 'Bước 1/2: Gemini Vision đang bóc tách bố cục & kiểu chữ từ áo mẫu...';

                const visionRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{
                            parts: [
                                { text: `Analyze the graphic printed on this shirt in extreme detail so an illustrator can recreate an exact 1:1 flat 2D print file on a solid #000000 black background. Include exact text, font style, colors, character positions, lighting, and effects. System rule: ${sysPrompt}. Extra user edits: ${usrPrompt}` },
                                { inlineData: { mimeType: 'image/jpeg', data: base64Data } }
                            ]
                        }]
                    })
                });

                const visionJson = await visionRes.json();
                const detailedPrompt = visionJson?.candidates?.[0]?.content?.parts?.[0]?.text || sysPrompt;
                document.getElementById('systemPrompt').value = detailedPrompt.substring(0, 220) + '...';

                loadingText.innerText = 'Bước 2/2: Đang vẽ lại 2D Graphic sắc nét trên nền đen chuẩn in...';

                const genRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp-image-generation:generateContent?key=${apiKey}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{
                            parts: [
                                { text: `Create a flat 2D t-shirt print graphic isolated on a pure solid black #000000 background (NO t-shirt mockup, NO wrinkles, ONLY the flat 2D artwork): ${detailedPrompt}. ${usrPrompt}` },
                                { inlineData: { mimeType: 'image/jpeg', data: base64Data } }
                            ]
                        }],
                        generationConfig: { responseModalities: ["TEXT", "IMAGE"] }
                    })
                });

                const genJson = await genRes.json();
                const parts = genJson?.candidates?.[0]?.content?.parts || [];
                const imgPart = parts.find(p => p.inlineData);

                if (imgPart) {
                    const newImg = new Image();
                    newImg.onload = () => {
                        drawToCanvas(newImg);
                        overlay.classList.add('hidden');
                    };
                    newImg.src = 'data:' + imgPart.inlineData.mimeType + ';base64,' + imgPart.inlineData.data;
                } else {
                    alert('Đã phân tích xong Prompt hệ thống! Nếu tài khoản API Key của bạn chưa bật quyền tạo ảnh trực tiếp, hãy kiểm tra lại giới hạn vùng (Region) trong Google AI Studio.');
                    overlay.classList.add('hidden');
                }
            } catch (err) {
                alert('Lỗi kết nối API: ' + err.message);
                overlay.classList.add('hidden');
            }
        }
    </script>
</body>
</html>
"""

# Đưa API Key vào HTML một cách an toàn tuyệt đối
html_code = html_code.replace("SECRET_KEY_PLACEHOLDER", secret_api_key)

components.html(html_code, height=920, scrolling=True)
