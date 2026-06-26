# Project Handover: Antigravity Skills Documentation (Docsify)

## Project Summary
這是一個自動化整合使用者建立的所有 AI Skills 並產出靜態說明書網站的專案。核心功能是透過 Python 腳本掃描整個資料夾的 `SKILL.md`，使用 Google Gemini API 自動翻譯並產出「一句話速查版」與結構化說明文件，最後以 Docsify 框架部署在 GitHub Pages 上。本專案也支援**無頭 CMS 模式**，允許從外部 GitHub Repo 的 Raw URL 直接載入 Markdown，達到跨專案即時同步說明的效果。

## Completed Work
1. **基礎建設**：成功配置 Docsify 框架，包含首頁 `README.md`、側邊選單與對應的路由。
2. **自動化轉換腳本 (`generate_docs.py`)**：
   - 自動遍歷資料夾，避開特定的黑名單目錄。
   - 讀取 `SKILL.md` 內容並透過 Gemini API 自動產出標準格式的 Markdown 說明。
3. **突破 API 頻率限制**：加入多模型輪替與 `time.sleep` 機制，解決了 Google API 的頻率限制問題。
4. **解決 GitHub Pages 雷區**：捨棄了 Jekyll 會忽略的 `_sidebar.md`，全面改用 `sidebar.md`。
5. **使用者體驗優化**：增強了解析能力，從已生成的 markdown 檔案中提取中文標題。
6. **動態外部讀取整合**：驗證了不需透過腳本，網頁端也能透過 `fetch` 自動渲染放在其他 Repo 的最新 `SKILL.md`。

## Current Progress
整個專案的基礎架構與自動化流程已經 100% 完成。所有現有 Skills 都已成功轉換並推播至 GitHub。外部動態載入的技術概念驗證 (POC) 也已完成。但目前發現了 `generate_docs.py` 在寫入時會洗掉手動加入的外部連結。

## Next Steps
1. **優先修復**：修改 `generate_docs.py` 中更新 `sidebar.md` 的邏輯，讓它能辨識並保留手動新增的外部 URL（包含 `http` 或 `https` 的連結），避免每次重新生成文件時覆蓋掉這些外部 Skills。
2. **UI/UX 優化**：未來可考慮為 Docsify 加上深色模式 (Dark Mode)、搜尋插件 (Search Plugin) 或是自訂的 CSS 品牌主題配色。

## Key Decisions
1. **捨棄 Jekyll 引擎**：決定直接放棄 `_sidebar.md` 的命名傳統，改為 `sidebar.md`。
2. **本機緩存優先**：實作了「若目標 Markdown 已存在則跳過 API 呼叫」的機制，大幅節省了 API 額度。
3. **Docsify 作為無頭 CMS 前端**：決定利用 Docsify 本身強大的 `fetch` 與 `Marked.js` 渲染能力。

## Technical Architecture
- **前端框架**：Docsify (Single Page Application, 內建 Marked.js 支援跨域讀取)。
- **自動化處理**：Python 3.x (`google-generativeai`, `PyYAML`, `python-dotenv`)。
- **部署環境**：GitHub Pages。

## Important Files
- `generate_docs.py`：核心腳本，負責掃描檔案、呼叫 API 與生成 Docsify 需要的結構。
- `sidebar.md`：控制左側目錄顯示的核心文件，支援本機檔案路徑與外部 URL。
- `docs/`：存放所有被轉換好的 Skill 說明 Markdown 檔。
- `progress.md`：追蹤專案待辦事項與開發進度的文件。

## Known Issues
- Gemini 的 API 免費額度有嚴格的限制。若發生 429 錯誤，腳本會自動輪替模型並在額度耗盡時暫停等待。
- **潛在覆寫風險**：目前執行 `generate_docs.py` 會導致 `sidebar.md` 被完全覆寫，這會洗掉手動添加的外部 Skill 連結。在修復前請小心執行。

## Continuation Prompt
如果你是接手這個專案的下一個 AI 助理，請仔細閱讀 `HANDOVER.md` (本文)、`progress.md` 與 `generate_docs.py` 的程式碼。請注意專案已捨棄 `_sidebar.md`，任何左側目錄更新請針對 `sidebar.md` 進行。若使用者想要新增「外部 GitHub Repo」的 Skill，請直接在 `sidebar.md` 中加入 GitHub Raw URL 即可。另外請特別注意，目前的 `generate_docs.py` 尚未修復「會覆寫 sidebar.md 中外部連結」的 Bug，執行任何腳本前需優先進行修復或特別小心。
