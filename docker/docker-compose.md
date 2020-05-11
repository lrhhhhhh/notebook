`Compose`是用于定义和运行多容器`Docker`应用程序的工具。通过`Compose`，您可以使用`YML`文件来配置应用程序需要的所有服务。然后，使用一个命令，就可以从`YML`文件配置中创建并启动所有服务。

[`YML`入门教程](https://www.runoob.com/w3cnote/yaml-intro.html)


Compose 使用的三个步骤：

- 使用`Dockerfile`定义应用程序的环境。
- 使用`docker-compose.yml`定义构成应用程序的服务，这样它们可以在隔离环境中一起运行。
- 最后，执行`docker-compose up`命令来启动并运行整个应用程序。

## 一个例子
```yaml
# yaml 配置
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```
该 Compose 文件定义了两个服务：`web`和`redis`。
- `web`：该 web 服务使用从 Dockerfile 当前目录中构建的镜像。然后，它将容器和主机绑定到暴露的端口 5000。此示例服务使用 Flask Web 服务器的默认端口 5000 。
- `redis`：该 redis 服务使用 Docker Hub 的公共 Redis 映像。


## 安装
[官方安装文档](https://docs.docker.com/compose/install/)
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


 sudo chmod +x /usr/local/bin/docker-compose

 sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

 docker-compose --version
```

## 运行
```shell
docker-compose up
docker-compose up -d
```

## `yml`配置指令参考
### `version`
指定本`yml`依从的`compose`哪个版本制定的。

### `build`
指定为构建镜像上下文路径  
例如 webapp 服务，指定为从上下文路径 `./dir/Dockerfile`所构建的镜像：
```yml
version: "3.7"
services:
  webapp:
    build: ./dir
```
或者，作为具有在上下文指定的路径的对象，以及可选的 Dockerfile 和 args：
```yaml
version: "3.7"
services:
  webapp:
    build:
      context: ./dir
      dockerfile: Dockerfile-alternate
      args:
        buildno: 1
      labels:
        - "com.example.description=Accounting webapp"
        - "com.example.department=Finance"
        - "com.example.label-with-empty-value"
      target: prod
```
- `context`：上下文路径。
- `dockerfile`：指定构建镜像的 Dockerfile 文件名。
- `args`：添加构建参数，这是只能在构建过程中访问的环境变量。
- `labels`：设置构建镜像的标签。
- `target`：多层构建，可以指定构建哪一层。

### `command`
覆盖容器启动的默认命令。
```yaml
command: ["bundle", "exec", "thin", "-p", "3000"]
```
### `container_name`
指定自定义容器名称，而不是生成的默认名称。
```yaml
container_name: my-web-container
```

### `depends_on`
设置依赖关系。

- `docker-compose up` ：以依赖性顺序启动服务。在以下示例中，先启动 db 和 redis ，才会启动 web。
- `docker-compose up SERVICE` ：自动包含 SERVICE 的依赖项。在以下示例中，docker-compose up web 还将创建并启动 db 和 redis。
- `docker-compose stop` ：按依赖关系顺序停止服务。在以下示例中，web 在 db 和 redis 之前停止。
```yaml
version: "3.7"
services:
  web:
    build: .
    depends_on:
      - db
      - redis
  redis:
    image: redis
  db:
    image: postgres
```
注意：`web`服务不会等待`redis db`完全启动 之后才启动。

### `entrypoint`
覆盖容器默认的`entrypoint`。
```yaml
entrypoint: /code/entrypoint.sh
```
也可以是以下格式：
```yaml
entrypoint:
    - php
    - -d
    - zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20100525/xdebug.so
    - -d
    - memory_limit=-1
    - vendor/bin/phpunit
```

### `env_file`
从文件添加环境变量。可以是单个值或列表的多个值。
```yaml
env_file: .env
```
也可以是列表格式：
```yaml
env_file:
  - ./common.env
  - ./apps/web.env
  - /opt/secrets.env
```

### `environment`
添加环境变量。您可以使用数组或字典、任何布尔值，布尔值需要用引号引起来，以确保 YML 解析器不会将其转换为 True 或 False。
```yaml
environment:
  RACK_ENV: development
  SHOW: 'true'
```

### `expose`
暴露端口，但不映射到宿主机，只被连接的服务访问。

仅可以指定内部端口为参数：
```yaml
expose:
 - "3000"
 - "8000"
```

### `image`
指定容器运行的镜像。以下格式都可以：
```yaml
image: redis
image: ubuntu:14.04
image: tutum/influxdb
image: example-registry.com:4000/postgresql
image: a4bc65fd # 镜像id
```

### `logging`
服务的日志记录配置。

driver：指定服务容器的日志记录驱动程序，默认值为json-file。有以下三个选项
```yaml
driver: "json-file"
driver: "syslog"
driver: "none"
```
仅在 json-file 驱动程序下，可以使用以下参数，限制日志得数量和大小。
```yaml
logging:
  driver: json-file
  options:
    max-size: "200k" # 单个文件大小为200k
    max-file: "10" # 最多10个文件
```
当达到文件限制上限，会自动删除旧得文件。

syslog 驱动程序下，可以使用 syslog-address 指定日志接收地址。
```yaml
logging:
  driver: syslog
  options:
    syslog-address: "tcp://192.168.0.42:123"
```

### `restart`
- `no`：是默认的重启策略，在任何情况下都不会重启容器。
- `always`：容器总是重新启动。
- `on-failure`：在容器非正常退出时（退出状态非0），才会重启容器。
- `unless-stopped`：在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器
```yaml
restart: "no"
restart: always
restart: on-failure
restart: unless-stopped
```

### `volumes`
将主机的数据卷或着文件挂载到容器里。
```yaml
version: "3.7"
services:
  db:
    image: postgres:latest
    volumes:
      - "/localhost/postgres.sock:/var/run/postgres/postgres.sock"
      - "/localhost/data:/var/lib/postgresql/data"
```

### `ports`
```yaml
ports:
  - 123:456
```
綁定容器的456端口到主机的123端口

## 创建
```shell
docker-compose build service_name
```

## 启动
```
docker-compose up
```