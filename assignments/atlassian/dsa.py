"""
Imagine you are the team that maintains the Atlassian employee directory. 
At Atlassian - there are multiple groups, and each can have one or more groups. Every employee is part of a group.
You are tasked with designing a system that could find the closest common parent group  given a target set of employees in the organization.


Example:
                Company (Engg, 3)
        HR                  Engg == (Engg, 3)
    Mona Springs          BE == (None, 2)            FE. (None, 1)             Deval
                        Alice Bob       Lisa Marley



RandomEmployee              

Questions:
1. Tree?
2. Binary tree? -> N-ary tree.
3. Parent groups can also have employees.
4. Everything under the tree.



def lca(employees: list) -> Group:


----- Implementation approach: ----


employees: Alice Bob Lisa


Mona -> Company -> HR -> Mona


O (V+E)


O target_employees * (V+E)


----------



Tree, Graph.
1. Directed graph.
2. cycles? No .valid DAG.

"""


from typing import Protocol
from dataclasses import dataclass

@dataclass(frozen=True)
class Employee:
    id: str

class GroupTreeNode:
    def __init__(self, name: str, subgroups: set['GroupTreeNode'] = None, employees: set[Employee]=None):
        self.name: str = name
        self.subgroups: set['GroupTreeNode'] = subgroups
        self.employees: set[Employee] = employees

class EmployeeDirectoryServiceInterface(Protocol):
    def lowest_common_ancestor(self, employees: list[Employee]) -> GroupTreeNode:
        ...




class EmployeeDirectoryServiceImpl:
    def __init__(self):
        self.employees: dict[str, Employee] = {
            'Mona': Employee("Mona"),
            'Springs': Employee('Springs'),
            'Alice': Employee('Alice'),
            'Bob': Employee('Bob'),
            'Lisa': Employee('Lisa'),
            'Marley': Employee('Marley'),
            'Deval': Employee('Deval')
        }
        # TODO: Codify this and move this function:
        # Root:
        HRNode = GroupTreeNode('HR', None, {self.employees['Mona'], self.employees['Springs']})
        BENode = GroupTreeNode('BE', None, {self.employees['Alice'], self.employees['Bob']})
        FENode = GroupTreeNode('FE', None, {self.employees['Lisa'], self.employees['Marley']})
        EnggNode = GroupTreeNode('Engg', {BENode, FENode}, {self.employees['Deval']})

        self.root: GroupTreeNode = GroupTreeNode('Company', {HRNode, EnggNode}, None)

    
    def lowest_common_ancestor(self, employees: list[Employee]) -> GroupTreeNode:
        target_set = set(employees)

        def dfs(node: GroupTreeNode) -> tuple[GroupTreeNode | None, int]:
            if node is None:
                return None, 0

            # print('node', node.name, node.employees, node.subgroups, '\n')

            count = 0
            # How many employees from the target set are in the 
            # current node:
            for employee in target_set:
                if node.employees and employee in node.employees:
                    count += 1

            if node.subgroups:
                for subgroup in node.subgroups:
                    ans, cnt = dfs(subgroup)
                    if ans is not None and cnt == len(target_set):
                        return ans, cnt
                    count += cnt

            # Check if the node is answer itself:
            if count == len(target_set):
                return node, count

            return None, count

        return dfs(self.root)


class EmployeeDirectoryServiceV2Interface(Protocol):
    def lowest_common_ancestor(self, employees: list[Employee]) -> GroupTreeNode:
        ...


class EmployeeDirectoryServiceImplV2:
    def __init__(self):
        self.employees: dict[str, Employee] = {
            'Mona': Employee("Mona"),
            'Springs': Employee('Springs'),
            'Alice': Employee('Alice'),
            'Bob': Employee('Bob'),
            'Lisa': Employee('Lisa'),
            'Marley': Employee('Marley'),
            'Deval': Employee('Deval'),
            'Jordan': Employee('Jordan'),
            'Penny': Employee('Penny'),
        }
        # TODO: Codify this and move this function:
        # Root:
        HRNode = GroupTreeNode('HR', None, {self.employees['Mona'], self.employees['Springs']})
        BENode = GroupTreeNode('BE', None, {self.employees['Alice'], self.employees['Bob']})
        FENode = GroupTreeNode('FE', None, {self.employees['Lisa'], self.employees['Marley']})
        DataEngg = GroupTreeNode('DataEngg', None, {self.employees['Jordan'], self.employees['Penny']})
        MLNode = GroupTreeNode('ML', {BENode, DataEngg}, None)
        EnggNode = GroupTreeNode('Engg', {BENode, FENode, DataEngg}, {self.employees['Deval']})

        self.root: GroupTreeNode = GroupTreeNode('Company', {HRNode, EnggNode, MLNode}, None)

    
    def lowest_common_ancestor(self, employees: list[Employee]) -> GroupTreeNode:
        target_set = set(employees)

        def dfs(node: GroupTreeNode) -> tuple[GroupTreeNode | None, set[Employee]]:
            if node is None:
                return None, set()

            # print('node', node.name, node.employees, node.subgroups, '\n')
            

            answer_set: set[Employee] = set()
            if node.employees:
                answer_set: set[Employee] = target_set & node.employees

            # print(node.name, 'answer_set v1', answer_set)
            

            if node.subgroups:
                for subgroup in node.subgroups:
                    ans_node, child_set = dfs(subgroup)
                    print(f'node: {node.name} calling {subgroup.name}: ', ans_node, child_set)
                    if ans_node is not None and child_set == target_set:
                        return ans_node, child_set
                    answer_set.update(child_set)



            # print(node.name, 'answer set v2', answer_set)
            # Check if the node is answer itself:
            if answer_set == target_set:
                return [node], answer_set

            return None, answer_set

        return dfs(self.root)





if __name__ == '__main__':
    # service: EmployeeDirectoryServiceInterface = EmployeeDirectoryServiceImpl()
    # assert service.lowest_common_ancestor([Employee('Mona'), Employee('Alice')])[0].name == 'Company'
    # assert service.lowest_common_ancestor([Employee('Alice'), Employee('Bob')])[0].name == 'BE'
    # assert service.lowest_common_ancestor([Employee('Deval'), Employee('Bob')])[0].name == 'Engg'    

    # print('Test cases - 1st passed!')


    servicev2: EmployeeDirectoryServiceV2Interface = EmployeeDirectoryServiceImplV2()
    assert servicev2.lowest_common_ancestor([Employee('Jordan'), Employee('Penny')])[0].name == 'DataEngg'
    assert servicev2.lowest_common_ancestor([Employee('Alice'), Employee('Jordan')])[0].name in ('Engg', 'ML')

    print('Test cases - 2nd passed!')

