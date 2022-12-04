import json

def help():
    help = """
    将子域名放到domain.txt，脚本会默认为子域加入通配符*
    例如：
    baidu.com
    jd.com
    运行脚本，生成new_file.json，为白名单配置文件。之后导入即可
    python3 firefox-proxy.py
    help不影响运行结果
    """
    print(help)

white_json = {
  "whitePatterns": [
    {
      "title": "1ighttack",
      "pattern": "burpsuite*",
      "type": 1,
      "protocols": 1,
      "active": True
    },
  ],
  "blackPatterns": []
}

def openfiles():
    new_file = open('new_file.json','w')

    with open('domain.txt', 'r+') as f:
        for domain in f.readlines():
            domain = domain.strip()
            add_json = {
                      "title": "1ighttack",
                      "pattern": "*.{}".format(domain),
                      "type": 1,
                      "protocols": 1,
                      "active": True
            }
            white_json["whitePatterns"].append(add_json)
        new_file.write(json.dumps(white_json, sort_keys=True, indent=4, separators=(', ', ': ')))

if __name__ == '__main__':
    help()
    openfiles()