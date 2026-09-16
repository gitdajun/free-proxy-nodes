# 免费节点与订阅管理

用于存放与维护公开可用的代理订阅链接及节点示例，配合 Clash / Mihomo / V2Ray 等客户端使用。

> **声明**  
> - 节点来自公开渠道，不保证长期可用与安全性  
> - 免费节点易失效、限速，不适合作为唯一线路  
> - 请遵守当地法律，仅用于合法用途  
> - 本仓库不提供付费节点，不收集用户信息

---

## 使用方法

### 订阅链接

将 `subscriptions/` 下对应文件中的链接导入客户端：

| 文件 | 用途 |
|------|------|
| `subscriptions/clash.txt` | Clash / Mihomo |
| `subscriptions/v2ray.txt` | V2Ray / VMess / VLESS 等 |
| `subscriptions/mixed.txt` | 混合协议 |

### 手动节点

`nodes/example.yaml` 提供 Clash 格式节点示例，可按需修改后导入。

---

## 自动更新

已配置 GitHub Actions：

- 每天定时运行（UTC 02:00）
- 可在 Actions 页手动触发 **Update Free Nodes**

在 `scripts/update_subscriptions.py` 的 `SOURCES` 中填入你信任的公开订阅地址后，工作流会自动拉取并写入 `subscriptions/`。

---

## 目录结构

```
├── README.md
├── LICENSE
├── update.log
├── .github/workflows/update-nodes.yml
├── scripts/update_subscriptions.py
├── subscriptions/
└── nodes/
```

---

## 推荐客户端

| 平台 | 软件示例 |
|------|----------|
| Windows | Clash Verge Rev / Mihomo Party / V2RayN |
| macOS | Clash Verge Rev / Surge |
| Android | Clash Meta / v2rayNG |
| iOS | Shadowrocket / Stash / Quantumult X |
| Linux | mihomo / Clash Meta |

---

## 免责

内容仅供学习与测试。使用风险自负。禁止用于违法用途。

## License

MIT License
