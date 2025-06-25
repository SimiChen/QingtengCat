# 邮件功能配置说明

## 概述
青藤猫教育咨询网站已集成邮件发送功能，当用户提交咨询表单时，系统会：
1. 将咨询信息发送到指定的接收邮箱
2. 向用户发送确认邮件

## 配置步骤

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境变量
创建 `.env` 文件并配置以下环境变量：

```bash
# Flask环境配置
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# 邮件服务器配置
MAIL_SERVER=smtp.qq.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USE_SSL=false
MAIL_USERNAME=your-email@qq.com
MAIL_PASSWORD=your-qq-email-app-password
MAIL_DEFAULT_SENDER=your-email@qq.com

# 接收咨询邮件的邮箱地址
RECIPIENT_EMAIL=info@qingtengmao.com
```

### 3. 邮箱配置说明

#### QQ邮箱配置
1. 登录QQ邮箱
2. 进入"设置" -> "账户"
3. 开启"POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 获取授权码（不是QQ密码）
5. 使用授权码作为 `MAIL_PASSWORD`

#### Gmail配置
1. 登录Gmail
2. 开启两步验证
3. 生成应用专用密码
4. 使用应用专用密码作为 `MAIL_PASSWORD`

#### 163邮箱配置
1. 登录163邮箱
2. 进入"设置" -> "POP3/SMTP/IMAP"
3. 开启SMTP服务
4. 获取授权码
5. 使用授权码作为 `MAIL_PASSWORD`

### 4. 安装python-dotenv（可选）
为了自动加载.env文件，建议安装python-dotenv：

```bash
pip install python-dotenv
```

然后在app.py中添加：
```python
from dotenv import load_dotenv
load_dotenv()
```

## 测试邮件功能

1. 启动应用：
```bash
python app.py
```

2. 访问联系页面：http://localhost:5000/contact

3. 填写并提交表单

4. 检查：
   - 接收邮箱是否收到咨询邮件
   - 用户邮箱是否收到确认邮件

## 邮件内容

### 发送给公司的咨询邮件包含：
- 申请人姓名、邮箱、电话
- 咨询项目类型
- 详细咨询内容
- 提交时间

### 发送给用户的确认邮件包含：
- 感谢信息
- 咨询项目确认
- 联系方式
- 预计回复时间

## 故障排除

### 常见错误及解决方案

1. **SMTP认证失败**
   - 检查邮箱地址和密码是否正确
   - 确认是否使用了授权码而不是登录密码
   - 检查邮箱是否开启了SMTP服务

2. **连接超时**
   - 检查网络连接
   - 确认SMTP服务器地址和端口正确
   - 检查防火墙设置

3. **邮件发送失败**
   - 检查接收邮箱地址是否正确
   - 确认发件人邮箱配置正确
   - 查看应用日志获取详细错误信息

### 调试模式
在开发环境中，设置 `MAIL_DEBUG=true` 可以查看详细的SMTP通信日志。

## 安全注意事项

1. **不要将邮箱密码提交到代码仓库**
2. **使用环境变量管理敏感信息**
3. **定期更换邮箱授权码**
4. **在生产环境中使用强密码**

## 生产环境部署

1. 设置 `FLASK_ENV=production`
2. 使用强密码作为 `SECRET_KEY`
3. 配置生产环境的邮件服务器
4. 设置适当的邮件发送频率限制
5. 监控邮件发送日志 