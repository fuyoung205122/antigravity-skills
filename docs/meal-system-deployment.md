# 家庭訂餐系統同步與部署

# 功能說明

將家庭訂餐系統（antigravity-meal）的程式碼自動同步至 GitHub 並部署至 Vercel 生產環境。

# 解決什麼問題

確保家庭訂餐系統的最新功能和修復能夠快速、準確地部署到生產環境，避免因手動部署流程繁瑣或出現錯誤而導致系統更新延遲或失敗。

# 適合什麼情境

*   當您對家庭訂餐系統進行了程式碼更新、功能新增或 Bug 修正後，希望將這些變更部署到線上正式網站。
*   需要確保生產環境的訂餐系統始終是最新版本。
*   希望自動化 Git 提交、推送以及 Vercel 生產環境的部署流程。

# 如何觸發

範例1：
「幫我部署訂餐系統到正式網站。」

範例2：
「請同步一下訂餐系統的程式碼到 GitHub 和 Vercel。」

範例3：
「我要更新正式網站，請幫我處理。」

範例4：
「同步並部署訂餐系統。」

範例5：
「訂餐系統上線，將最新的程式碼發布。」

# 輸入內容

*   **訂餐系統原始碼目錄**: `E:/2026andigravity2/12-製作/`
*   **Git 倉庫根目錄**: `E:/2026andigravity2/`
*   **主要的分支**: `master`
*   **Vercel 專案名稱**: `antigravity-meal`
*   **Vercel 環境變數**: `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `LINE_ACCESS_TOKEN`, `GEMINI_API_KEY`, `NVIDIA_API_KEY`, `CRON_SECRET` (這些環境變數應已在 Vercel 專案中配置好)

# 輸出內容

*   程式碼成功推送到 GitHub 的 `master` 分支。
*   訂餐系統（antigravity-meal）成功部署到 Vercel 生產環境，網址為 `https://antigravity-meal.vercel.app`。
*   終端會顯示部署成功的訊息，包含最新的 Production API 狀態。

# 注意事項

*   執行部署前，請確認 Git 倉庫根目錄下的 `.gitignore` 文件已正確配置，排除 `09-多媒體/` 目錄下的大型檔案（如 `.zip`, `.exe`, `.mp4` 等），以避免 Git 索引衝突。
*   若有大檔案誤入 Git 索引，執行 `git rm -r --cached .` 後再 `git add .` 進行重置和重新暫存。
*   部署後，強烈建議使用者在電腦端使用 `Ctrl + F5` 強制重新整理，並在手機端使用「無痕模式 / 私密瀏覽」來測試，以避免瀏覽器快取導致看到舊版頁面。

# 常見問題

**Q1: 為什麼部署後頁面沒有更新？**
A1: 這通常是瀏覽器快取的問題。請嘗試強制重新整理（`Ctrl + F5`）或在手機上使用無痕模式重新開啟網頁測試。

**Q2: 部署過程中出現 Git 錯誤，如何處理？**
A2: 請檢查您的 `.gitignore` 設定是否正確，並確認沒有大型檔案（例如影片、壓縮包）被誤加入 Git。可以嘗試執行 `git rm -r --cached .` 後再 `git add .` 來重置 Git 快取。

**Q3: Vercel 部署失敗，提示缺少環境變數？**
A3: 請確保您已在 Vercel 專案 `antigravity-meal` 的設定中，為生產環境配置了所有必需的環境變數，包括 `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `LINE_ACCESS_TOKEN`, `GEMINI_API_KEY`, `NVIDIA_API_KEY`, `CRON_SECRET`。

---