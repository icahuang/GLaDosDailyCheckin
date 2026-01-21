import requests
import os

def glados_checkin():
    # 从 GitHub Secrets 中读取 Cookie
    cookie = os.environ.get("GLADOS_COOKIE")
    if not cookie:
        print("未找到 GLADOS_COOKIE，请检查 Secrets 配置。")
        return

    url = "https://glados.network/api/user/checkin"
    url2 = "https://glados.network/api/user/status"
    
    origin = "https://glados.network"
    referer = "https://glados.network/console/checkin"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    
    payload = {'token': 'glados.network'}
    
    headers = {
        'cookie': cookie,
        'referer': referer,
        'origin': origin,
        'user-agent': user_agent,
        'content-type': 'application/json;charset=UTF-8'
    }

    try:
        # 发送签到请求
        response = requests.post(url, headers=headers, json=payload)
        checkin_data = response.json()
        print(f"签到结果: {checkin_data.get('message')}")
        
        # 查询余额/天数状态
        status_res = requests.get(url2, headers=headers)
        status_data = status_res.json()
        if status_data.get('code') == 0:
            left_days = int(float(status_data['data']['leftDays']))
            print(f"剩余会员天数: {left_days} 天")
            
    except Exception as e:
        print(f"签到出错: {e}")

if __name__ == "__main__":
    glados_checkin()