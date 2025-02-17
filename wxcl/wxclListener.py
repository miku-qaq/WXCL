import os
import shutil

from antlr4 import *

from .formatCode import format_directory
from .tool import *

if "." in __name__:
    from wxcl.wxclParser import wxclParser
else:
    from wxclParser import wxclParser

# This class defines a complete listener for a parse tree produced by wxclParser.
class wxclListener(ParseTreeListener):


    def __init__(self):
        self.page = 0

        # 项目全局文件
        self.appJsonFile = None
        self.appWxssFile = None
        self.appJsFile = None

        # 页面文件
        self.wxmlFile = None
        self.wxssFile = None
        self.jsFile = None
        self.jsonFile = None

        # 组件计数
        self.count = {
            "list": 0,
            "swiper": 0,
            "image": 0,
            "text": 0,
            "navigator": 0,
            "view": 0,
            "button": 0,
            "function": 0,
            "buttonBindFunction": 0,
            "form": 0,
            "radio-group": 0,
            "label": 0,
            "checkbox-group": 0,
            "input": 0
        }

    def exchange(self):
        temp = self.wxssFile
        self.wxssFile = self.appWxssFile
        self.appWxssFile = temp

    # id和class处理 并同时有id 在wxss中加上
    def DealWithIdAndClass(self, ctx, selfType: str):
        self.DealWithIdAndClassWithoutWxss(ctx, selfType)

        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + selfType + str(self.count[selfType]) + " {\n")

    def DealWithIdAndClassWithoutWxss(self, ctx, selfType: str):
        self.count[selfType] += 1
        if ctx.parentCtx.VariableName() is not None:
            self.wxmlFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:
            self.wxmlFile.write(" id=\"" + selfType + str(self.count[selfType]) + "\"")

    def DealWithClassAndName(self, ctx, selfType: str, name: str):
        self.count[selfType] += 1
        if ctx.parentCtx.VariableName() is not None:
            self.wxmlFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        self.wxmlFile.write(" name=\"" + name + "\"")
        self.wxmlFile.write(" id=\"" + name + "\"")

    # Enter a parse tree produced by wxclParser#project.
    def enterProject(self, ctx: wxclParser.ProjectContext):
        global PROJECT_DIR_NAME
        PROJECT_DIR_NAME = ctx.String().getText()[1:-1]
        # 创建项目目录
        if os.path.exists(PROJECT_DIR_NAME):
            shutil.rmtree(PROJECT_DIR_NAME)
        os.makedirs(PROJECT_DIR_NAME)

        # 创建项目文件app.json、app.wxss、app.js
        self.appJsonFile = open(PROJECT_DIR_NAME + "/app.json", "w", encoding=Encoding)
        self.appJsonFile.write("{\n")
        self.appWxssFile = open(PROJECT_DIR_NAME + "/app.wxss", "w", encoding=Encoding)
        self.appJsFile = open(PROJECT_DIR_NAME + "/app.js", "w", encoding=Encoding)
        self.appJsFile.write("App({\n")

    # Exit a parse tree produced by wxclParser#project.
    def exitProject(self, ctx: wxclParser.ProjectContext):
        # app.json文件处理关闭
        self.appJsonFile.write(APPJSON_CONST)
        self.appJsonFile.write("}")
        self.appJsonFile.close()

        # app.wxss文件处理关闭
        self.appWxssFile.close()

        # app.js文件处理关闭
        self.appJsFile.write("\n})")
        self.appJsFile.close()

        format_directory(PROJECT_DIR_NAME)

    # Enter a parse tree produced by wxclParser#navigationBar.
    def enterNavigationBar(self, ctx: wxclParser.NavigationBarContext):
        self.appJsonFile.write("\t\"window\": {\n"
                               f"\t\t\"navigationBarTextStyle\": \"{ctx.getChild(2).getText()}\",\n"
                               f"\t\t\"navigationBarTitleText\": {ctx.getChild(4).getText()},\n"
                               f"\t\t\"navigationBarBackgroundColor\": \"{ctx.getChild(6).getText()}\"\n"
                               "\t},\n")

    # Exit a parse tree produced by wxclParser#navigationBar.
    def exitNavigationBar(self, ctx: wxclParser.NavigationBarContext):
        pass

    # Enter a parse tree produced by wxclParser#appStyleVariableList.
    def enterAppStyleVariableList(self, ctx: wxclParser.StyleVariableListContext):
        self.exchange()

    # Exit a parse tree produced by wxclParser#appStyleVariableList.
    def exitAppStyleVariableList(self, ctx: wxclParser.StyleVariableListContext):
        self.exchange()

    # Enter a parse tree produced by wxclParser#pageList.
    def enterPageList(self, ctx: wxclParser.PageListContext):
        if not os.path.exists(PROJECT_DIR_NAME + "/pages"):
            os.makedirs(PROJECT_DIR_NAME + "/pages")

        self.appJsonFile.write("\t" + "\"pages\": [\n")

    # Exit a parse tree produced by wxclParser#pageList.
    def exitPageList(self, ctx: wxclParser.PageListContext):
        self.appJsonFile.write("\t" + "],\n")

    # Enter a parse tree produced by wxclParser#page.
    def enterPage(self, ctx: wxclParser.PageContext):
        self.page += 1
        for key in self.count:
            self.count[key] = 0
        PageName = ctx.String().getText()[1:-1]
        # 当前页面所有文件所处的路径
        dir_path = PROJECT_DIR_NAME + "/pages/" + PageName
        # 如果目标目录不存在，创建目录
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        else:
            print("页面名重复！")
            exit(1)

        self.wxmlFile = open(dir_path + "/" + PageName + ".wxml", "w", encoding=Encoding)
        self.wxssFile = open(dir_path + "/" + PageName + ".wxss", "w", encoding=Encoding)
        self.jsFile = open(dir_path + "/" + PageName + ".js", "w", encoding=Encoding)
        self.jsFile.write("Page({\n")
        self.jsonFile = open(dir_path + "/" + PageName + ".json", "w", encoding=Encoding)
        self.jsonFile.write(JSON_CONST)

        self.appJsonFile.write("\t\t" + "\"pages/" + PageName + "/" + PageName + "\"")

    # Exit a parse tree produced by wxclParser#page.
    def exitPage(self, ctx: wxclParser.PageContext):
        if self.count["swiper"] > 0:
            self.wxssFile.write(Function.hasAblum())

        self.wxmlFile.close()
        self.wxssFile.close()
        self.jsFile.write("})")
        self.jsFile.close()
        self.jsonFile.close()

        # 获取父节点的子节点列表
        children = ctx.parentCtx.children
        # 获取当前节点的索引
        current_index = children.index(ctx)
        # 判断当前节点是否是最后一个子节点
        if current_index < len(children) - 1:
            self.appJsonFile.write(",")
        self.appJsonFile.write("\n")

    # Enter a parse tree produced by wxclParser#pageContent.
    def enterPageContent(self, ctx: wxclParser.PageContentContext):
        pass

    # Exit a parse tree produced by wxclParser#pageContent.
    def exitPageContent(self, ctx: wxclParser.PageContentContext):
        pass

    # Enter a parse tree produced by wxclParser#styleVariableList.
    def enterStyleVariableList(self, ctx: wxclParser.StyleVariableListContext):
        pass

    # Exit a parse tree produced by wxclParser#styleVariableList.
    def exitStyleVariableList(self, ctx: wxclParser.StyleVariableListContext):
        pass

    # Enter a parse tree produced by wxclParser#styleVariable.
    def enterStyleVariable(self, ctx: wxclParser.StyleVariableContext):
        self.wxssFile.write("." + ctx.getChild(0).getText() + " {\n")

    # Exit a parse tree produced by wxclParser#styleVariable.
    def exitStyleVariable(self, ctx: wxclParser.StyleVariableContext):
        pass

    # Enter a parse tree produced by wxclParser#component.
    def enterComponent(self, ctx: wxclParser.ComponentContext):
        pass

    # Exit a parse tree produced by wxclParser#component.
    def exitComponent(self, ctx: wxclParser.ComponentContext):
        pass

    # Enter a parse tree produced by wxclParser#swiper.
    def enterSwiper(self, ctx: wxclParser.SwiperContext):
        # a为旁边的gui节点
        a = ctx.parentCtx.getChild(2)
        self.wxmlFile.write("<swiper autoplay=\"true\"")

        self.DealWithIdAndClass(ctx, "swiper")

        for i in range(1, a.getChildCount() - 1, 2):
            if a.getChild(i).getChild(0).getChild(0).getText() == "interval":
                self.wxmlFile.write(" interval=\"" + a.getChild(i).getChild(0).Number().getText() + "\"")
                break
        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParser#swiper.
    def exitSwiper(self, ctx: wxclParser.SwiperContext):
        self.wxmlFile.write("</swiper>\n")

    # Enter a parse tree produced by wxclParser#ablum.
    def enterAblum(self, ctx: wxclParser.AblumContext):
        for i in range(0, ctx.getChildCount(), 2):
            self.wxmlFile.write("<swiper-item>\n"
                                f"<image src=\"{ctx.getChild(i).getText()[1:-1]}\" mode=\"aspectFix\"/>\n"
                                "</swiper-item>\n")

    # Exit a parse tree produced by wxclParser#ablum.
    def exitAblum(self, ctx: wxclParser.AblumContext):
        pass

    # Enter a parse tree produced by wxclParser#text.
    def enterText(self, ctx: wxclParser.TextContext):
        self.wxmlFile.write("<text")
        self.DealWithIdAndClass(ctx, "text")
        self.wxmlFile.write(">")

        self.wxmlFile.write(ctx.getChild(2).getText()[1:-1])

        self.wxmlFile.write("</text>\n")

    # Exit a parse tree produced by wxclParser#text.
    def exitText(self, ctx: wxclParser.TextContext):
        pass

    # Enter a parse tree produced by wxclParser#image.
    def enterImage(self, ctx: wxclParser.ImageContext):
        self.wxmlFile.write("<image src=\"")
        self.wxmlFile.write(ctx.getChild(2).getText()[1:-1] + "\"")

        self.DealWithIdAndClass(ctx, "image")

        self.wxmlFile.write(" mode = \"aspectFit\"/>\n")

    # Exit a parse tree produced by wxclParser#image.
    def exitImage(self, ctx: wxclParser.ImageContext):
        pass

    # Enter a parse tree produced by wxclParser#button.
    def enterButton(self, ctx: wxclParser.ButtonContext):
        def bindFunction():
            self.count["buttonBindFunction"] += 1
            self.wxmlFile.write(f" bind:tap=\"buttonBindFunction{self.count["buttonBindFunction"]}\"")
            self.jsFile.write(f"\tbuttonBindFunction{self.count["buttonBindFunction"]}(e){{\n")

        self.wxmlFile.write("<button")
        self.DealWithIdAndClass(ctx, "button")

        match ctx.function().getChild(0).getText():
            case "submit":
                self.wxmlFile.write(" form-type=\"submit\"")
            case "reset":
                self.wxmlFile.write(" form-type=\"reset\"")
            case "navigation":
                bindFunction()
                pageName = ctx.getChild(2).getChild(2).getText()
                self.jsFile.write("\t\twx.navigateTo({\n"
                                  f"\t\t\turl: '/pages/{pageName}/{pageName}'\n"
                                  "\t\t});\n"
                                  "\t},\n")

        self.wxmlFile.write(">")
        self.wxmlFile.write(ctx.getChild(5).getText()[1:-1])
        self.wxmlFile.write("</button>\n")

    # Exit a parse tree produced by wxclParser#button.
    def exitButton(self, ctx: wxclParser.ButtonContext):
        pass

    # Enter a parse tree produced by wxclParser#function.
    def enterFunction(self, ctx: wxclParser.FunctionContext):
        pass

    # Exit a parse tree produced by wxclParser#function.
    def exitFunction(self, ctx: wxclParser.FunctionContext):
        pass

    # Enter a parse tree produced by wxclParser#list.
    def enterList(self, ctx: wxclParser.ListContext):
        self.wxmlFile.write("<view")

        self.DealWithIdAndClassWithoutWxss(ctx, "list")

        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParser#list.
    def exitList(self, ctx: wxclParser.ListContext):
        self.wxmlFile.write("</view>\n")

        pageContent = ctx.getChild(2)
        written_elements = set()  # 存储已写入的元素
        for i in range(pageContent.getChildCount()):
            element = pageContent.getChild(i).getChild(0).getChild(0).getText()
            if element not in written_elements:
                self.wxssFile.write("#list" + str(self.count["list"]) + " > " + element + " ")
                written_elements.add(element)  # 标记已写入

        self.wxssFile.write("{\n")

    # Enter a parse tree produced by wxclParser#form.
    def enterForm(self, ctx: wxclParser.FormContext):
        self.wxmlFile.write("<form")
        self.DealWithIdAndClassWithoutWxss(ctx, "form")
        self.wxmlFile.write(f" bindsubmit=\"form{self.count["form"]}Submit\"")
        self.wxmlFile.write(">\n")
        self.jsFile.write(f"form{self.count["form"]}Submit(e) {{\n"
                          "wx.request({"
                          f"url: {ctx.String().getText()}, "
                          "method: 'POST',"
                          "data: e.detail.value,"
                          "success(res) {"
                          "if (res.statusCode === 200) {"
                          "wx.showToast({"
                          "title: '提交成功',"
                          "icon: 'success'"
                          "});"
                          "} else {"
                          "wx.showToast({"
                          "title: '提交失败',"
                          "icon: 'none'"
                          "});"
                          "}"
                          "},"
                          "fail(err) {"
                          "wx.showToast({"
                          "title: '网络错误',"
                          "icon: 'none'"
                          "});"
                          "}"
                          "});"
                          "},\n")

    # Exit a parse tree produced by wxclParser#Form.
    def exitForm(self, ctx: wxclParser.FormContext):
        self.wxmlFile.write("</form>\n")
        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + "form" + str(self.count["form"]) + " {\n")

    # Enter a parse tree produced by wxclParser#Label.
    def enterLabel(self, ctx: wxclParser.LabelContext):
        self.wxmlFile.write("<label")
        self.DealWithIdAndClassWithoutWxss(ctx, "label")
        if ctx.String() is not None:
            self.wxmlFile.write(" for=\"" + ctx.getChild(2).getText()[1:-1] + "\"")
        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParser#Labal.
    def exitLabel(self, ctx: wxclParser.LabelContext):
        self.wxmlFile.write("</label>\n")
        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + "label" + str(self.count["label"]) + " {\n")

    # Enter a parse tree produced by wxclParser#RadioGroup.
    def enterRadioGroup(self, ctx: wxclParser.RadioGroupContext):
        name = ctx.getChild(2).getText()[1:-1]
        self.wxmlFile.write("<radio-group")
        self.DealWithClassAndName(ctx, "radio-group", name)
        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParserRadioGroup.
    def exitRadioGroup(self, ctx: wxclParser.RadioGroupContext):
        self.wxmlFile.write("</radio-group>\n")
        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + ctx.getChild(2).getText()[1:-1] + " {\n")

    # Enter a parse tree produced by wxclParser#RadioOption.
    def enterRadioOption(self, ctx: wxclParser.RadioOptionContext):
        self.wxmlFile.write("<label>\n")
        value = ctx.getChild(0).getText()[1:-1]
        self.wxmlFile.write(f'<radio value="{value}"')
        if ctx.getChildCount() > 1:
            self.wxmlFile.write(' checked="true"')
        self.wxmlFile.write("/>\n")
        self.wxmlFile.write(f"<text>{value}</text>\n")
        self.wxmlFile.write("</label>\n")

    # Exit a parse tree produced by wxclParserRadioOption.
    def exitRadioOption(self, ctx: wxclParser.RadioOptionContext):
        pass

    # Enter a parse tree produced by wxclParser#CheckboxGroup.
    def enterCheckboxGroup(self, ctx: wxclParser.CheckboxGroupContext):
        name = ctx.getChild(2).getText()[1:-1]
        self.wxmlFile.write("<checkbox-group")
        self.DealWithClassAndName(ctx, "checkbox-group", name)
        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParserRadioGroup.
    def exitCheckboxGroup(self, ctx: wxclParser.CheckboxGroupContext):
        self.wxmlFile.write("</checkbox-group>\n")
        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + ctx.getChild(2).getText()[1:-1] + " {\n")

    # Enter a parse tree produced by wxclParser#CheckboxOption.
    def enterCheckboxOption(self, ctx: wxclParser.CheckboxOptionContext):
        self.wxmlFile.write("<label>\n")
        value = ctx.getChild(0).getText()[1:-1]
        self.wxmlFile.write(f'<checkbox value="{value}"')
        if ctx.getChildCount() > 1:
            self.wxmlFile.write(' checked="true"')
        self.wxmlFile.write("/>\n")
        self.wxmlFile.write(f"<text>{value}</text>\n")
        self.wxmlFile.write("</label>\n")

    # Exit a parse tree produced by wxclParserRadioOption.
    def exitCheckboxOption(self, ctx: wxclParser.CheckboxOptionContext):
        pass

    # Enter a parse tree produced by wxclParser#input.
    def enterInput(self, ctx: wxclParser.InputContext):
        name = ""
        self.wxmlFile.write("<input")
        self.wxmlFile.write(" type=\"" + ctx.inputType().getText() + "\"")
        if len(ctx.String()) > 1:
            self.wxmlFile.write(" placeholder=" + ctx.String(0).getText())
            name = ctx.String(1).getText()[1:-1]
            self.DealWithClassAndName(ctx, "input", name)
        else:
            name = ctx.String(0).getText()[1:-1]
            self.DealWithClassAndName(ctx, "input", name)
        self.wxmlFile.write("/>\n")

        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write(f"#{name} {{\n")

    # Exit a parse tree produced by wxclParser#input.
    def exitInput(self, ctx: wxclParser.InputContext):
        pass

    # Enter a parse tree produced by wxclParser#view.
    def enterView(self, ctx: wxclParser.ViewContext):
        self.wxmlFile.write("<view")
        if ctx.parentCtx.VariableName() is not None:
            self.wxmlFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:
            self.count["view"] += 1
            self.wxmlFile.write(" id=\"" + "view" + str(self.count["view"]) + "\"")

        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParser#view.
    def exitView(self, ctx: wxclParser.ViewContext):
        self.wxmlFile.write("</view>\n")

        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + "view" + str(self.count["view"]) + " {\n")

    # Enter a parse tree produced by wxclParser#navigator.
    def enterNavigator(self, ctx: wxclParser.NavigatorContext):
        self.wxmlFile.write("<navigator url=\"/pages/"
                            + ctx.getChild(2).getText() + "/"
                            + ctx.getChild(2).getText() + "\"")

        self.DealWithIdAndClassWithoutWxss(ctx, "navigator")

        # self.wxmlFile.write(" open-type=\"navigate\">\n")
        self.wxmlFile.write(">\n")

    # Exit a parse tree produced by wxclParser#navigator.
    def exitNavigator(self, ctx: wxclParser.NavigatorContext):
        self.wxmlFile.write("</navigator>\n")

        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + "navigator" + str(self.count["navigator"]) + " {\n")

    # Enter a parse tree produced by wxclParser#gui.
    def enterGui(self, ctx: wxclParser.GuiContext):
        pass

    # Exit a parse tree produced by wxclParser#gui.
    def exitGui(self, ctx: wxclParser.GuiContext):
        self.wxssFile.write("}\n\n")

    # Enter a parse tree produced by wxclParser#style.
    def enterStyle(self, ctx: wxclParser.StyleContext):
        pass

    # Exit a parse tree produced by wxclParser#style.
    def exitStyle(self, ctx: wxclParser.StyleContext):
        pass

    # Enter a parse tree produced by wxclParser#color.
    def enterColor(self, ctx: wxclParser.ColorContext):
        self.wxssFile.write("\t" + "color: ")
        self.wxssFile.write(ctx.getChild(2).getText() + ";\n")

    # Exit a parse tree produced by wxclParser#color.
    def exitColor(self, ctx: wxclParser.ColorContext):
        pass

    # Enter a parse tree produced by wxclParser#width.
    def enterWidth(self, ctx: wxclParser.WidthContext):
        self.wxssFile.write("\t" + "width: " + ctx.getChild(2).getText() + ";\n")

    # Exit a parse tree produced by wxclParser#width.
    def exitWidth(self, ctx: wxclParser.WidthContext):
        pass

    # Enter a parse tree produced by wxclParser#height.
    def enterHeight(self, ctx: wxclParser.HeightContext):
        self.wxssFile.write("\t" + "height: " + ctx.getChild(2).getText() + ";\n")

    # Exit a parse tree produced by wxclParser#height.
    def exitHeight(self, ctx: wxclParser.HeightContext):
        pass

    # Enter a parse tree produced by wxclParser#border.
    def enterBorder(self, ctx: wxclParser.BorderContext):
        self.wxssFile.write(
            f"\tborder: {ctx.getChild(2).getText()} {ctx.getChild(4).getText()} {ctx.getChild(6).getText()};\n")
        self.wxssFile.write("\tbox-sizing: border-box;\n")

    # Exit a parse tree produced by wxclParser#border.
    def exitBorder(self, ctx: wxclParser.BorderContext):
        pass

    # Enter a parse tree produced by wxclParser#borderWidth.
    def enterBorderWidth(self, ctx: wxclParser.BorderWidthContext):
        pass

    # Exit a parse tree produced by wxclParser#borderWidth.
    def exitBorderWidth(self, ctx: wxclParser.BorderWidthContext):
        pass

    # Enter a parse tree produced by wxclParser#borderColor.
    def enterBorderColor(self, ctx: wxclParser.BorderColorContext):
        pass

    # Exit a parse tree produced by wxclParser#borderColor.
    def exitBorderColor(self, ctx: wxclParser.BorderColorContext):
        pass

    # Enter a parse tree produced by wxclParser#position.
    def enterPosition(self, ctx: wxclParser.PositionContext):
        match ctx.HorizontalValue().getText():
            case "left":
                self.wxssFile.write("\tmargin-left: 0;\n"
                                    "\tmargin-right: auto;\n")
            case "center":
                self.wxssFile.write("\tmargin-left: auto;\n"
                                    "\tmargin-right: auto;\n")
            case "right":
                self.wxssFile.write("\tmargin-left: auto\n"
                                    "\tmargin-right: 0;\n")

    # Exit a parse tree produced by wxclParser#position.
    def exitPosition(self, ctx: wxclParser.PositionContext):
        pass

    # Enter a parse tree produced by wxclParser#font.
    def enterFont(self, ctx: wxclParser.FontContext):
        self.wxssFile.write("\t" + "font: " + ctx.getChild(2).getText() + " "
                            + ctx.getChild(4).getText() + " "
                            + ctx.getChild(6).getText() + ";\n")

    # Exit a parse tree produced by wxclParser#font.
    def exitFont(self, ctx: wxclParser.FontContext):
        pass

    # Enter a parse tree produced by wxclParser#fontSize.
    def enterFontSize(self, ctx: wxclParser.FontSizeContext):
        pass

    # Exit a parse tree produced by wxclParser#fontSize.
    def exitFontSize(self, ctx: wxclParser.FontSizeContext):
        pass

    # Enter a parse tree produced by wxclParser#textAlign.
    def enterTextAlign(self, ctx: wxclParser.TextAlignContext):
        self.wxssFile.write("\tdisplay: flex;\n")

        if ctx.HorizontalValue().getText() != "left":
            self.wxssFile.write("\tjustify-content: ")
            horizontal = ctx.HorizontalValue().getText()
            match horizontal:
                case "center":
                    self.wxssFile.write("center")
                case "right":
                    self.wxssFile.write("flex-end")
            self.wxssFile.write(";\n")

        self.wxssFile.write("\talign-items: ")
        vertical = ctx.VerticalValue().getText()
        match vertical:
            case "top":
                self.wxssFile.write("flex-start")
            case "middle":
                self.wxssFile.write("center")
            case "bottom":
                self.wxssFile.write("flex-end")
        self.wxssFile.write(";\n")

        self.wxssFile.write("\tflex-wrap: wrap;\n")

    # Exit a parse tree produced by wxclParser#textAlign.
    def exitTextAlign(self, ctx: wxclParser.TextAlignContext):
        pass

    # Enter a parse tree produced by wxclParser#background.
    def enterBackground(self, ctx: wxclParser.BackgroundContext):
        self.wxssFile.write(f"\tbackground: {ctx.getChild(2).getText()}")
        if ctx.String() is not None:
            self.wxssFile.write(f" url({ctx.getChild(4).getText()} no-repeat center / cover)")
        self.wxssFile.write(f";\n")

    # Exit a parse tree produced by wxclParser#background.
    def exitBackground(self, ctx: wxclParser.BackgroundContext):
        pass

    # Enter a parse tree produced by wxclParser#spacing.
    def enterSpacing(self, ctx: wxclParser.SpacingContext):
        if ctx.rpxValue(0).Number().getText() != "0":
            self.wxssFile.write(f"\tmargin-top: {ctx.rpxValue(0).getText()};\n")
        if ctx.rpxValue(1).Number().getText() != "0":
            self.wxssFile.write(f"\tmargin-bottom: {ctx.rpxValue(1).getText()};\n")

    # Exit a parse tree produced by wxclParser#spacing.
    def exitSpacing(self, ctx: wxclParser.SpacingContext):
        pass

    # Enter a parse tree produced by wxclParser#borderRadius.
    def enterBorderRadius(self, ctx: wxclParser.BorderRadiusContext):
        self.wxssFile.write(ctx.getText() + ";\n")

    # Exit a parse tree produced by wxclParser#borderRadius.
    def exitBorderRadius(self, ctx: wxclParser.BorderRadiusContext):
        pass

    # Enter a parse tree produced by wxclParser#rpxValue.
    def enterRpxValue(self, ctx: wxclParser.RpxValueContext):
        pass

    # Exit a parse tree produced by wxclParser#rpxValue.
    def exitRpxValue(self, ctx: wxclParser.RpxValueContext):
        pass

     # Enter a parse tree produced by wxclParser#padding.
    def enterPadding(self, ctx: wxclParser.PaddingContext):
        self.wxssFile.write(ctx.getText() + ";\n")

    # Exit a parse tree produced by wxclParser#padding.
    def exitPadding(self, ctx: wxclParser.PaddingContext):
        pass

    # Enter a parse tree produced by wxclParser#list_col.
    def enterList_col(self, ctx: wxclParser.List_colContext):
        # list内部元素样式
        self.wxssFile.write("\twidth: " + f"{100 / int(ctx.getChild(2).getText()):.2f}" + "%;\n")

    # Exit a parse tree produced by wxclParser#list_col.
    def exitList_col(self, ctx: wxclParser.List_colContext):
        pass

    # Enter a parse tree produced by wxclParser#list_rowHeight.
    def enterList_rowHeight(self, ctx: wxclParser.List_rowHeightContext):
        self.wxssFile.write("\theight: " + ctx.getChild(2).getText() + ";\n")
        self.wxssFile.write("}\n\n")

        # x写完list单元样式后写list整体样式
        self.wxssFile.write("#list" + str(self.count["list"]) + " {\n")
        self.wxssFile.write(CSS_CENTER)

    # Exit a parse tree produced by wxclParser#list_rowHeight.
    def exitList_rowHeight(self, ctx: wxclParser.List_rowHeightContext):
        pass

    # Enter a parse tree produced by wxclParser#swiper_interval.
    def enterSwiper_interval(self, ctx: wxclParser.Swiper_intervalContext):
        pass

    # Exit a parse tree produced by wxclParser#swiper_interval.
    def exitSwiper_interval(self, ctx: wxclParser.Swiper_intervalContext):
        pass


del wxclParser
