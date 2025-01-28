# Generated from C:/Users/bochi/PycharmProjects/antlr/wxclDefinition/wxcl.g4 by ANTLR 4.13.1
from antlr4 import *
from tool import *

if "." in __name__:
    from .wxclParser import wxclParser
else:
    from wxclParser import wxclParser


# This class defines a complete listener for a parse tree produced by wxclParser.
class wxclListener(ParseTreeListener):
    # Enter a parse tree produced by wxclParser#project.
    def __init__(self):
        self.wxclFile = None
        self.wxssFile = None
        self.listCount = 0
        self.swiperCount = 0

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
        self.listCount = 0
        self.swiperCount = 0
        self.wxclFile = open("pages/" + ctx.getChild(3).getText() + ".wxcl", "a")
        self.wxssFile = open("pages/" + ctx.getChild(3).getText() + ".wxss", "a")

    # Exit a parse tree produced by wxclParser#page.
    def exitPage(self, ctx: wxclParser.PageContext):
        if self.swiperCount > 0:
            self.wxssFile.write(Function.hasAblum())

        self.wxclFile.close()
        self.wxssFile.close()

    # Enter a parse tree produced by wxclParser#pageContent.
    def enterPageContent(self, ctx: wxclParser.PageContentContext):
        pass

    # Exit a parse tree produced by wxclParser#pageContent.
    def exitPageContent(self, ctx: wxclParser.PageContentContext):
        pass

    # Enter a parse tree produced by wxclParser#component.
    def enterComponent(self, ctx: wxclParser.ComponentContext):
        pass

    # Exit a parse tree produced by wxclParser#component.
    def exitComponent(self, ctx: wxclParser.ComponentContext):
        pass

    # Enter a parse tree produced by wxclParser#swiper.
    def enterSwiper(self, ctx: wxclParser.SwiperContext):
        self.swiperCount += 1
        a = ctx.parentCtx.getChild(2)
        self.wxclFile.write("<swiper autoplay=\"true\"")
        self.wxclFile.write(" id=\"swiper\"" + str(self.swiperCount))
        for i in range(1, a.getChildCount() - 1, 2):
            if a.getChild(i).getChild(0).getChild(0).getText() == "interval":
                self.wxclFile.write(" interval=\"" + a.getChild(i).getChild(0).Number().getText() + "\"")
                break
        self.wxclFile.write(">\n")

        self.wxssFile.write("#swiper" + str(self.swiperCount) + " {\n")
        self.wxssFile.write("\twidth: 100%;\n")

    # Exit a parse tree produced by wxclParser#swiper.
    def exitSwiper(self, ctx: wxclParser.SwiperContext):
        self.wxclFile.write("</swiper>\n")

    # Enter a parse tree produced by wxclParser#ablum.
    def enterAblum(self, ctx: wxclParser.AblumContext):
        for i in range(1, ctx.getChildCount(), 4):
            self.wxclFile.write("<swiper-item>\n")
            self.wxclFile.write("<image src=\"" + ctx.getChild(i).getText() + "\" mode=\"aspectFix\"/>\n")
            self.wxclFile.write("</swiper-item>\n")

    # Exit a parse tree produced by wxclParser#ablum.
    def exitAblum(self, ctx: wxclParser.AblumContext):
        pass

    # Enter a parse tree produced by wxclParser#text.
    def enterText(self, ctx: wxclParser.TextContext):
        pass

    # Exit a parse tree produced by wxclParser#text.
    def exitText(self, ctx: wxclParser.TextContext):
        pass

    # Enter a parse tree produced by wxclParser#image.
    def enterImage(self, ctx: wxclParser.ImageContext):
        self.wxclFile.write("<image src = \"")
        self.wxclFile.write(ctx.getChild(3).getText() + "\"")
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
        self.listCount += 1
        self.wxclFile.write("<view class=\"list" + str(self.listCount) + "\">\n")

        self.wxssFile.write(".list" + str(self.listCount) + " {\n")

    # Exit a parse tree produced by wxclParser#list.
    def exitList(self, ctx: wxclParser.ListContext):
        self.wxclFile.write("</view>\n")

    # Enter a parse tree produced by wxclParser#input.
    def enterInput(self, ctx: wxclParser.InputContext):
        pass

    # Exit a parse tree produced by wxclParser#input.
    def exitInput(self, ctx: wxclParser.InputContext):
        pass

    # Enter a parse tree produced by wxclParser#nevigator.
    def enterNevigator(self, ctx: wxclParser.NevigatorContext):
        self.wxclFile.write("<navigator url =\" \"")
        if (ctx.parentCtx.parentCtx.parentCtx.getChild(0).getText() == "list"):
            self.wxclFile.write(" class=\"list" + str(self.listCount) + "-item\"")
        self.wxclFile.write(" open-type=\"navigate\">\n")

    # Exit a parse tree produced by wxclParser#nevigator.
    def exitNevigator(self, ctx: wxclParser.NevigatorContext):
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
        pass

    # Exit a parse tree produced by wxclParser#color.
    def exitColor(self, ctx: wxclParser.ColorContext):
        pass

    # Enter a parse tree produced by wxclParser#width.
    def enterWidth(self, ctx: wxclParser.WidthContext):
        self.wxssFile.write("\t" + "width: " + ctx.getChild(2).getText() + ";\n")

    # Exit a parse tree produced by wxclParser#width.
    def exitWidth(self, ctx: wxclParser.WidthContext):
        pass

    # Enter a parse tree produced by wxclParser#heigth.
    def enterHeigth(self, ctx: wxclParser.HeigthContext):
        self.wxssFile.write("\t" + "height: " + ctx.getChild(2).getText() + ";\n")

    # Exit a parse tree produced by wxclParser#heigth.
    def exitHeigth(self, ctx: wxclParser.HeigthContext):
        pass

    # Enter a parse tree produced by wxclParser#border.
    def enterBorder(self, ctx: wxclParser.BorderContext):
        pass

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
        pass

    # Exit a parse tree produced by wxclParser#position.
    def exitPosition(self, ctx: wxclParser.PositionContext):
        pass

    # Enter a parse tree produced by wxclParser#font.
    def enterFont(self, ctx: wxclParser.FontContext):
        pass

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
        pass

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
        pass

    # Exit a parse tree produced by wxclParser#list_col.
    def exitList_col(self, ctx: wxclParser.List_colContext):
        pass

    # Enter a parse tree produced by wxclParser#list_rowHeight.
    def enterList_rowHeight(self, ctx: wxclParser.List_rowHeightContext):
        pass

    # Exit a parse tree produced by wxclParser#list_rowHeight.
    def exitList_rowHeight(self, ctx: wxclParser.List_rowHeightContext):
        pass

    # Enter a parse tree produced by wxclParser#swiper_interval.
    def enterSwiper_interval(self, ctx: wxclParser.Swiper_intervalContext):
        pass

    # Exit a parse tree produced by wxclParser#swiper_interval.
    def exitSwiper_interval(self, ctx: wxclParser.Swiper_intervalContext):
        pass

    # Enter a parse tree produced by wxclParser#string.
    def enterString(self, ctx: wxclParser.StringContext):
        pass

    # Exit a parse tree produced by wxclParser#string.
    def exitString(self, ctx: wxclParser.StringContext):
        pass


del wxclParser
