import os
import requests

VERSION = "v1.0"
download_path = "/storage/emulated/0/Download/天生少爷命工具部署/"

def check_download_permission():
    if not os.path.exists(download_path):
        try:
            os.makedirs(download_path)
        except Exception:
            print("⚠️ 无法创建目录：", download_path)
            input("请手动授权后按回车继续...")

def get_download_list():
    try:
        response = requests.get("https://api.y11.top/fileecho.php?id=1512", timeout=10)
        response.raise_for_status()
        raw_list = response.text.strip().splitlines()

        tool_list = []
        for line in raw_list:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            name, url, code = parts
            available = check_url_validity(url)
            if not available:
                name += " 【链接不可用】"
            tool_list.append((name.strip(), url.strip(), code.strip()))
        return tool_list

    except Exception as e:
        print("❌ 获取在线工具列表失败：", e)
        return []

def check_url_validity(url):
    try:
        resp = requests.head(url, allow_redirects=True, timeout=5)
        return resp.status_code == 200
    except:
        return False

def download_menu():
    tools = get_download_list()
    if not tools:
        print("\n暂无可用工具。")
        return

    print("\n📦 可下载工具列表：")
    for i, (name, _, _) in enumerate(tools):
        print(f"{i + 1}. {name}")

    choice = input("\n请输入下载序号（或回车返回）：")
    if not choice.isdigit():
        return

    index = int(choice) - 1
    if 0 <= index < len(tools):
        name, url, code = tools[index]
        if "链接不可用" in name:
            print("⚠️ 当前链接不可用，无法下载。")
            return

        for attempt in range(3):
            input_code = input(f"请输入配对码（剩余{3 - attempt}次）：")
            if input_code == code:
                print("✅ 配对码正确，准备打开蓝奏云链接下载。")
                os.system(f'termux-open-url {url}')
                return
            else:
                print("❌ 配对码错误。")
        print("⛔ 尝试次数已达上限，返回主菜单。")
    else:
        print("⚠️ 无效选择。")

def main():
    check_download_permission()
    while True:
        print(f"\n=== 天生少爷命工具 启动器 {VERSION} ===")
        print("1. 下载工具")
        print("2. 退出")
        cmd = input("请输入你的选择：")
        if cmd == "1":
            download_menu()
        elif cmd == "2":
            print("再见！")
            break
        else:
            print("⚠️ 无效输入，请重新选择。")

if __name__ == "__main__":
    main()