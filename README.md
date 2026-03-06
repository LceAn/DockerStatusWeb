# DockerStatusWeb

> 🐳 基于 Flask 的 Docker 容器状态监控 Web 面板

[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

---

## 📖 简介

DockerStatusWeb 是一个**轻量级 Docker 容器状态监控工具**，基于 Python Flask 框架开发。通过简洁的 Web 界面，实时展示 Docker 容器的运行状态、资源占用和详细信息。

**适用场景：**
- 🖥️ **个人服务器** - 快速查看容器状态
- 🏢 **小型团队** - 简易容器监控方案
- 🧪 **开发环境** - 本地 Docker 管理
- 📊 **数据展示** - 容器信息 Web 化

---

## ✨ 功能特性

| 功能 | 说明 | 状态 |
|------|------|------|
| 📊 **容器列表** | 展示所有容器基本信息 | ✅ |
| 🟢 **状态监控** | 实时显示运行/停止状态 | ✅ |
| 📈 **资源信息** | CPU、内存占用展示 | ✅ |
| 🔍 **详细信息** | 端口映射、网络、卷挂载 | ✅ |
| 🎨 **美观界面** | 现代化 UI 设计 | ✅ |
| 📱 **响应式** | 适配移动端访问 | ✅ |

---

## 🚀 快速开始

### 前置要求

- Python 3.8+
- Docker & Docker Compose
- pip 包管理器

### 方式一：直接运行

1. **安装依赖**
```bash
pip install -r requirements.txt
```

2. **启动应用**
```bash
python manager.py
```

3. **访问面板**
打开浏览器访问：`http://127.0.0.1:5000`

### 方式二：Docker 运行

```bash
docker run -d \
  -p 5000:5000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name docker-status-web \
  lcean/docker-status-web:latest
```

---

## 📸 界面预览

```
┌─────────────────────────────────────────────────────────────┐
│  DockerStatusWeb                    🐳 v0.2.0               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  容器概览                                                   │
│  ┌─────────┬─────────┬─────────┬─────────┐                 │
│  │  总计   │ 运行中  │  已停止  │  错误   │                 │
│  │   12    │    8    │    3    │    1    │                 │
│  └─────────┴─────────┴─────────┴─────────┘                 │
│                                                             │
│  容器列表                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ nginx-proxy        🟢 运行   0.5% CPU   128MB       │   │
│  │ mysql-db           🟢 运行   2.1% CPU   512MB       │   │
│  │ redis-cache        🟢 运行   0.3% CPU   64MB        │   │
│  │ backup-service     ⚫ 停止   -          -           │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 项目结构

```
DockerStatusWeb/
├── app/
│   ├── __init__.py         # 应用工厂
│   ├── config.py           # 配置文件
│   ├── models/
│   │   ├── __init__.py
│   │   └── model.py        # 数据模型
│   ├── src/                # 静态资源
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/
│   │   └── index.html      # 主页面
│   └── views/
│       ├── __init__.py
│       └── main.py         # 路由处理
├── manager.py              # 启动脚本
├── requirements.txt        # 依赖列表
└── README.md               # 说明文档
```

---

## ⚙️ 配置说明

### 基础配置

编辑 `app/config.py`：

```python
class Config:
    # Flask 配置
    SECRET_KEY = 'your-secret-key'
    DEBUG = False
    
    # 应用配置
    REFRESH_INTERVAL = 5000  # 刷新间隔（毫秒）
    MAX_CONTAINERS = 100     # 最大显示容器数
    
    # Docker 配置
    DOCKER_HOST = 'unix:///var/run/docker.sock'
```

### 环境变量

```bash
# .env 文件
FLASK_ENV=production
FLASK_PORT=5000
FLASK_HOST=0.0.0.0
REFRESH_INTERVAL=5000
```

---

## 🔧 API 接口

### 获取容器列表

```http
GET /api/containers
```

**响应示例：**
```json
{
  "status": "success",
  "data": [
    {
      "id": "abc123",
      "name": "nginx-proxy",
      "status": "running",
      "cpu": "0.5%",
      "memory": "128MB",
      "ports": ["80:80", "443:443"]
    }
  ]
}
```

### 获取容器详情

```http
GET /api/containers/<container_id>
```

---

## 🛠️ 开发指南

### 本地开发

```bash
# 克隆项目
git clone https://github.com/LceAn/DockerStatusWeb.git

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
python manager.py --debug
```

### 添加新功能

1. 在 `app/views/main.py` 添加路由
2. 在 `app/templates/` 添加模板
3. 在 `app/models/model.py` 添加数据模型

---

## 📊 长期规划

| 版本 | 功能 | 状态 |
|------|------|------|
| v0.1 | 基础容器展示 | ✅ 已完成 |
| v0.2 | MVC 架构重构 | ✅ 已完成 |
| v0.3 | 实时数据更新 | 🚧 开发中 |
| v0.4 | 容器管理操作 | 📋 计划中 |
| v0.5 | 多主机支持 | 📋 计划中 |
| v1.0 | 完整监控面板 | 📋 计划中 |

### 未来功能

- [ ] 实时 WebSocket 数据推送
- [ ] 容器启动/停止/重启操作
- [ ] 日志查看功能
- [ ] 资源使用图表
- [ ] 多服务器管理
- [ ] 告警通知功能
- [ ] 类似哪吒探针的精美面板

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 提交 Bug
请提供：
1. 错误信息
2. 复现步骤
3. 环境信息（Python 版本、Docker 版本）

### 功能建议
欢迎提出新功能想法！

---

## 📄 许可证

本项目采用 [MIT License](LICENSE)

---

## 🔗 相关链接

- [Flask 文档](https://flask.palletsprojects.com/)
- [Docker API 文档](https://docs.docker.com/engine/api/)
- [问题反馈](https://github.com/LceAn/DockerStatusWeb/issues)
- [更新日志](https://github.com/LceAn/DockerStatusWeb/commits/main)

---

<div align="center">

**🐳 让 Docker 管理更简单**

Made with ❤️ by LceAn

</div>
