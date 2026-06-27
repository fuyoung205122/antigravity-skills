# 專案進度追蹤 (Progress)

## 目前階段 (Current Phase)
維護與優化階段 (Maintenance & Optimization)

## 已完成進度 (Completed)
- [x] 配置 Docsify 靜態網站框架與路由
- [x] 開發 `generate_docs.py` 自動化生成 Skill 說明並呼叫 Gemini API
- [x] 實作多模型輪替與 429 錯誤重試機制
- [x] 捨棄 `_sidebar.md` 改用 `sidebar.md` 避開 Jekyll 忽略規則
- [x] 實作本機緩存優先機制，減少不必要的 API 呼叫
- [x] 支援外部 GitHub Raw URL 動態載入
- [x] 完善專案交接文件 (`HANDOVER.md`, `progress.md`, `changelog.md`, `next_steps.md`)
- [x] **新增自動清理過期文件功能**：修改 `generate_docs.py`，使之能自動偵測並刪除 `docs/` 下已無對應 Skill 的舊 Markdown 檔案。
- [x] 釐清網站發布流程，確認透過本地 `41-存skill` 目錄執行 `git push` 來手動發布更新至 GitHub Pages。

## 進行中 / 待處理項目 (In Progress / To Do)
- [x] **修復 `sidebar.md` 覆寫與重複問題**：已修改寫入邏輯，加入 `dict.fromkeys` 去除重複的 Skill，並保留原有的外部連結。
- [ ] 支援 Docsify 深色模式 (Dark Mode) 或自訂 CSS 主題
- [ ] 加入搜尋功能 (Search Plugin)

## 最近更新紀錄 (Recent Updates)
- [2026-06-26] 專案交接：釐清 GitHub Pages (`antigravity-skills`) 與本地倉庫的同步關係，確認需以手動 `git push` 更新。修改 `generate_docs.py` 腳本，加入刪除過期 `.md` 檔案的自動清理機制。完成收工。
- [2026-06-25] 專案交接：發現 `generate_docs.py` 的覆寫風險。完成 `HANDOVER.md` 等多份交接文件編寫。
