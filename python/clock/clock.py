class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

        while self.hour < 0:
            self.hour += 24

        while self.hour >= 24:
            self.hour -= 24

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
            if self.hour < 0:
                self.hour += 24

        while self.minute > 59:
            self.minute = self.minute - 60
            self.hour += 1
            if self.hour >= 24:
                self.hour -= 24

    def __repr__(self):
        return f'Clock({self.hour}, {self.minute})'

    def __str__(self):
        """Return string representation of clock

        Returns:
            String : string representation of clock
        """
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        """Check if two clocks are equal

        Args:
            other (Clock): other clock to compare with

        Returns:
            bool: True if clocks are equal, False otherwise
        """
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        """Add minutes to clock, more than 60 minutes wraps around

        Args:
            minutes (int): minutes to be add to current time

        Returns:
            self: new clock
        """
        # return Clock(self.hour + minutes // 60, self.minute + minutes % 60)
        days = minutes // 1440  # 1440 minutos = 1 dia
        self.hour = self.hour + days * 24 + minutes % 1440 // 60
        self.minute = self.minute + minutes % 1440 % 60

        while self.hour < 0:
            self.hour += 24

        while self.hour >= 24:
            self.hour -= 24

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
            if self.hour < 0:
                self.hour += 24

        while self.minute > 59:
            self.minute = self.minute - 60
            self.hour += 1
            if self.hour >= 24:
                self.hour -= 24

        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        """subtract minutes from clock, if minutes is negative, wrap around

        Args:
            minutes (int): minutes to be subtracted from current time

        Returns:
            self: new clock with subtracted minutes
        """
        # return Clock(self.hour - minutes // 60, self.minute - minutes % 60)
        self.hour = self.hour - minutes // 60 + (minutes % 60 < 0)
        self.minute = self.minute - minutes % 60

        while self.hour < 0:
            self.hour += 24

        while self.hour >= 24:
            self.hour -= 24

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
            if self.hour < 0:
                self.hour += 24

        while self.minute > 59:
            self.minute = self.minute - 60
            self.hour += 1
            if self.hour >= 24:
                self.hour -= 24

        return Clock(self.hour, self.minute)


if __name__ == '__main__':
    clock = Clock(1, -160)
    print(clock)
