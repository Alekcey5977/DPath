from axisProcessor import AxisProcessor
from InitializerParent import ParentInitializer
from grammar_generated.GrammarVisitor import GrammarVisitor
from grammar_generated.GrammarParser import GrammarParser


class QueryVisitor(GrammarVisitor):
    def __init__(self, json_data):
        self.json_data = json_data
        self.parent_initializer = ParentInitializer(json_data)
        self.axis_processor = AxisProcessor(self.parent_initializer.get_parent_map())

    def visitQuery(self, ctx: GrammarParser.QueryContext):
        path_expr_ctx = ctx.pathExpr()
        steps = [child for child in path_expr_ctx.getChildren() if isinstance(child, GrammarParser.StepContext)]
        result = self.json_data  # Начинаем с корня JSON-данных
        for step in steps:
            result = self.apply_step(step, result)  # Применяем каждый шаг пути

        return result

    def apply_step(self, step_ctx, current_data):
        axis = step_ctx.axis().getText()  # Получаем ось (например, 'child' или 'parent')
        identifier = step_ctx.identifier().getText() if step_ctx.identifier() else None  # Получаем идентификатор (например, 'AVP_2')

        return self.axis_processor.process(axis, current_data, identifier)