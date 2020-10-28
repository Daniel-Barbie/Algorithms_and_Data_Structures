import pandas as pd


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.data = pd.DataFrame({"sentences": sentences, "times": times})
        self.input = ""
        self.pointer = 0
        self.result_df = None

    def _sort_df_ascii(pre_sorted_df, string_col_index, count_col_index):
        sorted_df = pre_sorted_df.copy()
        i = 0
        while i < len(sorted_df) and i < 3:
            count = sorted_df.iloc[i, count_col_index]
            list_ = [sorted_df.iloc[i, string_col_index]]
            start = i
            i += 1
            while i < len(sorted_df) and count == sorted_df.iloc[i, count_col_index]:
                list_.append(sorted_df.iloc[i, string_col_index])
                i += 1
            if len(list_) > 1:
                list_ = sorted(list_)
                for x in range(len(list_) - count_col_index):
                    sorted_df.iloc[start + x, string_col_index] = list_[x]
        return sorted_df

    def input_char(self, char):
        # if input ends, update DF
        if char == "#":
            # if input does not yet exist: add sentence and count=1
            if not self.data.sentences.isin([self.input]).any():
                # self.data = self.data.append({"sentences": self.input, "times": 1})
                self.data.loc[len(self.data)] = [self.input, 1]
            # if input does exist, raise count by 1
            else:
                self.data.loc[self.data["sentences"] == self.input, "times"] += 1
            # pre-sort DF by counts, so that the next time it is accessed, the result list is already sorted by count
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

        # not necessary as self.data is always sorted after inserting a new input (see if->#)
        #self.result_df.sort_values(by=["times"], ascending=False, inplace=True)

        # sort entries with the same count by ascii value of their string chars
        self.result_df = AutocompleteSystem._sort_df_ascii(self.result_df, 0, 1)

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
