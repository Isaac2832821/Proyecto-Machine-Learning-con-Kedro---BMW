from kedro.pipeline import Pipeline, node
from .nodes import split_data, train_model, evaluate_model

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=split_data,
            inputs=dict(
                df="bmw_classification_clean",
                target_column="params:target_column",
                test_size="params:test_size",
                random_state="params:random_state"
            ),
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="split_data_node"
        ),
        node(
            func=train_model,
            inputs=["X_train", "y_train", "params:model"],
            outputs="model",
            name="train_model_node"
        ),
        node(
            func=evaluate_model,
            inputs=["model", "X_test", "y_test"],
            outputs="accuracy",
            name="evaluate_model_node"
        ),
    ])