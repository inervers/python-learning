import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        resp = requests.get(url, timeout=10)
        print(f"{city}：{resp.text}")
    except requests.ConnectionError:
        print("网络连接失败，请检查网络")
    except Exception as e:
        print(f"出错了：{e}")

if __name__ == "__main__":
    city = input("请输入城市名（英文）：")
    get_weather(city)
