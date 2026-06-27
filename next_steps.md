# 下一步行動 (Next Steps)

## 優先任務 (High Priority)
1. **修復 `sidebar.md` 覆寫問題 (Bug Fix)**
   - **問題描述**：目前 `generate_docs.py` 每次執行都會覆寫整份 `sidebar.md`，導致手動寫入的外部 Skill (外部 GitHub Raw URL) 被洗掉。
   - **實作建議**：在更新 `sidebar.md` 前，先讀取既有的 `sidebar.md` 內容，過濾並保留帶有外部連結（如包含 `http://` 或 `https://`）的項目，然後再與本地自動生成的 Markdown 項目合併寫入。

## 後續優化 (Enhancements)
1. **UI/UX 強化**
   - 考慮在 Docsify 加上深色模式 (Dark Mode) 支援。
   - 考慮加入搜尋插件 (Search Plugin)，讓使用者能快速檢索所有的 Skills。
   - 調整 CSS，加入品牌主題配色。

## 發布與同步須知 (Deployment Guide)
- 本地生成的新文件不會自動推送到 GitHub Pages。
- 每次在 `41-存skill` 跑完 `generate_docs.py` 後，必須手動執行 `git add .`、`git commit -m "更新"` 與 `git push origin main` 才會更新線上網站。

## 啟動指引 (How to start)
下一次開工時，請先閱讀本文件與 `progress.md`，然後優先著手處理「修復 `sidebar.md` 覆寫問題」。
