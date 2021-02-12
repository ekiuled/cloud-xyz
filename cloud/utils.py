from cloud.xyz import XYZ, Cloud


def count(cloud: Cloud) -> int:
    return len(cloud)


def hist(cloud: Cloud) -> list[int]:
    pass


def erase(cloud: Cloud, low: float, high: float) -> Cloud:
    return list(filter(lambda point: low <= point.z <= hi, cloud))
