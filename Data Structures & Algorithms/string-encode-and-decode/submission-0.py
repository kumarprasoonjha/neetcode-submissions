class Solution:

  def encode(self, strs: list[str]) -> str:
    """Encodes a list of strings to a single string."""
    res = ""
    for s in strs:
      # Append length, delimiter, and string content
      res += str(len(s)) + "#" + s
    return res

  def decode(self, s: str) -> list[str]:
    """Decodes a single string back to the original list of strings."""
    res = []
    i = 0

    while i < len(s):
      # Step 1: Find the position of '#' to read the length prefix
      j = i
      while s[j] != "#":
        j += 1

      # Step 2: Convert the prefix into an integer
      length = int(s[i:j])

      # Step 3: Jump past the '#' delimiter
      i = j + 1

      # Step 4: Extract exactly 'length' characters
      res.append(s[i : i + length])

      # Step 5: Move index past the extracted string to start the next one
      i += length

    return res