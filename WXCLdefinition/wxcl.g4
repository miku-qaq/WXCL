grammar wxcl;

options {
    language=Python3;
}

/*
 * wxcl 语言的主规则，描述了整个项目的结构。
 * 由 `content`、`style`、`Theme`、`navigationBar` 和 `pageList` 组成。
 */
project: 'project' ':' String ';' navigationBar appStyleVariableList pageList ;

/*
 * 导航栏定义，包含：
 * - 颜色 (ColorValue)
 * - 标题 (String)
 * - 主题色 (HexColor)
 */
navigationBar: 'navigationBar' '{' ColorValue ',' String ',' HexColor '}' ;

/* 全剧样式变量列表 */
appStyleVariableList: styleVariable* ;

/* 页面列表 */
pageList: page+ ;

/*
 * 页面定义，包含：
 * - 页面的编号 (Number)
 * - 页面名称 (VariableName)
 * - 页面内容 (pageContent)
 * - 样式变量列表 (styleVariableList)
 */
page: 'page' '-' Number ':' String '{' pageContent '}' styleVariableList ;

/* 页面内容，由多个组件组成 */
pageContent: ( component )* ;

/* 样式变量列表 */
styleVariableList: styleVariable* ;

/* 样式变量定义 */
styleVariable: VariableName ':' gui ';' ;

/* 组件定义，支持样式变量或 GUI 绑定 */
component: ( swiper
    | text
    | image
    | button
    | list
    | form
    | label
    | radioGroup
    | checkboxGroup
    | input
    | view
    | navigator )
    ( '=>' (gui | VariableName) )? ';' ;

/* 轮播图组件 */
swiper: 'swiper' '[' ablum? ']' ;

/* 轮播图的相册 */
ablum: String ( ',' String )* ;

/* 文本组件 */
text: 'text' '-' String ;

/* 图片组件 */
image: 'image' '-' String ;

/* 按钮组件 */
button: 'button' '<' function '>' '-' String ;

/* 按钮的功能 */
function: 'navigation' '-' VariableName
    | 'submit'
    | 'reset'
    ;

/* 列表组件 */
list: 'list' '[' pageContent ']' ;

/* 表单组件 */
form: 'form' '<' String '>' '[' pageContent ']' ;

/* 标签组件 */
label: 'label' ( '<' String '>')? '[' pageContent ']' ;

/* 单选框组件 */
radioGroup: 'radio-group' ':' String '[' radioOption (',' radioOption)* ']' ;

/* 单选框选项，* 表示默认选中 */
radioOption: String '*'? ;

/* 复选框组件 */
checkboxGroup: 'checkbox-group' ':' String '[' checkboxOption (',' checkboxOption)* ']' ;

/* 复选框选项，* 表示默认选中 */
checkboxOption:  String '*'? ;

/* 输入框组件 */
input: 'input' '<' inputType '>' ('-' String)? ':' String ;

/* 输入框类型 */
inputType: 'text'
    | 'password' ;

/* 视图组件 */
view: 'view' '[' pageContent ']' ;

/* 导航组件 */
navigator: 'navigator' '<' VariableName '>' '[' pageContent ']' ;

/* GUI 样式定义 */
gui: '\'' style ( ',' style )* '\'' ;

/* 样式属性 */
style: color
    | width
    | height
    | border
    | position
    | font
    | textAlign
    | background
    | spacing
    | borderRadius
    | padding
    | list_col
    | list_rowHeight
    | swiper_interval ;

/* 颜色属性 */
color: 'color' ':' ColorValue ;

/* 宽度属性 */
width: 'width' ':' rpxValue ;

/* 高度属性 */
height: 'height' ':' rpxValue ;

/* 边框属性 */
border: 'border' '(' borderWidth ',' BorderStyle ',' borderColor ')' ;

/* 边框宽度 */
borderWidth: rpxValue
            | 'width-initial' ;

/* 边框颜色 */
borderColor: ColorValue
            | 'color-initial' ;

/* 位置属性 */
position: 'position' ':' HorizontalValue ;

/* 字体属性 */
font: 'font' '(' FontWeight ',' fontSize ',' String ')' ;

/* 字体大小 */
fontSize: rpxValue ;

/* 文本对齐 */
textAlign: 'align' ':' HorizontalValue '-' VerticalValue ;

/* 背景属性 */
background: 'background' '(' ColorValue (',' String)? ')';

/* 间距属性 */
spacing:'spacing' '(' rpxValue ',' rpxValue ')' ;

/* 圆角属性 */
borderRadius: 'border-radius' ':' rpxValue ;

/* 统一的数值单位 */
rpxValue: Number Unit;

/* 内边距属性 */
padding: 'padding' ':' rpxValue ;

/* 列表列数 */
list_col: 'listCol' ':' Number ;

/* 列表行高 */
list_rowHeight: 'listColHeight' ':' rpxValue ;

/* 轮播图间隔 */
swiper_interval: 'interval' ':' Number ;

/* 边框样式 */
BorderStyle: 'none'
    | 'solid'
    | 'dashed'
    | 'dotted' ;

/* 水平对齐方式 */
HorizontalValue: 'left' | 'right' | 'center' ;

/* 垂直对齐方式 */
VerticalValue: 'top' | 'bottom' | 'middle' ;

/* 字体粗细 */
FontWeight: 'bold'
    | 'normal'
    | 'lighter'
    | 'bolder' ;

/* 颜色值 */
ColorValue:  'red'
    | 'blue'
    | 'green'
    | 'yellow'
    | 'white'
    | 'black'
    | 'gray'
    | 'purple'
    | 'orange'
    | 'pink'
    | 'brown'
    | 'cyan' ;

/* 十六进制颜色 */
HexColor: '#' [0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F];

/* 布尔值 */
Boolean: 'true' | 'false' ;

/* 单位 */
Unit: 'rpx' | '%' | 'px' | 'vw' | 'vh' | 'em' ;

/* 数字类型 */
Number: [0-9]+ ('.' [0-9]+)? ;

/* 字符串 */
String: '"' ( ~["\r\n] )* '"' ;

/* 忽略空白符 */
WS: [\t\r\n ]+ -> skip ;

/* 变量名称 */
VariableName: [a-zA-Z_][a-zA-Z_0-9]*;

/* 注释 */
Comment: '//' ( ~[\r\n] )*  -> skip ;
