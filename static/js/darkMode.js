// Dark Mode Management
class DarkModeManager {
    constructor() {
        this.isDark = false;
        this.init();
    }

    init() {
        // 从localStorage读取状态
        this.isDark = localStorage.getItem('darkMode') === 'true' || 
                     (!localStorage.getItem('darkMode') && window.matchMedia('(prefers-color-scheme: dark)').matches);
        
        // 应用初始状态
        this.applyDarkMode();
        
        // 绑定事件监听器
        this.bindEvents();
        
        // 监听系统主题变化
        this.watchSystemTheme();
    }

    applyDarkMode() {
        if (this.isDark) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
        
        // 保存状态到localStorage
        localStorage.setItem('darkMode', this.isDark.toString());
        
        // 更新按钮状态
        this.updateButtonStates();
    }

    toggle() {
        this.isDark = !this.isDark;
        this.applyDarkMode();
    }

    updateButtonStates() {
        // 更新桌面端按钮
        const darkModeIcon = document.getElementById('darkModeIcon');
        if (darkModeIcon) {
            if (this.isDark) {
                darkModeIcon.classList.add('translate-x-6');
                darkModeIcon.classList.remove('translate-x-0');
            } else {
                darkModeIcon.classList.remove('translate-x-6');
                darkModeIcon.classList.add('translate-x-0');
            }
        }

        // 更新移动端按钮
        const mobileDarkModeIcon = document.getElementById('mobileDarkModeIcon');
        if (mobileDarkModeIcon) {
            if (this.isDark) {
                mobileDarkModeIcon.classList.add('translate-x-6');
                mobileDarkModeIcon.classList.remove('translate-x-0');
            } else {
                mobileDarkModeIcon.classList.remove('translate-x-6');
                mobileDarkModeIcon.classList.add('translate-x-0');
            }
        }
    }

    bindEvents() {
        // 桌面端深色模式切换
        const darkModeToggle = document.getElementById('darkModeToggle');
        if (darkModeToggle) {
            darkModeToggle.addEventListener('click', () => this.toggle());
        }

        // 移动端深色模式切换
        const mobileDarkModeToggle = document.getElementById('mobileDarkModeToggle');
        if (mobileDarkModeToggle) {
            mobileDarkModeToggle.addEventListener('click', () => this.toggle());
        }
    }

    watchSystemTheme() {
        // 监听系统主题变化
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        mediaQuery.addEventListener('change', (e) => {
            // 只有在用户没有手动设置过主题时才跟随系统
            if (localStorage.getItem('darkMode') === null) {
                this.isDark = e.matches;
                this.applyDarkMode();
            }
        });
    }
}

// 初始化深色模式管理器
document.addEventListener('DOMContentLoaded', function() {
    window.darkModeManager = new DarkModeManager();
}); 