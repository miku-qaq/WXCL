# Generated from C:/Users/bochi/PycharmProjects/antlr/wxclDefinition/wxcl.g4 by ANTLR 4.13.1
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
        self.wxclFile = None
        self.wxssFile = None
        self.count = {
            "list": 0,
            "swiper": 0,
            "image": 0,
            "text": 0,
            "navigator": 0
        }

    # 判别是否有嵌套的list id和class处理 并同时有id 在wxss中加上
    def DealWithIdAndClass(self, ctx, selfType: str):
        if ctx.parentCtx.parentCtx.parentCtx.getChild(0).getText() == "list":
            self.wxclFile.write(" class=\"list" + str(self.count["list"]) + "-item")
            if ctx.parentCtx.VariableName() is not None:
                self.wxclFile.write(" " + ctx.parentCtx.VariableName().getText())
            self.wxclFile.write("\"")
        elif ctx.parentCtx.VariableName() is not None:
            self.wxclFile.write(" class=\"" + ctx.parentCtx.VariableName().getText() + "\"")

        if ctx.parentCtx.gui() is not None:
            self.count[selfType] += 1
            self.wxclFile.write(" id=\"" + selfType + str(self.count[selfType]) + "\"")
            self.wxssFile.write("#" + selfType + str(self.count[selfType]) + " {\n")

    # Enter a parse tree produced by wxclParser#project.
    def enterProject(self, ctx: wxclParser.ProjectContext):
        pass

    # Exit a parse tree produced by wxclParser#project.
    def exitProject(self, ctx: wxclParser.ProjectContext):
        pass

    # Enter a parse tree produced by wxclParser#pageList.
    def enterPageList(self, ctx: wxclParser.PageListContext):
        pass

    # Exit a parse tree produced by wxclParser#pageList.
    def exitPageList(self, ctx: wxclParser.PageListContext):
        pass

    # Enter a parse tree produced by wxclParser#page.
    def enterPage(self, ctx: wxclParser.PageContext):
        self.page += 1
        self.count["wxclFile"] = None
        self.count["wxssFile"] = None
        self.count["list"] = 0
        self.count["swiper"] = 0
        self.count["image"] = 0
        self.count["text"] = 0
        self.count["navigator"] = 0
        self.wxclFile = open("pages/" + ctx.getChild(4).getText() + ".wxml", "w")
        self.wxssFile = open("pages/" + ctx.getChild(4).getText() + ".wxss", "w")

    # Exit a parse tree produced by wxclParser#page.
    def exitPage(self, ctx: wxclParser.PageContext):
        if self.count["swiper"] > 0:
            self.wxssFile.write(Function.hasAblum())

        self.wxclFile.close()
        self.wxssFile.close()

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
        pass

    # Exit a parse tree produced by wxclParser#button.
    def exitButton(self, ctx: wxclParser.ButtonContext):
        pass

    # Enter a parse tree produced by wxclParser#function.
    def enterFunction(self, ctx: wxclParser.FunctionContext):
        pass

    # Exit a parse tree produced by wxclParser#function.
    def exitFunction(self, ctx: wxclParser.FunctionContext):
        pass

    # Enter a parse tree produced by wxclParser#pageLocation.
    def enterPageLocation(self, ctx: wxclParser.PageLocationContext):
        pass

    # Exit a parse tree produced by wxclParser#pageLocation.
    def exitPageLocation(self, ctx: wxclParser.PageLocationContext):
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

    # Enter a parse tree produced by wxclParser#input.
    def enterInput(self, ctx: wxclParser.InputContext):
        pass

    # Exit a parse tree produced by wxclParser#input.
    def exitInput(self, ctx: wxclParser.InputContext):
        pass

    # Enter a parse tree produced by wxclParser#navigator.
    def enterNavigator(self, ctx: wxclParser.NavigatorContext):
        self.wxclFile.write("<navigator url=\" \"")

        # 检测嵌套双类
        self.DealWithIdAndClass(ctx, "navigator")

        self.wxclFile.write(" open-type=\"navigate\">\n")

    # Exit a parse tree produced by wxclParser#navigator.
    def exitNavigator(self, ctx: wxclParser.NavigatorContext):
        self.wxclFile.write("</navigator>\n")

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
            case "center":
                self.wxssFile.write("\tmargin: auto;\n")
            case "left":
                self.wxssFile.write("\tmargin-left: 0;\n")

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
        pass

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
        self.wxssFile.write(".list" + str(self.count["list"]) + "-item {\n")
        self.wxssFile.write("\twidth: " + f"{100 / int(ctx.getChild(2).getText()):.2f}" + "%;\n")

    # Exit a parse tree produced by wxclParser#list_col.
    def exitList_col(self, ctx: wxclParser.List_colContext):
        pass

    # Enter a parse tree produced by wxclParser#list_rowHeight.
    def enterList_rowHeight(self, ctx: wxclParser.List_rowHeightContext):
        self.wxssFile.write("\theight: " + ctx.getChild(2).getText() + ";\n")
        self.wxssFile.write(CSS_CENTER)
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
