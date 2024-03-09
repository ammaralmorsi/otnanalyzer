

class MFASOverheadGenerator:
    def __init__(self):
        self.current_frame_number = 0

    def get_next_value(self):
        next_value = self.current_frame_number
        self.current_frame_number = (self.current_frame_number + 1) % 256
        return next_value
