import time
import os
import subprocess
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = r"E:\2026andigravity2"
WORK_DIR = r"E:\2026andigravity2\41-存skill"
EXCLUDE_DIRS = [".git", "node_modules", "41-存skill", ".agents", "skillspector"]
DEBOUNCE_SECONDS = 10

class SkillSyncHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self._timer = None
        self.lock = threading.Lock()

    def _is_excluded(self, path):
        # 檢查路徑是否包含被排除的目錄
        parts = os.path.normpath(path).split(os.sep)
        for excl in EXCLUDE_DIRS:
            if excl in parts:
                return True
        return False

    def _should_trigger(self, event):
        if self._is_excluded(event.src_path):
            return False
        
        # 我們關心 SKILL.md 的任何變更，或是整個資料夾被刪除
        if event.is_directory and event.event_type == 'deleted':
            return True
        
        if event.src_path.endswith("SKILL.md"):
            return True
            
        return False

    def on_any_event(self, event):
        if self._should_trigger(event):
            with self.lock:
                if self._timer is not None:
                    self._timer.cancel()
                self._timer = threading.Timer(DEBOUNCE_SECONDS, self._run_sync)
                self._timer.start()
                print(f"[*] 偵測到變更 ({event.event_type}): {event.src_path}，將在 {DEBOUNCE_SECONDS} 秒後自動同步...")

    def _run_sync(self):
        print("\n" + "="*50)
        print("[*] 開始執行自動同步流程...")
        try:
            # 1. 執行 generate_docs.py
            print("  > 執行 generate_docs.py")
            subprocess.run(["python", "generate_docs.py"], cwd=WORK_DIR, check=True)
            
            # 2. 檢查 Git 狀態
            status_proc = subprocess.run(["git", "status", "--porcelain"], cwd=WORK_DIR, capture_output=True, text=True)
            if not status_proc.stdout.strip():
                print("  > 沒有需要發布的變更。")
                return

            # 3. 執行 Git Add
            print("  > 執行 git add .")
            subprocess.run(["git", "add", "."], cwd=WORK_DIR, check=True)
            
            # 4. 執行 Git Commit
            print("  > 執行 git commit")
            subprocess.run(["git", "commit", "-m", "Auto-sync: Skill updated"], cwd=WORK_DIR, check=True)
            
            # 5. 執行 Git Push
            print("  > 執行 git push")
            subprocess.run(["git", "push", "origin", "main"], cwd=WORK_DIR, check=True)
            
            print("[*] 自動同步流程執行完畢！線上網站將在 1~2 分鐘內更新。")
            
        except subprocess.CalledProcessError as e:
            print(f"[!] 自動同步執行失敗: {e}")
        except Exception as e:
            print(f"[!] 發生未預期的錯誤: {e}")
        print("="*50 + "\n等待新的變更...\n")


def main():
    print("啟動自動發布監控程式 (Auto Publisher)")
    print(f"監控目錄: {WATCH_DIR}")
    print(f"防彈跳時間: {DEBOUNCE_SECONDS} 秒")
    print("等待變更中... (按 Ctrl+C 停止)\n")
    
    event_handler = SkillSyncHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
