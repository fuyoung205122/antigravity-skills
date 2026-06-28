# 下一步行動 (Next Steps)

## 後續優化 (Enhancements)
1. **UI/UX 強化**
   - 考慮在 Docsify 加上深色模式 (Dark Mode) 支援。
   - 考慮加入搜尋插件 (Search Plugin)，讓使用者能快速檢索所有的 Skills。
   - 調整 CSS，加入品牌主題配色。

## 發布與同步須知 (Deployment Guide)
- 本地生成的新文件不會自動推送到 GitHub Pages。
- 每次在 `41-存skill` 跑完 `generate_docs.py` 後，必須手動執行 `git add .`、`git commit -m "更新"` 與 `git push origin main` 才會更新線上網站。

## 啟動指引 (How to start)
下一次開工時，請先閱讀本文件與 `progress.md`，目前優先的錯誤 (Bug) 皆已修復，您可以自由選擇接下來想要強化網站 UI/UX，或是新增其他的 Skill。
