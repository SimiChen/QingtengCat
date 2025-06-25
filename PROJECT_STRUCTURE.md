# 青藤猫教育咨询网站项目结构

## 项目概述
这是一个基于Flask框架的国际教育咨询公司网站，提供留学申请服务。网站采用现代化的响应式设计，支持深色模式切换。

## 技术栈
- **后端**: Flask (Python)
- **前端**: HTML5, CSS3, JavaScript
- **样式框架**: Tailwind CSS
- **动画库**: AOS (Animate On Scroll)
- **图标**: SVG图标库

## 项目结构

```
qingtengcat/
├── app.py                          # Flask主应用文件
├── demo.html                       # 演示文件
├── requirements.txt                # Python依赖包列表（完整版）
├── requirements-minimal.txt        # Python依赖包列表（最小版）
├── PROJECT_STRUCTURE.md            # 项目结构文档
│
├── .idea/                          # PyCharm IDE配置
│   ├── .gitignore
│   ├── misc.xml
│   ├── modules.xml
│   ├── qingtengcat.iml
│   ├── vcs.xml
│   ├── workspace.xml
│   └── inspectionProfiles/
│       └── profiles_settings.xml
│
├── static/                         # 静态资源目录
│   ├── css/
│   │   └── shared.css              # 共享CSS样式文件
│   │
│   ├── js/
│   │   ├── darkMode.js             # 深色模式管理脚本
│   │   └── navbar.js               # 导航栏加载脚本
│   │
│   └── svg/                        # SVG图标库
│       ├── ad.svg                  # 安道尔
│       ├── ae.svg                  # 阿联酋
│       ├── af.svg                  # 阿富汗
│       ├── ag.svg                  # 安提瓜和巴布达
│       ├── ai.svg                  # 安圭拉
│       ├── al.svg                  # 阿尔巴尼亚
│       ├── am.svg                  # 亚美尼亚
│       ├── ao.svg                  # 安哥拉
│       ├── aq.svg                  # 南极洲
│       ├── ar.svg                  # 阿根廷
│       ├── as.svg                  # 美属萨摩亚
│       ├── at.svg                  # 奥地利
│       ├── au.svg                  # 澳大利亚
│       ├── aw.svg                  # 阿鲁巴
│       ├── ax.svg                  # 奥兰群岛
│       ├── az.svg                  # 阿塞拜疆
│       ├── ba.svg                  # 波斯尼亚和黑塞哥维那
│       ├── bb.svg                  # 巴巴多斯
│       ├── bd.svg                  # 孟加拉国
│       ├── be.svg                  # 比利时
│       ├── bf.svg                  # 布基纳法索
│       ├── bg.svg                  # 保加利亚
│       ├── bh.svg                  # 巴林
│       ├── bi.svg                  # 布隆迪
│       ├── bj.svg                  # 贝宁
│       ├── bl.svg                  # 圣巴泰勒米
│       ├── bm.svg                  # 百慕大
│       ├── bn.svg                  # 文莱
│       ├── bo.svg                  # 玻利维亚
│       ├── bq.svg                  # 荷属安的列斯
│       ├── br.svg                  # 巴西
│       ├── bs.svg                  # 巴哈马
│       ├── bt.svg                  # 不丹
│       ├── bv.svg                  # 布韦岛
│       ├── bw.svg                  # 博茨瓦纳
│       ├── by.svg                  # 白俄罗斯
│       ├── bz.svg                  # 伯利兹
│       ├── ca.svg                  # 加拿大
│       ├── cc.svg                  # 科科斯群岛
│       ├── cd.svg                  # 刚果民主共和国
│       ├── cf.svg                  # 中非共和国
│       ├── cg.svg                  # 刚果共和国
│       ├── ch.svg                  # 瑞士
│       ├── ci.svg                  # 科特迪瓦
│       ├── ck.svg                  # 库克群岛
│       ├── pn.svg                  # 皮特凯恩群岛
│       ├── pr.svg                  # 波多黎各
│       ├── ps.svg                  # 巴勒斯坦
│       ├── pt.svg                  # 葡萄牙
│       ├── pw.svg                  # 帕劳
│       ├── py.svg                  # 巴拉圭
│       ├── qa.svg                  # 卡塔尔
│       ├── re.svg                  # 留尼汪
│       ├── ro.svg                  # 罗马尼亚
│       ├── rs.svg                  # 塞尔维亚
│       ├── ru.svg                  # 俄罗斯
│       ├── rw.svg                  # 卢旺达
│       ├── sa.svg                  # 沙特阿拉伯
│       ├── sb.svg                  # 所罗门群岛
│       ├── sc.svg                  # 塞舌尔
│       ├── sd.svg                  # 苏丹
│       ├── se.svg                  # 瑞典
│       ├── sg.svg                  # 新加坡
│       ├── sh.svg                  # 圣赫勒拿
│       ├── si.svg                  # 斯洛文尼亚
│       ├── sj.svg                  # 斯瓦尔巴和扬马延
│       ├── sk.svg                  # 斯洛伐克
│       ├── sl.svg                  # 塞拉利昂
│       ├── sm.svg                  # 圣马力诺
│       ├── sn.svg                  # 塞内加尔
│       ├── so.svg                  # 索马里
│       ├── sr.svg                  # 苏里南
│       ├── ss.svg                  # 南苏丹
│       ├── st.svg                  # 圣多美和普林西比
│       ├── sv.svg                  # 萨尔瓦多
│       ├── sx.svg                  # 荷属圣马丁
│       ├── sy.svg                  # 叙利亚
│       ├── sz.svg                  # 斯威士兰
│       ├── tc.svg                  # 特克斯和凯科斯群岛
│       ├── td.svg                  # 乍得
│       ├── tf.svg                  # 法属南部领地
│       ├── tg.svg                  # 多哥
│       ├── th.svg                  # 泰国
│       ├── tj.svg                  # 塔吉克斯坦
│       ├── tk.svg                  # 托克劳
│       ├── tl.svg                  # 东帝汶
│       ├── tm.svg                  # 土库曼斯坦
│       ├── tn.svg                  # 突尼斯
│       ├── to.svg                  # 汤加
│       ├── tr.svg                  # 土耳其
│       ├── tt.svg                  # 特立尼达和多巴哥
│       ├── tv.svg                  # 图瓦卢
│       ├── tw.svg                  # 台湾
│       ├── tz.svg                  # 坦桑尼亚
│       ├── ua.svg                  # 乌克兰
│       ├── ug.svg                  # 乌干达
│       ├── um.svg                  # 美国本土外小岛屿
│       ├── us.svg                  # 美国
│       ├── uy.svg                  # 乌拉圭
│       ├── uz.svg                  # 乌兹别克斯坦
│       ├── va.svg                  # 梵蒂冈
│       ├── vc.svg                  # 圣文森特和格林纳丁斯
│       ├── ve.svg                  # 委内瑞拉
│       ├── vg.svg                  # 英属维尔京群岛
│       ├── vi.svg                  # 美属维尔京群岛
│       ├── vn.svg                  # 越南
│       ├── vu.svg                  # 瓦努阿图
│       ├── wf.svg                  # 瓦利斯和富图纳
│       ├── ws.svg                  # 萨摩亚
│       ├── xk.svg                  # 科索沃
│       ├── ye.svg                  # 也门
│       ├── yt.svg                  # 马约特
│       ├── za.svg                  # 南非
│       ├── zm.svg                  # 赞比亚
│       └── zw.svg                  # 津巴布韦
│
├── templates/                      # HTML模板目录
│   ├── components/                 # 可复用组件
│   │   ├── navbar.html             # 导航栏组件
│   │   └── footer.html             # 页脚组件
│   │
│   ├── contact.html                # 联系我们页面
│   ├── features.html               # 特色服务页面
│   ├── index.html                  # 首页
│   └── placeholder.html            # 占位页面模板
│
└── __pycache__/                    # Python缓存文件
    └── app.cpython-312.pyc
```

## 核心文件说明

### 后端文件
- **app.py**: Flask主应用文件，包含所有路由定义
  - 首页路由 (`/`)
  - 联系我们路由 (`/contact`)
  - 特色服务路由 (`/features`)
  - 留学服务相关路由 (本科、硕士、博士、背景提升、语言培训)
  - 其他服务路由 (服务项目、关于我们等)
  - 法律信息相关路由 (隐私政策、服务条款等)

### 依赖管理文件
- **requirements.txt**: 完整版Python依赖包列表
  - 包含Flask及其所有子依赖
  - 包含未来可能需要的扩展包（已注释）
  - 适用于开发和测试环境
- **requirements-minimal.txt**: 最小版Python依赖包列表
  - 只包含当前项目实际使用的Flask
  - 适用于生产环境部署
  - 减少不必要的依赖包

### 前端模板
- **index.html**: 网站首页，包含完整的营销内容
- **contact.html**: 联系我们页面，包含联系表单
- **features.html**: 特色服务页面，展示不同国家的留学服务
- **placeholder.html**: 通用占位页面模板，用于未完成的页面

### 组件
- **navbar.html**: 响应式导航栏组件，包含深色模式切换
- **footer.html**: 页脚组件，包含联系信息和链接

### 静态资源
- **shared.css**: 共享CSS样式，包含深色模式、动画等
- **darkMode.js**: 深色模式管理脚本，支持状态持久化
- **navbar.js**: 导航栏加载脚本
- **svg/**: 完整的国家国旗SVG图标库

## 功能特性

### 1. 响应式设计
- 支持桌面端、平板和移动端
- 使用Tailwind CSS实现响应式布局

### 2. 深色模式
- 支持亮色/暗色主题切换
- 状态持久化存储
- 系统主题跟随
- 平滑切换动画

### 3. 动画效果
- 使用AOS库实现滚动动画
- 自定义CSS动画
- 悬停效果和过渡动画

### 4. 组件化架构
- 导航栏和页脚组件化
- 可复用的HTML组件
- 统一的样式管理

### 5. 多语言支持
- 支持中英文内容
- 国际化图标库

## 运行方式

### 1. 安装Python依赖

#### 方式一：使用完整版依赖（推荐用于开发）
```bash
pip install -r requirements.txt
```

#### 方式二：使用最小版依赖（推荐用于生产）
```bash
pip install -r requirements-minimal.txt
```

#### 方式三：手动安装Flask
```bash
pip install flask
```

### 2. 运行应用
```bash
python app.py
```

### 3. 访问网站
```
http://localhost:5000
```

### 4. 开发模式
应用默认运行在开发模式（debug=True），支持：
- 热重载（代码修改后自动重启）
- 详细的错误信息
- 调试工具栏

### 5. 生产部署
生产环境建议：
```bash
# 安装生产服务器
pip install gunicorn

# 运行生产服务器
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 开发说明

- 使用Flask的模板继承和组件化
- 静态资源通过Flask的`url_for`函数引用
- 支持热重载开发模式
- 使用Jinja2模板引擎

## 部署建议

- 生产环境建议使用Gunicorn或uWSGI
- 静态文件建议使用CDN加速
- 数据库可根据需要添加
- 建议添加日志记录和错误处理 