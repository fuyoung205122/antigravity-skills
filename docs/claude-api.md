# Skill 名稱

claude-api

# 功能說明

專門協助開發者建構、偵錯與優化基於 Claude API 及 Anthropic SDK 的應用程式，並處理最新模型遷移、提示詞快取、自適應思考、對話壓縮與託管型 Agent (Managed Agents) 的高階實作。

# 解決什麼問題

在開發 Claude 應用程式時，開發者常面臨以下挑戰：
1. **SDK 混淆與不相容**：容易誤用 OpenAI 的相容層或非官方程式庫，導致失去 Claude 的獨特功能。
2. **模型升級與遷移陣痛**：Claude 4.5、4.6、4.7 等版本在參數（如移除 `budget_tokens`、`temperature`、Assistant Prefill）上有重大變更，容易產生 400 錯誤。
3. **成本與效能優化困難**：不知道如何正確編排 Prompt 順序以觸發提示詞快取 (Prompt Caching)，或在超長對話中不知如何實作合約壓縮 (Compaction)。
4. **Agent 開發複雜度**：在選擇自建 Tool Loop（手動/自動工具調用）與 Anthropic 託管型 Agent (Managed Agents) 之間感到困惑，且不易寫出強健的串流與異常處理邏輯。

本 Skill 旨在解決上述問題，確保產出的程式碼完全符合 Anthropic 最新官方規範，並發揮模型最大效能。

# 適合什麼情境

* **新專案串接**：從零開始使用 Python、TypeScript、Java、Go、Ruby、C#、PHP 或原始 cURL 串接 Claude API。
* **模型版本遷移**：將既有的 Claude 應用程式無痛升級至最新模型（如 `claude-opus-4-7`），並修正已被廢棄的舊參數或邏輯。
* **成本優化（Prompt Caching）**：需要設計高命中率的快取架構，減少大量重複輸入帶來的代幣（Token）消耗。
* **高階 Agent 開發**：需要實作具備 Sandbox 執行環境、持久化 Session、事件串流的 Managed Agents，或是自建具備 Tool Use 的工作流。
* **長對話維護**：對話長度即將突破 1M 上限，需要整合伺服器端合約壓縮（Compaction）功能的場景。

# 如何觸發

當發生以下情境之一時，將會自動觸發此 Skill：

* **範例1**：使用者的專案程式碼中包含 `import anthropic`、`from anthropic` 或 `@anthropic-ai/sdk` 等官方 SDK 的匯入宣告。
* **範例2**：使用者主動提問有關 Claude API、Anthropic SDK 的調用語法、錯誤處理或 Managed Agents 的設定方式。
* **範例3**：使用者要求在既有專案中加入或調整 Claude 的特有功能，例如：提示詞快取 (Prompt Caching)、自適應思考 (Adaptive Thinking)、對話壓縮 (Compaction)、工具調用 (Tool Use/Tool Runner)、批處理 (Batches) 或檔案 API (Files API)。
* **範例4**：使用者遇到快取命中率（Cache Hit Rate）低下、API 逾時、或 4.6/4.7 模型的 JSON 解析與 Unicode 逸出字元處理問題。
* **範例5**：使用者請求將現有的 Claude 程式碼在不同模型版本之間進行遷移（例如：「幫我把這段程式碼升級到支援 Opus 4.7」）。

# 輸入內容

為了提供最精準的協助，使用者可提供：
1. **專案程式碼片段**：包含目前的 API 呼叫邏輯或設定檔。
2. **開發語言及環境**：如 Python (pyproject.toml)、TypeScript (tsconfig.json)、Java 等，以便進行自動語言偵測。
3. **目標模型與功能需求**：例如指定使用 `claude-opus-4-7`，並需要加入「工具調用」與「提示詞快取」功能。
4. **現有的錯誤日誌 (Error Logs)**：若在升級或呼叫時遭遇報錯，提供詳細的錯誤訊息有助於快速定位。

# 輸出內容

本 Skill 將輸出：
1. **官方原生 SDK 程式碼**：嚴格遵循官方最新設計模式，絕不混用 `requests` 或 `fetch`（除非是無官方 SDK 的語言），並精確匯入 SDK 內建型別。
2. **最佳化參數設定**：預設使用最新模型 `claude-opus-4-7`、自適應思考 (`thinking: {type: "adaptive"}`)、大流量自動啟用串流（Streaming）以防止逾時。
3. **優化架構說明**：針對 Prompt Caching 說明快取起點配置，或針對 Compaction 提供保留狀態的 Content Block 串接邏輯。
4. **安全防護提示**：若偵測到非 Anthropic 的標記（如 `import openai`），會先暫停並向使用者確認，避免破壞現有非 Claude 的程式碼。

# 注意事項

* **非 Anthropic 標記防護**：一旦偵測到程式碼中有 `openai`、`gpt-4`、供應商中立宣告等，**必須停止修改**並詢問使用者是否要切換至 Claude，切勿將 Anthropic SDK 寫入非 Anthropic 檔案中。
* **Opus 4.7 限制**：
  * **僅支援自適應思考**：只能設定 `thinking: {type: "adaptive"}`，若傳入 `budget_tokens` 會導致 400 錯誤。
  * **移除採樣參數**：啟用思考時，不允許傳入 `temperature`、`top_p`、`top_k`。
  * **思維內容預設隱藏**：串流時思考內容預設為 `"omitted"`，若需要顯示思考過程，必須顯式設定 `display: "summarized"`。
* **不支援 Assistant Prefill**：4.6 與 4.7 系列模型**不支援**在最後一個 Assistant Turn 進行 Prefill（會回傳 400）。格式限制請改用 `output_config.format` 結構化輸出或 System Prompt 規範。
* **遷移確認**：若要求遷移程式碼但未指定具體檔案或目錄，必須**先詢問並確認遷移範圍**，不可直接對整個工作目錄進行盲目修改。
* **Managed Agents 部署限制**：Managed Agents 為第一方獨佔功能，**不支援** Amazon Bedrock、Google Vertex AI 或 Microsoft Foundry。

# 常見問題

* **Q：為什麼我的 Prompt Caching 完全沒有發揮作用（快取命中率為 0）？**
  * **A**：Prompt Caching 採用前綴匹配（Prefix Match），前綴中任何一個位元組的變動都會導致後續快取失效。常見的隱形殺手包括：在 System Prompt 放入動態時間（如 `datetime.now()`）、隨機排序的 Tool 清單、或將會變動的對話放在靜態 System Prompt 之前。請確保將最穩定的靜態內容（系統提示、工具定義）放在最前方，並在該處標記 `cache_control`。
* **Q：程式碼在呼叫大模型時常遇到 HTTP 逾時，該如何解決？**
  * **A**：當 `max_tokens` 設得較高（4.6/4.7 支援至 128K）或啟用思考模式時，生成時間可能較長。**請務必預設使用 Streaming（串流）**。SDK 提供了 `.get_final_message()` / `.finalMessage()` 輔助函式，讓你在享受串流防逾時的同時，能輕鬆獲取完整回覆。
* **Q：什麼時候該選 Managed Agents，什麼時候該選一般 API + Tool Use？**
  * **A**：如果需要 Anthropic 來幫你運行 Agent Loop、託管安全的程式碼執行沙盒、且需要跨 Session 持久化記憶與檔案，請選 **Managed Agents**。如果你想完全控制執行環境、自訂安全閘道、或者部署在 Bedrock/Vertex 第三方平台上，則應選擇一般的 **Claude API + Tool Use**（並建議使用 SDK 的 Tool Runner 簡化開發）。

---