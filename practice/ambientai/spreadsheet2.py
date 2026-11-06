from typing import Literal, Optional, Protocol
from dataclasses import dataclass

"""
Design and implement an Excel Spreadsheet.
You are building a library that a front-end team may use to surface a spreadsheet to some users.
We want this to be a MVP library that can be expanded in the future if necessary.
All data can be stored in memory.

We have the following requirements:

We need to support integer values and formula values for the plus operator.

For example, cell values may be:

* -9, 2, 3, 100, etc. (maximum of 3 digits per integer)
* =2+8, =100+2, etc. (with exactly two integers)

We need to be able to reset cells to their default value, by giving the empty string.

We need to be able to view the spreadsheet, with both the raw and computed values shown.
For example, for "=2+8", the raw value is "=2+8" and the computed value is "10".
This does not have to look like a real spreadsheet, as long as the values are clear when printed.
Create a print method to print the whole spreadsheet, or return the spreadsheet data as a string.

The team will later focus on reference values, such as ``=A1+B2``.
You may look up syntax using a search engine.
"""



"""
Behaviour:
spreadsheet.set('A1', '5')
spreadsheet.set('B1', '=A1+1')
spreadsheet.set('C1', '=B1+1')
spreadsheet.set('D1', '=5+8')
spreadsheet.set('E1', '')
"""

Operand = Literal['+', '-', '*', '/']

def isnumber(s) -> bool:
    try:
        int(s)
        return True
    except:
        return False

class Cell:
    def __init__(self, sh: "SpreadsheetInterface", formula: str):
        self._spreadsheet: SpreadsheetInterface = sh
        self.raw_value = formula

    def evaluate(self) -> int:
        if self.raw_value == '':
            return 0
        # Parsing and other logic to come here
        # Parsing:
        left, op, right = self._parse()
        if op and right:
            parsed = []
            for v in (left, right):
                if type(v) is int:
                    parsed.append(v)
                else:
                    parsed.append(v.evaluate())
        else:
            return left

        ans = 0
        for v in parsed:
            ans += v

        return ans

    # 4
    # '=A1+1'
    # '=B1+1'
    #  '=5+8'
    # ''
    def _parse(self) -> tuple['str | int | Cell', Operand | None, 'int | Cell | None']:
        # Check if the value is an empty string or a raw integer:
        if self.raw_value == '':
            return 0, None, None
        # Check for integers: ex: 4
        if isnumber(self.raw_value):
            return int(self.raw_value), None, None

        # Check for expressions:
        if self.raw_value[0] == '=':
            raw: str = self.raw_value[1:]

            # Split on the basis of operand:
            values = raw.split('+') # Defaulting to +
            parsed_values = self.__parse_individual_values(values)

            return (parsed_values[0], '+', parsed_values[1]) # TODO: Right now operation is hardcoded with two values and one operator, this needs to be improved.


    def __parse_individual_values(self, values: list[str]) -> list['int | Cell']:
        # The value will be an int or a cell itself:
        res: list['int | Cell'] = []
        for value in values:
            if isnumber(value):
                res.append(int(value))
            else:
                cell: Cell = self._spreadsheet.get(value)
                res.append(cell)
        print('parsed_ind', res)
        return res


class SpreadsheetInterface(Protocol):
    def set(self, cell_ref: str, formula: str) -> None:
        ...

    def get(self, cell_ref: str) -> int:
        ...


class InMemorySpreadsheet:
    def __init__(self):
        # str -> Cell
        self.mp: dict[str, Cell] = {}

    def set(self, cell_ref: str, formula: str) -> None:
        self.mp[cell_ref] = Cell(sh=self, formula=formula)

    def get(self, cell_ref: str) -> int:
        if not cell_ref in self.mp:
            return 0
        cell = self.mp[cell_ref]
        return cell.evaluate()


if __name__ == '__main__':
    spreadsheet: SpreadsheetInterface = InMemorySpreadsheet()
    spreadsheet.set('A1', '5')
    print(spreadsheet.get('A1'))
    spreadsheet.set('B1', '=A1+1')
    print(spreadsheet.get('B1'))
    spreadsheet.set('C1', '=B1+1')
    print(spreadsheet.get('C1'))
    spreadsheet.set('D1', '=5+8')
    print(spreadsheet.get('C1'))
    spreadsheet.set('E1', '')
    print(spreadsheet.get('E1'))
