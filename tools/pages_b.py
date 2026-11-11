# -*- coding: utf-8 -*-
from lib import *


PHOTOS = {
    "fa-microchip": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&amp;fit=crop&amp;q=80&amp;w=600",
    "fa-bolt": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&amp;fit=crop&amp;q=80&amp;w=600",
    "fa-flask": "https://images.unsplash.com/photo-1581092160562-40aa08e78837?auto=format&amp;fit=crop&amp;q=80&amp;w=600",
}


def industry_card(href, icon, grad, title, desc):
    return f'''<a href="{href}" class="group block bg-white rounded-xl border border-slate-200 overflow-hidden hover:border-navyMain hover:shadow-md transition">
<div class="overflow-hidden"><img src="{PHOTOS[icon]}" width="600" height="400" alt="{title}" class="h-56 w-full object-cover group-hover:scale-105 transition duration-500" loading="lazy"></div>
<div class="p-7"><h2 class="font-bold text-navyMain text-xl mb-3">{title}</h2><p class="text-sm text-slate-600 leading-relaxed mb-5">{desc}</p>
<span class="text-sm font-bold text-navyMain">了解應用 <i class="fas fa-arrow-right ml-1 text-xs group-hover:translate-x-1 transition"></i></span></div>
</a>'''


def industries_index():
    path = "/industries/"
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("產業應用", path)])
    h = head("產業應用：半導體、智慧能源與研發實驗室的熱像檢測",
             "研楷提供半導體熱點排查、電力與儲能設施巡檢，以及研發實驗室熱散布驗證的熱像檢測與 AI 影像分析方案。", path, [bc_ld])
    body = nav("industries")
    body += page_header("Target Industries / 產業應用", "跨足尖端領域的精密監測",
                        "從晶圓封裝到電力設備，從研發驗證到產線巡檢，依場景選擇合適的熱像方案。", bc_html, "tint")
    body += f'''<div class="max-w-7xl mx-auto px-6 py-16 grid md:grid-cols-3 gap-8">
{industry_card("/industries/semiconductor/", "fa-microchip", "from-navyMain to-slate-700", "半導體產業", "提供製程中封裝測試與 Wafer 階段的非接觸式溫度 analysis，協助排除潛在熱點異常點檢。")}
{industry_card("/industries/power/", "fa-bolt", "from-slate-700 to-slate-900", "智慧能源", "變壓器、電力機房與儲能設施的 24/7 自動化熱顯巡檢，有效預防過熱引發之災損。")}
{industry_card("/industries/lab/", "fa-flask", "from-navyMain to-slate-600", "研發實驗室", "輔助 NPI（新產品導入）階段的熱散布驗證，協助將實驗數據轉化為工業生產標準。")}
</div>
'''
    body += cta(title="不確定屬於哪個場景？", text="描述您想檢測的對象與現場條件，我們協助判斷適合的機型與流程。", topic="Project Design")
    body += footer()
    write(path, h + body, "0.8")


def industry_page(slug, title, eyebrow, lead, summary, sections, models_html, faqs, desc):
    path = f"/industries/{slug}/"
    short = {"semiconductor": "半導體產業", "power": "智慧能源與電力", "lab": "研發實驗室"}[slug]
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("產業應用", "/industries/"), (short, path)])
    ld = [bc_ld, faq_ld(faqs),
          {"@context": "https://schema.org", "@type": "Service", "name": title, "serviceType": "紅外線熱像檢測",
           "provider": {"@id": SITE + "/#org"}, "areaServed": "TW", "description": desc}]
    h = head(title, desc, path, ld)
    body = nav("industries")
    body += page_header(eyebrow, title, lead, bc_html, "tint")
    body += f'''<div class="max-w-4xl mx-auto px-6 py-16 prose-as">
{answer_box(summary)}
{sections}
<h3>建議機型與方案</h3>
{models_html}
<h3>常見問題</h3>
{faq_block(faqs)}
</div>
'''
    body += cta(topic="Project Design")
    body += footer()
    write(path, h + body, "0.8")


def industries():
    industries_index()

    industry_page(
        "semiconductor", "半導體熱點檢測與熱像分析", "Semiconductor / 半導體產業",
        "提供製程中封裝測試與 Wafer 階段的非接觸式溫度 analysis，協助排除潛在熱點異常點檢。",
        "半導體應用的目標通常很小、溫差也很小，選擇熱像儀時應優先看解析度、NETD 與鏡頭（含微距）。"
        "研楷提供 15mK NETD 的 APEX 系列、可客製的 AP_G，以及結合 AI 的缺陷識別與熱場分析服務。",
        f'''<h2 class="text-2xl font-bold text-navyMain mb-4">常見檢測情境</h2>
<ul>
<li>封裝與載板的熱點排查</li>
<li>老化測試（burn-in）與測試座的溫度分布檢查</li>
<li>電源與功率元件的溫升驗證</li>
<li>PCB 與模組的板級熱點定位</li>
<li>設備腔體與載台的溫度均勻性確認</li>
</ul>
<h3>為什麼解析度與 NETD 特別重要</h3>
<p>半導體元件尺寸小，若解析度或鏡頭不足，單一像素會涵蓋過大面積，測到的是平均溫度而不是真正的熱點。同時，異常往往只比周圍高出少許，需要低 NETD 才能把微小溫差從雜訊中分辨出來。</p>
<h3>判讀時的注意事項</h3>
<ul>
<li><strong>發射率</strong>：金屬與封裝材料的發射率差異大，設定不當會造成測溫偏差。</li>
<li><strong>反射干擾</strong>：光亮表面容易反射周圍熱源，需注意檢測角度與環境。</li>
<li><strong>對焦與距離</strong>：目標越小，對焦與檢測距離對結果影響越明顯。</li>
<li><strong>環境穩定</strong>：氣流與背景溫度變化會影響讀值，建議固定條件做比較。</li>
</ul>
<h3>延伸：結合 AI 影像分析</h3>
<p>除了人工判讀，我們也提供 ML／DL 影像分析，涵蓋晶圓缺陷識別與複雜封裝熱場模擬，詳見 <a class="text-navyMain underline" href="/ai-inspection/">ML／DL 影像分析服務</a>。</p>''',
        '''<ul>
<li><a class="text-navyMain underline" href="/products/apex-series/">APEX 系列</a>：15mK NETD、1280×1024 解析度，適合小目標與低對比熱點。</li>
<li><a class="text-navyMain underline" href="/products/ap-g/">AP_G 系列</a>：需要特殊規格或客製時的選擇。</li>
<li><a class="text-navyMain underline" href="/products/instruments/">桌上型與穿透式儀器</a>：產線與實驗室的高精度、高幀率檢測。</li>
</ul>''',
        [("半導體熱點檢測要看熱像儀的哪些規格？",
          "優先看解析度、NETD 與鏡頭選配（尤其是微距），其次是幀率與資料輸出方式。目標越小、溫差越小，這些規格的影響越大。", True),
         ("熱像儀的測溫會受到材料影響嗎？",
          "會。不同材料的發射率不同，光亮的金屬表面還會反射環境熱輻射，需要正確設定發射率並注意檢測條件，才能得到可靠的溫度數值。", True)],
        "研楷提供半導體封裝測試與 Wafer 階段的熱點檢測方案：高靈敏度手持式熱像儀（APEX 15mK）、AP_G 客製機型與 AI 缺陷識別服務。")

    industry_page(
        "power", "電力與儲能設施熱像巡檢", "Smart Energy / 智慧能源與電力",
        "變壓器、電力機房與儲能設施的 24/7 自動化熱顯巡檢，有效預防過熱引發之災損。",
        "電力設備的異常常以局部溫升的形式先出現，熱像巡檢能在不停機、不接觸的情況下找出過熱的接點與元件。"
        "研楷提供 H 系列（電力維護）、PT 系列（高溫監控）與 APEX 系列，並可搭配定點巡檢方案。",
        f'''<h2 class="text-2xl font-bold text-navyMain mb-4">常見檢測標的</h2>
<ul>
<li>變壓器本體、套管與接點</li>
<li>開關櫃、斷路器與匯流排接頭</li>
<li>電纜終端與連接處</li>
<li>電力機房與 UPS、配電盤</li>
<li>儲能設施的電池櫃與電力轉換設備</li>
</ul>
<h3>巡檢的實務要點</h3>
<ul>
<li><strong>在足夠負載下檢測</strong>：負載太低時，接觸不良的溫升可能不明顯。</li>
<li><strong>設定發射率並注意反射</strong>：金屬表面反射強，需調整角度與設定，必要時使用高發射率標記。</li>
<li><strong>同類設備比較</strong>：比較三相或相同設備的溫差，比單看絕對溫度更容易發現異常。</li>
<li><strong>留存紀錄看趨勢</strong>：定期拍攝同一位置，才能觀察溫升是否持續擴大。</li>
<li><strong>判定標準依規範</strong>：警戒與處置標準請依貴單位或主管機關規定。</li>
</ul>
<h3>安全提醒</h3>
<p>熱像檢測是非接觸量測，但開啟盤面或接近帶電設備仍須遵守電業與現場安全規定。</p>
<h3>手持與定點巡檢</h3>
<p>手持式適合定期人工巡檢；若需要 24 小時持續監控，可評估定點式巡檢方案。{todo("定點／自動化巡檢方案的實際產品與規格")}</p>''',
        '''<ul>
<li><a class="text-navyMain underline" href="/products/h-series/">H 系列</a>：電力維護情境。</li>
<li><a class="text-navyMain underline" href="/products/pt-series/">PT 系列</a>：高溫設備與較高測溫上限需求。</li>
<li><a class="text-navyMain underline" href="/products/apex-series/">APEX 系列</a>：需要更高解析度與靈敏度的精細檢測。</li>
</ul>''',
        [("電力設備熱像巡檢多久做一次比較合適？",
          "頻率依設備重要性、負載變化與貴單位規範而定。建議先建立基準影像，再依風險等級排定週期，並保留紀錄觀察趨勢。", True),
         ("熱像儀可以取代停機檢測嗎？",
          "不能完全取代。熱像儀能在運轉中快速找出過熱位置，適合作為篩檢與預防維護工具，後續仍需依異常情況安排進一步的檢修。", True)],
        "研楷提供變壓器、電力機房與儲能設施的手持式熱像巡檢方案，涵蓋 H 系列電力維護、PT 系列高溫監控與 APEX 高靈敏度機型。")

    industry_page(
        "lab", "研發實驗室熱散布驗證", "R&D Laboratory / 研發實驗室",
        "輔助 NPI（新產品導入）階段的熱散布驗證，協助將實驗數據轉化為工業生產標準。",
        "在研發與新產品導入階段，熱像儀可以快速呈現樣品的溫度分布與熱路徑，縮短設計驗證時間。"
        "研楷提供高靈敏度的 APEX 系列、可客製的 AP_G，以及高幀率動態分析的桌上型儀器。",
        f'''<h2 class="text-2xl font-bold text-navyMain mb-4">常見應用</h2>
<ul>
<li>新產品與電路板的熱散布驗證</li>
<li>原型機的溫升測試與散熱設計比較</li>
<li>異質材料界面的熱傳導觀察</li>
<li>高幀率動態熱事件的紀錄與分析</li>
</ul>
<h3>實驗室選型重點</h3>
<ul>
<li><strong>解析度與微距能力</strong>：決定能看到多小的細節。</li>
<li><strong>NETD</strong>：決定能分辨多小的溫差。</li>
<li><strong>幀率</strong>：動態熱事件需要足夠的取樣速度。</li>
<li><strong>資料輸出與整合</strong>：原始資料能否匯出，供後續分析或自有程式使用。{todo("SDK／資料格式說明")}</li>
</ul>
<h3>從實驗數據到量產標準</h3>
<p>搭配 ML／DL 影像分析，可以把實驗階段的判讀規則轉為自動化檢測流程，延伸到產線使用，詳見 <a class="text-navyMain underline" href="/ai-inspection/">ML／DL 影像分析服務</a>。</p>''',
        '''<ul>
<li><a class="text-navyMain underline" href="/products/apex-series/">APEX 系列</a>：高靈敏度手持式熱像儀。</li>
<li><a class="text-navyMain underline" href="/products/ap-g/">AP_G 系列</a>：特殊規格與客製需求。</li>
<li><a class="text-navyMain underline" href="/products/instruments/">桌上型量測與穿透式儀器</a>：高精度、高幀率動態分析。</li>
</ul>''',
        [("研發階段為什麼需要熱像儀？",
          "熱像儀能一次呈現整個樣品的溫度分布，快速找出熱點與散熱瓶頸，比單點接觸式量測更有效率，也方便在不同設計版本之間做比較。", True)],
        "研楷提供研發實驗室與 NPI 階段的熱散布驗證方案：高靈敏度熱像儀、客製規格與高幀率桌上型儀器，並可延伸至 AI 自動化檢測。")


# ----------------------------------------------------------------- AI
def ai():
    path = "/ai-inspection/"
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("ML／DL 影像分析", path)])
    items = [
        ("Spot and Seam Welding Inspection", "點焊與縫焊檢測"),
        ("Material Quality Inspection / Detection", "材料品質檢測"),
        ("Glue Bead Inspection and Measurement", "膠線檢測與量測"),
        ("Packaging Label Inspection & Quality Verification", "包裝標籤檢測與品質驗證"),
        ("Product Seal Integrity & Packaging Quality Verification", "產品封口完整性與包裝品質驗證"),
        ("Packaging Integrity and Inspection", "包裝完整性檢測"),
        ("PCB Inspection and Quality Control", "PCB 檢測與品質管制"),
        ("Welding Inspection", "焊接檢測"),
    ]
    cards = "".join(
        f'<div class="bg-white p-5 rounded-xl border border-slate-100 flex items-start space-x-3">'
        f'<span class="w-1.5 h-1.5 bg-navyMain rounded-full mt-2 flex-shrink-0"></span>'
        f'<div><div class="text-navyText text-sm font-medium">{zh}</div><div class="text-xs text-slate-400">{en}</div></div></div>'
        for en, zh in items)
    ld = [bc_ld, {"@context": "https://schema.org", "@type": "Service", "name": "ML／DL 工業影像分析服務",
                  "serviceType": "工業視覺檢測與缺陷識別", "provider": {"@id": SITE + "/#org"}, "areaServed": "TW",
                  "description": "結合深度學習的工業視覺自動化分析，涵蓋晶圓缺陷識別、複雜封裝熱場模擬、異質材料界面熱傳導分析與客製化軟體整合。"}]
    h = head("ML／DL 影像分析服務：晶圓缺陷識別、熱場模擬與工業視覺檢測",
             "研楷提供結合深度學習的工業視覺檢測服務：晶圓缺陷識別、複雜封裝熱場模擬、異質材料界面熱傳導分析，以及焊接、膠線、封裝與 PCB 檢測。",
             path, ld)
    body = nav("ai")
    body += page_header("Advanced Analytics / 人工智慧服務", "ML／DL 影像分析服務",
                        "自主研發的深度學習核心算法，提供高維度工業視覺自動化分析，優化產線良率與缺陷點檢。", bc_html, "tint")
    body += f'''<div class="max-w-5xl mx-auto px-6 py-16">
{answer_box("研楷的 ML／DL 影像分析服務把深度學習用在工業視覺檢測，涵蓋晶圓缺陷識別、複雜封裝熱場模擬、異質材料界面熱傳導分析與客製化軟體整合，"
            "可搭配熱像儀資料，也可處理一般視覺影像。")}
<h2 class="text-2xl font-bold text-navyMain mb-6">服務項目</h2>
<ul class="prose-as mb-10">
<li><strong>晶圓缺陷識別</strong></li>
<li><strong>複雜封裝熱場模擬</strong></li>
<li><strong>異質材料界面熱傳導分析</strong></li>
<li><strong>客製化軟體整合</strong></li>
</ul>
<div class="p-8 bg-navyLight border border-slate-200 rounded-2xl">
<div class="flex items-center space-x-5 mb-6 pb-5 border-b border-slate-200">
<div class="w-14 h-14 bg-navyMain text-white rounded-xl flex items-center justify-center text-xl shadow-md"><i class="fas fa-brain"></i></div>
<div><h2 class="text-xl font-bold text-navyMain">智慧製造核心視覺檢測矩陣</h2><div class="text-xs text-slate-400 uppercase tracking-wider mt-1">Semi Application &amp; Lab Application Related</div></div>
</div>
<div class="grid md:grid-cols-2 gap-4">{cards}</div>
</div>

<h2 class="text-2xl font-bold text-navyMain mt-14 mb-6">合作流程</h2>
<ol class="grid md:grid-cols-4 gap-5 text-sm">
<li class="p-5 bg-white border border-slate-200 rounded-xl"><div class="font-tech text-navyMain mb-2">01</div><strong class="text-navyMain">需求訪談</strong><p class="text-slate-500 mt-2">釐清檢測對象、缺陷定義與目標指標。</p></li>
<li class="p-5 bg-white border border-slate-200 rounded-xl"><div class="font-tech text-navyMain mb-2">02</div><strong class="text-navyMain">樣本與資料</strong><p class="text-slate-500 mt-2">收集影像樣本並標註缺陷類型。</p></li>
<li class="p-5 bg-white border border-slate-200 rounded-xl"><div class="font-tech text-navyMain mb-2">03</div><strong class="text-navyMain">模型開發驗證</strong><p class="text-slate-500 mt-2">訓練模型並以實際樣本驗證效果。</p></li>
<li class="p-5 bg-white border border-slate-200 rounded-xl"><div class="font-tech text-navyMain mb-2">04</div><strong class="text-navyMain">部署與整合</strong><p class="text-slate-500 mt-2">整合至現有設備、產線或軟體流程。</p></li>
</ol>
<p class="mt-4">{todo("請確認上述合作流程是否符合實際作法，並補充可公開的案例與成效數據")}</p>
</div>
'''
    body += cta(title="想了解 AI 影像分析能否解決您的檢測問題？",
                text="提供您的檢測對象與目前痛點，我們會評估可行性與合作方式。", topic="Software Development")
    body += footer()
    write(path, h + body, "0.8")


# ---------------------------------------------------------------- FAQ
FAQ_ALL = [
    ("研楷與高德智感、高德紅外是什麼關係？",
     "研楷有限公司（Aperture Science Co., Ltd.）為高德智感（Guide Sensmart）的授權代理商。高德智感為高德紅外（Guide Infrared）的全資子公司。"
     "研楷同時開發台灣自有品牌 AP_G 系列。", True),
    ("NETD 是什麼？數字越小越好嗎？",
     "NETD（噪聲等效溫差）代表熱像儀能分辨的最小溫差，單位通常為 mK。數字越小，對微小溫差越敏感。"
     "但它只是其中一項指標，還需搭配解析度、鏡頭與使用距離一起評估。", True),
    ("熱像儀的解析度要怎麼選？",
     "依目標大小與檢測距離決定。目標越小或距離越遠，越需要高解析度與合適的鏡頭，才能讓目標佔有足夠像素。"
     "一般設備巡檢可選用較入門的解析度，半導體熱點等小目標則建議高解析度搭配微距鏡頭。", True),
    ("為什麼要設定發射率？",
     "熱像儀測得的是物體發出的紅外輻射，不同材料的發射率不同，光亮的金屬又會反射周圍熱源。發射率設定不正確，溫度讀值就會偏差。", True),
    ("APEX、E、H、PT、AP_G 五個系列怎麼選？",
     "APEX 為高靈敏度、高解析度；E 為入門巡檢；H 為電力維護；PT 為旗艦高溫監控；AP_G 為台灣自有品牌，可客製。"
     "建議依檢測目標大小、溫度範圍與預算選擇，或聯絡顧問協助。", True),
    ("可以只買熱像儀，不用 AI 影像分析嗎？",
     "可以。手持式熱像儀可單獨採購，AI／ML 影像分析是另外提供的選配服務。", True),
    ("支援 OEM 或客製規格嗎？",
     "支援。AP_G 系列提供 OEM 與客製化規格開發，歡迎提供需求與預估數量。", True),
    ("AP_G 在台灣做了哪些製程？與原廠產品有何不同？", todo("請補充 AP_G 的台灣製程與定位差異"), False),
    ("保固與校正怎麼處理？", todo("請補充保固年限、校正週期與送修流程"), False),
    ("隨附軟體是否有中文？可以輸出報告嗎？", todo("請補充軟體語言與報告輸出格式"), False),
    ("如何詢價？交期多久？",
     f'請透過<a class="text-navyMain underline" href="/contact/">聯絡頁</a>填寫需求，或來電 {PHONE}。交期：{todo("請補充一般交期")}', False),
]


def faq():
    path = "/faq/"
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("常見問題", path)])
    ld = [bc_ld, faq_ld(FAQ_ALL)]
    h = head("常見問題：熱像儀選型、NETD、解析度與售後",
             "手持式熱像儀常見問題：NETD 與解析度怎麼選、發射率為什麼重要、APEX／E／H／PT／AP_G 系列差異，以及 OEM、保固與詢價方式。",
             path, ld)
    body = nav("faq")
    body += page_header("FAQ / 常見問題", "熱像儀選型與採購常見問題",
                        "整理買家最常問的規格、選型與服務問題。找不到答案，歡迎直接聯絡我們。", bc_html, "tint")
    body += f'<div class="max-w-4xl mx-auto px-6 py-16">{faq_block(FAQ_ALL)}</div>'
    body += cta(title="還有其他問題？", text="告訴我們您的使用情境，顧問團隊會直接回覆。", topic="General Inquiry")
    body += footer()
    write(path, h + body, "0.7")


# ------------------------------------------------------------- CONTACT
def contact():
    path = "/contact/"
    bc_html, bc_ld = breadcrumbs([("首頁", "/"), ("聯絡諮詢", path)])
    ld = [bc_ld, {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + path,
                  "mainEntity": {"@id": SITE + "/#org"}}]
    h = head("聯絡諮詢：專案諮詢預約", "聯絡研楷有限公司（Aperture Science）：硬體採購、軟體開發、專案設計與售後服務諮詢。電話 "
             + PHONE + "，地址 " + ADDRESS + "。", path, ld)
    body = nav("")
    body += f'''<div class="max-w-7xl mx-auto px-6 pt-12 pb-20">
{bc_html}
<div class="grid md:grid-cols-2 gap-16">
<div>
<h1 class="text-4xl md:text-5xl font-bold text-navyMain mb-6">專案諮詢預約</h1>
<p class="text-slate-600 mb-10 text-lg font-light">Aperture Science 顧問團隊將針對您的應用場景提供專業的軟硬體建議。</p>
<div class="space-y-8">
<div class="flex items-start space-x-5"><div class="w-12 h-12 bg-navyLight rounded flex items-center justify-center text-navyMain border border-slate-200"><i class="fas fa-envelope"></i></div>
<div><div class="text-[10px] text-slate-400 font-tech uppercase">Official Email</div><div class="text-navyText text-xl font-light" data-email>Admin [at] Aperturescience.com.tw</div></div></div>
<div class="flex items-start space-x-5"><div class="w-12 h-12 bg-navyLight rounded flex items-center justify-center text-navyMain border border-slate-200"><i class="fas fa-phone"></i></div>
<div><div class="text-[10px] text-slate-400 font-tech uppercase">Consultant HotLine</div><div class="text-navyText text-xl font-light"><a href="tel:+886933027706">{PHONE}</a></div></div></div>
<div class="flex items-start space-x-5"><div class="w-12 h-12 bg-navyLight rounded flex items-center justify-center text-navyMain border border-slate-200"><i class="fas fa-map-marker-alt"></i></div>
<div><div class="text-[10px] text-slate-400 font-tech uppercase">Headquarters</div><div class="text-navyText text-xl font-light">{ADDRESS}</div></div></div>
</div>
</div>
<div class="bg-white p-8 md:p-10 tech-border-accent rounded-lg shadow-xl border border-slate-100">
<form id="contact-form" class="space-y-6">
<div class="hp-field"><label>如果您是人類，請將此欄位留空：</label><input type="text" id="hp_name" name="hp_name" tabindex="-1" autocomplete="off"></div>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
<input type="text" id="company" required placeholder="公司名稱 / Company" aria-label="公司名稱" class="w-full bg-navyLight border border-slate-200 p-4 text-navyText focus:bg-white focus:border-navyMain outline-none rounded transition placeholder-slate-400">
<input type="text" id="contact_name" required placeholder="聯絡人 / Contact Name" aria-label="聯絡人" class="w-full bg-navyLight border border-slate-200 p-4 text-navyText focus:bg-white focus:border-navyMain outline-none rounded transition placeholder-slate-400">
</div>
<select id="inquiry_type" aria-label="需求類別" class="w-full bg-navyLight border border-slate-200 p-4 text-navyText focus:bg-white focus:border-navyMain outline-none rounded cursor-pointer">
<option value="General Inquiry" selected>請選擇需求類別 / Inquiry Type</option>
<option value="Hardware Inquiry">硬體採購 (Hardware Inquiry)</option>
<option value="Software Development">軟體開發 (Software Development)</option>
<option value="Project Design">專案設計 (Project Design)</option>
<option value="After-sales Service">售後服務 (After-sales Service)</option>
</select>
<input type="email" id="email" required placeholder="電子信箱 / Email Address" aria-label="電子信箱" class="w-full bg-navyLight border border-slate-200 p-4 text-navyText focus:bg-white focus:border-navyMain outline-none rounded transition placeholder-slate-400">
<textarea id="message" rows="4" required placeholder="需求內容描述 / Message Description" aria-label="需求內容" class="w-full bg-navyLight border border-slate-200 p-4 text-navyText focus:bg-white focus:border-navyMain outline-none rounded transition placeholder-slate-400"></textarea>
<div id="form-status" class="hidden text-sm p-4 rounded-sm bg-navyLight text-navyMain border border-slate-200" role="status">正在準備郵件... 系統將自動打開您的電子郵件軟體。</div>
<button type="submit" class="w-full bg-navyMain text-white font-bold py-5 hover:bg-slate-700 transition tracking-[0.2em] uppercase rounded-sm shadow-md">Submit Request / 傳送諮詢</button>
</form>
</div>
</div>
</div>
'''
    body += footer()
    write(path, h + body, "0.8")


# --------------------------------------------------------------- LEGAL
def legal():
    for slug, zh, en, blocks in [
        ("privacy", "隱私權保護政策", "Privacy Policy", [
            ("1. 個人資料之蒐集", "研楷有限公司（以下簡稱本公司）蒐集您的個人資料（如姓名、公司名稱、電話及電子郵件），僅限於提供產品諮詢、專案評估與後續服務之用。除非法律要求或經您授權，我們絕不會將您的資料提供給第三方。"),
            ("2. 資料儲存與安全", "我們致力於確保您的個人資料安全，並採取符合工業標準的加密與防火牆技術，防止未經授權的存取與洩露。"),
            ("3. 使用者權利", "您可以隨時聯絡本公司要求查詢、閱覽、補充或更正您的個人資料，亦可要求停止蒐集或刪除相關資訊。")]),
        ("terms", "服務條款", "Terms of Service", [
            ("1. 產品資訊免責聲明", "本網站所載之產品規格、軟體功能說明與測試數據僅供參考。正式之技術規格與服務範圍，應以本公司簽署之正式報價單（Quotation）或合約文件為準。"),
            ("2. 智慧財產權", "本網站所有內容（包含但不限於文字、圖片、標誌、專利技術描述）均受智慧財產權法保護。未經書面許可，嚴禁任何形式的轉載、重製或商業利用。"),
            ("3. 法律管轄", "本服務條款之解釋與適用，均依中華民國法律為準據。如因本服務產生爭議，合意以台灣桃園地方法院為第一審管轄法院。")]),
    ]:
        path = f"/{slug}/"
        bc_html, bc_ld = breadcrumbs([("首頁", "/"), (zh, path)])
        desc = {"privacy": "研楷有限公司隱私權保護政策：說明本公司蒐集個人資料的範圍與用途、資料儲存與安全措施，以及您查詢、更正或刪除資料的權利。",
                "terms": "研楷有限公司服務條款：說明網站產品資訊免責聲明、智慧財產權保護，以及法律管轄與爭議處理方式。"}[slug]
        h = head(zh, desc, path, [bc_ld])
        body = nav("")
        inner = "".join(f"<h4>{t}</h4><p>{p}</p>" for t, p in blocks)
        body += f'''<div class="max-w-4xl mx-auto px-6 pt-12 pb-20">
{bc_html}
<header class="mb-10 border-b border-slate-200 pb-8">
<h1 class="text-3xl md:text-4xl font-bold text-navyMain mb-3 font-tech uppercase">{en} / <span class="text-slate-500 normal-case">{zh}</span></h1>
<p class="text-slate-400">最後更新日期：2026 年 5 月</p>
</header>
<div class="legal-content">{inner}</div>
<a href="/" class="inline-block mt-12 text-navyMain hover:underline font-bold">← 返回首頁 BACK TO HOME</a>
</div>
'''
        body += footer()
        write(path, h + body, "0.3")


def notfound():
    h = head("找不到頁面", "您要找的頁面不存在或已移動，請回到研楷 Aperture Science 首頁、產品方案或聯絡頁繼續瀏覽。", "/404.html", None, noindex=True)
    body = nav("")
    body += '''<div class="max-w-3xl mx-auto px-6 py-28 text-center">
<div class="font-tech text-6xl text-navyMain mb-6">404</div>
<h1 class="text-3xl font-bold text-navyMain mb-4">找不到這個頁面</h1>
<p class="text-slate-600 mb-10">網站已改版為多頁式，舊的網址可能已移動。請從下列入口繼續：</p>
<div class="flex flex-wrap justify-center gap-4">
<a href="/" class="bg-navyMain text-white px-6 py-3 rounded-sm font-bold">回首頁</a>
<a href="/products/" class="border border-navyMain text-navyMain px-6 py-3 rounded-sm font-bold">產品方案</a>
<a href="/contact/" class="border border-navyMain text-navyMain px-6 py-3 rounded-sm font-bold">聯絡諮詢</a>
</div></div>
'''
    body += footer()
    write("/404.html", h + body, index=False)


def run():
    industries(); ai(); faq(); contact(); legal(); notfound()
