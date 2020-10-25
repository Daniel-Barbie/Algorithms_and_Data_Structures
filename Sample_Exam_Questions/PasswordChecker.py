class PasswordChecker:

    def _check_length(pw):
        if len(pw) < 6:
            return 6 - len(pw)
        elif len(pw) > 20:
            # return len(pw)-20
            return 20 - len(pw)
        else:
            return 0

    def _check_up_low_dig(pw):
        upper = 0
        lower = 0
        digit = 0
        for i in pw:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            elif i.isdigit():
                digit += 1
        return [upper, lower, digit]

    def _check_lower(pw):
        # lower = 0
        for i in pw:
            if i.islower():
                # lower += 1
                return 0
        return 1

    def _check_upper(pw):
        # upper = 0
        for i in pw:
            if i.isupper():
                # upper += 1
                return 0
        return 1

    def _check_digit(pw):
        # digit = 0
        for i in pw:
            if i.isdigit():
                # digit += 1
                return 0
        return 1

    def _check_repeating(pw):
        changes = 0
        i = 0
        repeater = ""
        repeater_count = 0
        while i < len(pw) - 2:
            if pw[i] == pw[i + 1] and pw[i] == pw[i + 2]:
                if repeater == pw[i]:
                    repeater_count += 1
                else:
                    changes += repeater_count // 3
                    repeater = pw[i]
                    repeater_count = 3
            else:
                changes += repeater_count // 3
                repeater = ""
                repeater_count = 0
            i += 1
        return changes

    def check_password(self, pw):
        changes = 0
        length_change = PasswordChecker._check_length(pw)
        lower_change = PasswordChecker._check_lower(pw)
        upper_change = PasswordChecker._check_upper(pw)
        digit_change = PasswordChecker._check_digit(pw)
        repeating_change = PasswordChecker._check_repeating(pw)

        if length_change < 0:
            changes += abs(repeating_change + length_change)
            changes += (lower_change + upper_change + digit_change)

        elif length_change > 0:
            change_list = [lower_change, upper_change, digit_change]
            i = 0
            while length_change > 0 and i <= 2:
                length_change -= change_list[i]
                i += 1
            changes += (length_change + lower_change + upper_change + digit_change + repeating_change)

        else:
            change_list = [lower_change, upper_change, digit_change]
            i = 0
            while repeating_change > 0 and i <= 2:
                repeating_change -= change_list[i]
                i += 1
            changes += (repeating_change + lower_change + upper_change + digit_change)

        return changes


pwc = PasswordChecker()
print(pwc.check_password("abcaaaax2222x22a"))
print(pwc.check_password("1234567890123456789012345600000"))