'''我的主页'''
import streamlit as st
import os
from PIL import Image
from reportlab.pdfgen import canvas
import time

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '我的网址推荐', '我的老挝'])
st.audio("See_You_Again.mp3")
str_1 = "大 家 好 我 是 周 子 洋 ， 欢 迎 来 到 我 的 主 页 ， 这 是 我 去 年 去 厦 门 时 拍 的 照 片"
str_2 = "我 很 喜 欢 打 篮 球 ， 我 的 偶 像 是 科 比 · 布 莱 恩 特 ， 我 也 很 喜 欢 旅 行  ， 我 喜 欢 航 拍 。 你 还 可 以 通 过 右 侧 边 栏 来 体 验 更 多 功 能 :blush:"
def page_1():
    '''我的兴趣推荐'''
    st.header('兴趣推荐', divider='rainbow')
    if st.button('开始你的奇幻之旅'):
        st.balloons()
        st.write_stream(introduce_1)
        st.write_stream(introduce_2)

def page_2():
    '''我的图片处理工具'''
    st.header('图片处理工具', divider='rainbow')
    upload_file = st.file_uploader("上传图片", type=['png', 'jpg', 'jpeg'])
    if upload_file:
        tab_1, tab_2 , tab_3, tab_4, tab_5 , tab_6, tab_7, tab_8, tab_9= st.tabs(['原图', '换色(1)', '换色(2)', '换色(3)', '反色', '图片转PDF(请选择当前目录的文件)', '增强对比度', '黑白滤镜', '叠加效果'])
        file_name = upload_file.name
        file_type = upload_file.type
        file_size = upload_file.size
        image = Image.open(upload_file)
        opposite_image = Image.open(upload_file)
        PDF_image = Image.open(upload_file)
        All_image = Image.open(upload_file)
        co_image = Image.open(upload_file)
        bw_image = Image.open(upload_file)
        with tab_1:
            st.image(image)
        with tab_2:
            st.write('右键"另存为"保存图片')
            st.image(img_change(image, 0, 2, 1))
        with tab_3:
            st.write('右键"另存为"保存图片')
            st.image(img_change(image, 1, 0, 2))
        with tab_4:
            st.write('右键"另存为"保存图片')
            st.image(img_change(image, 2, 1, 0))
        with tab_5:
            st.write('右键"另存为"保存图片')
            st.image(img_opposite_color(opposite_image))
        with tab_6:
            try:
                c = canvas.Canvas("PDF.pdf", pagesize = (PDF_image.width, PDF_image.height))
                c.drawImage(file_name, 0, 0, mask="auto")
                c.save()
                st.success("PDF生成成功, 请到当前目录查看:satisfied:")
            except:
                st.error("PDF生成失败,请检查文件是否在当前目录下:pensive:")
        with tab_7:
            st.write('右键"另存为"保存图片')
            st.image(img_change_co(co_image))
        with tab_8:
            st.write('右键"另存为"保存图片')
            st.image(img_change_bw(bw_image))
        with tab_9:
            col1, col2, col3 = st.columns([4, 4, 4])
            with col1:
                st.image(image)
            with col2:
                ch = st.toggle('反色滤镜')
                co = st.toggle('增强对比度')
                bw = st.toggle('黑白滤镜')
            with col3:
                st.write('对图片进行反色处理')
                st.write('让图片颜色更加鲜艳')
                st.write('将图片变为灰度图')
            # 点击按钮处理图片
            b = st.button('开始处理')
            if b:
                if ch:
                    All_image = img_opposite_color(All_image)
                if co:
                    All_image = img_change_co(All_image)
                if bw:
                    All_image = img_change_bw(All_image)
                st.write('右键"另存为"保存图片')
                st.image(All_image)

def page_3():
    '''我的智能词典'''
    st.header('智能词典', divider='rainbow')
    with open("words_space.txt", "r", encoding="utf-8") as f:
        words_list = f.read().split('\n')
    
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    words_dict = {}
    for word in words_list:
        words_dict[word[1]] = [int(word[0]), word[2]]

    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])

    word = st.text_input("请输入要查询的单词")
    st.link_button('点我试试', 'https://www.yuanshen.com/#/')
    if word in words_dict:
        cixing, mean = words_dict[word][1].split('.')
        st.write('解释：', mean)
        st.caption('词性：' + cixing + '.')
        st.caption('词典中的第' + str(words_dict[word][0]) + '个单词')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.caption('查询次数：' + str(times_dict[n]))
    
    elif word != '' and word not in words_dict:
        st.error('抱歉，没有找到该单词')

    elif word == 'python':
        st.code('''
        #恭喜你发现彩蛋
        print("hello world")
    ''')
        st.balloons()

    elif word == '周子洋':
        st.write(":rainbow[你好，我是周子洋，很高兴认识你!]")
        st.balloons()

    if word in words_dict:
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        
def page_4():
    '''我的留言区'''
    st.header('留言区', divider='rainbow')
    with open("leave_messages.txt", "r", encoding="utf-8") as f:
        messages_list = f.read().split('\n')
    
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message('🌞'):
                st.text(f'{i[1]}:{i[2]}')
        elif i[1] == '编程猫':
            with st.chat_message('🌝'):
                st.text(f'{i[1]}:{i[2]}')
        elif i[1] == '周子洋':
            with st.chat_message('🎖️'):
                st.write(f'{i[1]}:{i[2]}')
        else:
            with st.chat_message('🎩'):
                st.text(f'{i[1]}:{i[2]}')
    name = st.text_input('你的名字:')
    new_message = st.text_input('说点什么...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n' 
            message = message[:-1]
            f.write(message)
def page_5():
    '''我的网址推荐'''
    st.header('网址推荐', divider='rainbow')
    com = st.selectbox('请选择网站', 
                       ['BLD ezine', '中国法律法规数据库', '国家中小学智慧教育平台', 'CCTV节目官网', 'CSDN', 
                        'Github', 'Gitee', '通义千问', 'OpenAI', 'Microsoft Visual Studio', '通义灵码', 'DJI大疆创新', "卡巴斯基网络威胁实时地图", "在线黑客模拟网站"]
                       )
    com_dict = {
        'BLD ezine': 'https://bld_ezine.gitee.io/',
        '中国法律法规数据库': 'https://flk.npc.gov.cn/',
        '国家中小学智慧教育平台': 'https://basic.smartedu.cn/',
        'CCTV节目官网': 'https://tv.cctv.com/live/',
        'CSDN': 'https://www.csdn.net/',
        'Github': 'https://github.com/',
        'Gitee': 'https://gitee.com/',
        '通义千问': 'https://tongyi.aliyun.com/qianwen/',
        'OpenAI': 'https://openai.com/',
        'Microsoft Visual Studio': 'https://visualstudio.microsoft.com',
        '通义灵码': 'https://tongyi.aliyun.com/lingma/', 
        'DJI大疆创新': 'https://www.dji.com/', 
        '卡巴斯基网络威胁实时地图': 'https://cybermap.kaspersky.com/', 
        '在线黑客模拟网站' : 'https://pranx.com/hacker/'
    }
    st.link_button(f'跳转到：{com}', com_dict[com])

def page_6():
    '''我的老挝'''
    st.header('老挝', divider='rainbow')
    com = st.text_input('Bing搜索')
    bing = f'https://cn.bing.com/search?q={com}'
    st.link_button(f'搜索 {com}', bing)
    with st.form("form"):
        input = st.text_input('输入算式：')
        if st.form_submit_button("计算"):
            try:
                st.write(f'答案是：{eval(input)}')
            except:
                st.error('输入错误, 只能输入0-9, + , -, *, /和英文输入法下的()')
    st.link_button('爷要去看视频！', 'https://www.bilibili.com/')
    if st.button('点我逝世'):
        with open('关机.bat', 'w') as f:
            f.write('shutdown -s')
        os.system('关机.bat')
        st.info("文件夹中有取消关机.bat, 运行即可解除！")


def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def img_opposite_color(img):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (255 - r, 255 - g, 255 - b)
    return img


def introduce_1():
    for word in str_1.split():
        yield word
        time.sleep(0.02)

    col_1, col_2 = st.columns(2)
    with col_1:
        st.image("image_1.jpg")
    with col_2:
        st.image("image_2.jpg")

def introduce_2():
    for word in str_2.split():
        yield word
        time.sleep(0.02)
    col_1, col_2 = st.columns([1, 2.32])
    with col_1:
        st.image("image_3.jpg")
    with col_2:
        st.image("image_4.jpg")

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的网址推荐':
    page_5()
elif page == '我的老挝':
    page_6()