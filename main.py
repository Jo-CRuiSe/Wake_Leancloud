import requests

def get_status(url):
    
    r=requests.get(url=url)

    return r.status_code

def main():
    status=get_status("https://console-e1.leancloud.cn/") #修改为自己的valine评论地址

    if status==200:
        print("激活成功！HTTP状态码为：",status)
    else:
        print("激活失败！HTTP状态码为：",status)

if __name__ == "__main__":
    main()
    
