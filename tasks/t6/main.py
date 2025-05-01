class SmartTrafficLight:
    def __init__(self, st1: list, st2: list):
        self.list_streets = [st1, st2]

    def turngreen(self) -> str | None:
        return None if (len(self.list_streets) == 0) else self.list_streets.pop(self.list_streets.index(max(self.list_streets)))[1] if len(self.list_streets) == 1 else None if (self.list_streets[0][0] == self.list_streets[1][0]) else self.list_streets.pop(self.list_streets.index(max(self.list_streets)))[1]


a = SmartTrafficLight([45, '27th ave'], [73, '3rd st'])
print(a.turngreen())
print(a.turngreen())