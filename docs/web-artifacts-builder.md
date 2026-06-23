# Web Artifacts Builder

# 功能說明

這是一套用於建立複雜、多組件 Claude.ai HTML Artifacts 的工具套件，整合了 React、Tailwind CSS 與 shadcn/ui 等現代前端技術。

# 解決什麼問題

當開發需求涉及複雜的狀態管理、多層級路由或需要高品質元件庫（如 shadcn/ui）時，傳統的單一 JSX 檔案難以處理。此工具提供標準的前端開發流程（初始化、開發、打包），解決了複雜應用在 Claude 介面中難以部署與展示的問題。

# 適合什麼情境

*   需要複雜狀態管理（State Management）的互動式應用。
*   需要使用 shadcn/ui 專業元件（如 Dialog, Command, Data Table）的專案。
*   需要多個 React 組件協作的大型介面。
*   希望避免「AI 罐頭感（AI slop）」、追求獨特設計風格的 Artifact。
*   需要模擬多頁面或路由導覽的 Web App 原型。

# 如何觸發

範例1：請幫我使用 `web-artifacts-builder` 初始化一個名為 "stock-tracker" 的新專案。

範例2：我需要一個具備狀態管理的複雜 React 儀表板，請幫我準備開發環境。

範例3：請幫我把目前開發好的 React 組件打包（Bundle）成單一的 HTML Artifact。

範例4：建立一個使用 shadcn/ui 元件的專業數據分析工具，並確保設計不使用紫色漸層。

範例5：請執行初始化腳本並為我配置一個帶有 Tailwind CSS 的進階任務管理系統。

# 輸入內容

*   **專案名稱**：用於初始化專案資料夾。
*   **React 程式碼**：組件邏輯與 TypeScript 代碼。
*   **設定需求**：如特定的 shadcn/ui 元件需求。
*   **根目錄檔案**：必須包含 `index.html` 以供打包使用。

# 輸出內容

*   **初始化環境**：包含 Vite、React、TypeScript、Tailwind CSS 及 40+ 個預裝 shadcn/ui 元件。
*   **打包檔案 (`bundle.html`)**：一個自包含（Self-contained）的單一 HTML 檔案，內嵌所有 JS 與 CSS，可直接在 Claude 中預覽。

# 注意事項

*   **非簡易用途**：不建議用於簡單的單一 HTML/JSX 需求，僅適用於複雜專案。
*   **環境限制**：需要 Node 18+ 環境。
*   **設計風格指南**：強烈建議避開過度置中、紫色漸層、統一圓角與 Inter 字體，以維持視覺質感。
*   **打包流程**：必須執行 `scripts/bundle-artifact.sh` 才能生成可預覽的 Artifact。

# 常見問題

*   **Q：這個工具生成的 Artifact 可以在 Claude 以外的地方跑嗎？**
    *   A：可以，生成的 `bundle.html` 是標準的 HTML 檔案，可在任何現代瀏覽器運行。
*   **Q：一定要用 TypeScript 嗎？**
    *   A：是的，此套件預設配置為 React 18 + TypeScript 以確保開發品質。
*   **Q：打包後的檔案體積會很大嗎？**
    *   A：腳本會將所有依賴項 Inline 化，雖然比單一 HTML 大，但足以在 Claude 的 Artifact 視窗中流暢運行。

---