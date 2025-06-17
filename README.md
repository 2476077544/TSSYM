# 天生少爷命工具 - Termux 启动器

这是一个基于 Termux 的 Android 启动器，用于从蓝奏云一键下载配对码工具。

## ✅ 使用方法

```bash
pkg update -y && pkg install python curl -y
pip install requests -q
curl -O https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/main.py
python main.py
```

> 替换 `YOUR_USERNAME/YOUR_REPO_NAME` 为你自己的 GitHub 仓库路径。

## 📂 工具保存目录

默认保存路径为：
```
/storage/emulated/0/Download/天生少爷命工具部署/
```

## 🛠️ 功能说明

- 获取云端工具列表（来自 API）
- 输入编号和配对码后打开蓝奏云链接下载
- 链接不可用时自动标记提示