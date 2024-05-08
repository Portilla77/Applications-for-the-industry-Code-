import os
import matplotlib.pyplot as plt
import pandas as pd

def setup_plot_directory() -> str:
    """ Create a directory to store graphics if it does not exist and return the directory path.
        Returns:
            str: Path of the directory where the graphics will be saved.
    """
    folder_path = 'Portfolio/ML/plots'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def setup_data_directory() -> str:
    """ Create a directory to store dataframes if it does not exist and return the directory path.
        Returns:
            str: Path of the directory where the dataframes will be saved.
    """
    folder_path = 'Portfolio/ML/dataframe'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def save_plot(fig: plt.Figure, filename: str = 'plot.png',
              dpi: int = 300, show: bool = True) -> None:
    """ Save a graphic to the specified directory.
        Args:
            fig (matplotlib.figure.Figure): Matplotlib figure to be saved.
            filename (str, optional): Name of the file under which the graphic will be saved.
                                      Default is 'plot.png'.
            dpi (int, optional): Resolution in dots per inch for the saved graphic. Default is 300.
            show (bool, optional): If True, displays the graphic. Default is True.
    """
    folder_path = setup_plot_directory()
    file_path = os.path.join(folder_path, filename)
    fig.savefig(file_path, dpi=dpi, bbox_inches='tight')
    if show:
        plt.show()
    plt.close(fig)

def save_dataframe(data: pd.DataFrame, filename: str = 'output.csv',
                   index: bool = False) -> None:
    """ Save a DataFrame in CSV format to the specified directory.
        Args:
            data (pandas.DataFrame): DataFrame to be saved.
            filename (str, optional): Name of the file under which the DataFrame will be saved.
                                      Default is 'output.csv'.
            index (bool, optional): If True, the DataFrame's index will be included in the file.
                                    Default is False.
    """
    folder_path = setup_data_directory()
    file_path = os.path.join(folder_path, filename)
    data.to_csv(file_path, index=index)

def save_dataframe_as_html(data: pd.DataFrame, filename: str = 'output.html',
                           index: bool = False) -> None:
    """ Save a DataFrame in HTML format to the specified directory.
        Args:
            data (pandas.DataFrame): DataFrame to be saved.
            filename (str, optional): Name of the file under which the DataFrame will be saved.
                                      Default is 'output.html'.
            index (bool, optional): If True, the DataFrame's index will be included in the file.
                                    Default is False.
    """
    folder_path = setup_data_directory()
    file_path = os.path.join(folder_path, filename)
    data.to_html(file_path, index=index)
