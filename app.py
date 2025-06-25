from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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