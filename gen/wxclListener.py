# Generated from C:/Users/bochi/PycharmProjects/antlr/wxclDefinition/wxcl.g4 by ANTLR 4.13.1
# -*- coding: gbk -*-
import os
import shutil

from antlr4 import *
from tool import *

if "." in __name__:
    from gen.wxclParser import wxclParser
else:
    from wxclParser import wxclParser


# This class defines a complete listener for a parse tree produced by wxclParser.
class wxclListener(ParseTreeListener):
    def __init__(self):
        self.page = 0
        self.appJsonFile = None
        self.wxclFile = None
        self.wxssFile = None
        self.jsFile = None
        self.jsonFile = None
        self.count = {
            "list": 0,
            "swiper": 0,
            "image": 0,
            "text": 0,
            "navigator": 0,
            "view": 0,
            "button": 0,
            "function": 0,
            "buttonBindFunction":0
        }

    # id和class处理 并同时有id 在wxss中加上
    def DealWithIdAndClass(self, ctx, selfType: str):
        if ctx.parentCtx.VariableName() is not None:
            self.wxclFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:
            self.count[selfType] += 1
            self.wxclFile.write(" id=\"" + selfType + str(self.count[selfType]) + "\"")
            self.wxssFile.write("#" + selfType + str(self.count[selfType]) + " {\n")

    # Enter a parse tree produced by wxclParser#project.
    def enterProject(self, ctx: wxclParser.ProjectContext):
        if os.path.exists(PROJECT_DIR_NAME):
            shutil.rmtree(PROJECT_DIR_NAME)
        os.makedirs(PROJECT_DIR_NAME)

        self.appJsonFile = open(PROJECT_DIR_NAME + "/app.json", "w")
        self.appJsonFile.write("{\n")

    # Exit a parse tree produced by wxclParser#project.
    def exitProject(self, ctx: wxclParser.ProjectContext):
        self.appJsonFile.write(APPJSON_CONST)
        self.appJsonFile.write("}")
        self.appJsonFile.close()

    # Enter a parse tree produced by wxclParser#navigationBar.
    def enterNavigationBar(self, ctx: wxclParser.NavigationBarContext):
        self.appJsonFile.write("\t" + "\"window\": {\n"
                               + "\t\t" + "\"navigationBarTextStyle\": " + "\"" + ctx.getChild(2).getText() + "\",\n"
                               + "\t\t" + "\"navigationBarTitleText\": " + ctx.getChild(4).getText() + ",\n"
                               + "\t\t" + "\"navigationBarBackgroundColor\": " + "\"" + ctx.getChild(
            6).getText() + "\"\n"
                               + "\t},\n")

    # Exit a parse tree produced by wxclParser#navigationBar.
    def exitNavigationBar(self, ctx: wxclParser.NavigationBarContext):
        pass

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
        self.count["wxclFile"] = None
        self.count["wxssFile"] = None
        self.count["jsFile"] = None
        self.count["jsonFile"] = None
        self.count["list"] = 0
        self.count["swiper"] = 0
        self.count["image"] = 0
        self.count["text"] = 0
        self.count["navigator"] = 0
        self.count["view"] = 0
        self.count["button"] = 0
        self.count["function"] = 0
        self.count["buttonBindFunction"] = 0
        PageName = ctx.getChild(4).getText()
        # 当前页面所有文件所处的路径
        dir_path = PROJECT_DIR_NAME + "/pages/" + PageName
        # 如果目标目录不存在，创建目录
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        else:
            print("页面名重复！")
            exit(1)

        self.wxclFile = open(dir_path + "/" + PageName + ".wxml", "w")
        self.wxssFile = open(dir_path + "/" + PageName + ".wxss", "w")
        self.jsFile = open(dir_path + "/" + PageName + ".js", "w")
        self.jsFile.write("Page({\n")
        self.jsonFile = open(dir_path + "/" + PageName + ".json", "w")
        self.jsonFile.write(JSON_CONST)

        self.appJsonFile.write("\t\t" + "\"pages/" + PageName + "/" + PageName + "\"")

    # Exit a parse tree produced by wxclParser#page.
    def exitPage(self, ctx: wxclParser.PageContext):
        if self.count["swiper"] > 0:
            self.wxssFile.write(Function.hasAblum())

        self.wxclFile.close()
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

    # Enter a parse tree produced by wxclParser#styleList.
    def enterStyleList(self, ctx: wxclParser.StyleVariableListContext):
        pass

    # Exit a parse tree produced by wxclParser#styleList.
    def exitStyleList(self, ctx: wxclParser.StyleVariableListContext):
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
        self.wxclFile.write("<swiper autoplay=\"true\"")

        if ctx.parentCtx.VariableName() is not None:
            self.wxclFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:  # id样式添加判断
            self.count["swiper"] += 1
            self.wxclFile.write(" id=\"swiper" + str(self.count["swiper"]) + "\"")
            self.wxssFile.write("#swiper" + str(self.count["swiper"]) + " {\n")
            self.wxssFile.write("\twidth: 100%;\n")

        for i in range(1, a.getChildCount() - 1, 2):
            if a.getChild(i).getChild(0).getChild(0).getText() == "interval":
                self.wxclFile.write(" interval=\"" + a.getChild(i).getChild(0).Number().getText() + "\"")
                break
        self.wxclFile.write(">\n")

    # Exit a parse tree produced by wxclParser#swiper.
    def exitSwiper(self, ctx: wxclParser.SwiperContext):
        self.wxclFile.write("</swiper>\n")

    # Enter a parse tree produced by wxclParser#ablum.
    def enterAblum(self, ctx: wxclParser.AblumContext):
        for i in range(0, ctx.getChildCount(), 2):
            self.wxclFile.write("<swiper-item>\n")
            self.wxclFile.write("<image src=\"" + ctx.getChild(i).getText()[1:-1] + "\" mode=\"aspectFix\"/>\n")
            self.wxclFile.write("</swiper-item>\n")

    # Exit a parse tree produced by wxclParser#ablum.
    def exitAblum(self, ctx: wxclParser.AblumContext):
        pass

    # Enter a parse tree produced by wxclParser#text.
    def enterText(self, ctx: wxclParser.TextContext):
        self.wxclFile.write("<text")
        self.DealWithIdAndClass(ctx, "text")
        self.wxclFile.write(">")

        self.wxclFile.write(ctx.getChild(2).getText()[1:-1])

        self.wxclFile.write("</text>\n")

    # Exit a parse tree produced by wxclParser#text.
    def exitText(self, ctx: wxclParser.TextContext):
        pass

    # Enter a parse tree produced by wxclParser#image.
    def enterImage(self, ctx: wxclParser.ImageContext):
        self.wxclFile.write("<image src=\"")
        self.wxclFile.write(ctx.getChild(2).getText()[1:-1] + "\"")

        self.DealWithIdAndClass(ctx, "image")

        self.wxclFile.write(" mode = \"aspectFit\"/>\n")

    # Exit a parse tree produced by wxclParser#image.
    def exitImage(self, ctx: wxclParser.ImageContext):
        pass

    # Enter a parse tree produced by wxclParser#button.
    def enterButton(self, ctx: wxclParser.ButtonContext):
        self.wxclFile.write("<button")
        self.DealWithIdAndClass(ctx, "button")
        self.count["buttonBindFunction"] += 1
        self.wxclFile.write(" bind:tap=\"buttonBindFunction" + str(self.count["buttonBindFunction"]) + "\"")
        self.wxclFile.write(" type=\"primary\">")
        self.wxclFile.write(ctx.getChild(5).getText()[1:-1])
        self.wxclFile.write("</button>\n")

        self.jsFile.write("\tbuttonBindFunction" + str(self.count["buttonBindFunction"]) + "(e) {\n")
        match ctx.getChild(2).getText():
            case _:
                pageName = ctx.getChild(2).getChild(2).getText()
                self.jsFile.write("\t\twx.navigateTo({\n"
                                  + "\t\t\turl: '/pages/" + pageName + "/" + pageName + "'\n"
                                  + "\t\t});\n")
        self.jsFile.write("\t},\n")


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
        self.wxclFile.write("<view")

        if ctx.parentCtx.VariableName() is not None:
            self.wxclFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        self.count["list"] += 1
        self.wxclFile.write(" id=\"list" + str(self.count["list"]) + "\"")

        self.wxclFile.write(">\n")

    # Exit a parse tree produced by wxclParser#list.
    def exitList(self, ctx: wxclParser.ListContext):
        self.wxclFile.write("</view>\n")

        pageContent = ctx.getChild(2)
        written_elements = set()  # 存储已写入的元素
        for i in range(pageContent.getChildCount()):
            element = pageContent.getChild(i).getChild(0).getChild(0).getText()
            if element not in written_elements:
                self.wxssFile.write("#list" + str(self.count["list"]) + " > " + element + " ")
                written_elements.add(element)  # 标记已写入

        self.wxssFile.write("{\n")

    # Enter a parse tree produced by wxclParser#input.
    def enterInput(self, ctx: wxclParser.InputContext):
        pass

    # Exit a parse tree produced by wxclParser#input.
    def exitInput(self, ctx: wxclParser.InputContext):
        pass

    # Enter a parse tree produced by wxclParser#view.
    def enterView(self, ctx: wxclParser.ViewContext):
        self.wxclFile.write("<view")
        if ctx.parentCtx.VariableName() is not None:
            self.wxclFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:
            self.count["view"] += 1
            self.wxclFile.write(" id=\"" + "view" + str(self.count["view"]) + "\"")

        self.wxclFile.write(">\n")

    # Exit a parse tree produced by wxclParser#view.
    def exitView(self, ctx: wxclParser.ViewContext):
        self.wxclFile.write("</view>\n")

        if ctx.parentCtx.gui() is not None:
            self.wxssFile.write("#" + "view" + str(self.count["view"]) + " {\n")

    # Enter a parse tree produced by wxclParser#navigator.
    def enterNavigator(self, ctx: wxclParser.NavigatorContext):
        self.wxclFile.write("<navigator url=\"/pages/"
                            + ctx.getChild(2).getText() + "/"
                            + ctx.getChild(2).getText() + "\"")

        # 检测嵌套双类 此处较为特殊，暂时不支持
        # self.DealWithIdAndClass(ctx, "navigator")
        if ctx.parentCtx.VariableName() is not None:
            self.wxclFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:
            self.count["navigator"] += 1
            self.wxclFile.write(" id=\"" + "navigator" + str(self.count["navigator"]) + "\"")

        # self.wxclFile.write(" open-type=\"navigate\">\n")
        self.wxclFile.write(">\n")

    # Exit a parse tree produced by wxclParser#navigator.
    def exitNavigator(self, ctx: wxclParser.NavigatorContext):
        self.wxclFile.write("</navigator>\n")

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
        self.wxssFile.write("\t" + "border: "
                            + ctx.getChild(2).getText() + " "
                            + ctx.getChild(4).getText() + " "
                            + ctx.getChild(6).getText() + ";\n")
        self.wxssFile.write("\t" + "box-sizing: border-box;\n")

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
        match ctx.getChild(2).getText():
            case "left":
                pass
            case "center":
                self.wxssFile.write("\tmargin:0 auto;\n")
            case "right":
                self.wxssFile.write("\tmargin: 0 0 auto 0;\n")

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
        if ctx.getChild(2).getText() != "left" or ctx.getChild(4).getText() != "top":
            self.wxssFile.write("\t" + "display: flex" + ";\n")
        if ctx.getChild(2).getText() != "left":
            self.wxssFile.write("\t" + "justify-content: ")
            horizontal = ctx.getChild(2).getText()
            match horizontal:
                case "center":
                    self.wxssFile.write("center" + ";\n")
                case "right":
                    self.wxssFile.write("flex-end" + ";\n")
        if ctx.getChild(4).getText() != "top":
            self.wxssFile.write("\t" + "align-items: ")
            vertical = ctx.getChild(4).getText()
            match vertical:
                case "middle":
                    self.wxssFile.write("center" + ";\n")
                case "bottom":
                    self.wxssFile.write("flex-end" + ";\n")
        self.wxssFile.write("\t" + "flex-wrap: wrap" + ";\n")

    # Exit a parse tree produced by wxclParser#textAlign.
    def exitTextAlign(self, ctx: wxclParser.TextAlignContext):
        pass

    # Enter a parse tree produced by wxclParser#background.
    def enterBackground(self, ctx: wxclParser.BackgroundContext):
        self.wxssFile.write("\t" + "background: " + ctx.getChild(2).getText() + " "
                            + "url(" + ctx.getChild(4).getText() + ") "
                            + "no-repeat center / cover" + ";\n")

    # Exit a parse tree produced by wxclParser#background.
    def exitBackground(self, ctx: wxclParser.BackgroundContext):
        pass

    # Enter a parse tree produced by wxclParser#rpxValue.
    def enterRpxValue(self, ctx: wxclParser.RpxValueContext):
        pass

    # Exit a parse tree produced by wxclParser#rpxValue.
    def exitRpxValue(self, ctx: wxclParser.RpxValueContext):
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
