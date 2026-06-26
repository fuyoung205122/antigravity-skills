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

## 進行中 / 待處理項目 (In Progress / To Do)
- [ ] **修復 `sidebar.md` 覆寫問題**：目前的 `generate_docs.py` 會完全覆寫 `sidebar.md`，導致手動新增的外部 GitHub Raw URL 連結被洗掉。需要修改寫入邏輯，保留原有的外部連結。
- [ ] 支援 Docsify 深色模式 (Dark Mode) 或自訂 CSS 主題
- [ ] 加入搜尋功能 (Search Plugin)

## 最近更新紀錄 (Recent Updates)
- [2026-06-25] 專案交接：發現 `generate_docs.py` 的覆寫風險。完成 `HANDOVER.md`、`progress.md`、`changelog.md` 與 `next_steps.md` 的編寫，完成收工交接準備。
