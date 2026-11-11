# -*- coding: utf-8 -*-
from lib import *

HOME_FAQ = [
    ("手持式熱像儀的 NETD 是什麼？數字越小越好嗎？",
     "NETD（噪聲等效溫差）代表熱像儀能分辨的最小溫差，單位通常是 mK。數字越小，代表對微小溫差越敏感，影像細節與低對比目標的辨識度通常越好。"
     "但實際效果還要搭配解析度、鏡頭與使用距離一起評估，不能只看單一數字。", True),
    ("研楷與高德智感（Guide Sensmart）是什麼關係？",
     "研楷有限公司為高德智感（Guide Sensmart）的授權代理商，提供其手持式紅外線熱像儀；同時開發台灣自有品牌 AP_G 系列與客製化規格。", True),
    ("可以只買熱像儀，不用 AI 影像分析服務嗎？",
     "可以。手持式熱像儀可單獨採購。AI／ML 影像分析是另外提供的選配服務，適合需要把檢測流程自動化或做缺陷識別的產線與實驗室。", True),
]


def home():
    crumbs = None
    ld = [ORG_LD,
          {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website",
           "url": SITE + "/", "name": "研楷 Aperture Science", "inLanguage": "zh-TW",
           "publisher": {"@id": SITE + "/#org"}},
          faq_ld(HOME_FAQ)]
    h = head("研楷 Aperture Science｜手持式熱像儀與 AI 影像分析",
             "研楷有限公司（Aperture Science Co., Ltd.）專注手持式紅外線熱像儀與 AI/ML 影像分析，為高德智感 Guide Sensmart 授權代理商，"
             "服務半導體、智慧能源與研發實驗室的精密熱點檢測。", "/", ld)
    body = nav("")
    body += f'''<section class="hero-bg relative">
<div class="max-w-7xl mx-auto px-6 py-20 md:py-28 grid lg:grid-cols-2 gap-14 items-center">
<div>
<div class="inline-flex items-center space-x-3 px-3 py-1 bg-navyMain/5 border border-navyMain/20 text-navyMain text-xs font-tech mb-8 tracking-[0.2em]">
<span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-navyMain opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-navyMain"></span></span>
<span>PRECISION PERCEPTION | EST. 2024</span>
</div>
<h1 class="text-5xl md:text-7xl font-bold text-navyMain leading-[1.1] mb-8 tracking-tight">精準感知<br><span class="text-transparent bg-clip-text bg-gradient-to-r from-navyMain to-slate-500">智能檢測</span></h1>
<p class="text-xl text-slate-700 max-w-xl mb-4 leading-relaxed font-light">「定義工業熱顯新標準」</p>
<p class="text-base text-slate-500 max-w-xl mb-10 leading-relaxed">整合手持式紅外線熱像儀與 AI/ML 深度學習分析，為半導體、智慧能源與研發實驗室提供數據驅動的關鍵決策。</p>
<div class="flex flex-wrap gap-4 items-center">
<a href="/products/" class="bg-navyMain text-white px-8 py-4 font-bold hover:bg-slate-700 transition inline-flex items-center space-x-3 rounded-sm shadow-md"><span>探索產品 EXPLORE</span><i class="fas fa-chevron-right text-xs"></i></a>
<a href="/contact/" class="border border-navyMain text-navyMain px-8 py-4 font-bold hover:bg-navyMain hover:text-white transition rounded-sm">專案諮詢 CONTACT</a>
</div>
</div>
<div class="relative rounded-2xl overflow-hidden bg-black shadow-2xl tech-border-accent">
<img src="/assets/img/guide-handheld.webp" width="1200" height="675" alt="Guide Sensmart 手持式紅外線熱像儀" class="w-full h-auto" fetchpriority="high">
<div class="absolute bottom-0 left-0 right-0 p-5 bg-gradient-to-t from-black/80 to-transparent text-white">
<div class="text-[10px] font-tech tracking-[0.25em] text-white/60 uppercase">Guide Sensmart Authorized</div>
<div class="font-bold">手持式紅外線熱像儀</div>
</div>
</div>
</div>
</section>

<div class="py-16 bg-navyLight border-y border-slate-200 overflow-hidden" aria-label="合作客戶">
<div class="logo-slider">
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">TSMC</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">ITRI</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">CPC</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">TAIPOWER</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">GE POWER</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">UMC</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default"><span class="text-2xl font-bold text-navyMain font-tech">ASE GROUP</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">TSMC</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">ITRI</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">CPC</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">TAIPOWER</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">GE POWER</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">UMC</span></div>
<div class="flex items-center justify-center w-[250px] grayscale opacity-50 hover:opacity-100 hover:grayscale-0 transition cursor-default" aria-hidden="true"><span class="text-2xl font-bold text-navyMain font-tech">ASE GROUP</span></div>
</div>
</div>

<section class="max-w-7xl mx-auto px-6 py-16">
{answer_box("研楷有限公司（Aperture Science Co., Ltd.）是位於桃園的手持式熱像儀與 AI 影像分析服務商，為高德智感（Guide Sensmart）授權代理商，"
            "並提供台灣自有品牌 AP_G 系列與客製化開發，服務對象涵蓋半導體、電力能源與研發實驗室。")}
<div class="grid md:grid-cols-3 gap-8">
<a href="/products/" class="group bg-white rounded-xl border border-slate-200 p-8 shadow-sm hover:shadow-md hover:border-navyMain transition">
<div class="w-12 h-12 bg-navyMain text-white rounded-lg flex items-center justify-center mb-6"><i class="fas fa-camera"></i></div>
<h2 class="text-xl font-bold text-navyMain mb-3">手持式紅外線熱像儀</h2>
<p class="text-sm text-slate-600 leading-relaxed mb-6">高德智感授權的 APEX、E、H、PT 系列，以及台灣自有品牌 AP_G 與 OEM 客製。</p>
<span class="text-sm font-bold text-navyMain">查看產品系列 <i class="fas fa-arrow-right ml-1 text-xs group-hover:translate-x-1 transition"></i></span>
</a>
<a href="/ai-inspection/" class="group bg-white rounded-xl border border-slate-200 p-8 shadow-sm hover:shadow-md hover:border-navyMain transition">
<div class="w-12 h-12 bg-navyMain text-white rounded-lg flex items-center justify-center mb-6"><i class="fas fa-brain"></i></div>
<h2 class="text-xl font-bold text-navyMain mb-3">ML／DL 影像分析</h2>
<p class="text-sm text-slate-600 leading-relaxed mb-6">結合深度學習的缺陷識別與自動化檢測，涵蓋焊接、膠線、封裝與 PCB 等場景。</p>
<span class="text-sm font-bold text-navyMain">了解 AI 服務 <i class="fas fa-arrow-right ml-1 text-xs group-hover:translate-x-1 transition"></i></span>
</a>
<a href="/products/instruments/" class="group bg-white rounded-xl border border-slate-200 p-8 shadow-sm hover:shadow-md hover:border-navyMain transition">
<div class="w-12 h-12 bg-navyMain text-white rounded-lg flex items-center justify-center mb-6"><i class="fas fa-microscope"></i></div>
<h2 class="text-xl font-bold text-navyMain mb-3">工業／半導體儀器</h2>
<p class="text-sm text-slate-600 leading-relaxed mb-6">桌上型量測與穿透式（X-ray &amp; IR）檢測儀器，以及 X 光設備品保工具。</p>
<span class="text-sm font-bold text-navyMain">查看儀器類別 <i class="fas fa-arrow-right ml-1 text-xs group-hover:translate-x-1 transition"></i></span>
</a>
</div>
</section>

<section class="bg-navyLight border-y border-slate-200">
<div class="max-w-7xl mx-auto px-6 py-16">
<div class="text-xs font-tech text-slate-400 tracking-[0.4em] mb-3 uppercase">Industries / 產業應用</div>
<h2 class="text-3xl font-bold text-navyMain mb-10">依您的產業找方案</h2>
<div class="grid md:grid-cols-3 gap-8">
<a href="/industries/semiconductor/" class="group block bg-white rounded-xl border border-slate-200 overflow-hidden hover:border-navyMain hover:shadow-md transition">
<div class="overflow-hidden"><img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&amp;fit=crop&amp;q=80&amp;w=600" width="600" height="400" alt="半導體產業應用情境" class="h-48 w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy"></div>
<div class="p-6"><h3 class="font-bold text-navyMain text-lg mb-2">半導體產業</h3><p class="text-sm text-slate-600 leading-relaxed">提供製程中封裝測試與 Wafer 階段的非接觸式溫度 analysis，協助排除潛在熱點異常點檢。</p></div>
</a>
<a href="/industries/power/" class="group block bg-white rounded-xl border border-slate-200 overflow-hidden hover:border-navyMain hover:shadow-md transition">
<div class="overflow-hidden"><img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&amp;fit=crop&amp;q=80&amp;w=600" width="600" height="400" alt="智慧能源與電力設施" class="h-48 w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy"></div>
<div class="p-6"><h3 class="font-bold text-navyMain text-lg mb-2">智慧能源與電力</h3><p class="text-sm text-slate-600 leading-relaxed">變壓器、電力機房與儲能設施的 24/7 自動化熱顯巡檢，有效預防過熱引發之災損。</p></div>
</a>
<a href="/industries/lab/" class="group block bg-white rounded-xl border border-slate-200 overflow-hidden hover:border-navyMain hover:shadow-md transition">
<div class="overflow-hidden"><img src="https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&amp;fit=crop&amp;q=80&amp;w=600" width="600" height="400" alt="研發實驗室" class="h-48 w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy"></div>
<div class="p-6"><h3 class="font-bold text-navyMain text-lg mb-2">研發實驗室</h3><p class="text-sm text-slate-600 leading-relaxed">輔助 NPI 階段的熱散布驗證，把實驗數據轉化為量產標準。</p></div>
</a>
</div>
</div>
</section>

<section class="max-w-7xl mx-auto px-6 py-20">
<div class="text-xs font-tech text-slate-400 tracking-[0.4em] mb-3 uppercase">Why Aperture Science</div>
<h2 class="text-3xl font-bold text-navyMain mb-10">為什麼選擇研楷</h2>
<div class="grid md:grid-cols-2 gap-6">
<div class="p-6 bg-navyLight border-l-2 border-navyMain rounded-sm"><h3 class="text-navyMain font-bold mb-2">原廠授權代理</h3><p class="text-sm text-slate-600 leading-relaxed">高德智感（Guide Sensmart）授權代理商，提供手持式熱像儀產品線。</p></div>
<div class="p-6 bg-navyLight border-l-2 border-navyMain rounded-sm"><h3 class="text-navyMain font-bold mb-2">軟硬體一體化</h3><p class="text-sm text-slate-600 leading-relaxed">自研算法適配高階感測器，讓熱像資料能進一步用於分析與判讀。</p></div>
<div class="p-6 bg-navyLight border-l-2 border-navyMain rounded-sm"><h3 class="text-navyMain font-bold mb-2">顧問式服務</h3><p class="text-sm text-slate-600 leading-relaxed">不只販售硬體，更針對產線與實驗室的痛點提供解決方案。</p></div>
<div class="p-6 bg-navyLight border-l-2 border-navyMain rounded-sm"><h3 class="text-navyMain font-bold mb-2">台灣在地支援與客製</h3><p class="text-sm text-slate-600 leading-relaxed">台灣自有品牌 AP_G 系列與 OEM 客製化開發，提供在地技術支援。</p></div>
</div>
</section>

<section class="bg-navyLight border-t border-slate-200">
<div class="max-w-4xl mx-auto px-6 py-16">
<h2 class="text-3xl font-bold text-navyMain mb-8">常見問題</h2>
{faq_block(HOME_FAQ)}
<a href="/faq/" class="inline-block mt-8 text-navyMain font-bold hover:underline">查看全部常見問題 →</a>
</div>
</section>
'''
    body += cta()
    body += footer()
    write("/", h + body, "1.0")


# ---------------------------------------------------------------- ABOUT
def about():
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("關於研楷", "/about/")])
    ld = [ORG_LD, bc_ld]
    h = head("關於研楷：從半導體實驗室出發的熱像檢測團隊",
             "研楷有限公司（Aperture Science Co., Ltd.）核心團隊源自半導體實驗室量測儀器開發，結合紅外線熱像與 AI/ML 影像分析，"
             "為高德智感 Guide Sensmart 授權代理商，並開發自有品牌 AP_G。", "/about/", ld)
    body = nav("about")
    body += page_header("Corporate Background / 發展脈絡", "傳承精密，定義未來",
                        "我們從半導體實驗室的量測儀器出發，把對精度與數據穩定性的要求，帶進工業熱像檢測。", bc_html)
    body += f'''<div class="max-w-7xl mx-auto px-6 py-16 grid lg:grid-cols-3 gap-14">
<div class="lg:col-span-2 prose-as">
<h2 class="text-2xl font-bold text-navyMain mb-4">公司簡介</h2>
<p><strong class="text-navyMain">研楷有限公司（Aperture Science Co., Ltd.）</strong>核心團隊起源於「半導體實驗室量測儀器」開發，在追求奈米級精度與數據穩定性的環境中，我們傳承了精密檢測的基因。</p>
<p>面對工業 4.0 的挑戰，我們將紅外線熱像技術與 AI（ML/DL）影像識別深度整合，從被動觀測轉向主動分析與趨勢預測。公司成立於 2024 年，總部位於桃園。</p>

<h3>名稱與品牌說明</h3>
<ul>
<li><strong>研楷有限公司</strong>：英文名稱為 Aperture Science Co., Ltd.，為設立於台灣的公司，與任何同名的虛構企業或娛樂作品無關。</li>
<li><strong>高德智感（Guide Sensmart）</strong>：武漢高德智感科技有限公司，2016 年成立，為高德紅外（Guide Infrared，1999 年成立）的全資子公司。研楷為其授權代理商。
<span class="text-xs text-slate-400">（資料來源：高德紅外官方網站 guideir.com）</span></li>
<li><strong>AP_G</strong>：研楷開發的台灣自有品牌手持式熱像儀系列，詳見 <a class="text-navyMain underline" href="/products/ap-g/">AP_G 系列</a>。</li>
</ul>

<h3>我們的服務方式</h3>
<ul>
<li><strong>軟硬體一體化</strong>：自研算法無縫適配高階感測器，確保數據解析度最大化。</li>
<li><strong>顧問式服務</strong>：我們不只販售硬體，更提供針對產線痛點的解決方案。</li>
</ul>

<h3>台灣製造說明</h3>
<p>{todo("請說明 AP_G 在台灣完成的製程與研發項目（例如組裝、校正、算法、軟體），以及與高德原廠產品的關係")}</p>

<h3>團隊與合作</h3>
<figure class="relative w-full h-[320px] rounded-lg overflow-hidden tech-border-accent shadow-xl bg-gradient-to-br from-navyMain to-slate-700 flex items-center justify-center not-prose"><img src="/assets/img/team.webp" width="1200" height="889" alt="Aperture Science 團隊討論" class="absolute inset-0 w-full h-full object-cover z-10" loading="lazy"><figcaption class="text-white/80 font-tech text-sm tracking-widest uppercase z-0">Aperture Science Team</figcaption></figure>
<p class="mt-6">{todo("可公開的合作案例（應用情境、成效）")}</p>
</div>

<aside class="space-y-6">
<div class="bg-navyLight border border-slate-200 rounded-xl p-6">
<h2 class="font-bold text-navyMain mb-4">公司資料</h2>
<dl class="text-sm text-slate-600 space-y-3">
<div><dt class="text-xs text-slate-400">公司名稱</dt><dd>研楷有限公司<br>Aperture Science Co., Ltd.</dd></div>
<div><dt class="text-xs text-slate-400">成立</dt><dd>2024 年</dd></div>
<div><dt class="text-xs text-slate-400">地址</dt><dd>{ADDRESS}</dd></div>
<div><dt class="text-xs text-slate-400">電話</dt><dd>{PHONE}</dd></div>
</dl>
<a href="/contact/" class="mt-6 block text-center bg-navyMain text-white py-3 rounded-sm font-bold hover:bg-slate-700 transition">聯絡諮詢</a>
</div>
</aside>
</div>
'''
    body += cta(title="想進一步了解？", text="歡迎預約專案諮詢，我們會依您的應用場景提供軟硬體建議。", topic="General Inquiry")
    body += footer()
    write("/about/", h + body, "0.8")


# ------------------------------------------------------------- PRODUCTS
SERIES = [
    ("apex-series", "APEX 系列", "業界最高靈敏度", "HIGH NETD · 15mK",
     "業界最高靈敏度——採用業界頂尖 15mK 超高靈敏度感測核心，能精準捕捉微小溫差，適用於半導體熱點排查、電力設備巡檢與精密研發實驗室。"),
    ("e-series", "E 系列", "入門巡檢", "ENTRY",
     "入門巡檢型手持式熱像儀，適合日常設備巡檢與基礎維護。"),
    ("h-series", "H 系列", "電力維護", "POWER MAINTENANCE",
     "針對電力設備維護情境的手持式熱像儀。"),
    ("pt-series", "PT 系列", "旗艦高溫監控", "HIGH TEMPERATURE",
     "旗艦級高溫監控型熱像儀，適合高溫製程與設備的溫度監測。"),
    ("ap-g", "AP_G 系列", "台灣自有品牌", "MADE IN TAIWAN",
     "研楷在地化生產的泛用型手持式熱像儀系列，並提供 OEM 與客製規格開發。"),
]


def products_index():
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("產品方案", "/products/")])
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "url": f"{SITE}/products/{s}/"}
             for i, (s, n, *_rest) in enumerate(SERIES)]
    ld = [bc_ld, {"@context": "https://schema.org", "@type": "ItemList", "name": "研楷手持式熱像儀產品系列",
                  "itemListElement": items}]
    h = head("產品方案：手持式熱像儀、AI 影像分析與工業儀器",
             "研楷產品方案總覽：高德智感 Guide Sensmart 授權的 APEX、E、H、PT 手持式熱像儀系列、台灣自有品牌 AP_G、ML/DL 影像分析與工業／半導體儀器。",
             "/products/", ld)
    body = nav("products")
    body += page_header("Solutions & Products / 產品方案", "全方位工業感測矩陣",
                        "整合手持式紅外線熱像技術與 ML／DL 影像分析，為企業打造可靠的「工業之眼」。", bc_html, "tint")
    cards = ""
    for slug, name, pos, badge, desc in SERIES:
        cards += f'''<a href="/products/{slug}/" class="group bg-white rounded-xl border border-slate-200 shadow-sm hover:shadow-md hover:border-navyMain transition p-7 flex flex-col">
<span class="self-start bg-navyMain/5 text-navyMain text-[10px] font-bold px-2.5 py-1 font-tech tracking-wider rounded mb-4">{badge}</span>
<h3 class="text-xl font-bold text-navyMain mb-1">{name}</h3>
<div class="text-sm text-slate-400 mb-3">{pos}</div>
<p class="text-sm text-slate-600 leading-relaxed mb-6 flex-1">{desc}</p>
<span class="text-sm font-bold text-navyMain">規格與適用場景 <i class="fas fa-arrow-right ml-1 text-xs group-hover:translate-x-1 transition"></i></span>
</a>'''
    body += f'''<div class="max-w-7xl mx-auto px-6 py-16">
<h2 class="text-2xl font-bold text-navyMain mb-2">手持式紅外線熱像儀</h2>
<p class="text-slate-600 mb-8 max-w-3xl">高德智感（Guide Sensmart）授權的 APEX、E、H、PT 系列，加上研楷自有品牌 AP_G，涵蓋入門巡檢到高靈敏度研發檢測。</p>
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">{cards}</div>

<h2 class="text-2xl font-bold text-navyMain mt-16 mb-6">系列對照</h2>
<div class="overflow-x-auto rounded-xl border border-slate-200 bg-white">
<table class="spec-table min-w-[640px]">
<thead><tr class="bg-navyLight"><th class="!w-auto">系列</th><th class="!w-auto">定位</th><th class="!w-auto">適合情境</th><th class="!w-auto">頁面</th></tr></thead>
<tbody>
<tr><td><strong>APEX</strong></td><td>業界最高靈敏度（15mK NETD）</td><td>半導體熱點排查、精密研發、電力巡檢</td><td><a class="text-navyMain underline" href="/products/apex-series/">查看</a></td></tr>
<tr><td><strong>E</strong></td><td>入門巡檢</td><td>日常設備巡檢、基礎維護</td><td><a class="text-navyMain underline" href="/products/e-series/">查看</a></td></tr>
<tr><td><strong>H</strong></td><td>電力維護</td><td>配電與電力設備維護</td><td><a class="text-navyMain underline" href="/products/h-series/">查看</a></td></tr>
<tr><td><strong>PT</strong></td><td>旗艦高溫監控</td><td>高溫製程與設備監測</td><td><a class="text-navyMain underline" href="/products/pt-series/">查看</a></td></tr>
<tr><td><strong>AP_G</strong></td><td>台灣自有品牌、可客製</td><td>泛用巡檢、OEM 與特殊規格需求</td><td><a class="text-navyMain underline" href="/products/ap-g/">查看</a></td></tr>
</tbody></table>
</div>
<p class="text-xs text-slate-400 mt-3">各系列詳細規格請參閱各系列頁面，或洽顧問團隊取得原廠規格書。</p>

<h2 class="text-2xl font-bold text-navyMain mt-16 mb-6">其他方案</h2>
<div class="grid md:grid-cols-2 gap-8">
<a href="/products/instruments/" class="group flex gap-6 bg-white rounded-xl border border-slate-200 hover:border-navyMain hover:shadow-md transition p-6">
<img src="/assets/img/benchtop-xray-ir-illustration.webp" width="1200" height="718" alt="桌上型量測與穿透式儀器示意圖" class="w-36 h-28 object-cover rounded-lg bg-slate-100" loading="lazy">
<div><h3 class="font-bold text-navyMain text-lg mb-2">工業／半導體儀器</h3><p class="text-sm text-slate-600 leading-relaxed">桌上型精密量測、穿透式 X-ray &amp; IR 檢測與 X 光設備品保工具。</p></div>
</a>
<a href="/ai-inspection/" class="group flex gap-6 bg-white rounded-xl border border-slate-200 hover:border-navyMain hover:shadow-md transition p-6">
<img src="https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&amp;fit=crop&amp;q=80&amp;w=800" width="800" height="533" alt="ML／DL 影像分析" class="w-36 h-28 shrink-0 object-cover rounded-lg" loading="lazy">
<div><h3 class="font-bold text-navyMain text-lg mb-2">ML／DL 影像分析服務</h3><p class="text-sm text-slate-600 leading-relaxed">晶圓缺陷識別、熱場模擬、焊接與封裝檢測等客製化視覺分析。</p></div>
</a>
</div>
</div>
'''
    body += cta()
    body += footer()
    write("/products/", h + body, "0.9")


def series_page(slug, name, pos, badge, summary, scenarios, rows, tips, faqs, known_note=None,
                image=True, extra_html="", brand="Guide Sensmart", product_ld_extra=None, official=None):
    path = f"/products/{slug}/"
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("產品方案", "/products/"), (name, path)])
    prod = {
        "@context": "https://schema.org", "@type": "Product",
        "name": f"{name} 手持式紅外線熱像儀", "category": "手持式紅外線熱像儀",
        "description": summary,
        "brand": {"@type": "Brand", "name": brand},
        "url": SITE + path,
        "seller": {"@id": SITE + "/#org"},
    }
    if product_ld_extra:
        prod.update(product_ld_extra)
    ld = [bc_ld, prod, faq_ld(faqs)]
    h = head(f"{name}｜{pos}手持式熱像儀", summary, path, ld)
    body = nav("products")
    body += page_header(f"Handheld Thermal Camera / {badge}", f"{name}：{pos}", summary, bc_html, "tint")
    scen = "".join(f"<li>{s}</li>" for s in scenarios)
    tip_html = "".join(f"<li>{t}</li>" for t in tips)
    img = ""
    if image:
        img = ('<figure class="rounded-2xl overflow-hidden bg-black shadow-lg mb-8">'
               '<img src="/assets/img/guide-handheld.webp" width="1200" height="675" '
               'alt="Guide 手持式紅外線熱像儀（示意）" class="w-full h-auto" loading="lazy">'
               '<figcaption class="text-xs text-white/60 px-4 py-2 bg-black">產品外觀示意，實際外觀依型號而異。</figcaption></figure>')
    note = f'<p class="text-xs text-slate-400 mt-3">{known_note}</p>' if known_note else ""
    off = (f'<a href="{official[0]}" target="_blank" rel="noopener noreferrer" class="mt-4 block text-center border border-navyMain text-navyMain py-4 rounded-sm font-bold hover:bg-navyMain hover:text-white transition">'
           f'{official[1]} <i class="fas fa-external-link-alt text-xs ml-1"></i></a>') if official else ""
    body += f'''<div class="max-w-7xl mx-auto px-6 py-16 grid lg:grid-cols-5 gap-14">
<div class="lg:col-span-3 prose-as">
{answer_box(summary)}
<h2 class="text-2xl font-bold text-navyMain mb-4">適用場景</h2>
<ul>{scen}</ul>
<h3>選型時建議確認</h3>
<ul>{tip_html}</ul>
{extra_html}
<h3>常見問題</h3>
<div class="not-prose">{faq_block(faqs)}</div>
</div>
<aside class="lg:col-span-2">
{img}
<div class="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
<div class="px-6 py-4 bg-navyMain text-white font-bold">{name} 規格摘要</div>
{spec_table(rows)}
</div>
{note}
<a href="/contact/?topic=Hardware%20Inquiry&amp;product={name.replace(" ", "%20")}" class="mt-6 block text-center bg-navyMain text-white py-4 rounded-sm font-bold hover:bg-slate-700 transition">詢問 {name} 報價與規格書</a>
{off}
</aside>
</div>
'''
    body += cta(product=name.replace(" ", "%20"))
    body += footer()
    write(path, h + body, "0.8")


def products_series():
    common_rows = lambda res, netd: [
        ("解析度 Resolution", res), ("熱靈敏度 NETD", netd), ("測溫範圍", None), ("測溫精度", None),
        ("幀率", None), ("鏡頭／視場角", None), ("顯示螢幕", None), ("電池續航", None),
        ("防護等級", None), ("認證", None), ("隨附軟體", None), ("保固", None)]

    series_page(
        "apex-series", "APEX 系列", "業界最高靈敏度", "HIGH NETD",
        "業界最高靈敏度——高德智感（Guide Sensmart）授權的手持式熱像儀，採用業界頂尖 15mK 超高靈敏度感測核心，能精準捕捉微小溫差，"
        "適用於半導體熱點排查、電力設備巡檢與精密研發實驗室。解析度 1280×1024。",
        ["半導體封裝、載板與板級熱點排查", "電力設備巡檢（變壓器、開關櫃、接點）", "精密研發實驗室的熱散布與溫升驗證"],
        common_rows("1280 × 1024 px", "15 mK"),
        ["<strong>解析度與目標大小</strong>：目標越小，越需要高解析度搭配合適鏡頭，才能在可用距離內取得足夠像素。",
         "<strong>NETD</strong>：低 NETD 有助於分辨微小溫差，適合低對比目標，例如半導體熱點。",
         "<strong>鏡頭選配</strong>：是否需要微距或望遠鏡頭，取決於您的檢測距離與目標尺寸。",
         "<strong>報告與資料輸出</strong>：確認隨附軟體能否輸出符合貴單位格式的檢測報告。"],
        [("APEX 系列的 NETD 與解析度是多少？",
          "依現有官方網站資訊，APEX 系列 NETD 為 15 mK，解析度為 1280×1024 像素。正式規格以原廠規格書與報價單為準。", True),
         ("APEX 系列適合做半導體熱點檢測嗎？",
          "高解析度與低 NETD 的組合適合小目標、低對比的熱點檢測，但實際效果還取決於鏡頭、檢測距離與表面發射率，建議先提供樣品與情境，由顧問評估。", True)],
        known_note="解析度與 NETD 數值依現有官方網站資訊；其餘規格待原廠資料確認。",
        official=("https://www.guideir.cn/", "高德智感原廠官網"))

    series_page(
        "e-series", "E 系列", "入門巡檢", "ENTRY",
        "E 系列是高德智感（Guide Sensmart）授權的入門巡檢型手持式熱像儀，適合日常設備巡檢與基礎維護。",
        ["廠區與設施的日常設備巡檢", "馬達、軸承、配電箱等的基礎溫度檢查", "預算有限、先建立熱像巡檢流程的團隊"],
        common_rows(None, None),
        ["<strong>解析度是否夠用</strong>：在您的巡檢距離下，目標設備是否能被清楚辨識。",
         "<strong>測溫範圍</strong>：是否涵蓋您常見設備的實際工作溫度。",
         "<strong>隨附軟體</strong>：是否能快速產出巡檢報告，方便交接與留存。",
         "<strong>未來升級</strong>：若之後需要更高解析度或更低 NETD，可評估 H 或 APEX 系列。"],
        [("E 系列和 H 系列、APEX 系列怎麼選？",
          "E 系列定位為入門巡檢；H 系列針對電力維護；APEX 系列則以高靈敏度與高解析度為主。建議依檢測目標大小、對溫差的要求與預算選擇，或直接聯絡顧問協助選型。", True)])

    series_page(
        "h-series", "H 系列", "電力維護", "POWER MAINTENANCE",
        "H 系列是高德智感（Guide Sensmart）授權、針對電力維護情境的手持式熱像儀，適合配電與電力設備的熱像巡檢。",
        ["變壓器、開關櫃、斷路器與匯流排接點檢測", "電纜終端與接頭的過熱檢查", "電力機房與配電室的定期巡檢"],
        common_rows(None, None),
        ["<strong>測溫範圍與精度</strong>：電力設備的判讀仰賴準確的溫度數值。",
         "<strong>鏡頭視場角</strong>：配電設備常需保持安全距離，需確認是否有望遠鏡頭可選。",
         "<strong>防護等級與電池續航</strong>：影響戶外與長時間巡檢的實用性。",
         "<strong>報告輸出</strong>：確認是否能輸出符合貴單位格式的巡檢報告。"],
        [("H 系列可以用於電力設備的定期巡檢嗎？",
          "H 系列定位為電力維護用途，適合納入定期巡檢流程。判定標準請依貴單位或主管機關規範，建議搭配趨勢紀錄與同類設備相間比較。", True)])

    series_page(
        "pt-series", "PT 系列", "旗艦高溫監控", "HIGH TEMPERATURE",
        "PT 系列是高德智感（Guide Sensmart）授權的旗艦級高溫監控型熱像儀，適合高溫製程與設備的溫度監測。",
        ["高溫製程與爐體周邊設備的溫度監測", "高溫設備的狀態巡檢與異常預警", "需要較高測溫上限的工業現場"],
        common_rows(None, None),
        ["<strong>溫度量程上限</strong>：確認涵蓋您實際製程的最高溫度。",
         "<strong>高溫段的測溫精度與校正</strong>：高溫範圍的精度規格可能與常溫段不同。",
         "<strong>量程切換與濾鏡</strong>：是否需要特殊濾鏡或量程設定來避免飽和。",
         "<strong>現場環境</strong>：粉塵、高溫輻射與防護等級的需求。"],
        [("PT 系列的最高測溫是多少？",
          "詳細測溫範圍請以原廠規格書為準，歡迎聯絡顧問索取並協助評估是否符合您的製程溫度。", False)])

    ap_g_extra = f'''<h3>台灣製造說明</h3>
<p>AP_G 由研楷在地化生產，針對工業巡檢、設備維護與現場快速診斷需求設計，並提供在地技術支援與 OEM 客製化開發。</p>
<p>{todo("請說明在台灣完成的製程與研發項目，以及使用的感測器／核心來源，確保『台灣製造』標示有據可循")}</p>'''
    series_page(
        "ap-g", "AP_G 系列", "台灣自有品牌", "MADE IN TAIWAN",
        "AP_G 是研楷自有品牌的泛用型手持式熱像儀系列，在台灣生產製造，針對工業巡檢、設備維護與現場快速診斷設計，並提供 OEM 與客製規格開發。",
        ["工業巡檢與設備維護的泛用型需求", "現場快速診斷", "需要特殊規格或品牌客製的 OEM 專案"],
        common_rows(None, None),
        ["<strong>是否需要客製規格</strong>：解析度、外殼、介面或軟體功能是否需調整。",
         "<strong>在地服務</strong>：維修、校正與技術支援的流程與時程。",
         "<strong>數量與交期</strong>：OEM 專案需確認最小訂購量與開發時程。"],
        [("AP_G 系列提供客製化嗎？", "提供。AP_G 支援 OEM 與客製規格開發，歡迎提供您的需求規格與預估數量，由顧問團隊評估。", True),
         ("AP_G 與高德智感原廠產品有什麼不同？",
          f'{todo("請說明定位差異")}', False)],
        extra_html=ap_g_extra, image=False, brand="AP_G")


def instruments():
    path = "/products/instruments/"
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("產品方案", "/products/"), ("工業／半導體儀器", path)])
    ld = [bc_ld]
    h = head("工業／半導體儀器：桌上型量測、穿透式 X-ray & IR 與 X 光品保工具",
             "研楷提供桌上型精密量測、穿透式 X-ray & IR 無損檢測儀器，以及針對半導體封裝與 X 光設備的標準化校正、劑量監測與影像品保測試工具。",
             path, ld)
    body = nav("products")
    body += page_header("Category / 儀器設備", "工業／半導體儀器類別",
                        "專為產線與實驗室打造的高精度量測與無損檢測儀器，以及設備品保工具。", bc_html, "tint")
    body += f'''<div class="max-w-7xl mx-auto px-6 py-16 space-y-16">
<section class="grid md:grid-cols-2 gap-12 items-center">
<figure class="rounded-2xl overflow-hidden bg-slate-100 border border-slate-200">
<img src="/assets/img/benchtop-xray-ir-illustration.webp" width="1200" height="718" alt="桌上型量測與穿透式 X-ray 與 IR 儀器示意圖" class="w-full h-auto" loading="lazy">
<figcaption class="text-xs text-slate-400 px-4 py-2 bg-white">示意圖 Illustration，非實際機型外觀。</figcaption>
</figure>
<div class="prose-as">
<h2 class="text-2xl font-bold text-navyMain mb-4">桌上型量測與穿透式儀器（X-ray &amp; IR）</h2>
<p>專為產線與實驗室打造的高精度穿透式無損點檢儀器，適合高負載、高幀率動態與高精密熱點檢測。</p>
<ul><li>適用領域：實驗室特規高精度、高幀率動態分析</li></ul>
<p>{todo("機型、規格與可公開的應用案例")}</p>
</div>
</section>

<section class="grid md:grid-cols-2 gap-12 items-center">
<div class="prose-as md:order-1">
<h2 class="text-2xl font-bold text-navyMain mb-4">X 光設備品保工具</h2>
<p>針對半導體封裝與工業級 X-ray 設備，提供標準化校正、劑量監測與影像品保測試工具，確保量測穩定性。</p>
<ul><li>適用領域：半導體 NPI 階段、設備精度校正</li></ul>
<p>{todo("工具型號與規格")}</p>
</div>
<figure class="rounded-2xl overflow-hidden bg-white border border-slate-200 md:order-2">
<img src="/assets/img/tld-dosimeter.webp" width="470" height="205" alt="TLD 劑量計等品保工具範例" class="w-full h-auto" loading="lazy">
<figcaption class="text-xs text-slate-400 px-4 py-2">品保工具範例（TLD 劑量計）。</figcaption>
</figure>
</section>
</div>
'''
    body += cta(title="需要儀器選型或規格諮詢？", topic="Hardware Inquiry", product="工業半導體儀器")
    body += footer()
    write(path, h + body, "0.7")


def run():
    home(); about(); products_index(); products_series(); instruments()
