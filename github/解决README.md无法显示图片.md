### 原因
由于dns被污染，无法访问`raw.githubusercontent.com`

### ubuntu下解决方法
```shell script
sudo su
vim etc/hosts
```

添加如下内容:
```
199.232.68.133 raw.githubusercontent.com
199.232.68.133 githubusercontent.com
```

保存并退出
