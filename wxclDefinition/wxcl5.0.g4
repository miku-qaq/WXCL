grammar wxcl;

options { language = Python3; }

project: 'content' ':' 'style' '<' Theme '>' navigationBar  pageList;
navigationBar: 'navigationBar' '{' ColorValue ',' String ',' HexColor '}';        //导航栏颜色、文字、背景色
pageList: page+ ;
page:'page' '-' Number ':' VariableName  '{' pageContent '}' styleVariableList;   //VariableName为页面名称
pageContent: ( component )+;

styleVariableList: styleVariable* ;
styleVariable: VariableName ':' gui ';' ;

component: ( swiper              //组件类型
    | text
    | image
    | button
    | list
    | input
    | view
    | navigator)
    ('=>' (gui | VariableName) )? ';'
    ;
swiper: 'swiper' '[' ablum ']' ;
ablum: ( String ';' )+ ;
text: 'text' '-'   String  ;
image: 'image' '-'  String  ;
button: 'button' '-' function ;
function: 'navigation' '<' pageLocation '>'
    | 'LogIn'
    | 'Pay'
    | 'LogOut'
    ;
pageLocation: 'page' Number ;              //页面位置
list: 'list' '[' pageContent ']' ;
input: 'input' '-' InputType ;
view:'view' '[' pageContent ']' ;
navigator: 'navigator' '<' VariableName '>' '[' pageContent ']';


gui: '\'' style ( ',' style )* '\'' ;
style: color                               //样式类型
    | width
    | height
    | border
    | position
    | font
    | textAlign
    | background
    | list_col
    | list_rowHeight
    | swiper_interval
    ;
color: 'color' ':' ColorValue ;
width: 'width' ':' rpxValue ;
height: 'height' ':' rpxValue ;
border: 'border' '(' borderWidth ',' BorderStyle ',' borderColor ')' ;
borderWidth: rpxValue
            | 'width-initial'
            ;
borderColor: ColorValue
            | 'color-initial'
            ;
position: 'position' ':' HorizontalValue ;
font: 'font' '('  FontWeight ',' fontSize ',' String ')';
fontSize: rpxValue ;
textAlign: 'align' ':' HorizontalValue '-' VerticalValue ;
background: 'background' '(' ColorValue ','  String ')';
rpxValue: Number Unit;                                      //单位为rpx
list_col: 'listCol' ':' Number ;
list_rowHeight: 'listColHeight' ':' rpxValue ;
swiper_interval: 'interval' ':' Number ;




Theme: 'simple'                          //主题类型
    | 'fashion'
    | 'retro'
    ;
BorderStyle: 'none'                      //边框样式可选值
            |'solid'
            | 'dashed'
            | 'dotted'
            ;
HorizontalValue: 'left' | 'right' | 'center';
VerticalValue: 'top' | 'bottom' | 'middle';
FontWeight: 'bold'                       //字体粗细可选值
          | 'normal'
          | 'lighter'
          | 'bolder'
          ;
InputType: 'text'                        //输入框类型
          | 'password'
          ;
ColorValue:  'red'                       //颜色值
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
           | 'cyan'
           ;
HexColor: '#' [0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F];   // 16进制颜色值
Unit: 'rpx' | '%' | 'px' | 'vw' | 'vh' | 'em';                                      // 单位
Number: [0-9]+ ('.' [0-9]+)? ;                                                      // 支持整数和小数 两者都翻译成这个
String: '"' ( ~["\r\n] )* '"' ;                                                     // 字符串
WS: [\t\r\n ]+ -> skip ;                                                            // 跳过空白字符
VariableName: [a-zA-Z_][a-zA-Z_0-9]*;                                               // 变量名、标识符
