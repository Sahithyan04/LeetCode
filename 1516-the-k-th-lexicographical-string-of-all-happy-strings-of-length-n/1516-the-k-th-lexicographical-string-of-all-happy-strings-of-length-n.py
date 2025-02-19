class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.current_string = ""
        self.result = ""
        self.index_in_sorted_list = 0

        self.generate_happy_strings(n, k)
        return self.result

    def generate_happy_strings(self, n, k):
        if len(self.current_string) == n:
            self.index_in_sorted_list += 1
            if self.index_in_sorted_list == k:
                self.result = self.current_string
            return

        # Try adding each character ('a', 'b', 'c') to the current string
        for current_char in ["a", "b", "c"]:
            # Skip if the current character is the same as the last one
            if (
                len(self.current_string) > 0
                and self.current_string[-1] == current_char
            ):
                continue

            self.current_string += current_char

            # Recursively generate the next character
            self.generate_happy_strings(n, k)

            # If the result is found, stop further processing
            if self.result != "":
                return

            # Backtrack by removing the last character
            self.current_string = self.current_string[:-1]