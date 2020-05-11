https://docs.docker.com/  
http://www.dockerinfo.net/document  
https://www.runoob.com/docker/docker-tutorial.html  

## docker镜像加速
在`/etc/docker/daemon.json`中写入如下内容（如果文件不存在请新建该文件）：
```shell
{
    "registry-mirrors":["https://registry.docker-cn.com"]
}
```
重启服务
```shell
sudo systemctl daemon-reload
sudo systemctl restart docker
```

检查是否成功
```shell
docker info
>>>Registry Mirrors:
     https://registry.docker-cn.com/

```

## 命令

### 使用`docker images`查看本地主机上的镜像

### 使用`docker search image_name`在`docker hub`上查找镜像

### 使用`docker pull image_name`拉取镜像
```shell
docker pull python3.8
```

### 更新镜像
更新镜像并打标签
```shell
docker commit -m="leave your message" -a="author" container_id_or_container_name image_name:version
```

```shell
docker run ubuntu:16.04 /bin/echo "hello world"
```
`ubuntu:16.04`是指定要运行的镜像(若本地不存在则从镜像仓库拉取下载)，在这个镜像中执行`/bin/echo "hello world"`


### 查看docker运行情况
```shell
docker ps

docker ps -a
```
输出以下信息:
- `CONTAINER ID`, 容器`ID`，唯一
- `IMAGE`，使用的镜像               
- `COMMAND`，使用容器时运行的命令             
- `CREATED`，容器创建时间             
- `STATUS`，容器状态，一共有七种：`created`(已创建), `restarting`(重启中), `running`(运行中), `removing`(迁移中), `paused`(暂停), `exited`(停止), `dead`死亡              
- `PORTS`, 容器的端口信息(如映射信息)和使用的连接类型(`tcp`\`udp`)               
- `NAMES`，自动分配的容器名

### 运行交互式的容器
```shell
docker run -it -p 1234:5000 --name my_container image_name /bin/bash
```
各个参数解析：
- `-t`: 在新容器内指定一个伪终端或终端。
- `-i`: 允许你对容器内的标准输入 (STDIN) 进行交互。
- `-p`: 端口映射(将容器内部的端口1234映射到当前电脑的5000)

### 使用`exit`命令或者使用`CTRL+D`来退出容器

### 使用后台模式启动容器
```shell
docker run -d ubuntu:16.04 /bin/sh -c "while true; do echo hello world; sleep 2; done"
```

### 使用`docker logs id_or_name`查看容器内的标准输出

### 使用`docker stop id_or_name`停止容器

### 使用`docker start id_or_name`来启动已经停止的容器

### 使用`docker restart id_or_name`来重启容器

### 进入容器
```shell
docker exec -it id_or_name /bin/bash
``` 

### 导出容器
```shell
docker export id_or_name > filename.tar
```

### 导入容器快照
`docker import`: 从归档文件中创建镜像。
`docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]`
OPTIONS说明：
- `-c`:应用docker 指令创建镜像；
- `-m`:提交时的说明文字；
```shell
cat filename.tar | docker import - repository_name:v1
docker import filename.tar repository_name:v1
docker import http://xxx.com/image
```

### 使用`docker rm -f id_or_name`删除容器

### 使用`docker rmi image_name`删除镜像

### `docker port id_or_name`查看容器的端口信息

### `docker top id_or_name`查看容器内部运行的进程

### `docker inspect id_or_name`查看容器的底层信息

### 删除所有<none>容器
```
docker rmi $(docker images | grep "none" | awk '{print $3}')
```
