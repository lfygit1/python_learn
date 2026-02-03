import tkinter as tk
import random
import sys
import math


class TipApp:
    def __init__(self):
        self.batch_windows = []
        self.single_window = None
        self.final_window = None
        # 将tips列表定义为实例变量，避免重复
        self.tips = [
            '我们的相遇你遗忘不了',
            '我心里认定是你，那就是你了',
            '还算你眼光不错，最后选了我啊',
            '你的整个存在本身，对我来说都很重要',
            '我当然也是心有所求',
            '程序和结果都不重要，你才重要',
            '我们一定会再次相会',
            '这个世界上如果没有你，该是如何的了无生趣',
            '我愿意被她玩弄感情',
            '但是我的心是有偏向的，它偏向你',
            '你是我独特而不同，不可失去的颜色',
            '凡我所能，无有不应',
            '我的刀柄，始终在您手上',
            '我永远在你身后，而一切会如你所愿',
            '真心是藏不住的陛下',
            '无论是哪里，我都会和你一起去',
        ]

    def create_smooth_gradient(self, canvas, width, height, base_color='pink'):
        """创建平滑渐变背景 - 使用更细腻的渐变"""
        center_x = width // 2
        center_y = height // 2
        max_distance = math.sqrt(center_x ** 2 + center_y ** 2)
        if base_color == 'pink':
            # 更平滑的粉色渐变
            colors = [
                '#FF69B4',  # 热粉色
                '#FF85C1',  # 稍浅
                '#FFA1CF',  # 更浅
                '#FFBDDC',  # 浅粉色
                '#FFD9EA',  # 极浅粉
                '#FFF5F9'  # 几乎白色
            ]
        else:
            # 其他颜色的平滑渐变
            colors = [
                '#FF1493', '#FF69B4', '#FFB6C1', '#FFE4E1'
            ]
        # 使用更细的网格创建平滑渐变
        for x in range(0, width, 3):
            for y in range(0, height, 3):
                distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
                ratio = min(distance / max_distance, 1.0)
                if ratio < 0.2:
                    color = colors[0]
                elif ratio < 0.4:
                    t = (ratio - 0.2) / 0.2
                    color = self.interpolate_color(colors[0], colors[1], t)
                elif ratio < 0.6:
                    t = (ratio - 0.4) / 0.2
                    color = self.interpolate_color(colors[1], colors[2], t)
                elif ratio < 0.8:
                    t = (ratio - 0.6) / 0.2
                    color = self.interpolate_color(colors[2], colors[3], t)
                else:
                    t = (ratio - 0.8) / 0.2
                    color = self.interpolate_color(colors[3], colors[4] if len(colors) > 4 else colors[3], t)
                canvas.create_rectangle(x, y, x + 3, y + 3, fill=color, outline=color)

    def interpolate_color(self, color1, color2, t):
        """在两个颜色之间插值"""
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return f'#{r:02x}{g:02x}{b:02x}'

    def create_heart_gradient(self, canvas, size, base_color):
        """创建渐变爱心 - 优化版，减少锯齿"""
        center_x = size * 20
        center_y = size * 20
        # 根据基础颜色生成渐变颜色组
        if base_color == 'd9c7ef':
            colors = ['#d9c7ef', '#e5d9f5', '#f0ebfa']
        elif base_color == 'f9879a':
            colors = ['#f9879a', '#fca6b4', '#fdc5ce']
        elif base_color == 'cbf1f7':
            colors = ['#cbf1f7', '#dbf5fa', '#ebf9fc']
        elif base_color == 'ffe48f':
            colors = ['#ffe48f', '#ffebad', '#fff2cc']
        else:
            colors = ['#FFB6C1', '#FFC0CB', '#FFD1DC']
        scale_factor = 0.7

        # 大爱心 - 最浅色
        points_large = []
        for t in range(0, 1256, 5):  # 增加点数，减少步长
            t = t / 100
            x = (size + 2) * 16 * (math.sin(t) ** 3) * scale_factor
            y = -(size + 2) * (
                    13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * scale_factor
            points_large.append(x + center_x)
            points_large.append(y + center_y)
        canvas.create_polygon(points_large, fill=colors[2], outline=colors[2], smooth=True)

        # 中爱心 - 中等浅色
        points_medium = []
        for t in range(0, 1256, 5):  # 增加点数，减少步长
            t = t / 100
            x = (size + 1) * 16 * (math.sin(t) ** 3) * scale_factor
            y = -(size + 1) * (
                    13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * scale_factor
            points_medium.append(x + center_x)
            points_medium.append(y + center_y)
        canvas.create_polygon(points_medium, fill=colors[1], outline=colors[1], smooth=True)

        # 小爱心 - 相对较深但仍较浅
        points_small = []
        for t in range(0, 1256, 5):  # 增加点数，减少步长
            t = t / 100
            x = size * 16 * (math.sin(t) ** 3) * scale_factor
            y = -size * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * scale_factor
            points_small.append(x + center_x)
            points_small.append(y + center_y)
        canvas.create_polygon(points_small, fill=colors[0], outline=colors[0], smooth=True)
        return center_x, center_y

    def show_single_tip(self):
        """初始单个弹窗"""
        self.single_window = tk.Tk()
        self.single_window.title('柿柿如意')

        # 屏幕居中显示
        screen_width = self.single_window.winfo_screenwidth()
        screen_height = self.single_window.winfo_screenheight()
        window_width = 350
        window_height = 120
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.single_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 创建画布作为背景
        canvas = tk.Canvas(
            self.single_window,
            width=window_width,
            height=window_height,
            highlightthickness=0
        )
        canvas.pack(fill='both', expand=True)

        # 创建平滑粉色渐变背景
        self.create_smooth_gradient(canvas, window_width, window_height, 'pink')
        # 添加白色文字
        canvas.create_text(
            window_width // 2,
            window_height // 2,
            text="- 世界无限 -",
            fill='white',
            font=('微软雅黑', 23, 'bold'),
            anchor='center'
        )
        # 绑定空格键退出
        self.single_window.bind('<space>', self.on_space_global)
        self.single_window.attributes('-topmost', True)
        # 关闭单个弹窗后，启动批量弹窗
        self.single_window.protocol("WM_DELETE_WINDOW", self.start_batch_tips)
        self.single_window.mainloop()

    def get_tip_color(self, tip):
        """根据提示语内容返回对应的基础颜色"""
        if tip in self.tips[0:4]:
            return 'd9c7ef'
        elif tip in self.tips[4:8]:
            return 'f9879a'
        elif tip in self.tips[8:12]:
            return 'cbf1f7'
        elif tip in self.tips[12:16]:
            return 'ffe48f'
        else:
            return 'pink'

    def get_text_color(self, base_color):
        """根据爱心基础颜色返回合适的文字颜色"""
        if base_color == 'd9c7ef':  # 淡紫色爱心
            return '#5A4FCF'  # 深紫色
        elif base_color == 'f9879a':  # 粉色爱心
            return '#C2185B'  # 深粉色
        elif base_color == 'cbf1f7':  # 淡蓝色爱心
            return '#1565C0'  # 深蓝色
        elif base_color == 'ffe48f':  # 淡黄色爱心
            return '#E65100'  # 深橙色
        else:  # 默认粉色爱心
            return '#C2185B'  # 深粉色

    def create_single_batch_window(self):
        """创建单个批量弹窗"""
        try:
            window = tk.Toplevel()
            self.batch_windows.append(window)

            # 移除窗口装饰
            window.overrideredirect(True)
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            # 窗口尺寸
            heart_size = 10
            window_width = heart_size * 40
            window_height = heart_size * 40

            # 简单随机分布
            max_x = max(0, screen_width - window_width)
            max_y = max(0, screen_height - window_height)

            if max_x > 0 and max_y > 0:
                x = random.randrange(0, max_x)
                y = random.randrange(0, max_y)
            else:
                x = (screen_width - window_width) // 2
                y = (screen_height - window_height) // 2

            window.geometry(f"{window_width}x{window_height}+{x}+{y}")

            # 设置窗口背景为透明
            window.configure(bg='white')
            window.attributes('-transparentcolor', 'white')

            # 创建画布
            canvas = tk.Canvas(
                window,
                width=window_width,
                height=window_height,
                highlightthickness=0,
                bg='white'
            )
            canvas.pack(fill='both', expand=True)

            # 使用实例变量中的tips列表
            tip = random.choice(self.tips)
            base_color = self.get_tip_color(tip)
            text_color = self.get_text_color(base_color)  # 获取合适的文字颜色
            # 创建渐变爱心并获取中心坐标
            heart_center_x, heart_center_y = self.create_heart_gradient(canvas, heart_size, base_color)

            # 在爱心正中心添加文字 - 使用协调的文字颜色
            canvas.create_text(
                heart_center_x,
                heart_center_y,
                text=tip,
                fill=text_color,  # 使用协调的颜色
                font=('幼圆', 17, 'bold'),
                justify='center',
                width=heart_size * 19,
                anchor='center'
            )
            # 绑定空格键退出
            window.bind('<space>', self.on_space_global)
            window.attributes('-topmost', True)

        except Exception as e:
            print(f"创建爱心窗口时出错: {e}")

    def start_batch_tips(self):
        """启动批量弹窗"""
        if self.single_window:
            self.single_window.destroy()
            self.single_window = None

        temp_root = tk.Tk()
        temp_root.withdraw()

        # 增加爱心数量到150个，加快弹出速度
        for i in range(150):
            temp_root.after(50 * i, self.create_single_batch_window)

        temp_root.after(50 * 150 + 1000, lambda: self.show_final_tip(temp_root))

    def show_final_tip(self, temp_root):
        """显示最终弹窗"""
        temp_root.destroy()

        for window in self.batch_windows:
            try:
                window.destroy()
            except Exception:
                pass
        self.batch_windows.clear()

        self.final_window = tk.Tk()
        self.final_window.title('柿柿如意')

        screen_width = self.final_window.winfo_screenwidth()
        screen_height = self.final_window.winfo_screenheight()
        window_width = 350
        window_height = 120
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.final_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        canvas = tk.Canvas(
            self.final_window,
            width=window_width,
            height=window_height,
            highlightthickness=0
        )
        canvas.pack(fill='both', expand=True)

        # 创建平滑粉色渐变背景
        self.create_smooth_gradient(canvas, window_width, window_height, 'pink')
        canvas.create_text(
            window_width // 2,
            window_height // 2,
            text="此爱不变",
            fill='white',
            font=('华文行楷', 39),
            anchor='center'
        )
        self.final_window.protocol("WM_DELETE_WINDOW", self.final_exit)
        self.final_window.attributes('-topmost', True)
        self.final_window.bind('<space>', self.final_exit)
        self.final_window.mainloop()  # 添加mainloop确保窗口显示

    def final_exit(self, event=None):
        if self.final_window:
            self.final_window.destroy()
        sys.exit()

    def on_space_global(self, event=None):
        if self.single_window:
            self.single_window.destroy()

        for window in self.batch_windows:
            try:
                window.destroy()
            except Exception:
                pass
        if self.final_window:
            self.final_window.destroy()
        sys.exit()


if __name__ == '__main__':
    app = TipApp()
    app.show_single_tip()