## 数据类型
5种简单数据类型: 数字, 字符串, 布尔值, null, undefined
1种复杂数据类型: object

## typeof
用来检测变量的类型, 返回结果如下:
boolean, string, number, object, function, undefined
null是一个特殊的object对象


## 字符串是不可变类型

## Number
js所有数字都用浮点数值表示, 浮点数值必须包含一个小数点

## 布尔类型
当if语句里没有表达式，只是某个值时，会自动执行Boolean()操作, 非空字符串, 非零数值, 任意object都转换为true,
0和NaN, null为false


## for in
```
for(x in container)
```

## 对象
objectName.propertyName
objectName.methodName()

## string
length, toUpperCase(), toLowerCase(), replace(), split(),
concat(), indexOf(), lastIndexOf(), substring(), substr(), trim()


## Date()

## Array()
map(), forEach(), reverse(), sort()

## Math
格式为:Math.PI
E, LN2, LN10, LOG2E, LOG10E, PI
max(), min, abs(), round(), ceil(), floor(), random()

## RegExp

## BOM
### window对象
所有js全局对象, 函数, 变量均自动成为window对象的成员
全局变量是window对象的属性
全局函数时window对象的方法
DOM的document也是window对象的属性之一
`window.document.getElementById("header")`
`window.open()`

### screen
window.screen对象包含有关用户客户端显示屏幕的信息

### Location
location.href, 返回完整的url
location.host, 返回一个URL的主机名和端口
location.hostname, 返回URL的主机名
location.port
loca tion.protocol, 返回所使用的的web协议

location.assign() 载入一个新的文档
location.reload() 重新载入当前文档
location.replace() 用新的文档替换当前文档

### history
浏览器的历史信息
length, back(), forward(), go()跳转到histroy列表中的某个具体页面


### navigator
navigator对象的属性:
appCodeName: 浏览器的代码名
appName: 浏览器的名称
appVersion: 浏览器的平台和版本信息
cookieEnabled: 浏览器是否使用cookie
platform: 运行浏览器的操作系统
userAgent: 返回由客户机发送服务器的user-agent头部的值

navigator不应被用于检测浏览器版本

### 弹窗
alert() 警告
confirm() 确认
prompt()


### 计时事件
通过在一个设定的时间间隔之后执行代码
setTimeOut(x)   暂停x毫秒后执行代码
clearTimeOut(x) 停止setTimeOut()执行
setInterval(x) 每间隔x毫秒执行代码
clearInterval(x) 停止setInterval()执行
```javascript
setTimeOut(function(){
    console.log("lover! sucker! fucker!");
}, 3000);
```

## DOM
文档对象模型(DOM)是中立于平台和语言的接口，它允许程序和脚本动态地访问和更新文档的内容、结构和样式
当网页被加载时，浏览器会创建页面的文档对象模型(DOM)

```javascript
document.write()
document.getElementById(id).innerHTML
document.getElementById(id).outerHTML
document.getElementById(id).innerHTML = new HTML
document.getElementById(id).outerHTML = new HTML
```

读取和修改节点对象属性
```javascript
document.getElementById(id).attribute;  或者用className
document.getElementById(id).getAttrubute(name);

document.getElementById(id).attribute = new value;
document.getElementById(id).setAttribute(name, value);
document.getElementById(id).removeAttribute(name);
```

操作css
```javascript
document.getElementById(id).style.property = new styel;
document.getElementById(id).className = className = class name
```

增加、删除和替换节点
```javascript
createElement(), createTextNode(), cloneNode()

appendChild(newItem), insertBefore(newItem, existingItem)

removeChild()
```

## 事件
### DOM0级事件处理程序
所有浏览器都支持
### DOM2级事件处理程序, （十分重要：布尔值的含义）
IE9以后大部分浏览器都支持
可以添加多个事件处理程序
添加事件: addEventListener(事件名, 函数, 布尔值)
移除事件: removeEventListener(事件名, 函数, 布尔值)

### 兼容性
```javascript
function addHandler(){
    if(myBtn.addEventListener){
        myBtn.addEventListener("click", myfunction, false);
    }
    else if(myBtn.attachEvent){
        myBtn.attachEvent("onclick", myfunction);
    }
    else{
        myBtn.onclick = myfunction;
    }
}
```

### 事件对象
在触发DOM上的某个事件时，会产生一个事件对象event.所有浏览器都支持event对象，但支持的方式不同
event.target, 事件目标
event.type, 被触发的事件类型
event.preventDefault(), 取消事件的默认行为
event.stopPropagation(), 取消事件的进一步捕获或冒泡

### 事件类型
#### UI事件(框架和对象事件)
load事件，当页面无安全加载后触发
unload事件，事件在文档被完全卸载后触发
select事件，当用户选择文本框时触发
resize事件，当窗口高度或者宽度被调整时触发
scroll事件，当文档被滚动时触发

#### 焦点事件
在页面元素获得或失去焦点时触发
blur事件：在页面失去焦点时触发
focus事件，在页面获得焦点时触发
onfocusin，元素即将获得焦点时触发
onfocusout，元素即将失去焦点时触发
#### 鼠标事件
onclick
ondbclick
onmouseover
onmouseout
onmouseup
onmousedown
onmouseleave
onmousemove  鼠标被移动
#### 键盘事件
onkeydown
onkeypress 某个键盘按键被按下并松开
onkeyup

键码: event.keyCode
#### 表单事件

form  (reset方法)
input(text, password, radio, checkbox)
select
textarea
button
