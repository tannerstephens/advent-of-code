from math import inf, prod
from numbers import Number

from tinsel import BaseSolution, Processing
from tinsel.consts import NOOP


class RestrictedNumber:
    def __init__(self, ident: str | None = None, gt: Number | None = None, lt: Number | None = None):
        if gt is None:
            self.gt = -inf
        else:
            self.gt = gt

        if lt is None:
            self.lt = inf
        else:
            self.lt = lt

        self.ident = ident or "self"

    def __gt__(self, val):
        if val >= self.lt:
            return False

        self.gt = max(val, self.gt)

        return True

    def __lt__(self, val):
        if val <= self.gt:
            return False

        self.lt = min(self.lt, val)

        return True

    def __ge__(self, val):
        return self > (val - 1)

    def __le__(self, val):
        return self < (val + 1)

    def range(self) -> int:
        return self.lt - self.gt - 1

    def copy(self):
        return RestrictedNumber(self.ident, self.gt, self.lt)

    def __repr__(self):
        return f"({self.gt} < {self.ident} < {self.lt})"


class Solution(BaseSolution):
    VAR_TO_INDEX = {"x": 0, "m": 1, "a": 2, "s": 3}

    def next_workflow(self, rating: list[int], workflow: list[tuple[str, str, int, str]]) -> str:
        for var, op, val, goto in workflow[:-1]:
            var = rating[self.VAR_TO_INDEX[var]]
            if (op == "<" and var < val) or (op == ">" and var > val):
                return goto

        return workflow[-1]

    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.workflows = {}

        workflows, ratings = p.split("\n\n", mapping=Processing)

        for ((name, parts),) in workflows.re_findall(r"(.+){(.+)}", mapping=NOOP):
            mappings = []
            parts = parts.split(",")

            for part in parts[:-1]:
                cond, goto = part.split(":")

                mappings.append((cond[0], cond[1], int(cond[2:]), goto))

            mappings.append(parts[-1])

            self.workflows[name] = mappings

        self.accepted = []

        for rating in ratings.re_findall(r"\d+", mapping=int):
            wf = "in"

            while wf not in ("A", "R"):
                wf = self.next_workflow(rating, self.workflows[wf])

            if wf == "A":
                self.accepted.append(rating)

        return sum(sum(r) for r in self.accepted)

    def collapse_workflows(
        self,
        workflows: dict[str, tuple],
        current_workflow: str | None = None,
        values: list[RestrictedNumber] | None = None,
    ) -> list[list[RestrictedNumber]]:
        if values is None:
            values = [RestrictedNumber(c, 0, 4001) for c in "xmas"]

        if current_workflow is None:
            current_workflow = "in"

        accepted = []

        values_clone = values[:]

        for var, op, val, goto in workflows[current_workflow][:-1]:
            i = self.VAR_TO_INDEX[var]

            passthrough = values_clone[:]
            tmp = values_clone[i].copy()

            if op == "<":
                if goto != "R" and (var := values_clone[i].copy()) < val:
                    passthrough[i] = var

                    if goto == "A":
                        accepted.append(passthrough)
                    else:
                        accepted.extend(self.collapse_workflows(workflows, goto, passthrough))
                tmp >= val
            else:
                if goto != "R" and (var := values_clone[i].copy()) > val:
                    passthrough[i] = var

                    if goto == "A":
                        accepted.append(passthrough)
                    else:
                        accepted.extend(self.collapse_workflows(workflows, goto, passthrough))
                tmp <= val

            values_clone[i] = tmp

        back = workflows[current_workflow][-1]
        if back == "A":
            accepted.append(values_clone[:])
        elif back != "R":
            accepted.extend(self.collapse_workflows(workflows, back, values_clone[:]))

        return accepted

    def part2(self, puzzle_input: str):
        return sum(
            prod(part.range() for part in collapsed_workflow)
            for collapsed_workflow in self.collapse_workflows(self.workflows)
        )
