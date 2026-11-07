"""
Find the closest Org for target Employees
a) Imagine you are the team that maintains the Atlassian employee directory. At Atlassian – there are multiple groups, and each can have one or more groups. Every employee is part of a group. You are tasked with designing a system that could find the closest common parent group giv a target set of employees in the organization.
b) The Atlassian hierarchy sometimes can have shared group across an org or employees shared across different groups – How will the code evolve n this case if the requirement is to provide ONE closest common group
c) The system now introduced 4 methods to update the structure of the hierarchy in the org. Supose these dynamic updates are done in separate threads while getCommonGroupForEmployees is being called, How ill your system handled reads and writes into the system efficiently such that at any given time getCommonGroupForEmployees always reflects the latest updated state of the hierarchy?
d) The company consists of a single level of groups with no subgroups. Each group has a set of employees.
"""
from collections import deque
from dataclasses import dataclass
from typing import Protocol
from pprint import pprint

@dataclass(frozen=True)
class Employee:
    id: str


@dataclass(eq=False)
class TreeNode:
    name: str
    employees: set[Employee]
    subgroups: set['TreeNode']

    @staticmethod
    def from_name(name: str) -> 'TreeNode':
        return TreeNode(
            name=name,
            employees=set(),
            subgroups=set()
        )

class EmployeeDirectoryServiceInterface(Protocol):
    def add_group(self, name: str, parent: TreeNode | None = None) -> TreeNode:
        ...

    def add_group_employee(self, group_node: TreeNode, employee: Employee) -> None:
        ...

    def find_lowest_common_ancestor(self, employees: list[Employee]) -> TreeNode | None:
        ...


class EmployeeDirectoryService:
    def __init__(self):
        self.root = self.add_group(name='company')

    def add_group(self, name: str, parent: TreeNode | None = None) -> TreeNode:
        node = TreeNode.from_name(name=name)
        # We need to create root node if parent is None
        if parent is None:
            return node

        parent.subgroups.add(node)
        return node

    def add_group_employee(self, group_node: TreeNode, employee: Employee) -> None:
        group_node.employees.add(employee)

    def find_lowest_common_ancestor(self, employees: list[Employee]) -> TreeNode | None:
        target_set = set(employees)
        def dfs(node: TreeNode) -> tuple[TreeNode, int]:
            if node is None:
                return None, 0

            count = 0
            # Traverse the node's employees and increase the count:
            for employee in node.employees:
                if employee in target_set:
                    count += 1

            for subgroup in node.subgroups:
                newnode, cnt = dfs(subgroup)
                if cnt == len(employees):
                    return newnode, cnt
                count += cnt

            # This itself is the LCA node:
            if count == len(employees):
                return node, count

            return None, count

        return dfs(self.root)[0]
            

    def print_dir(self):
        queue: deque[TreeNode] = deque([self.root])
        order = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.name)

                for child in node.subgroups:
                    queue.append(child)

            order.append(level)

        pprint(order)


class EmployeeDirectoryServiceV2(EmployeeDirectoryService):
    """A DAG: groups can have multiple parents and employees multiple groups.

    Group names are unique and provide a deterministic alphabetical tie-break.
    Use the service methods to modify the graph so it stays acyclic.
    """

    def __init__(self):
        self.groups: dict[str, TreeNode] = {}
        super().__init__()

    def _validate_group(self, group: TreeNode) -> None:
        if self.groups.get(group.name) is not group:
            raise ValueError('Group does not belong to this directory')

    def add_group(self, name: str, parent: TreeNode | None = None) -> TreeNode:
        if name in self.groups:
            raise ValueError(f'Group already exists: {name}')
        if parent is not None:
            self._validate_group(parent)
        node = super().add_group(name, parent)
        self.groups[name] = node
        return node

    def add_subgroup(self, parent: TreeNode, subgroup: TreeNode) -> None:
        """Attach an existing group to another parent without creating a cycle."""
        self._validate_group(parent)
        self._validate_group(subgroup)
        stack = [subgroup]
        visited = set()
        while stack:
            node = stack.pop()
            if node is parent:
                raise ValueError('Adding this subgroup would create a cycle')
            if node not in visited:
                visited.add(node)
                stack.extend(node.subgroups)
        parent.subgroups.add(subgroup)

    def add_group_employee(self, group_node: TreeNode, employee: Employee) -> None:
        self._validate_group(group_node)
        group_node.employees.add(employee)

    def find_lowest_common_ancestor(self, employees: list[Employee]) -> TreeNode | None:
        """Return one lowest common group, breaking ties by group name.

        A common group contains every target directly or through subgroups.
        It is lowest if none of its subgroups is also a common group.
        Empty input or an employee missing from the rooted graph returns None.
        """
        targets = set(employees)
        if not targets:
            return None

        matches: dict[TreeNode, set[Employee]] = {}

        def dfs(node: TreeNode) -> set[Employee]:
            if node not in matches:
                found = node.employees & targets
                for subgroup in node.subgroups:
                    # Union avoids counting shared employees or paths twice.
                    found |= dfs(subgroup)
                matches[node] = found
            return matches[node]

        if dfs(self.root) != targets:
            return None

        common_groups = {node for node, found in matches.items() if found == targets}
        lowest_groups = [
            node for node in common_groups
            if not (node.subgroups & common_groups)
        ]
        return min(lowest_groups, key=lambda node: node.name)

    def print_dir(self):
        """Print each group once at its shortest distance from the root."""
        queue = deque([self.root])
        visited = {self.root}
        order = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.name)
                for child in sorted(node.subgroups, key=lambda group: group.name):
                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
            order.append(level)
        pprint(order)


def build_example_tree(directory: EmployeeDirectoryService) -> None:
    engineering = directory.add_group('engineering', directory.root)
    frontend = directory.add_group('frontend', engineering)
    backend = directory.add_group('backend', engineering)
    payments = directory.add_group('payments', backend)
    benefits = directory.add_group('benefits', backend)
    payroll = directory.add_group('payroll', payments)
    remittance = directory.add_group('remittance', payments)
    retirements = directory.add_group('retirements', benefits)
    flex = directory.add_group('flex', benefits)

    for employee_id in ('a', 'b', 'c'):
        directory.add_group_employee(payments, Employee(employee_id))
    for employee_id in ('d', 'e'):
        directory.add_group_employee(flex, Employee(employee_id))
    directory.add_group_employee(remittance, Employee('f'))


if __name__ == '__main__':
    directory = EmployeeDirectoryService()
    build_example_tree(directory)
    directory.print_dir()


    print('LCA', directory.find_lowest_common_ancestor(employees=[
        Employee('a'), Employee('f'), Employee('b')
    ]))
    print('LCA', directory.find_lowest_common_ancestor(
        employees=[Employee(name) for name in ('a', 'b', 'c', 'd', 'e', 'f')]
    ))

    # Question (b): shared groups and multiple employee memberships.
    directory_v2 = EmployeeDirectoryServiceV2()
    build_example_tree(directory_v2)
    payments = directory_v2.groups['payments']
    benefits = directory_v2.groups['benefits']
    shared_services = directory_v2.add_group('shared services', payments)
    directory_v2.add_subgroup(benefits, shared_services)
    directory_v2.add_group_employee(benefits, Employee('a'))
    directory_v2.add_group_employee(shared_services, Employee('shared-worker'))

    print('\nV2: shared groups are printed once')
    directory_v2.print_dir()
    common_group = directory_v2.find_lowest_common_ancestor([
        Employee('a'), Employee('shared-worker')
    ])
    # Both payments and benefits are lowest; alphabetical order selects benefits.
    print('V2 LCA (alphabetical tie-break):', common_group.name)
