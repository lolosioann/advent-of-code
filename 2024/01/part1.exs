{left, right} = AOC.parse_input("input.txt")
left = Enum.sort(left)
right = Enum.sort(right)

IO.inspect(AOC.distance(left, right))
