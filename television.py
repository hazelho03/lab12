class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initiallize television with default values"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle television power"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute state of the television when tv off"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel"""
        if self.__status:
            self.__channel = Television.MIN_CHANNEL if self.__channel == Television.MAX_CHANNEL else self.__channel + 1

    def channel_down(self) -> None:
        """Decrease the channel"""
        if self.__status:
            self.__channel = Television.MAX_CHANNEL if self.__channel == Television.MIN_CHANNEL else self.__channel - 1

    def volume_up(self) -> None:
        """Increase volume, stop at maximum and unmuting if muted"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease volume, stop at minimum and unmuting if muted"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return a string representation of television's state"""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
