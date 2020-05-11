# html和html5基础

## html介绍
- 由尖括号包围的关键词, 如<html>
- 需要显示的文本内容, 放置在标签对的内部
- 网页的内容需要在<html>标签中, 标题、字符格式、语言、样式、关键字、描述等信息显示在<head>标签中, 而网页展示的内容需嵌套在<body>标签中

```html
<html>
    <head></head>
    <body></body>
</html>
```

## 文本标签和属性
常见的文本修饰标签
| 标签 | 描述 |
| - | - |
| `<h1></h1>` | 标题一标签 |
| `<b></b>` | 定义粗体 |
|`<strong></strong>`| 定义强调文本 |
| `<i></i>` |定义斜体字|
|`<em></em>`|定义强调文本|
|`<s></s>`|定义加删除线文本|
|`<del></del>`|定义被删除文本|

h1-h6标题标签, b/i/em/strong, 这些标签会增加SEO权重

## 标签的属性和嵌套
```html
<h1><p color:"red">hello, world</p></h1>
```

## 常用的区块标签
|标签|描述|
|-|-|
|`<p></p>`|段落标签|
|`<div></div>`|区块布局标签|
|`<span></span>`|区块布局标签|

p标签有语义性, 利于搜索引擎处理, 两个p标签之间有换行
div之间无换行
span为无样式标签

## 常用的单标签及其属性
|标签|描述|
|-|-|
|`<hr/>`|水平线标签|
|`<br/>`|换行符标签|
|`<pre></pre>`|格式化标签|

pre标签保留格式

## 字符实体
|显示结果|描述|实体名称|
|-|-|-|
|&nbsp|空格|`&nbsp`|
|&lt;|小于号|`&lt;`|
|&gt;|大于号|`&gt;`|
|&amp;|和号|`&amp;`|
|&quot;|引号|`&quot;`|
|&times;|乘号|`&times;`|
|&divide;|除号|`&divide;`|
|&copy;|版权|`&copy;`|
|&reg;|注册商标|`&reg;`|

## html的注释
`<!-- 要注释的内容 -->`
html注释不能嵌套注释


## 超级链接标签
`href`
链接地址, 网络地址需要在前面加入协议`https://`
`title`
链接的提示文字
### `target`属性
`_self`(默认)(默认为空), 为在本页面打开;
`_blank`, 在新窗户打开
`_parent`在父窗口中打开
`_top`在当前浏览器中打开, 而框架会消失

### 让网页中的链接统一设置为在新窗口打开
```html
<head>
    <base target="_blank">
</head>
```


## 锚记链接
语法格式
```html
<a href="#key">点击我查看详解</a>
<a name="key"></a>
```
只有`#`将返回当前页顶部
有点类似选择器, 点击了就去往那个地方

## 图像标签
```html
<img src="图片路径" alt="图片替代文本" title="提示文字" width="宽度" height=高度""/>
```
相对路径与绝对路径
绝对路径: 文件在硬盘上真正存在的路径
相对路径: 在同一目录下, 即文件树形势下互为兄弟, 可以直接写文件名称进行访问; `../`指上一层
`alt`对搜索引擎起到作用, 用于SEO, 当图森图样破时提示
`title`是鼠标悬浮时显示文字信息


## 图片热点地图
一张图片点击不同地方进入不同的链接,

```html
<img src="" usemap="#foo">
<map name="foo">
    <area shape="rect" coords="10,10,50,50" href=""/>
    <area shape="circle" coords="100,40,20" href=""/>
    <area shape="poly" coords="100,20,100,50,200,50,200,20" href=""/>
</map>
```

## 表格标签
```html
<table>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
```
属性
|属性名|含义|
|-|-|
|width|表格的宽度|
|border|围绕表格的边框宽度, 默认无边框, 加了后就有边框|
|cellspacing|单元格之间的距离|
|cellpadding|规定单元格边沿与内容之间的空白, 单元格内容与单元格框的间距|
|align|控制居中(已经不推荐使用)|
|bgcolor|背景颜色(已经不推荐使用)|

tr标签
|属性|含义|属性值|
|-|-|-|
|align|表格每个格子内的内容的水平对齐方式|left, center, right|
|valign|表格每个格子内的内容的垂直对齐方式|top, middle, bottom, baseline|

td标签同tr标签类似, 额外属性有
|属性|用途|
|-|-|
|width|表格单元格的宽度|
|height|表格单元格的高度|
|colspan|单元格可横跨的列数|
|rowspan|单元格可横跨的行数|

## 表头`th`
th, 包裹在第一行中
```html
<table>
    <tr>
        <th></th>
    </tr>
</table>
```

## 标题`caption`
```html
<table>
    <caption>我是表格名</caption>
    <tr><th></th></tr>
    <tr><td></td></tr>
</table>
```

## 其他一些表格标签
```html
<table>
    <thead>
        <caption>我是表格名</caption>
        <tr><th></th></tr>
        <tr><td></td></tr>
    </thead>
    <tfoot></tfoot>
    <tbody></tbody>
</table>
```

表格中嵌套表格的方法为在td中添加表格

## 细线表格
单元格间距造成的, 即table的`cellspacing`属性


## 列表
无序列表`ul`和有序列表列表`ol`
```html
<ul type="circle">     <!--disc为实心小圆点, circle为空心小圆点， square -->
    <li>1</li>
    <li>2</li>
</ul>
```

有序列表类似
type属性的可选值有`a`和`1`和`A`和`i`和`I`, 表示序号使用阿拉伯数字, 小写英文字母, 大写英文字母, 罗马字母

## 自定义列表
dt列表中的上层项目, dd列表中的下层项目
```html
<dl>
    <dt></dt>
    <dd></dd>

    <dt></dt>
    <dd></dd>
</dl>
```

## `form`标签
|属性|含义|
|-|-|
|action|规定当提交表单时向何处发送表单数据|
|method|get和post规定用于发送form-data的http方法|


## `input`标签
`<input type="类型" name="名称" />`
类型有如下
text, 文本输入框
password, 密码
radio, 单选按钮
checkbox, 复选框
file, 文件上传
hidden, 隐藏域
submit, 提交按钮, 通过`value`更改文本信息
reset, 重置按钮
button, 普通按钮
image, 图像按钮, 引入图像, 如放大镜图片代表搜索按钮

其中单选按钮, 有时候要设置成一组
```html
性别: <input type="radio" name="sex"/>男 <input type="radio" name="sex"/>女
```


## 下拉框标签`select`
`select`标签属性
- `name`规定下拉列表的名字
- `size`规定下拉列表中可见选项的数目
- `multiple`规定可选择多个选项

`option`标签属性
- `value`定义送完服务器的选项值
- `selected`规定选项表示为选中状态
- `disabled`规定此选项应在首次加载时被禁用

`optgroup`标签, 把相关的选项组合在一起
- `label` 为选项组规定描述
```html
<select name="名称">
    <option value="值1">文字信息</option>
    <option value="值2">文字信息</option>
</select>
```

## `textarea`
```html
<textarea name="myname" cols="50" rows="3">
    默认内容
</textarea>
```


## label
label标签可以提供很好的用户体验, 点击label标签, 对应的控件会被选择, 有两种表现方式, 有两种表现方式:

```html
<label for="userName">用户名:</label>
<input type="text" id="userName"/>
```

## `frameset`和`frame`
## `iframe`


## `meta`标签
meta标签是单标签, 格式为`<meta 属性="值"/>`
meta标签位于head内, 分为两大部分, 为http标题信息(http-equiv)和页面描述信息(name)


### meta标签的http标题信息
```html
<meta http-equiv="参数" content="参数变量值"/>
```
其中`http-equiv`属性主要有一下几种参数:
- expires(期限), GMT时间格式
```html
<meta http-equiv="expires" content="Wed, 20 June 2016 10:30:00 GMT">
```
- pragma(cache模式), 禁止浏览器从本地计算机的缓存中调阅页面的内容
```html
<meta http-equiv="pragma" content="no-cache">
```
- refresh(刷新), 定时刷新让网页自动链接到其它网页
```html
<!-- 5秒钟后刷新到URL网址 -->
<meta http-equiv="refresh" content="5;URL=http://www.baidu.com"/>
```
- content-type(显示字符集设定)
```html
<meta http-equiv="content-type" content="text/html; charset=utf-8">
```

### meta标签的页面描述信息
name是描述网页的, 对应于content(网页内容), 以便搜索引擎机器人查找与分类, 格式为
```html
<meta name="参数" content="具体参数值" />

<!-- keywords, 告诉搜索引擎网页的关键字 -->
<meta name="keywords" content="网上购物, 网上商城, 手机" />

<!--  description(网页描述), 告诉搜索引擎网页的主要内容 -->
<meta name="description" content="我是二手东"/>

<!-- robots(机器人向导), 提示搜索引擎是否可以搜索与检索  -->
<!--
all：搜索引擎将索引此网页，且页面上的链接可以被查询，等价于index和follow

none：搜索引擎将忽略此网页，且页面上的链接不可以被查询，等价于noindex和nofollow

index：文件将被索引

follow：搜索引擎通过此网页的链接，索引搜索其它的网页。

noindex：文件将不被检索，但网页中的链接，可以索引搜索其它的网页

nofollow：文件将不被检索，搜索引擎不可以通过此网页的链接，继续索引其它网页

-->
<meta name="robots" content="all" />


<!-- author(作者)  -->
<meta name="author" content="作者的名字">
```
