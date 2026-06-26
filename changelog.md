# 變更紀錄 (Changelog)

## [2026-06-25]
### Added
- 建立 `progress.md`，統整專案目前階段、已完成進度與待處理項目。
- 建立 `changelog.md` 與 `next_steps.md` 完善長期維護專案的交接流程與文件體系。

### Changed
- 更新 `HANDOVER.md` 專案交接文件，重新整理專案資訊與狀態。
- 更新 `HANDOVER.md` 內的 Continuation Prompt，加入 `sidebar.md` 覆寫風險警告，提醒後續接手人員。

### Security / Risk
- 發現並確認了 `generate_docs.py` 在執行時會覆寫 `sidebar.md` 內容的風險，這會導致手動加入的外部 GitHub Raw URL 遺失。已將此問題列為最高優先級待處理事項。
