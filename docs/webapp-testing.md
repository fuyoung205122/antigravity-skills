# Web Application Testing (webapp-testing)

# 功能說明

使用 Playwright 框架自動化測試、互動及調試本機 Web 應用程式的工具包。

# 解決什麼問題

在開發 Web 應用時，手動測試 UI 功能、檢查多個伺服器協作（如前後端分離）以及調試動態渲染的 DOM 非常耗時且容易出錯。此 Skill 解決了本機伺服器生命週期管理的複雜性，並提供了標準化的流程來驗證前端行為與獲取偵錯資訊（如截圖和日誌）。

# 適合什麼情境

1. **前端功能驗證**：自動點擊按鈕、填寫表單並驗證預期結果。
2. **UI 回歸測試**：在修改程式碼後，確保現有介面與功能依然正常。
3. **多伺服器測試**：需要同時啟動後端 API 伺服器與前端開發伺服器進行整合測試。
4. **視覺偵錯**：自動拍攝網頁截圖以檢查 CSS 佈局或動態渲染內容。
5. **Log 分析**：捕捉並查看瀏覽器的 Console Logs 以排查 JavaScript 錯誤。

# 如何觸發

範例1：檢查本機開發中的 Vite 專案是否能正常開啟。
`python scripts/with_server.py --server "npm run dev" --port 5173 -- python my_test.py`

範例2：啟動 Python 後端與 React 前端並執行自動化腳本。
`python scripts/with_server.py --server "python api.py" --port 8000 --server "npm start" --port 3000 -- python integration_test.py`

範例3：對一個靜態 HTML 檔案進行自動化操作（如 `index.html`）。
直接撰寫 Playwright 腳本並使用 `page.goto('file:///path/to/index.html')`。

範例4：捕捉網頁載入完成後的完整頁面截圖。
在腳本中使用 `page.screenshot(path='debug.png', full_page=True)`。

範例5：查看本機應用程式在執行過程中是否有任何 Console 報錯。
使用 `examples/console_logging.py` 模式來啟動自動化流程。

# 輸入內容

1. **伺服器指令**：啟動本機伺服器的命令（如 `npm run dev`）。
2. **連接埠 (Port)**：伺服器運行的 Port 號碼。
3. **Python 腳本**：包含 Playwright 邏輯的自動化程式碼。
4. **目標路徑**：本地 HTML 檔案路徑或 URL。

# 輸出內容

1. **執行結果**：自動化腳本的成功或失敗回報。
2. **視覺產出**：瀏覽器截圖 (PNG)。
3. **偵錯資訊**：瀏覽器控制台日誌 (Console Logs)、DOM 結構分析。
4. **狀態回饋**：伺服器是否成功啟動與關閉的記錄。

# 注意事項

1. **優先查看幫助**：在執行任何內建腳本前，請務必先加上 `--help` 參數查看用法。
2. **等待網路閒置**：對於動態應用程式，務必使用 `page.wait_for_load_state('networkidle')`，否則可能抓取到不完整的 DOM。
3. **無頭模式**：在自動化環境中，務必以 `headless=True` 模式啟動 Chromium。
4. **資源管理**：測試結束後必須呼叫 `browser.close()` 以釋放系統資源。
5. **腳本精簡**：避免將大型腳本源碼完整讀入對話 Context，建議將其視為黑箱工具直接調用。

# 常見問題

**Q: 為什麼我的 Selector 找不到元素？**
A: 通常是因為網頁尚未完成動態渲染。請確保使用了正確的等待機制（如 `wait_for_selector`）或確認是否已達到 `networkidle` 狀態。

**Q: 如何同時測試前後端？**
A: 使用 `with_server.py` 並傳入多個 `--server` 參數，它會自動管理多個進程的啟動與關閉。

**Q: 支援哪些瀏覽器？**
A: 預設與建議使用 Chromium，並透過 Playwright 的 Python 接口進行控制。

---