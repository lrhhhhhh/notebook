### react redux项目的文件结构
- [React+Redux工程目录结构，最佳实践](https://www.jianshu.com/p/f913860f1494)
- [react-redux-universal-hot-example](https://github.com/erikras/react-redux-universal-hot-example/tree/master/src) 


### 如何理解redux
- 将redux理解成状态机，应用从一个initialState通过不同的action变换成另一个state。这种变换通过reducer实现，reducer接受action，使得state从旧的状态按条件转移到新的状态
- 所有的动作都在action中发生，如向服务器请求数据
- 动作发生在action中，在请求动作中，我们得到了数据，
我们通过reducer有选择的将数据提取出来，根据这些数据，
使得state得到转移