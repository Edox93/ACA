class NumberChecker:
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, value):
        return value < self.threshold


class FrequencyDroper:
    def __init__(self, freq):
        self.freq = freq
        self.pos = 0

    def __call__(self, value):
        res = None
        self.pos += 1

        if self.pos % self.freq == 0:
            res = False
        else:
            res = True

        return res


numbers = [4, 7, 4, 1, 3, 5, 6, 9]

freq_dropper = FrequencyDroper(3)
checker_ten = NumberChecker(10)
checker_five = NumberChecker(5)

print(list(filter(checker_ten, numbers)))
print(list(filter(checker_five, numbers)))
print(list(filter(freq_dropper, numbers)))
