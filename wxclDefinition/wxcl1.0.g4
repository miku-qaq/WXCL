grammar wxcl1.0;

options { language = Python3; }

project: 'content:' pageList ;
pageList: page+ ;
page:'page' Number ':' Describe  '{' pageContent '}' ;
pageContent: ( component ';')+;



component: ( swiper              //组件类型
    | text
    | image
    | button
    | list
    | input )
    ('=>' gui )?
    ;
swiper: 'swiper' '[' ablum ']' ;
ablum: ( string ';' )+ ;
text: 'text' '-' '"'  string '"' ;
image: 'image' '-' '"' string '"' ;
button: 'button' '-' function ;
function: 'navigation' '<' pageLocation '>'
    | 'LogIn'
    | 'Pay'
    | 'LogOut'
    ;
pageLocation: 'page' Number ;         //页面位置
list: 'list' '[' pageContent ']' ;
input: 'input' '-' InputType ;



gui: '"' ( style ';')* '"' ;
style: color                            //样式类型
    | width
    | heigth
    | border
    | position
    | font
    | textAlign
    | background
    ;
color: 'color' ':' ColorValue ;
width: 'width' ':' rpxValue ;
heigth: 'height' ':' rpxValue ;
border: 'border' '(' borderWidth ',' BorderStyle ',' borderColor ')' ;
borderWidth: rpxValue
            | 'width-initial'
            ;
borderColor: ColorValue
            | 'color-initial'
            ;
position: 'position' ':' PositionValue ;
font: 'font' ':' string',' FontWeight ',' fontSize ;
fontSize: rpxValue ;
textAlign: 'align' ':' PositionValue ;
background: 'background' '(' ColorValue ','  string ',' 'no-repeat' ')';
rpxValue: Number 'rpx' ;                 //单位为rpx





Describe: 'OrderPage'                    //页面描述
    | 'LoginPage'
    | 'RegisterPage'
    | 'MyPage'
    | 'ShopPage'
    | 'Map'
    | 'Home'
    ;
BorderStyle: 'none'                      //边框样式可选值
            |'solid'
            | 'dashed'
            | 'dotted'
            ;
PositionValue: 'right'                   //文本、组件位置可选值
              |'left'
              |'center'
              ;
FontWeight: 'bold'                       //字体粗细可选值
          | 'normal'
          ;
InputType: 'text'                        //输入框类型
          | 'password'
          ;
ColorValue:  'red'                       //颜色值
           | 'blue'
           | 'green'
           |  'yellow'
           | 'white'
           | 'black'
           ;
Number: [0-9]+ ;                         //数字
string: (MultiLetter|Number|Describe|BorderStyle|PositionValue|FontWeight|InputType|ColorValue)+;  //字符串
MultiLetter: [a-zA-Z]+ ;                 //字母序列
WS: [\t\r\n ]+ -> skip ;                 //跳过空白字符