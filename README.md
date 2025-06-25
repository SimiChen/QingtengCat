# 青藤猫教育咨询网站

## 项目简介
青藤猫教育咨询网站是一个基于Flask框架的国际教育咨询公司网站，提供留学申请服务。网站采用现代化的响应式设计，支持深色模式切换。

## 快速开始

### 环境要求
- Python 3.7+
- pip

### 安装依赖

#### 开发环境（推荐）
```bash
pip install -r requirements.txt
```

#### 生产环境（最小依赖）
```bash
pip install -r requirements-minimal.txt
```

#### 手动安装
```bash
pip install flask
```

### 运行项目
```bash
python app.py
```

### 访问网站
打开浏览器访问：http://localhost:5000

## 项目特性

- ✅ 响应式设计，支持多设备访问
- ✅ 深色模式切换，支持状态持久化
- ✅ 组件化架构，可复用的HTML组件
- ✅ 现代化UI设计，使用Tailwind CSS
- ✅ 平滑动画效果，使用AOS库
- ✅ 完整的路由系统，支持多页面
- ✅ 国际化图标库，支持多国家

## 项目结构

```
qingtengcat/
├── app.py                    # Flask主应用
├── requirements.txt          # 完整依赖列表
├── requirements-minimal.txt  # 最小依赖列表
├── static/                   # 静态资源
│   ├── css/shared.css       # 共享样式
│   ├── js/                  # JavaScript文件
│   └── svg/                 # 国家图标库
├── templates/               # HTML模板
│   ├── components/          # 可复用组件
│   └── *.html              # 页面模板
└── README.md               # 项目说明
```

## 主要页面

- **首页** (`/`) - 完整的营销页面
- **联系我们** (`/contact`) - 联系表单
- **特色服务** (`/features`) - 国家选择页面
- **留学服务** - 本科、硕士、博士申请等

## 开发说明

### 开发模式
项目默认运行在开发模式，支持：
- 热重载（代码修改后自动重启）
- 详细的错误信息
- 调试工具栏

### 生产部署
生产环境建议使用Gunicorn：
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 技术栈

- **后端**: Flask (Python)
- **前端**: HTML5 + CSS3 + JavaScript
- **样式**: Tailwind CSS
- **动画**: AOS库
- **图标**: SVG图标库

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证。

## 联系方式

如有问题或建议，请联系项目维护者。 