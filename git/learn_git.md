## 常用命令
```shell
git init
git add *
git add -A
git commit -m "your message"
git push -u origin master
```

## git添加空文件夹的方法
在要添加的文件夹下面新建名为`.gitkeep`或`.keep`的空文本文件

## 打标签
```shell

```

## 删除已提交文件
```shell
git rm -r --cached floder
```

## git配合github的使用流程
### 先建立本地git，编写`.gitignore`文件, 然后`add`和`commit`
```shell
git init
git add -A
git commit -m 'init'
```
### 在github上新建repository, 然后给本地项目添加远程仓库
```
git remote add origin git@github.com:your_account/your_repository
```
做成这些的前提是已经将`SSH Key`公钥添加到了自己的github账户列表中

### `push`到远程仓库
```shell
git push -u origin master
```

## 从远程仓库获取更新到本地
#### 用fetch不会merge
```shell
git fetch origin master
```
#### 用pull会merge
```shell
git pull origin master
```