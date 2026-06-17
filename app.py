import os
from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# Premium HTML Template bundled into the background runner
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Naturally Dubai</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Instrument Sans', sans-serif; background-color: #F7F4EB; color: #4A3E3D; }
        .font-serif { font-family: 'Playfair Display', serif; }
        .glass-panel { background: rgba(253, 251, 247, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(205, 220, 190, 0.5); }
    </style>
</head>
<body class="min-h-screen pb-28">

    <!-- Free AI Configuration Portal -->
    <div id="settings-panel" class="max-w-md mx-auto p-4 mt-4 bg-white rounded-2xl border border-[#CDDCBE] shadow-sm">
        <h3 class="text-xs font-bold uppercase tracking-wider text-[#6C8451] mb-2">🌿 Connect Your Free AI Brain</h3>
        <p class="text-[11px] text-[#8C7A6B] mb-3">Paste your free Groq API Key below to get unlimited, creative responses with zero costs.</p>
        <div class="flex space-x-2">
            <input type="password" id="api-key-input" placeholder="gsk_..." class="flex-1 text-xs p-2.5 bg-[#FDFBF7] border border-[#CDDCBE] rounded-xl focus:outline-none">
            <button onclick="saveApiKey()" class="bg-[#8FA872] text-white text-xs px-4 py-2 rounded-xl font-medium">Connect</button>
        </div>
        <p id="settings-status" class="text-[10px] text-[#6C8451] mt-1 hidden">✓ Connected to Free Live Brain.</p>
    </div>

    <!-- Header App Bar -->
    <header class="pt-6 px-6 max-w-md mx-auto flex justify-between items-center">
        <div>
            <h1 class="font-serif text-2xl font-semibold text-[#4A3E3D] tracking-tight">Network Naturally</h1>
            <p class="text-[10px] text-[#6C8451] font-bold tracking-wider uppercase">Dubai Personal Edition</p>
        </div>
        <div class="w-10 h-10 rounded-full bg-[#CDDCBE] flex items-center justify-center font-bold text-[#6C8451] text-sm shadow-sm border border-white">V</div>
    </header>

    <!-- Main Views Container -->
    <main class="max-w-md mx-auto px-4 pt-6 space-y-6">
        
        <!-- Tab 1: Progress Tracker Dashboard -->
        <div id="view-grow" class="space-y-6">
            <div class="glass-panel p-6 rounded-3xl shadow-sm relative overflow-hidden">
                <div class="flex justify-between items-start">
                    <div>
                        <span class="text-[11px] bg-[#CDDCBE] text-[#6C8451] font-semibold px-2.5 py-1 rounded-full">Level 4: Relationship Builder</span>
                        <h2 class="text-xl font-bold font-serif text-[#4A3E3D] mt-3">Welcome back, Varsha</h2>
                        <p class="text-xs text-[#8C7A6B] mt-1">Consistency Streak: <span class="text-[#6C8451] font-bold">🔥 8 Days</span></p>
                    </div>
                    <div class="text-right">
                        <div class="text-3xl font-serif font-semibold text-[#6C8451]">74<span class="text-xs text-[#8C7A6B]">/100</span></div>
                        <div class="text-[9px] font-bold tracking-wider text-[#8C7A6B] uppercase mt-0.5">Referral Ready</div>
                    </div>
                </div>
                <div class="w-full bg-[#EFECE1] h-2 rounded-full mt-4 overflow-hidden">
                    <div class="bg-[#8FA872] h-full rounded-full" style="width: 74%"></div>
                </div>
            </div>

            <!-- Daily Goals Checklist -->
            <div>
                <h3 class="text-xs font-bold tracking-wider uppercase text-[#8C7A6B] px-1 mb-3">Daily 15-Minute Missions</h3>
                <div class="space-y-2.5">
                    <label class="p-4 rounded-2xl border border-[#EFECE1] bg-white shadow-sm flex items-center space-x-3.5 cursor-pointer hover:border-[#CDDCBE]">
                        <input type="checkbox" checked class="accent-[#8FA872] w-4 h-4">
                        <div>
                            <p class="text-sm font-medium text-[#4A3E3D]">Observe 3 Dubai HR Directors on LinkedIn</p>
                            <span class="text-[10px] font-medium text-[#8FA872]">5 Minutes • Mindset</span>
                        </div>
                    </label>
                    <label class="p-4 rounded-2xl border border-[#EFECE1] bg-white shadow-sm flex items-center space-x-3.5 cursor-pointer hover:border-[#CDDCBE]">
                        <input type="checkbox" class="accent-[#8FA872] w-4 h-4">
                        <div>
                            <p class="text-sm font-medium text-[#4A3E3D]">Engage genuinely with 1 thought leadership post</p>
                            <span class="text-[10px] font-medium text-[#8FA872]">5 Minutes • Visibility</span>
                        </div>
                    </label>
                </div>
            </div>
        </div>

        <!-- Tab 2: Free Live AI Persona Arena -->
        <div id="view-simulate" class="hidden space-y-4">
            <div class="px-1">
                <h2 class="text-xl font-serif font-bold text-[#4A3E3D]">Live Persona Arena</h2>
                <p class="text-xs text-[#8C7A6B] mt-0.5">Simulate fluid conversations with custom Dubai characters.</p>
            </div>

            <div class="flex space-x-2 overflow-x-auto pb-1">
                <button onclick="switchPersona('tariq')" id="btn-tariq" class="px-4 py-2 rounded-full text-xs font-medium border bg-[#8FA872] text-white border-[#8FA872]">Tariq (HR Director)</button>
                <button onclick="switchPersona('chloe')" id="btn-chloe" class="px-4 py-2 rounded-full text-xs font-medium border bg-white text-[#8C7A6B] border-[#EFECE1]">Chloe (TA Lead)</button>
            </div>

            <div class="bg-white rounded-3xl border border-[#EFECE1] h-96 p-4 flex flex-col justify-between shadow-sm">
                <div id="chat-box" class="overflow-y-auto space-y-3 text-xs pr-1">
                    <div id="persona-intro" class="p-3 bg-[#F7F4EB] rounded-2xl text-[#8C7A6B] text-center italic border border-dashed border-[#CDDCBE]">
                        Simulating Tariq Al-Mansoori (Semi-Gov, 14y exp). He values classic professionalism. Introduce yourself or make an industry observation.
                    </div>
                </div>
                <div class="flex items-center space-x-2 mt-2">
                    <input type="text" id="chat-input" placeholder="Type your message here..." class="flex-1 bg-[#FDFBF7] border border-[#CDDCBE] rounded-xl px-4 py-3 text-xs focus:outline-none focus:border-[#8FA872]">
                    <button id="btn-send-chat" onclick="handleLiveChat()" class="bg-[#E6ECE0] text-[#6C8451] font-bold px-4 py-3 rounded-xl hover:bg-[#CDDCBE] text-xs">Send</button>
                </div>
            </div>

            <div id="sim-feedback" class="hidden bg-[#E6ECE0]/50 border border-[#CDDCBE] p-4 rounded-2xl text-xs">
                <span class="font-bold text-[#6C8451]">🌿 Coach's Live Blueprint Review:</span>
                <p id="sim-feedback-text" class="text-[#4A3E3D] mt-1 leading-relaxed"></p>
            </div>
        </div>

        <!-- Tab 3: Free Live Message Analyzer View -->
        <div id="view-analyze" class="hidden space-y-4">
            <div class="px-1">
                <h2 class="text-xl font-serif font-bold text-[#4A3E3D]">Live Outreach Guard</h2>
                <p class="text-xs text-[#8C7A6B] mt-0.5">Let the AI scan your drafts before you message them on LinkedIn.</p>
            </div>
            <div class="bg-white rounded-3xl border border-[#EFECE1] p-4 shadow-sm">
                <textarea id="analyzer-input" placeholder="Paste your draft message here..." class="w-full h-32 bg-[#FDFBF7] border border-[#CDDCBE] rounded-2xl p-4 text-xs resize-none focus:outline-none"></textarea>
                <button id="btn-run-analysis" onclick="handleLiveAnalysis()" class="w-full mt-3 bg-[#8FA872] text-white font-medium text-xs py-3 rounded-xl shadow-sm hover:bg-[#6C8451]">Run Deep Diagnostic Audit</button>
            </div>
            <div id="analyzer-result" class="hidden space-y-4">
                <div class="bg-white rounded-2xl p-4 border border-[#EFECE1] text-xs space-y-2">
                    <p id="audit-output-text" class="text-[#4A3E3D] whitespace-pre-line leading-relaxed"></p>
                </div>
            </div>
        </div>

    </main>

    <!-- Navigation Control System -->
    <nav class="fixed bottom-6 left-1/2 -translate-x-1/2 w-[90%] max-w-xs glass-panel rounded-full py-2.5 px-5 shadow-lg flex justify-between items-center z-50">
        <button onclick="showView('grow')" class="flex flex-col items-center text-[#6C8451]"><span class="text-lg">🌿</span><span class="text-[9px] font-semibold mt-0.5">Grow</span></button>
        <button onclick="showView('simulate')" class="flex flex-col items-center text-[#8C7A6B] hover:text-[#6C8451]"><span class="text-lg">🎭</span><span class="text-[9px] font-semibold mt-0.5">Simulate</span></button>
        <button onclick="showView('analyze')" class="flex flex-col items-center text-[#8C7A6B] hover:text-[#6C8451]"><span class="text-lg">✨</span><span class="text-[9px] font-semibold mt-0.5">Analyze</span></button>
    </nav>

    <script>
        let apiKey = localStorage.getItem('nn_groq_key') || '';
        let conversationHistory = [];
        let currentPersona = {
            name: "Tariq Al-Mansoori",
            details: "HR Director at a major Dubai Semi-Government entity with 14 years experience. Polite, busy, deeply values high-level professional courtesy, and skips transactional messages or job pleas."
        };

        if(apiKey) { document.getElementById('settings-status').classList.remove('hidden'); }

        function saveApiKey() {
            const key = document.getElementById('api-key-input').value.trim();
            if(key) {
                localStorage.setItem('nn_groq_key', key);
                apiKey = key;
                document.getElementById('settings-status').classList.remove('hidden');
                document.getElementById('api-key-input').value = '';
                alert("Key saved locally!");
            }
        }

        function showView(viewId) {
            ['grow', 'simulate', 'analyze'].forEach(v => document.getElementById('view-' + v).classList.add('hidden'));
            document.getElementById('view-' + viewId).classList.remove('hidden');
        }

        function switchPersona(type) {
            const chatBox = document.getElementById('chat-box');
            const intro = document.getElementById('persona-intro');
            conversationHistory = [];
            
            if(type === 'tariq') {
                currentPersona = { name: "Tariq Al-Mansoori", details: "HR Director at a Semi-Government entity. Prefers formal structure and local corporate trends." };
                document.getElementById('btn-tariq').className = "px-4 py-2 rounded-full text-xs font-medium border bg-[#8FA872] text-white border-[#8FA872]";
                document.getElementById('btn-chloe').className = "px-4 py-2 rounded-full text-xs font-medium border bg-white text-[#8C7A6B] border-[#EFECE1]";
                intro.innerText = "Simulating Tariq. He values classic professionalism. Introduce yourself or make an industry observation.";
            } else {
                currentPersona = { name: "Chloe Vance", details: "Talent Acquisition Lead at a hyper-growth Tech Hub in DIFC. Fast-paced, uses direct conversational language, loves short trend hooks." };
                document.getElementById('btn-chloe').className = "px-4 py-2 rounded-full text-xs font-medium border bg-[#8FA872] text-white border-[#8FA872]";
                document.getElementById('btn-tariq').className = "px-4 py-2 rounded-full text-xs font-medium border bg-white text-[#8C7A6B] border-[#EFECE1]";
                intro.innerText = "Simulating Chloe. She is fast-paced and hyper-focused. Skip long introductions and make a quick, specific observation.";
            }
            chatBox.innerHTML = '';
            chatBox.appendChild(intro);
            document.getElementById('sim-feedback').classList.add('hidden');
        }

        async function postToServer(endpoint, payload) {
            try {
                const response = await fetch(endpoint, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ ...payload, key: apiKey })
                });
                const data = await response.json();
                return data.reply || data.output;
            } catch (err) {
                return "Server connection glitch. Trying again...";
            }
        }

        async function handleLiveChat() {
            const input = document.getElementById('chat-input');
            const userText = input.value.trim();
            if(!userText) return;

            const sendBtn = document.getElementById('btn-send-chat');
            sendBtn.innerText = "Thinking...";
            sendBtn.disabled = true;

            appendMsg('user', userText);
            input.value = '';
            
            conversationHistory.push({ role: "user", content: userText });

            const systemPrompt = `You are simulating ${currentPersona.name}: ${currentPersona.details}. 
            You are talking on LinkedIn messages to Varsha, an Indian HR professional with 2 years of experience.
            Respond exactly how this busy professional would. If Varsha acts transactional, asks for a job, or sounds desperate, respond with brief, cold corporate distance. If she shares an elegant observation about Dubai workplace dynamics, be warm and engaging.
            Keep your response short (2-3 sentences max). At the absolute end of your response, put a divider line exactly like this "---" and write a 1-sentence supportive, constructive feedback tip for Varsha from a coaching perspective, explaining how well she balanced warmth vs intent.`;

            const fullHistory = [{ role: "system", content: systemPrompt }, ...conversationHistory];
            
            const rawOutput = await postToServer('/chat', { messages: fullHistory });
            sendBtn.innerText = "Send";
            sendBtn.disabled = false;
            
            if(!rawOutput) return;

            const parts = rawOutput.split('---');
            const personaReply = parts[0].trim();
            const coachFeedback = parts[1] ? parts[1].trim() : "Focus on keeping statements short, confident, and observation-driven.";

            conversationHistory.push({ role: "assistant", content: personaReply });
            appendMsg('persona', personaReply);

            document.getElementById('sim-feedback-text').innerText = coachFeedback;
            document.getElementById('sim-feedback').classList.remove('hidden');
        }

        function appendMsg(sender, text) {
            const box = document.getElementById('chat-box');
            const wrapper = document.createElement('div');
            wrapper.className = `flex ${sender === 'user' ? 'justify-end' : 'justify-start'}`;
            const bubble = document.createElement('div');
            bubble.className = `max-w-[85%] p-3 rounded-2xl leading-relaxed ${sender === 'user' ? 'bg-[#8FA872] text-white rounded-tr-none' : 'bg-[#F7F4EB] text-[#4A3E3D] rounded-tl-none'}`;
            bubble.innerText = text;
            wrapper.appendChild(bubble);
            box.appendChild(wrapper);
            box.scrollTop = box.scrollHeight;
        }

        async function handleLiveAnalysis() {
            const text = document.getElementById('analyzer-input').value.trim();
            if(!text) return;

            const analyzeBtn = document.getElementById('btn-run-analysis');
            analyzeBtn.innerText = "Analyzing Draft Alignment...";
            analyzeBtn.disabled = true;

            const fullPrompt = [{
                role: "system",
                content: "You are an elite executive communications coach for 'Network Naturally Dubai'. Analyze the following networking outreach draft message from Varsha. Rate it strictly out of 100 based on relationship potential and confidence (penalize heavily if she directly asks for a job, referrals, or openings). Provide clear feedback highlighting why it feels transactional or robotic, and give her an ultra-elegant, natural Gen-Z professional rewrite that sounds effortless and curious."
            }, {
                role: "user",
                content: `Analyze this draft: "${text}"`
            }];

            const output = await postToServer('/chat', { messages: fullPrompt });
            analyzeBtn.innerText = "Run Deep Diagnostic Audit";
            analyzeBtn.disabled = false;
            
            if(!output) return;

            document.getElementById('audit-output-text').innerText = output;
            document.getElementById('analyzer-result').classList.remove('hidden');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def proxy_chat():
    data = request.json
    api_key = data.get('key')
    messages = data.get('messages', [])
    
    if not api_key:
        return jsonify({"reply": "🔑 API Key Error: It looks like no key was entered in the app configuration panel."}), 400
        
    try:
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'llama3-8b-8192',  # Highly reliable alternative free model
                'messages': messages,
                'temperature': 0.7
            },
            timeout=20
        )
        res_data = response.json()
        
        # If Groq returns an error, pass its message straight to Varsha's screen
        if 'error' in res_data:
            return jsonify({"reply": f"❌ Server Message: {res_data['error'].get('message', 'Key validation issue.')}"})
            
        return jsonify({"reply": res_data['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"reply": f"🚨 Diagnostic Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
