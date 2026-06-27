import os
import time
import re
import yaml
import google.generativeai as genai
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("找不到 GEMINI_API_KEY，請確認 .env 檔案是否設定正確。")
    exit(1)

# 設定 Gemini API
genai.configure(api_key=API_KEY)
# 嘗試幾種不同的模型名稱，避免 404 錯誤
# 優先使用的進階模型清單
model_names = [
    'gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-flash-latest',
    'gemini-3.5-flash', 'gemini-3.1-pro-preview', 'gemini-pro-latest',
    'gemini-2.5-flash-lite', 'gemini-3-pro-preview', 'gemini-3-flash-preview',
    'gemini-3.1-flash-lite'
]
models_pool = []
current_model_idx = 0

print("正在偵測可用的 API 模型...")
available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
print(f"你的 API Key 支援的模型數量: {len(available_models)}")

for name in model_names:
    full_name = f"models/{name}" if not name.startswith("models/") else name
    if any(m.endswith(name) for m in available_models):
        print(f"[*] 加入可用模型池: {name}")
        models_pool.append(genai.GenerativeModel(name))

if not models_pool:
    fallback = 'gemini-flash-latest'
    print(f"[!] 找不到偏好的模型，嘗試強制使用 {fallback}")
    models_pool.append(genai.GenerativeModel(fallback))

BASE_DIR = r"E:\2026andigravity2"
OUTPUT_DIR = os.path.join(BASE_DIR, "41-存skill")
DOCS_DIR = os.path.join(OUTPUT_DIR, "docs")
SIDEBAR_FILE = os.path.join(OUTPUT_DIR, "sidebar.md")
INDEX_FILE = os.path.join(OUTPUT_DIR, "README.md")

# 要排除的目錄
EXCLUDE_DIRS = {".git", "node_modules", "41-存skill", ".agents", "skillspector"}

prompt_template = """
你的任務是為新建立的 Skill 自動產生使用說明。

當使用者輸入：
* Skill說明書
* Skill文件
* Skill README

請根據以下 [原始 Skill 內容]，輸出：

# Skill 名稱

# 功能說明

一句話說明用途。

# 解決什麼問題

說明存在原因。

# 適合什麼情境

列出常見使用情境。

# 如何觸發

提供至少 5 個實際範例。

例如：

範例1：

範例2：

範例3：

範例4：

範例5：

# 輸入內容

需要提供什麼資料。

# 輸出內容

會得到什麼結果。

# 注意事項

使用限制。

# 常見問題

FAQ。

最後額外產生：

# 一句話速查版

格式：

Skill名稱
→ 功能摘要

方便建立 Skill Index。

---
[原始 Skill 內容]:
{content}
"""

def get_skill_files(base_path):
    skill_files = []
    for root, dirs, files in os.walk(base_path):
        # 排除不需要的目錄
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file == "SKILL.md":
                skill_files.append(os.path.join(root, file))
    return skill_files

def extract_skill_name(content, file_path):
    # 嘗試從 YAML frontmatter 解析
    if content.startswith('---'):
        end_idx = content.find('---', 3)
        if end_idx != -1:
            yaml_content = content[3:end_idx]
            try:
                parsed = yaml.safe_load(yaml_content)
                if parsed and 'name' in parsed:
                    return parsed['name']
            except yaml.YAMLError:
                pass
                
    # 如果解析不到，使用資料夾名稱
    return os.path.basename(os.path.dirname(file_path))

def generate_docsify_content(skill_content):
    global current_model_idx
    prompt = prompt_template.format(content=skill_content)
    while True:
        model = models_pool[current_model_idx]
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            error_msg = str(e)
            print(f"API 呼叫失敗 ({model.model_name}): {error_msg}")
            if "429" in error_msg:
                current_model_idx += 1
                if current_model_idx >= len(models_pool):
                    print("[!] 所有模型的配額皆已用盡，暫停 60 秒後重試第一個模型...")
                    time.sleep(60)
                    current_model_idx = 0
                else:
                    print(f"[*] 觸發頻率限制，自動切換至下一個模型: {models_pool[current_model_idx].model_name}")
            else:
                return None

def extract_quick_lookup(generated_text):
    # 找出「一句話速查版」底下的內容
    match = re.search(r'# 一句話速查版\s*\n*(.*?)(?:\n# |$)', generated_text, re.DOTALL)
    if match:
        lines = match.group(1).strip().split('\n')
        lines = [line for line in lines if line.strip() and not line.startswith('格式：')]
        return "\n".join(lines)
    return ""

def extract_display_name(generated_text, default_name):
    match = re.search(r'# Skill 名稱\s*\n+([^#\n]+)', generated_text)
    if match:
        title = match.group(1).strip().replace('*', '').strip()
        if title:
            m = re.match(r'^(.*?)\s*[\(（](.*?)[\)）]$', title)
            
            def has_chinese(s):
                return any('\u4e00' <= c <= '\u9fff' for c in s)
                
            if m:
                part1, part2 = m.group(1).strip(), m.group(2).strip()
                if has_chinese(part1) and not has_chinese(part2):
                    return f"{part1} ({part2})"
                elif has_chinese(part2) and not has_chinese(part1):
                    return f"{part2} ({part1})"
                else:
                    return f"{part1} ({part2})"
            
            if title.lower() != default_name.lower():
                if has_chinese(title):
                    return f"{title} ({default_name})"
            return title
    return default_name

def main():
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)

    skill_files = get_skill_files(BASE_DIR)
    print(f"找到 {len(skill_files)} 個 SKILL.md 檔案。")
    
    sidebar_items = []
    quick_lookups = []
    valid_doc_files = set()
    
    for idx, filepath in enumerate(skill_files):
        print(f"[{idx+1}/{len(skill_files)}] 正在處理: {filepath}")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            skill_name = extract_skill_name(content, filepath)
            # 清理檔名不可用字元
            safe_filename = "".join([c for c in skill_name if re.match(r'\w|-', c)])
            if not safe_filename:
                safe_filename = f"skill_{idx}"
                
            output_path = os.path.join(DOCS_DIR, f"{safe_filename}.md")
            
            # 檢查是否已經轉換過，避免浪費額度
            if os.path.exists(output_path):
                print(f"  > [*] 已經存在，跳過轉換: {skill_name}")
                with open(output_path, 'r', encoding='utf-8') as f:
                    generated_text = f.read()
                display_name = extract_display_name(generated_text, skill_name)
                sidebar_items.append(f"* [{display_name}](docs/{safe_filename}.md)")
                valid_doc_files.add(f"{safe_filename}.md")
                continue

            print(f"  > Skill 名稱: {skill_name}")
            
            # 呼叫 API
            generated_text = generate_docsify_content(content)
            if not generated_text:
                continue
                
            # 移除速查版部分，讓正文不要包含速查版
            main_content = re.sub(r'# 一句話速查版.*$', '', generated_text, flags=re.DOTALL | re.IGNORECASE).strip()
            
            # 取得速查版
            quick_lookup = extract_quick_lookup(generated_text)
            if quick_lookup:
                quick_lookups.append(quick_lookup)
                
            # 存入 docs/
            output_path = os.path.join(DOCS_DIR, f"{safe_filename}.md")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(main_content)
                
            display_name = extract_display_name(generated_text, skill_name)
            sidebar_items.append(f"* [{display_name}](docs/{safe_filename}.md)")
            valid_doc_files.add(f"{safe_filename}.md")
            
            # 每次成功呼叫後固定等待 5 秒，避免快速觸發限制
            time.sleep(5)
            
        except Exception as e:
            print(f"  > 處理失敗: {e}")
            
    # 清理已經不存在的 skill 文件
    print("正在清理已刪除的 Skill 文件...")
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".md") and filename not in valid_doc_files:
            file_to_remove = os.path.join(DOCS_DIR, filename)
            try:
                os.remove(file_to_remove)
                print(f"  > [-] 已刪除過期的文件: {filename}")
            except Exception as e:
                print(f"  > 無法刪除文件 {filename}: {e}")
                
    # 更新 sidebar.md
    print("正在更新 sidebar.md...")
    
    # 讀取現有的 sidebar.md 內容，保留外部連結
    existing_external_links = []
    if os.path.exists(SIDEBAR_FILE):
        with open(SIDEBAR_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if 'http://' in line or 'https://' in line:
                    existing_external_links.append(line.rstrip('\n'))

    sidebar_content = "<!-- sidebar -->\n* [首頁](/)\n* Skills\n"
    
    # 處理重複項目 (利用 dict.fromkeys 保持順序並去重)
    unique_items = list(dict.fromkeys(sidebar_items))
    for item in unique_items:
        sidebar_content += f"  {item}\n"
        
    # 補回外部連結
    for ext_link in existing_external_links:
        sidebar_content += f"{ext_link}\n"
        
    with open(SIDEBAR_FILE, 'w', encoding='utf-8') as f:
        f.write(sidebar_content)
        
    # 更新 README.md
    print("正在更新 README.md...")
    readme_content = "# Antigravity Skills Documentation\n\n歡迎來到 Skill 說明書網站！\n\n## 一句話速查版\n\n"
    if quick_lookups:
        unique_qls = list(dict.fromkeys(quick_lookups))
        for ql in unique_qls:
            readme_content += f"{ql}\n"
    else:
        readme_content += "目前尚未產生速查資料。\n"
        
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(readme_content)
        
    print("全部完成！你可以啟動 docsify 檢視成果了。")

if __name__ == "__main__":
    main()
