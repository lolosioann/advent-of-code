defmodule AOC do
  def parse_input(file_path) do
    file_path
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(fn line ->
      [a, b] = String.split(line)
      {String.to_integer(a), String.to_integer(b)}
    end)
    |> Enum.unzip()
  end

  def distance(a, b) when length(a) == length(b) do
    Enum.zip(a, b)
    |> Enum.reduce(0, fn {x, y}, acc -> acc + abs(x - y) end)
  end
end
