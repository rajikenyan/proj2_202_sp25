import csv
import math
from dataclasses import dataclass
from typing import *

@dataclass (frozen=True)
class Row:
    country: str
    year: int
    ehco2: float 
    ehco2_capita: float
    energyco2: float
    energyco2_capita: float
    tco2: float
    tco2_capita: float
@dataclass (frozen=True)
class Node:
    value: Row
    next: 'Node'=None

# Then your functions.
# ...
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename, 'r') as file:
        header = file.readline()
        parts = header.split(',')
        if len(parts) != 8:
            return None
        head = None
        for line in file.readlines(): 
            try: 
                line = line.split(',')
                country = line[0]
                year = int(line[1])
                ehco2 = float(line[2]) 
                ehco2_capita = float(line[3])
                energyco2 = float(line[4])
                energyco2_capita = float(line[5])
                tco2 = float(line[6])
                tco2_capita = float(line[7])
            except Exception as e:
                print("wrong type", e, line)
            data_row = Row(country, year, ehco2, ehco2_capita, energyco2, energyco2_capita, 
                            tco2, tco2_capita)
            head = LLappend(head, data_row)
        return head
def LLappend(cur_head: Node, value: Row) -> Node:
    if cur_head == None:
        return Node(value, None)
    new_head = Node(cur_head.value, next = LLappend(cur_head.next, value))
    return new_head


def listlen(data: Optional[Node]) -> int:
    if data == None:
        return 0
    return 1 + listlen(data.next)

def filter_rows(data: Optional[Node], field_name: str, comparison: str, value: Union[str, float, int]) -> Optional[Node]:
    if data == None:
        return None
    if field_name not in ["country", "year", "electricity_and_heat_co2_emissions","electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions", "energy_co2_emissions_per_capita","total_co2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita"]:
        print('invalid field',field_name)
        return None   #error 
    if comparison not in ["less_than", "greater_than", "equal"]:
        print('invalid comp', comparison)
        return None
    if field_name == "country" and comparison != "equal":
        print('country only supposrts equal', field_name, comparison)
        return None
    if field_name == "country" and type(value) != str:
        print('country has to be a str', type(value))
        return None #error
    if field_name == "year" and type(value) != int:
        print('year has to be int', type(value))
        return None
    if field_name in ["electricity_and_heat_co2_emissions","electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions", "energy_co2_emissions_per_capita","total_co2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita"] and not (type(value) == float or type(value) == int):
        print('invalid comparison', type(value))
        return None

    sublist = None
    save = data
    while save != None:
        if filter_match(save.value, field_name, comparison, value) == True:
            sublist = LLappend(sublist, save.value) 
        save = save.next 
    return sublist 

def filter_match(row: Row, field_name: str, comparison: str, value: Union[str, float, int]) -> bool:
    if field_name == "country":
        op1 = row.country
    elif field_name == "year":
        op1 = row.year
    elif field_name == "electricity_and_heat_co2_emissions":
        op1 = row.ehco2
    elif field_name == "electricity_and_heat_co2_emissions_per_capita":
        op1 = row.ehco2_capita
    elif field_name == "energy_co2_emissions":
        op1 = row.energyco2
    elif field_name == "energy_co2_emissions_per_capita":
        op1 = row.energyco2_capita
    elif field_name == "total_co2_emissions_excluding_lucf":
        op1 = row.tco2
    elif field_name == "total_co2_emissions_excluding_lucf_per_capita":
        op1 = row.tco2_capita
    else:
        return False
    if comparison == "equal":
        return op1 == value
    elif comparison == "less_than":
        return op1 < value
    return op1 > value

if __name__ == '__main__':
    head = read_csv_lines('some-ghg-emissions.csv')
    
    """head = None
    head = LLappend(head, Row('Ind', 1550, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))
    print(head)
    head = LLappend(head, Row('USA', 1234, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))
    print(head, head.next)
    head = LLappend(head, Row('China', 1111, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))
    print(head, head.next, head.next.next)
    for i in range(0,7000):
        head = LLappend(head, Row('China', 1000+i, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))
        print(i)"""


# Put your data definitions first!

# ...

# Then your functions.

# ...
