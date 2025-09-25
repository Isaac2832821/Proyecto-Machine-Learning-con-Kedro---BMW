from typing import Dict
from kedro.pipeline import Pipeline
from proyecto_ml.pipelines import data_engineering as de
from proyecto_ml.pipelines import data_science as ds

def register_pipelines() -> Dict[str, Pipeline]:
    return {
        "data_engineering": de.create_pipeline(),
        "data_science": ds.create_pipeline(),
        "__default__": de.create_pipeline() + ds.create_pipeline(),
    }