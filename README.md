# 研楷 Aperture Science 官方網站

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
