from collections import deque
from enum import Enum
from math import lcm
from typing import Type

from tinsel import BaseSolution, Processing


class PulseType(Enum):
    LOW = "low"
    HIGH = "high"


class Pulse:
    def __init__(self, origin: "Module", target: "Module", pulse_type: PulseType) -> None:
        self.origin = origin
        self.target = target
        self.pulse_type = pulse_type

    def resolve(self) -> list["Pulse"]:
        # print(f"{self.origin} -{self.pulse_type.value}-> {self.target}")
        return self.target.pulse(self.origin, self.pulse_type)

    @property
    def type(self):
        return self.pulse_type


class Module:
    def __init__(self, name, connections: list["Module"] = None, from_connections: list["Module"] = None):
        self.name = name
        self.connections = connections or []
        self.from_connections = from_connections or []

    def pulse(self, origin: "Module", pulse_type: PulseType) -> list[Pulse]:
        return []

    def pulse_connections(self, pulse_type: PulseType) -> list[Pulse]:
        return [Pulse(self, conn, pulse_type) for conn in self.connections]

    def add_connection(self, module: "Module"):
        self.connections.append(module)

    def add_from(self, module: "Module"):
        self.from_connections.append(module)

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def evolve(self, new_type: Type["Module"]):
        new_instance = new_type(self.name, self.connections, self.from_connections)

        self.__class__ = new_instance.__class__
        self.__dict__ = new_instance.__dict__

    def reset(self):
        pass


class FlipFlop(Module):
    def __init__(self, name, connections: list["Module"] = None, from_connections: list["Module"] = None):
        super().__init__(name, connections, from_connections)

        self.state = False

    def pulse(self, origin: "Module", pulse_type: PulseType) -> list[Pulse]:
        if pulse_type is PulseType.LOW:
            self.state = not self.state

            pulse_type = PulseType.HIGH if self.state else PulseType.LOW

            return self.pulse_connections(pulse_type)
        return []

    def reset(self):
        self.state = False


class Conjuction(Module):
    def __init__(self, name, connections: list["Module"] = None, from_connections: list["Module"] = None):
        super().__init__(name, connections, from_connections)
        self.last_pulse: dict[Module, PulseType] = {conn: PulseType.LOW for conn in self.from_connections}

    def add_from(self, module: Module):
        self.last_pulse[module] = PulseType.LOW
        return super().add_from(module)

    def pulse(self, origin: Module, pulse_type: PulseType) -> list[Pulse]:
        self.last_pulse[origin] = pulse_type

        # print(f"\t{self.name} - {self.last_pulse}")

        if all(pulse is PulseType.HIGH for pulse in self.last_pulse.values()):
            return self.pulse_connections(PulseType.LOW)
        return self.pulse_connections(PulseType.HIGH)

    def reset(self):
        for module in self.last_pulse:
            self.last_pulse[module] = PulseType.LOW


class Broadcast(Module):
    def pulse(self, origin: Module, pulse_type: PulseType) -> list[Pulse]:
        return self.pulse_connections(pulse_type)


class Button(Module):
    def pulse(self, origin: Module, pulse_type: PulseType) -> list[Pulse]:
        return self.pulse_connections(PulseType.LOW)


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)

        self.modules: dict[str, Module] = {}

        for module, targets in p.split_each_line(" -> "):
            targets = targets.split(", ")

            if module == "broadcaster":
                module_name = "broadcaster"
                module_type = Broadcast
            else:
                module_name = module[1:]
                if module[0] == "%":
                    module_type = FlipFlop
                else:
                    module_type = Conjuction

            if module_name not in self.modules:
                self.modules[module_name] = module_type(module_name)
            else:
                self.modules[module_name].evolve(module_type)

            module = self.modules[module_name]

            for tg in targets:
                if tg not in self.modules:
                    self.modules[tg] = Module(tg)

                module.add_connection(self.modules[tg])
                self.modules[tg].add_from(module)

        high = 0
        low = 0

        rx = self.modules["rx"]

        self.rx_cons = []
        self.super_modules = set()

        for module in self.modules.values():
            module.reset()

            if (type(module) is Conjuction) and rx in module.connections:
                self.rx_cons.append(module)

        for module in self.rx_cons:
            for mod2 in module.from_connections:
                if mod2 not in self.super_modules:
                    self.super_modules.add(mod2)

        self.solutions = {}

        for press in range(1, 1001):
            pulses = deque([Pulse(None, self.modules["broadcaster"], PulseType.LOW)])
            while pulses:
                pulse = pulses.popleft()

                if pulse.type is PulseType.LOW:
                    low += 1
                else:
                    high += 1

                if (
                    pulse.pulse_type is PulseType.HIGH
                    and pulse.origin in self.super_modules
                    and pulse.target in self.rx_cons
                ):
                    self.solutions[pulse.origin] = press
                    self.super_modules.remove(pulse.origin)

                pulses.extend(pulse.resolve())

        return high * low

    def part2(self, puzzle_input: str):
        press = 1000

        while self.super_modules:
            press += 1
            pulses = deque([Pulse(None, self.modules["broadcaster"], PulseType.LOW)])
            while pulses:
                pulse = pulses.popleft()

                if (
                    pulse.pulse_type is PulseType.HIGH
                    and pulse.origin in self.super_modules
                    and pulse.target in self.rx_cons
                ):
                    self.solutions[pulse.origin] = press
                    self.super_modules.remove(pulse.origin)

                pulses.extend(pulse.resolve())

        return lcm(*self.solutions.values())
