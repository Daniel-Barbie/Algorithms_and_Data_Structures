import pandas as pd


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.data = pd.DataFrame({"sentences": sentences, "times": times})
        self.input = ""
        self.pointer = 0
        self.result_df = None

    def input_char(self, char):
        if char == "#":
            if not self.data.sentences.isin([self.input]).any():
                # self.data = self.data.append({"sentences": self.input, "times": 1})
                self.data.loc[len(self.data)] = [self.input, 1]
            else:
                self.data.loc[self.data["sentences"] == self.input, "times"] += 1
            self.data.sort_values(by=["times"], ascending=False, inplace=True)
            self.input = ""
            self.pointer = 0
            self.result_df = None
            return []

        self.input = self.input + char
        # self.data.apply(lambda x: result_list.append(x) if x.sentences.value[self.pointer] == char else None)
        if self.result_df is None:
            self.result_df = self.data.loc[self.data["sentences"].str[self.pointer] == char].copy()
        else:
            self.result_df = self.result_df.loc[self.result_df["sentences"].str[self.pointer] == char].copy()

        # how to access self
        # self.result_df = self.data.query("sentences[self.pointer] == char")
        # list comprehension is quick, but not suitable here?
        # self.result_df = [x for x in self.data["A"]]

        self.result_df.sort_values(by=["times"], ascending=False, inplace=True)
        i = 0
        while i< len(self.result_df) and i < 3:
            count = self.result_df.iloc[i, 1]
            list_ = [self.result_df.iloc[i, 0]]
            start = i
            i += 1
            while i < len(self.result_df) and count == self.result_df.iloc[i, 1]:
                list_.append(self.result_df.iloc[i, 0])
                i += 1
            if len(list_) > 1:
                list_ = sorted(list_)
                for x in range(len(list_) - 1):
                    self.result_df.iloc[start + x, 0] = list_[x]
        self.pointer += 1
        return self.result_df.iloc[0:3, :]


acs = AutocompleteSystem(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
print(acs.input_char("i"))
print(acs.input_char(" "))
print(acs.input_char("a"))
print(acs.input_char("#"))
print(acs.input_char("a"))
print(acs.input_char("#"))
print(acs.input_char("a"))
print(acs.input_char("#"))
print(acs.data)
