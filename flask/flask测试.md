## 测试
- [Testing Flask Applications](https://flask.palletsprojects.com/en/1.1.x/testing/)  
- [Testing Flask Applications中文翻译](https://dormousehole.readthedocs.io/en/latest/testing.html)

### pytest相关文档
- [@pytest.fixture](https://docs.pytest.org/en/latest/fixture.html#fixtures)
- [@pytest.mark.parametrize](https://docs.pytest.org/en/latest/parametrize.html#pytest-mark-parametrize)
- [pytest的一个系列教程](https://www.cnblogs.com/poloyy/tag/Pytest/)


## 要点提炼
- `Flask`提供的测试渠道是使用`Werkzeug`的`Client`类
- 文件结构: 在应用的根文件夹中添加一个测试文件夹`tests`, 在里面新建各个测试脚本，名称类似`test_*.py`的文件会被 pytest 自动发现
- conftest.py为全局配置文件，我们可以在里面实例化测试用的client和已经登陆了的client
- pytest的teardown是通过生成器返回执行对应语句实现的