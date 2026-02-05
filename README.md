# PolyAlphaBot

## macOS 开机自启动（LaunchAgent）

### 安装说明
首次使用请先赋权：
```bash
chmod +x install_autostart.sh uninstall_autostart.sh
```

一键安装：
```bash
./install_autostart.sh
```

安装后效果：
- 开机自动启动
- 异常崩溃自动重启
- 后台持续运行
- 日志写入项目目录 `logs/`

---

### 服务检测方法（4 种）
1. 检查服务状态：
```bash
launchctl list | grep com.polyalphabot
```

2. 检查端口占用（如你配置了端口）：
```bash
lsof -i :<PORT>
```

3. HTTP 测试（如你开启了本地服务）：
```bash
curl http://localhost:<PORT>
```

4. 查看日志：
```bash
tail -f logs/polyalphabot.out.log
```

---

### 管理命令
查看状态：
```bash
launchctl list | grep com.polyalphabot
```

停止服务：
```bash
launchctl unload ~/Library/LaunchAgents/com.polyalphabot.plist
```

启动服务：
```bash
launchctl load ~/Library/LaunchAgents/com.polyalphabot.plist
```

查看日志：
```bash
tail -f logs/polyalphabot.out.log
tail -f logs/polyalphabot.err.log
```

---

### 技术说明
- 使用 **LaunchAgent** 机制启动服务
- 配置文件位置：`~/Library/LaunchAgents/com.polyalphabot.plist`
- 安装脚本会自动检测项目路径，并写入 plist
- 通过 `--directory` 参数显式指定工作目录，避免 macOS 权限限制导致的 `os.getcwd()` 失败

---

### 故障排查
**服务未启动**
```bash
launchctl list | grep com.polyalphabot
tail -f logs/polyalphabot.err.log
```

**端口被占用**
```bash
lsof -i :<PORT>
```

**权限问题（Documents/Desktop 等目录）**
- 已通过 `--directory` 参数避免工作目录权限问题
- 若仍失败，请在系统设置中授予终端“完全磁盘访问”

**重新安装服务**
```bash
./uninstall_autostart.sh
./install_autostart.sh
```
