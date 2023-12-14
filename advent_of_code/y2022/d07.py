from tinsel import BaseSolution, Processing


class FileSystem:
    def __init__(self) -> None:
        self.file_system = {"_dirs": []}
        self.cwd = self.file_system
        self.path = []

        self.dir_sizes = {}

    def cd(self, dr: str):
        if dr not in self.cwd:
            self.cwd[dr] = {"_size": 0, "..": self.cwd, "_dirs": [], "_path": tuple([*self.path, dr])}
            self.cwd["_dirs"].append(dr)

        self.cwd = self.cwd[dr]

        if dr == "..":
            self.path.pop()
        else:
            self.path.append(dr)

    def ls(self, contents: list[str]):
        for content in contents:
            size = int(content.split()[0])

            directory = self.file_system

            for dr in self.path:
                directory = directory[dr]
                directory["_size"] += size

                self.dir_sizes[directory["_path"]] = directory["_size"]

    def sum_filesystem(self, cwd=None):
        if cwd is None:
            cwd = self.file_system["/"]

        return cwd["_size"] * (cwd["_size"] <= 100000) + sum(self.sum_filesystem(cwd[dr]) for dr in cwd["_dirs"])

    def get_directory_size_to_delete(self):
        target = -40000000 + self.file_system["/"]["_size"]
        return min(value for value in self.dir_sizes.values() if value >= target)


class Solution(BaseSolution):
    def part1(self, puzzle_input: str):
        p = Processing(puzzle_input)
        self.f = FileSystem()

        ls_out = []

        for line in p.lines():
            if line[0] == "$":
                if ls_out:
                    self.f.ls(ls_out)
                    ls_out = []

                if (dr := line.split()[-1]) != "ls":
                    self.f.cd(dr)
            elif line[0].isdigit():
                ls_out.append(line)

        return self.f.sum_filesystem()

    def part2(self, puzzle_input: str):
        return self.f.get_directory_size_to_delete()
