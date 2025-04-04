
import requests
import time
import os

def main():
    # 获取环境变量中的敏感信息
    cookie = os.environ.get('WEBSITE_COOKIE')
    iyuu_token = os.environ.get('IYUU_TOKEN')
    
    # 请求URL
    sign_url = "https://nb.mcy002.org/wp-admin/admin-ajax.php?_nonce=19eefb6e5c&action=3144d3a38f681c0f2b40ba62c419ba49&type=goSign"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "Cookie": cookie,
        "Referer": "https://nb.mcy002.org/"
    }
    
    result_message = ""
    status_code = 0
    
    try:
        # 发送签到请求
        response = requests.get(sign_url, headers=headers)
        status_code = response.status_code
        
        print(f"状态码: {status_code}")
        print(f"响应内容: {response.text}")
        
        # 尝试解析JSON响应
        try:
            result_json = response.json()
            if 'msg' in result_json:
                result_message = result_json['msg']
            else:
                result_message = response.text[:100]
        except:
            result_message = response.text[:100]
            
    except Exception as e:
        error_msg = f"发生错误: {e}"
        print(error_msg)
        result_message = error_msg
    
    # 发送IYUU通知
    if iyuu_token:
        send_iyuu_notification(iyuu_token, status_code, result_message)

def send_iyuu_notification(iyuu_token, status_code, result_message):
    # 构建通知URL和参数
    notification_url = f"https://iyuu.cn/{iyuu_token}.send"
    
    # 获取当前时间
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    # 构建通知内容
    title = "网站签到结果通知"
    content = f"时间: {current_time}\n状态码: {status_code}\n签到结果: {result_message}"
    
    # 构建请求参数
    params = {
        "text": title,
        "desp": content
    }
    
    try:
        # 发送IYUU通知
        notification_response = requests.get(notification_url, params=params)
        
        # 打印通知结果
        print(f"IYUU通知状态码: {notification_response.status_code}")
        print(f"IYUU通知响应: {notification_response.text}")
        
    except Exception as e:
        print(f"发送IYUU通知失败: {e}")

if __name__ == "__main__":
    main()
