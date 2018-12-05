import redis


def insert_pagelink(str,type):
    try:
        r=redis.Redis(host='192.168.219.129',port=6379,db=0)
    except:
        print('连接redis失败')
    else:
        if type == 1:
            r.lpush('page_link',str)

def insert_nextpage(str,type):
    try:
        r=redis.Redis(host='192.168.219.129',port=6379,db=0)
    except:
        print('连接redis失败')
    else:
        if type == 1:
            r.lpush('next_page',str)
