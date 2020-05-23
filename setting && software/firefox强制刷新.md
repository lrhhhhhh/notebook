[来源](http://www.zhecoo.com/2016/07/13/firefox%E7%81%AB%E7%8B%90%E6%B5%8F%E8%A7%88%E5%99%A8web%E5%BC%80%E5%8F%91%E8%B0%83%E8%AF%95%E5%BC%80%E5%90%AF%E5%BC%BA%E5%88%B6%E5%88%B7%E6%96%B0%E7%BC%93%E5%AD%98%E6%A8%A1%E5%BC%8F/)


Firefox火狐浏览器web开发调试开启强制刷新缓存模式

最近做项目的时候，在火狐浏览器发现缓存难清理，用Ctrl+F5 Ctrl+R 等在谷歌和IE浏览器的快捷键没用，搜索了一下，发现火狐清理缓存比较麻烦，默认快捷键 Ctrl + Shift + Del 键是弹窗选择性清理，还要点击按钮选择，在web开发调试中非常的不方便，也不科学。
然后问度娘后发现火狐是要进入它的参数设置里设置本地不缓存的：

火狐浏览器地址栏输入：about:config
- 1.找到browser.cache.check_doc_frequency选项，双击将3改成1
- 2.找到browser.cache.disk.enable 把true改为 false
- 3.找到browser.cache.memory.enable 把true改为 false
