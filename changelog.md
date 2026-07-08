# 變更紀錄 (Changelog)

## [2026-06-28]
### Added
- 建立 `auto_publisher.py` (Watchdog) 達成全自動發布監控機制。當偵測到 `SKILL.md` 異動時，會延遲 10 秒後自動執行 `generate_docs.py` 並推播至 GitHub。
- 建立 `start_auto_sync.bat` 與 `sync_now.bat`，讓使用者能一鍵啟動背景監控，或是一鍵執行單次強制同步。

### Fixed
- 解決 `bat` 檔在 Windows 終端機執行時因為中文 UTF-8 編碼造成的亂碼與指令失效問題（已全面改為純英文提示）。
- 解決 `python` 指令意外抓取到 `hermes-agent` 虛擬環境的問題，改為直接綁定絕對路徑的系統 Python 3.12 執行檔，確保套件依賴正確。
## [2026-06-27]
### Fixed
- 修復 `generate_docs.py` 中 `sidebar_items` 重複產生的問題。現在腳本會利用 `dict.fromkeys` 自動去除重複的 Skill 項目。
- 修復 `generate_docs.py` 會將 `sidebar.md` 內手動添加的外部連結覆寫洗掉的問題。現在寫入前會預先讀取並保留 `http://` 與 `https://` 的外部連結。

### Deployed
- 將乾淨且正確的 `sidebar.md` 推播至 GitHub Pages。
## [2026-06-26]
### Added
- 為 `generate_docs.py` 腳本新增自動清理功能。當腳本執行完畢時，會自動比對並刪除 `docs/` 資料夾中已經沒有對應實體 Skill 的 Markdown 殘留文件。

### Documented
- 釐清並確定了 GitHub Pages 的發布機制：確認 `E:\2026andigravity2\41-存skill` 是綁定 `antigravity-skills` 的本地倉庫，發布更新只需在該目錄下執行標準的 `git add .`, `git commit`, `git push origin main` 指令，而非依賴跨倉庫自動同步。

## [2026-06-25]
### Added
- 建立 `progress.md`，統整專案目前階段、已完成進度與待處理項目。
- 建立 `changelog.md` 與 `next_steps.md` 完善長期維護專案的交接流程與文件體系。

### Changed
- 更新 `HANDOVER.md` 專案交接文件，重新整理專案資訊與狀態。
- 更新 `HANDOVER.md` 內的 Continuation Prompt，加入 `sidebar.md` 覆寫風險警告，提醒後續接手人員。

### Security / Risk
- 發現並確認了 `generate_docs.py` 在執行時會覆寫 `sidebar.md` 內容的風險，這會導致手動加入的外部 GitHub Raw URL 遺失。已將此問題列為最高優先級待處理事項。
