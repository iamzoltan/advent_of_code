import numpy as np


with open('day11.txt', 'r') as file:
    monkey_text = file.readlines()


class Monkey:
    def __init__(
            self,
            number,
            starting_items,
            operation,
            op_val,
            test_val,
            true_mon,
            false_mon
        ):
        self.number = number
        self.items = starting_items
        self.operation = operation
        self.op_val = op_val
        self.test_val = test_val
        self.true_mon = true_mon
        self.false_mon = false_mon

    def op(self, value):
        if self.operation == '*':
            return value * self.op_val
        elif self.operation == '+':
            return value + self.op_val
        elif self.operation == "**":
            return value * value

    def test(self, value):
        if value % self.test_val == 0:
            return self.true_mon
        else:
            return self.false_mon


def parse_monkey_text(text):
    """Parse monkey text and return a list of Monkey class"""
    monks = []
    monkey_num = 0
    starting_items = []
    operation = ""
    op_val = 0
    test_val = 0
    true_mon = 0
    false_mon = 0
    # Model Monkeys
    for monkey_info in text:
        if monkey_info == '\n':
            continue
        monkey_info = monkey_info.strip('\n').strip(' ').split(' ')
        if monkey_info[0] == 'Monkey':
            monkey_num = int(monkey_info[-1].strip(':'))
            continue
        elif monkey_info[0] == 'Starting':
            starting_items = [int(x.strip(',')) for x in monkey_info[2:]]
            continue
        elif monkey_info[0] == 'Operation:':
            if monkey_info[-1] == 'old':
                operation = "**"
            else:
                op_val = int(monkey_info[-1])
                operation = monkey_info[-2]
            continue
        elif monkey_info[0] == 'Test:':
            test_val = int(monkey_info[-1])
            continue
        elif monkey_info[1] == 'true:':
            true_mon = int(monkey_info[-1])
            continue
        elif monkey_info[1] == 'false:':
            false_mon = int(monkey_info[-1])
            # instantiate monkey at end of info
            monk = Monkey(
                monkey_num,
                starting_items,
                operation,
                op_val,
                test_val,
                true_mon,
                false_mon
            )
            monks.append(monk)
            continue
    return monks


def calc_monkey_biz(num_iters, relief_factor, monkeys):
    num_inspects = [0] * len(monkeys)
    divs = [x.test_val for x in monkeys]
    common_fact = 1
    # Handle large ints by reducing size with common factor
    for div in set(divs):
        common_fact *= div
    for i in range(num_iters):
        for j, monkey in enumerate(monkeys):
            for item in monkey.items:
                if relief_factor != 1:
                    val = int(monkey.op(item)/relief_factor)
                else: 
                    val = monkey.op(item) % common_fact
                tossed_to = monkey.test(val)
                assert j != tossed_to
                monkeys[tossed_to].items.append(val)
                num_inspects[j] += 1
            monkey.items = []
    num_inspects.sort()
    monkey_biz = num_inspects[-1] * num_inspects[-2]
    return monkey_biz


# Part 1
monkeys = parse_monkey_text(monkey_text)
print(calc_monkey_biz(20, 3, monkeys))
# Part 2
monkeys = parse_monkey_text(monkey_text)
print(calc_monkey_biz(10000, 1, monkeys))

