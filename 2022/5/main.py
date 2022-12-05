from collections import defaultdict, deque
import re
from pathlib import Path

# regex
BASE = re.compile(r"(?<= )(\d+)(?= )")
CRATE = re.compile(r"(?<=\[)(\S+)(?=\])")
MOVE = re.compile(
    r"(?:move )(?P<how_many>\d+)(?: from )(?P<from>\d+)(?: to )(?P<to>\d+)"
)
# regex


def parse(data: str) -> tuple[dict[deque[str]], list[dict[str, int]]]:
    stacks, moves = data.split("\n\n")

    *stacked, base = stacks.split("\n")
    columns = defaultdict(deque)
    column_pos = dict()
    for column in re.finditer(BASE, base):
        column_pos[column.start()] = column.group()
    for line in stacked:
        for c in CRATE.finditer(line):
            columns[column_pos[c.start()]].append(c.group())

    move_list = []
    for move in moves.split("\n"):
        if m := MOVE.match(move):
            move_list.append((m := m.groupdict()))
    return columns, move_list


def part1(
    columns: dict[deque[str]], move_list: list[dict[str, int]]
) -> dict[deque[str]]:
    for move in move_list:
        c = columns[move["from"]]
        for _ in range(int(move["how_many"])):
            e = c.popleft()
            columns[move["to"]].appendleft(e)
    return "".join(r[0] for k, r in sorted(columns.items()))


def part2(
    columns: dict[deque[str]], move_list: list[dict[str, int]]
) -> dict[deque[str]]:
    for move in move_list:
        c = columns[move["from"]]
        stack = deque()
        for _ in range(int(move["how_many"])):
            e = c.popleft()
            stack.appendleft(e)
        for e in stack:
            columns[move["to"]].appendleft(e)
    return "".join(r[0] for k, r in sorted(columns.items()))


def play(data: str, method: callable) -> str:
    columns, move_list = parse(data)
    return method(columns, move_list)


data = Path("input.txt").read_text()
print("Part 1:", play(data, part1))
print("Part 2:", play(data, part2))
