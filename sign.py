import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auto_sign_in():
    # 从环境变量获取敏感信息
    cookies_str = os.environ.get('COOKIE', '')
    iyuu_token = os.environ.get('IYUU_TOKEN', '')
    
    # IYUU通知URL
    iyuu_url = f"https://iyuu.cn/{iyuu_token}.send"
    
    # 设置浏览器选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式，必须在GitHub Actions中使用
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0')
    
    def send_iyuu_notification(title, content):
        """发送IYUU通知"""
        try:
            params = {
                "text": title,
                "desp": content
            }
            response = requests.get(iyuu_url, params=params)
            print(f"IYUU通知发送状态: {response.status_code}")
            return response.status_code == 200
        except Exception as e:
            print(f"发送IYUU通知时出错: {e}")
            return False
    
    try:
        # 初始化浏览器
        driver = webdriver.Chrome(options=chrome_options)
        
        # 访问网站
        url = 'https://nb.mcy002.org/'
        driver.get(url)
        
        # 解析cookie字符串
        cookie_items = cookies_str.split('; ')
        for cookie_item in cookie_items:
            if '=' in cookie_item:
                name, value = cookie_item.split('=', 1)  # 只在第一个=处分割
                driver.add_cookie({'name': name, 'value': value, 'domain': 'nb.mcy002.org'})
        
        # 刷新页面以应用cookie
        driver.refresh()
        print("已刷新页面并应用cookie")
        
        # 用于跟踪签到状态
        sign_in_success = False
        error_message = ""
        
        # 等待"已阅"按钮加载，并点击
        try:
            print("正在寻找'已阅'按钮...")
            yidu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.poi-dialog__footer__btn.poi-dialog__footer__btn_default[title='']"))
            )
            yidu_button.click()
            print("已成功点击'已阅'按钮")
        except Exception as e:
            error_message = f"点击'已阅'按钮时出错: {e}"
            print(error_message)
        
        # 等待"签到"按钮加载，并点击
        try:
            print("正在寻找'签到'按钮...")
            qiandao_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#inn-nav__point-sign-daily .inn-nav__point-sign-daily__btn[title='签到']"))
            )
            qiandao_button.click()
            print("已成功点击'签到'按钮，签到完成！")
            sign_in_success = True
        except Exception as e:
            error_message = f"点击'签到'按钮时出错: {e}"
            print(error_message)
        
        # 等待一段时间，以便完成操作
        time.sleep(5)
        
        # 发送通知
        if sign_in_success:
            send_iyuu_notification(
                "网站签到成功", 
                f"网站 nb.mcy002.org 已成功签到\n时间：{time.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        else:
            send_iyuu_notification(
                "网站签到失败", 
                f"网站 nb.mcy002.org 签到失败\n时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n错误信息：{error_message}"
            )
        
    except Exception as e:
        error_message = f"程序运行过程中出错: {e}"
        print(error_message)
        send_iyuu_notification(
            "网站签到失败", 
            f"网站 nb.mcy002.org 签到失败\n时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n错误信息：{error_message}"
        )
    
    finally:
        # 关闭浏览器
        try:
            driver.quit()
            print("浏览器已关闭")
        except:
            print("关闭浏览器时出错")

if __name__ == "__main__":
    print("开始自动签到程序...")
    auto_sign_in()
    print("程序执行完毕")
