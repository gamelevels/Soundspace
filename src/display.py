def ConvertSeconds(Seconds: int) -> tuple[int, int]:
    Minutes = int(Seconds/60)
    Hours = int(Seconds/3600)
    Seconds = int(Seconds % 60)

    return Hours, Minutes, Seconds