

class PRBSPayloadGenerator:
    def __init__(self, seed:int):
        self.poly:list[int] = [int(i) for i in f'{seed & 0x7FFFFFFF:0>31b}']

    def get_next_payload(self) -> list[int]:
        return [self._get_next_prbs_byte() for _ in range(4 * 3808)]

    def _get_next_prbs_byte(self) -> int:
        byte:list[str] = []
        for _ in range(8):
            feedback:int = self.poly[30]^self.poly[27]
            self.poly.insert(0, feedback)
            byte.append(str(1 - self.poly.pop(-1)))
        return int(''.join(byte), 2)
