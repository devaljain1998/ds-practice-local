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

Later we will focus on reference values, such as `=A1+B2`.

sheet = Spreadsheet()
sheet.modify("A1", "5")
sheet.modify("B1", "=20+1")
sheet.modify("A1", "-9")
sheet.modify("A3", "")
sheet.modify("A3", "1")
sheet.modify("A3", "")
sheet.modify("A3", "")
sheet.print()

You can use the following code to get started. Feel free to modify the starter code, use it, extend it, or ignore it. Move, add, or remove classes or functions as you see fit.
You may look up syntax using a search engine.

We now want to support reference values, such as ``=B2+B3``.

Additions should now take either integers, or cell references, or a combination.
If a cell references another cell which has not been set, consider the value of that other cell to be 0.

Let's first discuss how you would implement that, and what some key challenges might be.
"""
from dataclasses import dataclass
import sys
from typing import Optional


OPERANDS = {'+'}

def is_number(x: str) -> tuple[bool, int]:
    try:
        val = int(float(x))
        return True, val
    except:
        return False, -1

@dataclass
class Cell:
    label: str
    raw_value: str
    _computed_value: None | int
    spreadsheet: "Spreadsheet"
    dependents: set["Cell"]
    is_cached: bool = False

    def __init__(self, label: str, raw_value: str, spreadsheet: "Spreadsheet"):
        self.spreadsheet = spreadsheet
        self.label = label
        self.raw_value = raw_value
        self.dependents = set()
        self.is_cached = False
        self._computed_value = None

    @property
    def computed_value(self):
        if self.is_cached:
            return self._computed_value
        self._computed_value = self._evaluate()
        return self._computed_value

    def _evaluate(self) -> int:
        operand_fn = {
            '+': lambda x, y: x+y 
        }
        left, operand, right = self._parse_raw_value()
        if isinstance(left, Cell):
            left = left._evaluate()
        if operand is not None:
            if isinstance(right, Cell):
                right = right._evaluate()
                return operand_fn[operand](left, right)
            if isinstance(right, int):
                return operand_fn[operand](left, right)
    
        return left
            

    def _parse_raw_value(self) -> tuple[None | int, None | str, None | int]:
        """
        Example raw values:
            5
            =20+1
            -9
            ''
            1
            =A1+1
            =A1+B1
        """
        print(f'trying to decode {self.raw_value}')
        if self.raw_value is None:
            raise ValueError('raw_value cannot be null.')
        # Try to parse empty string:
        if self.raw_value == '':
            return None, None, None
        
        # Try to parse full int:
        ok, num = is_number(self.raw_value)
        if ok:
            return num, None, None

        # Try to parse: =20+1
        if self.raw_value and self.raw_value[0] == '=':
            self.raw_value = self.raw_value[1:]

        # Try to parse left + right:
        found = False
        for operand in OPERANDS:
            try:
                left_raw_val, right_raw_val = self.raw_value.split(operand)
                found = True
            except:
                continue

        if not found:
            raise ValueError(f'Not able to parse the raw value: {self.label}:{self.raw_value}')

        # Convert left_raw_val and right_raw_val:
        left: None | int = None
        right: None | int = None

        # Check for int:
        ok, leftn = is_number(left_raw_val)
        if ok:
            left = leftn
        # If not number it should be a cell:
        else:
            left_cell: Cell = self.spreadsheet.lookup(left_raw_val)
            left = left_cell._evaluate()

        ok, rightn = is_number(right_raw_val)
        if ok:
            right = rightn
        # If not number it should be a cell:
        else:
            right_cell: Cell = self.spreadsheet.lookup(right_raw_val)
            if right_cell:
                right = right_cell._evaluate()

        return left, operand, right

    def mark_cache_invalid(self):
        self.is_cached = False
        for dependent in self.dependents:
            dependent.mark_dependendents_invalid()


    


class Spreadsheet:
    def __init__(self):
        self.cells: dict[str, Cell] = {}

    def modify(self, cell_ref: str, formula: str):
        # It is a new cell:
        if not cell_ref in self.cells:
            self.cells[cell_ref] = Cell(
                label=cell_ref,
                raw_value=formula,
                spreadsheet=self
            )
        else:
            cell = self.cells[cell_ref]
            cell.raw_value = formula
            cell.is_cached = False
            # Make sure to update all the cell dependents as invalid:
            cell.mark_cache_invalid()


    def print(self):
        print('Spreadsheet value:')
        for key, val in sorted(self.cells.items()):
            print(key, val.computed_value)
        print('============================')

    def lookup(self, cell_ref) -> Optional[Cell]:
        return self.cells.get(cell_ref)


# Testing the code:
if __name__ == '__main__':
    sheet = Spreadsheet()
    sheet.modify("A1", "5")
    sheet.modify("B1", "=20+1")
    sheet.modify('A1', '-1')
    # print(sheet.cells)
    # sys.exit(1)
    sheet.modify('C1', '=B1+1')
    sheet.print()
