from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
from datetime import datetime
from config import config

# 加载环境变量
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv未安装，使用系统环境变量

app = Flask(__name__)

# 获取配置
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])

# 初始化邮件扩展
mail = Mail(app)

# 获取接收咨询邮件的邮箱地址
RECIPIENT_EMAIL = app.config.get('RECIPIENT_EMAIL', 'info@qingtengmao.com')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        # 获取表单数据
        data = request.get_json()
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        service = data.get('service', '').strip()
        message = data.get('message', '').strip()
        
        # 验证必填字段
        if not all([name, email, phone, message]):
            return jsonify({
                'success': False,
                'message': '请填写所有必填字段'
            }), 400
        
        # 验证邮箱格式
        if '@' not in email or '.' not in email:
            return jsonify({
                'success': False,
                'message': '请输入有效的邮箱地址'
            }), 400
        
        # 服务类型映射
        service_map = {
            'undergraduate': '本科申请',
            'graduate': '研究生申请',
            'phd': '博士申请',
            'background': '背景提升',
            'other': '其他服务'
        }
        service_name = service_map.get(service, service)
        
        # 构建邮件内容
        subject = f'青藤猫教育咨询 - 新咨询申请 ({name})'
        
        html_content = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                <h2 style="color: #5D5CDE; border-bottom: 2px solid #5D5CDE; padding-bottom: 10px;">
                    青藤猫教育咨询 - 新咨询申请
                </h2>
                
                <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #5D5CDE; margin-top: 0;">申请人信息</h3>
                    <p><strong>姓名：</strong>{name}</p>
                    <p><strong>邮箱：</strong>{email}</p>
                    <p><strong>电话：</strong>{phone}</p>
                    <p><strong>咨询项目：</strong>{service_name}</p>
                </div>
                
                <div style="background-color: #fff; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                    <h3 style="color: #5D5CDE; margin-top: 0;">咨询内容</h3>
                    <p style="white-space: pre-wrap;">{message}</p>
                </div>
                
                <div style="margin-top: 20px; padding: 15px; background-color: #e8f5e8; border-radius: 8px;">
                    <p style="margin: 0; color: #2d5a2d;">
                        <strong>提交时间：</strong>{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}
                    </p>
                </div>
                
                <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #666;">
                    <p>此邮件由青藤猫教育咨询网站自动发送，请及时回复客户。</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # 发送邮件
        msg = Message(
            subject=subject,
            recipients=[RECIPIENT_EMAIL],
            html=html_content
        )
        
        mail.send(msg)
        
        # 发送确认邮件给客户
        confirmation_subject = '感谢您的咨询 - 青藤猫教育咨询'
        confirmation_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                <h2 style="color: #5D5CDE; border-bottom: 2px solid #5D5CDE; padding-bottom: 10px;">
                    感谢您的咨询
                </h2>
                
                <p>尊敬的 {name}，</p>
                
                <p>感谢您选择青藤猫教育咨询！我们已收到您的咨询申请，我们的专业顾问将在24小时内与您联系。</p>
                
                <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #5D5CDE; margin-top: 0;">您的咨询信息</h3>
                    <p><strong>咨询项目：</strong>{service_name}</p>
                    <p><strong>提交时间：</strong>{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}</p>
                </div>
                
                <p>如果您有任何紧急问题，请随时联系我们：</p>
                <ul>
                    <li>电话：+86 123-4567-8910</li>
                    <li>邮箱：info@qingtengmao.com</li>
                </ul>
                
                <p>祝您留学申请顺利！</p>
                
                <p>青藤猫教育咨询团队</p>
                
                <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #666;">
                    <p>此邮件为自动发送，请勿直接回复。</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        confirmation_msg = Message(
            subject=confirmation_subject,
            recipients=[email],
            html=confirmation_html
        )
        
        mail.send(confirmation_msg)
        
        return jsonify({
            'success': True,
            'message': '咨询提交成功！我们将在24小时内与您联系。'
        })
        
    except Exception as e:
        print(f"邮件发送错误: {str(e)}")
        return jsonify({
            'success': False,
            'message': '提交失败，请稍后重试或直接联系我们。'
        }), 500

@app.route('/features')
def features():
    return render_template('features.html')

# 留学服务相关路由
@app.route('/undergraduate')
def undergraduate():
    return render_template('placeholder.html', title='本科申请服务', description='专业的本科申请指导，助您圆梦名校')

@app.route('/master')
def master():
    return render_template('placeholder.html', title='硕士申请服务', description='专业的硕士申请指导，助您圆梦名校')

@app.route('/phd')
def phd():
    return render_template('placeholder.html', title='博士申请服务', description='专业的博士申请指导，助您圆梦名校')

@app.route('/background')
def background():
    return render_template('placeholder.html', title='背景提升服务', description='专业的背景提升指导，增强您的申请竞争力')

@app.route('/language')
def language():
    return render_template('placeholder.html', title='语言培训服务', description='专业的语言培训指导，提升您的语言能力')

@app.route('/language_training')
def language_training():
    return render_template('placeholder.html', title='语言培训服务', description='专业的语言培训指导，提升您的语言能力')

# 其他服务路由
@app.route('/services')
def services():
    return render_template('placeholder.html', title='服务项目', description='了解我们提供的所有留学服务项目')

@app.route('/about')
def about():
    return render_template('placeholder.html', title='关于我们', description='了解青藤猫教育咨询有限公司')

# 关于我们相关路由
@app.route('/team')
def team():
    return render_template('placeholder.html', title='专家团队', description='认识我们的专业顾问团队')

@app.route('/success_cases')
def success_cases():
    return render_template('placeholder.html', title='成功案例', description='查看我们的成功申请案例')

@app.route('/news')
def news():
    return render_template('placeholder.html', title='新闻动态', description='了解最新的留学资讯和公司动态')

@app.route('/join')
def join():
    return render_template('placeholder.html', title='加入我们', description='加入青藤猫，开启您的职业新篇章')

# 法律信息相关路由
@app.route('/privacy')
def privacy():
    return render_template('placeholder.html', title='隐私政策', description='了解我们的隐私保护政策')

@app.route('/terms')
def terms():
    return render_template('placeholder.html', title='服务条款', description='了解我们的服务条款')

@app.route('/disclaimer')
def disclaimer():
    return render_template('placeholder.html', title='免责声明', description='了解我们的免责声明')

@app.route('/cookie')
def cookie():
    return render_template('placeholder.html', title='Cookie 政策', description='了解我们的Cookie使用政策')

# 额外的路由（features.html中使用的）
@app.route('/undergraduate_application')
def undergraduate_application():
    return render_template('placeholder.html', title='本科申请服务', description='专业的本科申请指导，助您圆梦名校')

@app.route('/graduate_application')
def graduate_application():
    return render_template('placeholder.html', title='硕士申请服务', description='专业的硕士申请指导，助您圆梦名校')

@app.route('/phd_application')
def phd_application():
    return render_template('placeholder.html', title='博士申请服务', description='专业的博士申请指导，助您圆梦名校')

@app.route('/background_enhancement')
def background_enhancement():
    return render_template('placeholder.html', title='背景提升服务', description='专业的背景提升指导，增强您的申请竞争力')

@app.route('/company_profile')
def company_profile():
    return render_template('placeholder.html', title='公司简介', description='了解青藤猫教育咨询有限公司')

@app.route('/expert_team')
def expert_team():
    return render_template('placeholder.html', title='专家团队', description='认识我们的专业顾问团队')

@app.route('/news_and_events')
def news_and_events():
    return render_template('placeholder.html', title='新闻动态', description='了解最新的留学资讯和公司动态')

@app.route('/join_us')
def join_us():
    return render_template('placeholder.html', title='加入我们', description='加入青藤猫，开启您的职业新篇章')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('placeholder.html', title='隐私政策', description='了解我们的隐私保护政策')

@app.route('/service_terms')
def service_terms():
    return render_template('placeholder.html', title='服务条款', description='了解我们的服务条款')

@app.route('/cookie_policy')
def cookie_policy():
    return render_template('placeholder.html', title='Cookie 政策', description='了解我们的Cookie使用政策')

if __name__ == '__main__':
    app.run(debug=True) 