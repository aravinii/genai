from sklearn.preprocessing import FunctionTransformer
import numpy as np

def clip_transformer(a_min, a_max):
    return FunctionTransformer(
        np.clip,
        kw_args={"a_min": a_min, "a_max": a_max},
        feature_names_out="one-to-one",
    )

def zero_to_nan(x):
    return np.where(x == 0, np.nan, x)