# DockerStatusWeb
基于Python FLask框架编写的Docker容器信息Web展示

# 更新记录
- 20240807_V0.0.1：创建项目，初步实现单端效果
- 20240807_V0.0.2：将目录结构更改为MVC


# 长期规划
1. 多端，设计服务端、客户端
2. 样式准备借鉴哪吒探针面板样式（还是很优雅的）
3. 目前处于开发阶段，脚本仍是原始状态，后期考虑封装为Docker容器，或程序。


# 目录结构
```
.
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   └── model.py
│   ├── src
│   ├── templates
│   │   └── index.html
│   └── views
│       ├── __init__.py
│       └── main.py
└── manager.py
```

# 使用方法
1. 前期准备
   - Python
   1. 安装Python
   2. 需要安装模块
     ```
        Flask
        requests
        psutil
     ```
   - Docker
    1. 安装Docker
    2. 安装监听2375端口容器：socat
    
    ```
        docker run -d --restart=always \
            -p 127.0.0.1:2375:2375 \
            -v /var/run/docker.sock:/var/run/docker.sock \
            alpine/socat \
            tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
    ```

3. 运行
```
python manager.py
```
4. 运行成功后，访问Web页面 `http://127.0.0.1:5000`
   ![image](https://github.com/user-attachments/assets/2f38fa00-c06d-406d-848a-7d7c3d032d46)

