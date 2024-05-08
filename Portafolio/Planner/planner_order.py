from datetime import datetime,timedelta
import math
import attr
import numpy as np
import pandas as pd

def order_dummy(len_total_sku:int,available_sku:int) -> pd.DataFrame:
    """ Generate a DataFrame simulating order data for a set number of SKUs.

    This function creates a DataFrame with simulated order data including SKUs,
    times, and quantities. Each entry represents an order, with SKUs randomly
    generated within a specified range. The function ensures unique order identifiers
    and randomizes the time and quantity associated with each SKU.

    Args:
        len_total_sku (int): Total number of orders to generate.
        available_sku (int): Upper limit for the SKU range from which random SKUs are to be generated.

    Return:
        pd.DataFrame: A DataFrame with three columns: 'Sku', 'Time', and 'Quantity',
                  indexed by unique order identifiers."""
    np.random.seed(1)
    test_order = {
        "Sku": [f"Material {np.random.randint(1,available_sku)}"
                for x in range(1,len_total_sku+1)],
        "Time": [np.random.randint(10,100) for x in range(1,len_total_sku+1)],
        "Quantity": [np.round(np.random.randint(10,100),2) for x in range(1,len_total_sku+1)]
    }
    df_order = pd.DataFrame(test_order)
    df_order.index = [f"Order {i}" for i in range(1,len_total_sku+1)]
    return df_order

@attr.s(slots=True)
class PlaneerOrder():
    """Class that allows working with a set of orders and a capacity
    given by some resource. Its objective is to process the available
    orders and send an alert when the resource needs to be loaded or
    refilled and then process the remaining orders.

    Methods:
        convert_dataframe: As its name indicates, it converts a
        dataframe to a readable dictionary for subsequent methods.
        order_planner.
        order_planner: Processes a dictionary containing the information
        of orders in the key and quantities associated with these in its value,
        this is: {(order 1,value 1),...,(order n, value n)}.
        This helps us measure which orders we can process and which we cannot.
        Those that cannot be processed are stored in a dictionary that it returns
        a resource filling message and subsequently apply recursion on the remaining
        orders.
    """
    date = attr.ib(default = None, type = float)
    _formats = attr.ib(default = ['days','hours','minutes'], type = list)
    df_dummy = attr.ib(default = None , type = pd.DataFrame)
    greatest_value = attr.ib(default = None, type = float)

    def convert_data(self):
        """Converts the 'df_dummy' DataFrame into a dictionary where each key
        corresponds to an order index and the value is another dictionary holding
        'Quantity' and 'Time' data.

        Return:
            dict: A dictionary with order indexes as keys and corresponding 'Quantity'
            and 'Time' as values."""
        empty_data = {}
        for index, row in self.df_dummy.iterrows():
            empty_data[index] = {'Quantity': row['Quantity'], 'Time': row['Time']}
        print(empty_data)
        return empty_data

    def _format_day(self,day:int,hour:float,minutes:float) -> str:
        """Formats a time duration given in days, hours, and minutes.

        Args:
            day (int): The number of days.
            hour (int): The number of hours.
            minutes (int): The number of minutes.

        Return:
            str: A formatted string representing the time duration in days, hours, and minutes.
        """
        data = [day,hour,minutes]
        match_time  = []
        for time_value,time_unit in zip(data,self._formats):
            if time_value>0:
                if time_value>=1:
                    match_time.append(f'{time_value} {time_unit}')
                else:
                    match_time.append(str(time_value)+ ' '+ time_unit.rstrip('s'))
        return ', '.join(match_time)

    def _unit_converter(self,number: float) -> str:
        """Converts a floating point number representing total hours into a
        formatted string displaying the equivalent amount of time in days,
        hours, and minutes.

        The input is split into the integer and decimal part. The integer part represents
        complete hours, and the decimal part is converted to minutes.

        Args:
            number (float): A floating number representing the total hours.

        Return:
            str: A formatted string that displays the time in days, hours, and minutes.
        """
        self.date = number
        part_float,part_int=math.modf(self.date)
        round_float=np.round(part_float,2)
        minutes = int((round_float*60))
        part_int= datetime(1,1,1) + timedelta(hours = self.date)
        return self._format_day(part_int.day-1,part_int.hour,minutes)

    def order_planer(self, value_maximum:float, data: dict) -> dict:
        """Processes orders and ensures the maximum quantity is not exceeded.
        Orders that can be fulfilled with the current available value are processed.
        If an order exceeds the available value,send a message to fill out the resource
        and be able to start the process again.

        Args:
            value_maximum (float): The maximum value against which the orders.
            data (dict): A dictionary of orders where the key is the order identifier

        Return:
            dict: A dictionary of processed orders."""

        current_value = value_maximum
        new_list = {}
        for x, y in data.items():
            if y.get('Quantity') <= current_value:
                current_value = current_value-y.get('Quantity')
                new_list[x] = {'Quantity':y['Quantity'],'Time':y['Time']}
                print(f"{x} can be processed as {np.round(current_value, 2)}"+
                      " units remain available, This order has a duration of"+
                      f" {self._unit_converter(int(np.round(y.get('Time'), 2)))} hours.")
            else:
                print("Fill resource as they are needed "+
                      f"{np.round(np.abs(current_value - y.get('Quantity')), 2)} units "
                      f"to process {x}.")
                unmatched_item = {k: v for k, v in data.items() if k not in new_list}
                self.order_planer(value_maximum, unmatched_item)
                return new_list
