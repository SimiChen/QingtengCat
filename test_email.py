#!/usr/bin/env python3
"""
邮件功能测试脚本
用于验证邮件配置是否正确
"""

import os
import sys
from datetime import datetime

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("警告: python-dotenv未安装，将使用系统环境变量")

from flask import Flask
from flask_mail import Mail, Message
from config import config

def test_email_config():
    """测试邮件配置"""
    print("=== 青藤猫教育咨询网站 - 邮件功能测试 ===\n")
    
    # 创建测试应用
    app = Flask(__name__)
    app.config.from_object(config['development'])
    
    # 检查配置
    print("1. 检查邮件配置:")
    print(f"   MAIL_SERVER: {app.config.get('MAIL_SERVER', '未设置')}")
    print(f"   MAIL_PORT: {app.config.get('MAIL_PORT', '未设置')}")
    print(f"   MAIL_USE_TLS: {app.config.get('MAIL_USE_TLS', '未设置')}")
    print(f"   MAIL_USERNAME: {app.config.get('MAIL_USERNAME', '未设置')}")
    print(f"   MAIL_PASSWORD: {'已设置' if app.config.get('MAIL_PASSWORD') else '未设置'}")
    print(f"   RECIPIENT_EMAIL: {app.config.get('RECIPIENT_EMAIL', '未设置')}")
    print()
    
    # 检查必要的配置
    required_configs = ['MAIL_USERNAME', 'MAIL_PASSWORD', 'RECIPIENT_EMAIL']
    missing_configs = []
    
    for config_name in required_configs:
        if not app.config.get(config_name):
            missing_configs.append(config_name)
    
    if missing_configs:
        print("❌ 缺少必要的邮件配置:")
        for config_name in missing_configs:
            print(f"   - {config_name}")
        print("\n请检查.env文件或环境变量设置")
        return False
    
    print("✅ 邮件配置检查通过")
    print()
    
    # 初始化邮件扩展
    mail = Mail(app)
    
    # 测试邮件发送
    print("2. 测试邮件发送:")
    
    try:
        with app.app_context():
            # 发送测试邮件
            test_subject = f'青藤猫邮件功能测试 - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            test_body = f"""
            <html>
            <body>
                <h2>邮件功能测试</h2>
                <p>这是一封测试邮件，用于验证青藤猫教育咨询网站的邮件功能是否正常工作。</p>
                <p>发送时间: {datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}</p>
                <p>如果您收到这封邮件，说明邮件功能配置正确！</p>
            </body>
            </html>
            """
            
            msg = Message(
                subject=test_subject,
                recipients=[app.config.get('RECIPIENT_EMAIL')],
                html=test_body
            )
            
            mail.send(msg)
            print("✅ 测试邮件发送成功！")
            print(f"   接收邮箱: {app.config.get('RECIPIENT_EMAIL')}")
            print("   请检查接收邮箱是否收到测试邮件")
            
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        print("\n可能的解决方案:")
        print("1. 检查邮箱地址和密码是否正确")
        print("2. 确认是否使用了授权码而不是登录密码")
        print("3. 检查邮箱是否开启了SMTP服务")
        print("4. 检查网络连接")
        return False

def main():
    """主函数"""
    try:
        success = test_email_config()
        if success:
            print("\n🎉 邮件功能测试完成！")
            print("现在可以启动应用并测试联系表单了")
        else:
            print("\n❌ 邮件功能测试失败")
            print("请根据错误信息修复配置后重试")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n测试被用户中断")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 测试过程中发生错误: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main() 