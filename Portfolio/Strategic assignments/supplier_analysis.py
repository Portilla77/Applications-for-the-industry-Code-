import pandas as pd
import numpy as np

def normalize_values(currency_value, value_min, value_max):
    """Normalizes a given value within a defined range.

    Args:
        - currency_value (float): The current value to normalize.
        - value_min (float): Minimum value within the normalization range.
        - value_max (float): Maximum value within the normalization range.

    Return:
        - float: Normalized value in [0,1].
    """

    return (currency_value - value_min) / (value_max - value_min)

def weighted_values(values, weights_):
    """Calculates the weighted sum of a given series of values,
      using a dictionary of weights.

    Args:
        - values (pd.Series): Contains the values to be weighted.
        - weights_ (dict): Maps the names of the evaluation criteria
          to their respective weights.

    Return:
        -float: Weighted sum of the values.
    """

    return sum(value * weights_[factor] for value, factor in zip(values, values.index))


def weighted_calculation(sequence):
    """Calculates the percentage of each element in a sequence
    relative to its total sum.

    Args:
        -sequence (list[float]): List of numerical values.

    Return:
          -list[float]: List of percentages corresponding to each
                        element of the original sequence.
    """
    total = sum(sequence)
    return [np.round((score*100 / total),2) for score in sequence]

def supplier_analysis(data_supplier:list,number_supplier:list,
                    evaluation_criteria:list, weightings:dict) -> pd.DataFrame:
    """Performs an analysis of suppliers (players) by normalizing
    their data, applying weightings, and calculating their
    percentage of allocation.

    Args:
      - data_supplier (list): List of lists that contains the data of
                              the suppliers.
      - number_supplier (list): List of identifiers/names of the suppliers.
      - evaluation_criteria (list): List of evaluation criteria used for
                                    the suppliers.
      - weightings (dict): Dictionary that maps the evaluation criteria to their
                          respective weights.

    Return:
        - pd.DataFrame: DataFrame that contains the original data of the suppliers,
          their normalized values, weighted sums, and the percentage of allocation for
          each supplier.
    """
    supplier_df = pd.DataFrame(data_supplier, index=number_supplier,
                              columns = evaluation_criteria)
    value_min, value_max = supplier_df.min(), supplier_df.max()
    process = supplier_df.apply(lambda x: normalize_values(x, value_min[x.name], value_max[x.name]))
    weighted_sums = process.apply(lambda x: weighted_values(x, weightings), axis=1)
    percentage_sequence = weighted_calculation(weighted_sums)
    supplier_df["Allocation per player (%)"] = percentage_sequence
    return supplier_df
