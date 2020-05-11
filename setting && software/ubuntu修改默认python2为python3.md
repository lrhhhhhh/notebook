查看python命令的指向
```shell
sudo ls -l /usr/bin | grep python
```

修改软链接
```shell
sudo ln -s /usr/bin/python3 /usr/bin/
```