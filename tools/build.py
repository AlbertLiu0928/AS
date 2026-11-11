# -*- coding: utf-8 -*-
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
import lib
import pages_a
import pages_b
from lib import OUT, SITE, LASTMOD, PAGES

pages_a.run()
pages_b.run()

# ---- sitemap.xml
urls = ""
for path, pr in sorted(PAGES, key=lambda x: (-float(x[1]), x[0])):
    urls += (f"<url><loc>{SITE}{path}</loc><lastmod>{LASTMOD}</lastmod>"
             f"<priority>{pr}</priority></url>\n")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")

# ---- robots.txt (AI crawlers explicitly allowed)
robots = """# 研楷 Aperture Science — robots.txt
User-agent: *
Allow: /
Disallow: /legacy/
Disallow: /tools/

# AI / answer-engine crawlers: allowed so product information can be cited.
User-agent: GPTBot
Allow: /
Disallow: /legacy/
Disallow: /tools/

User-agent: OAI-SearchBot
Allow: /
Disallow: /legacy/
Disallow: /tools/

User-agent: ClaudeBot
Allow: /
Disallow: /legacy/
Disallow: /tools/

User-agent: Claude-SearchBot
Allow: /
Disallow: /legacy/
Disallow: /tools/

User-agent: PerplexityBot
Allow: /
Disallow: /legacy/
Disallow: /tools/

User-agent: Google-Extended
Allow: /
Disallow: /legacy/
Disallow: /tools/

Sitemap: https://aperturescience.com.tw/sitemap.xml
"""
open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(robots)

# ---- llms.txt
llms = f"""# 研楷有限公司 Aperture Science Co., Ltd.

> 研楷有限公司（Aperture Science Co., Ltd.）是位於台灣桃園的手持式紅外線熱像儀與 AI/ML 影像分析服務商，為高德智感（Guide Sensmart，高德紅外 Guide Infrared 旗下）授權代理商，並開發台灣自有品牌 AP_G 系列。服務對象：半導體、智慧能源與電力、研發實驗室。

Contact: {lib.PHONE} ・ {lib.ADDRESS} ・ {SITE}/contact/

## 產品
- [產品方案總覽]({SITE}/products/): 手持式熱像儀系列對照與其他方案
- [APEX 系列]({SITE}/products/apex-series/): 高靈敏度（15mK NETD、1280×1024）手持式熱像儀
- [E 系列]({SITE}/products/e-series/): 入門巡檢
- [H 系列]({SITE}/products/h-series/): 電力維護
- [PT 系列]({SITE}/products/pt-series/): 旗艦級高溫監控
- [AP_G 系列]({SITE}/products/ap-g/): 台灣自有品牌，支援 OEM 與客製
- [工業／半導體儀器]({SITE}/products/instruments/): 桌上型量測、穿透式 X-ray & IR、X 光設備品保工具

## 服務
- [ML／DL 影像分析]({SITE}/ai-inspection/): 晶圓缺陷識別、封裝熱場模擬、焊接／膠線／PCB 檢測

## 產業應用
- [半導體熱點檢測]({SITE}/industries/semiconductor/)
- [電力與儲能設施熱像巡檢]({SITE}/industries/power/)
- [研發實驗室熱散布驗證]({SITE}/industries/lab/)

## 公司與支援
- [關於研楷]({SITE}/about/): 公司背景、名稱與品牌說明
- [常見問題]({SITE}/faq/): NETD、解析度、發射率、系列選型
- [聯絡諮詢]({SITE}/contact/)
"""
open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write(llms)

# ---- legacy copy of the original one-page site (noindex, images re-pointed to ../)
# Created once from the pre-redesign commit; never overwritten afterwards.
legacy_fp = os.path.join(OUT, "legacy", "index.html")
if not os.path.exists(legacy_fp):
    src = subprocess.run(["git", "-C", OUT, "show", "157cb30:index.html"],
                         capture_output=True, text=True, check=True).stdout
    src = re.sub(r"(?<![\w/.])Image(\d)\.(jpg|JPG|png)", r"../Image\1.\2", src)
    src = src.replace('<meta charset="UTF-8">',
                      '<meta charset="UTF-8">\n    <meta name="robots" content="noindex, nofollow">\n'
                      '    <link rel="canonical" href="https://aperturescience.com.tw/">', 1)
    os.makedirs(os.path.dirname(legacy_fp), exist_ok=True)
    open(legacy_fp, "w", encoding="utf-8").write(src)

# ---- README
readme = """# 研楷 Aperture Science 官方網站

靜態網站，部署於 GitHub Pages（網域見 `CNAME`）。

## 結構
- `/` 首頁、`/about/`、`/products/`（含各系列）、`/industries/`、`/ai-inspection/`、`/faq/`、`/contact/`
- `assets/` 共用 CSS、JS 與壓縮後圖片
- `sitemap.xml`、`robots.txt`、`llms.txt`：搜尋引擎與 AI 爬蟲用
- `legacy/` 改版前的一頁式舊站存檔（noindex），根目錄的 `Image1–7` 為原始圖片，保留不動

## 還原舊版
- Git：`git checkout v1-original-onepage`（commit `157cb30`），或使用分支 `backup/original-onepage`
- 或在 GitHub 對合併的改版 commit 做 Revert

## 待補內容
頁面上以橘色虛線標示「待補」的欄位，是需要公司提供的資料（規格、保固、案例等）。上線前請補齊或移除。
"""
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(readme)

print("pages:", len(PAGES))
