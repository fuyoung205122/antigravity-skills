---
name: skill_documentation_generator
description: 為新建立的 Skill 自動產生符合 Docsify 網站格式的使用說明書與速查表。
---

# Skill Documentation Generator

## Trigger
當使用者輸入以下關鍵字或類似指令時觸發：
* Skill說明書
* Skill文件
* Skill README
* 幫我把這個 Skill 做成文件

## Input
* 使用者提供的一個或多個已經寫好的 `SKILL.md` 內容。
* 或者是明確的 Skill 名稱與其功能邏輯。

## Output
產生標準化的 Markdown 文件，包含：
1. Skill 名稱
2. 功能說明
3. 解決什麼問題
4. 適合什麼情境
5. 如何觸發（含 5 個範例）
6. 輸入內容
7. 輸出內容
8. 注意事項
9. 常見問題
10. 一句話速查版（用於建立 Skill Index）

## Workflow
1. **分析輸入**：讀取使用者提供的 Skill 內容，理解其核心用途、觸發條件與限制。
2. **生成各段落**：
   - **功能說明**：濃縮成一句話。
   - **解決什麼問題**：說明存在原因與痛點。
   - **適合什麼情境**：條列常見應用場景。
   - **如何觸發**：設計 5 個實際且生活化的對話範例。
   - **輸入/輸出**：明確定義需要的資料與預期的結果。
   - **注意事項與常見問題**：推測使用限制與 FAQ。
3. **速查版彙整**：在文件最下方產生「Skill名稱 → 功能摘要」的速查格式。
4. **輸出 Markdown**：直接輸出可存入 Docsify `docs/` 資料夾的 `.md` 檔案內容，並提醒使用者更新 `_sidebar.md`。

## Example
**User:** 幫我產生 "github_research" 的 Skill說明書。
**Agent:** 
(讀取 github_research 的內容...)
# github_research
# 功能說明
...
