from kedro.pipeline import Pipeline, node
from .nodes import limpiar_sales, limpiar_classification, limpiar_used

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=limpiar_sales,
            inputs="bmw_sales",
            outputs="bmw_sales_clean",
            name="limpiar_sales_node"
        ),
        node(
            func=limpiar_classification,
            inputs="bmw_classification",
            outputs="bmw_classification_clean",
            name="limpiar_classification_node"
        ),
        node(
            func=limpiar_used,
            inputs="bmw_used",
            outputs="bmw_used_clean",
            name="limpiar_used_node"
        ),
    ])