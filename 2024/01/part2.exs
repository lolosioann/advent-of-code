{left, right} = AOC.parse_input("input.txt")

counts = Enum.frequencies(right)

left
|> Enum.uniq()
|> Enum.reduce(0, fn n, acc -> acc + n * Map.get(counts, n, 0) end)
|> IO.inspect()
