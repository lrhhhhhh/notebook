
## 简介
CSS, 层叠样式表, 网页与内容分离的一种样式设计语言

## 写法格式
外链样式, 通过载入的方式加载, 后缀为.css
```html
<head>
    <link rel="stylesheet" href="" />
</head>
```

页内样式, 直接在本页面写css
```html
<head>
    <style></style>
</head>
```

行内样式, 在html标签内部, 以属性的方式, 只会对文本标签起作用


## 选择器
标签选择器
```html
h1{color:red}
```
class选择器
```html
<head>
    .myClassName{color:red;}
    .another{font-size:50px;}
</head>
<body>
    <h1 class="myClassName another">title</h1>
</body>
```
id选择器
```html
<head>
    #idSelect{color:red;}
</head>
<body>
    <!-- 只能有一个id选择器 -->
    <h1 id="idSelect">title</h1>

</body>
```

通用选择器
```html
<head>
    *{font-size:40px; color:red;}
</head>
```

后代选择器
```html
ol li{color:red;}

.class1 .classSon1{color:green;}
```

编组选择器
```html
h1, h2, h3, .className1, #idName1{color:red;}
```

伪类选择器
|选择器|含义|
|-|-|
|link|初始样式|
|visited|已访问后的样式|
|hover|鼠标移入时的样式|
|active|活动样式|
```html
<style>
    a:link{color:red;}
    a:hover{color:blue;}
</style>
```

## 文本样式
|属性|名称|值|
|-|-|-|
|`font-family`|字体|中文字体需要嵌套在引号中, 多字体使用英文逗号|
|font-size|字号|number|
|font-weight|字体粗细|normal/bold/100-900|
|font-variant|小型大写字母|normal/small-caps|
|line-height|行高|number|
|text-ransform|大小写转换|lowercase/capitalize/uppercase|
|text-decoration|文本修饰|none/underline/overline/line-through|

## 文本区块
|属性|名称|值|
|-|-|-|
|letter-spacing|字母间距|number|
|text-indent|文本缩进|number|
|text-align |水平对齐|left/center/right|
|vertical-aligin|垂直对齐|baseline/sub/super/top/middle/bottom|
|display|显示类型|none/block/inline/inline-block|


```html
<head>
    span, b, em, a{display: block;}          <!-- 将行级元素转换为块级元素 -->
    div{display: inline;} <!-- 块级元素转换为行级元素 -->
</head>
```


## CSS的背景以及图片

background-image: url();

background-color

background-repeat, 背景图像在纵向和横向上重铺, 属性值有以下三个
no-repeat, 不平铺
repeat-x
repeat-y

background-position背景定位
background-position: x y
x轴可以使用left, center, right或精确数值
y轴可以使用top, center, bottom或精确数值
```html
background-position: left bottom;
```

background-attachment背景固定
有两个属性值:
scroll(默认)
fixed

background简写规则
background: 颜色 路径 重复 偏移 固定
```html
<style>
    .className{
        background: #ccc url() no-repeat right bottom;
    }
</style>
```


## 盒子模型
min-height与min-width, max-height与max-width
px像素, %百分比

内边距padding
元素到边界的距离
padding-top, padding-right, padding-bottom, padding-left
padding会增加元素的长和宽
```
padding: 10px;  四个方向的边距都为10px
padding: 10px 20px; 上下为10px, 左右为20px
padding: 10px 20px 30px; 上, 左右， 下
padding: 10px 20px 30px 40px; 上 右 下 左
```

外边距margin
两个标签元素之间的距离
margin-top, margin-right, margin-bottom, margin-left

边框boder
|属性|名称|值|
|-|-|-|
|border-width|边框宽度|numner|
|border-color|边框颜色|颜色值/transparent|
|border-style|边框样式|solid/dotted/dashed|
```html
border: 10px red solid;
```
border-bottom-color
边界的交叉为斜线分隔

## 浮动
float:left 向左浮动, 同理right, none(默认值, 不浮动)
浮动的元素自动换行

clear: left; 左侧不允许有浮动元素(不许左侧有元素压着本元素), 同理right, both


## css3
border-radius:20px;
border-radius:50%; 圆

box-shadow
有6个参数, x轴偏移, y轴偏移, 阴影模糊半径, 阴影扩展半径, 阴影颜色, 阴影类型
box-shadow: 10px 10px 5px 5px red inset;  inset为内阴影
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{background-color:darkturquoise}
        .box{
            margin: 200px;
            width: 500px;
            height: 300px;
            background: #c00;
            box-shadow: 10px 10px 5px 5px rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
```


## text-shadow
text-shadow的参数有四个, x轴偏移, y轴偏移, 阴影模糊半径, 阴影


## 自定义字体
@font-face语法格式
@font-face{
    font-family: 字体名称;
    src: 字体路径;
    font-weight: 字体粗细;
    font-style: 字体风格;
}

## 子元素选择器
first-child
last-child
```html
ul li:first-child{}
ul li:nth-child(5){}
ul li:nth-child(odd){}
ul li:nth-child(3n){}
ul li:nth-last-child(3){}  倒数第三个
```

first-of-type
last-of-type
nth-of-type

::selection
```html
    h1::selection{background:red; color:#fff;}
    ::selection{background:red; color:#fff;}
```

::before和::after
可以在元素之前添加内容, 也可以改变元素的css



## flex布局
[点击链接](https://www.runoob.com/w3cnote/flex-grammar.html)