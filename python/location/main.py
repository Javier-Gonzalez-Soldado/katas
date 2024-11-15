from typing import List


def main():
    file_content = read_file("puzzle_input.txt")
    print(process_movs(file_content))


def process_movs(movs: str) -> int:
    coordinates = [[0, 0]]
    init_coordinate = [0, 0]
    for move in movs:
        new_coordinate = get_new_coordinate(init_coordinate, move)
        if new_coordinate not in coordinates:
            coordinates.append(new_coordinate.copy())
    return len(coordinates)


def get_new_coordinate(current_coordinate: List[int], move: str) -> List[int]:
    if move == ">":
        current_coordinate[0] += 1
    elif move == "<":
        current_coordinate[0] -= 1
    elif move == "^":
        current_coordinate[1] += 1
    elif move == "v":
        current_coordinate[1] -= 1

    return current_coordinate


def read_file(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()
