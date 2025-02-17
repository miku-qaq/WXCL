# Generated from /Users/macbookpro/Desktop/antlr/wxclDefinition/wxcl.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .wxclParser import wxclParser
else:
    from wxclParser import wxclParser

# This class defines a complete generic visitor for a parse tree produced by wxclParser.

class wxclVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by wxclParser#project.
    def visitProject(self, ctx:wxclParser.ProjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#navigationBar.
    def visitNavigationBar(self, ctx:wxclParser.NavigationBarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#appStyleVariableList.
    def visitAppStyleVariableList(self, ctx:wxclParser.AppStyleVariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#pageList.
    def visitPageList(self, ctx:wxclParser.PageListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#page.
    def visitPage(self, ctx:wxclParser.PageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#pageContent.
    def visitPageContent(self, ctx:wxclParser.PageContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#styleVariableList.
    def visitStyleVariableList(self, ctx:wxclParser.StyleVariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#styleVariable.
    def visitStyleVariable(self, ctx:wxclParser.StyleVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#component.
    def visitComponent(self, ctx:wxclParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#swiper.
    def visitSwiper(self, ctx:wxclParser.SwiperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#ablum.
    def visitAblum(self, ctx:wxclParser.AblumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#text.
    def visitText(self, ctx:wxclParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#image.
    def visitImage(self, ctx:wxclParser.ImageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#button.
    def visitButton(self, ctx:wxclParser.ButtonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#function.
    def visitFunction(self, ctx:wxclParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#list.
    def visitList(self, ctx:wxclParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#form.
    def visitForm(self, ctx:wxclParser.FormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#label.
    def visitLabel(self, ctx:wxclParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#radioGroup.
    def visitRadioGroup(self, ctx:wxclParser.RadioGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#radioOption.
    def visitRadioOption(self, ctx:wxclParser.RadioOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#checkboxGroup.
    def visitCheckboxGroup(self, ctx:wxclParser.CheckboxGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#checkboxOption.
    def visitCheckboxOption(self, ctx:wxclParser.CheckboxOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#input.
    def visitInput(self, ctx:wxclParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#inputType.
    def visitInputType(self, ctx:wxclParser.InputTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#view.
    def visitView(self, ctx:wxclParser.ViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#navigator.
    def visitNavigator(self, ctx:wxclParser.NavigatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#gui.
    def visitGui(self, ctx:wxclParser.GuiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#style.
    def visitStyle(self, ctx:wxclParser.StyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#color.
    def visitColor(self, ctx:wxclParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#width.
    def visitWidth(self, ctx:wxclParser.WidthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#height.
    def visitHeight(self, ctx:wxclParser.HeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#border.
    def visitBorder(self, ctx:wxclParser.BorderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#borderWidth.
    def visitBorderWidth(self, ctx:wxclParser.BorderWidthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#borderColor.
    def visitBorderColor(self, ctx:wxclParser.BorderColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#position.
    def visitPosition(self, ctx:wxclParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#font.
    def visitFont(self, ctx:wxclParser.FontContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#fontSize.
    def visitFontSize(self, ctx:wxclParser.FontSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#textAlign.
    def visitTextAlign(self, ctx:wxclParser.TextAlignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#background.
    def visitBackground(self, ctx:wxclParser.BackgroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#spacing.
    def visitSpacing(self, ctx:wxclParser.SpacingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#borderRadius.
    def visitBorderRadius(self, ctx:wxclParser.BorderRadiusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#rpxValue.
    def visitRpxValue(self, ctx:wxclParser.RpxValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#padding.
    def visitPadding(self, ctx:wxclParser.PaddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#list_col.
    def visitList_col(self, ctx:wxclParser.List_colContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#list_rowHeight.
    def visitList_rowHeight(self, ctx:wxclParser.List_rowHeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by wxclParser#swiper_interval.
    def visitSwiper_interval(self, ctx:wxclParser.Swiper_intervalContext):
        return self.visitChildren(ctx)



del wxclParser