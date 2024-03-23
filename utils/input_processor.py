from config.frame import OtnFrameConfig


class InputProcessor:
    def __init__(self, filepath: str):
        self.file_path: str = filepath
        self.frames: list[str] = self.read_frames()
        self.formatted_frames: list[list[list[str]]] = self.format_frames()

    def read_frames(self) -> list[str]:
        frames_list = []
        with open(self.file_path, 'r') as file:
            for frame in file:
                frames_list.append(frame.strip())
        return frames_list

    def format_frames(self) -> list[list[list[str]]]:
        return [self.format_frame(row_frame) for row_frame in self.frames]

    def format_frame(self, row_frame: str) -> list[list[str]]:
        decimal_values: list[str] = row_frame.split()
        hex_values: list[str] = self.hexlify(decimal_values)
        return self.to_2d(hex_values)

    def hexlify(self, decimal_values: list[str]) -> list[str]:
        return [hex(int(value))[2:].zfill(2) for value in decimal_values]

    def to_2d(self , hex_values: list[str]):
        ncols: int = OtnFrameConfig.DEFAULT_OTU_FRAME.value.dimension.ncols
        return [hex_values[i:i + ncols] for i in range(0, len(hex_values), ncols)]
