from cloud.xyz import XYZ, Cloud
import matplotlib.pyplot as plt


def count(cloud: Cloud) -> int:
    return len(cloud)


def hist(cloud: Cloud, bins: int) -> None:
    plt.hist(list(map(lambda point: point.z, cloud)), bins)
    plt.xlabel('Altitude (Z)')
    plt.ylabel('Points')
    plt.show()


def erase(cloud: Cloud, low: float, high: float) -> Cloud:
    return list(filter(lambda point: not low <= point.z <= high, cloud))
