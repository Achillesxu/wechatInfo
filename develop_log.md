## 2018-05-14
    1. 上传github用于部署服务器
    2. 添加基础的配置文件setting.py
    3. 添加requirements.txt文件
    4. 添加开发日志文件develop_log.md

## 2018-05-19
    1. 添加.gitignore
    2. 添加/msg接口用于接收微信消息
    3. 添加app_get_token_per_2_hour.py周期获取微信的access_token
    4. 测试获取access token的接口

## 2018-05-20
    1. 修改app_get_token_per_2_hour.py及相关文件
    2. 配置测试接口，用于测试
    3. 数据库接入ssdb，连接数据库客户端使用redis.py

## 2018-05-26
    1. 决定基于werebot开发，熟悉库
    2. 接入WeRobot，重写接口
    3. 消息采用加密形式，参数由app_get_token_per_2_hour.py 传入，supervisor调用脚本内
    4. app_id, app_secret, app_aes_key存入数据库
    5. 调试文本及图片消息接口
    6. 消息接口调试

## 2018-05-26
    1. 添加获取分类接口