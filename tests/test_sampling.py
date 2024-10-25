from pytest import approx
from shapely.geometry.point import Point

import random_land_points as rlp

from random_land_points import get_country_polygons
from random_land_points import random_point_in_polygon


def test_get_total_country_area():

    area = rlp.get_total_country_area('France')
    assert area == approx(71.5, rel=1e-2)

def test_get_num_polygons():

    num = rlp.get_num_polygons('Austria')
    assert num == 1

def test_get_center_points():

    center = rlp.get_center_points('Austria')

    assert len(center) == 1
    assert center[0][0] == approx(14.13, rel=1e-2)
    assert center[0][1] == approx(47.58, rel=1e-2)

def test_random_point_in_polygon():

    polygon = get_country_polygons('Austria')[0]

    point = random_point_in_polygon(polygon)

    # Confirm it is within the bounds of the polygon

    # Compute max x and y values
    max_x = max(polygon.exterior.xy[0])
    max_y = max(polygon.exterior.xy[1])

    # Compute min x and y values
    min_x = min(polygon.exterior.xy[0])
    min_y = min(polygon.exterior.xy[1])

    assert point[0] >= min_x
    assert point[0] <= max_x
    assert point[1] >= min_y
    assert point[1] <= max_y

    # Create a point type and confirm it is within the polygon
    point = Point(point)
    assert polygon.contains(point)

def test_random_points():

    points = rlp.random_points('Austria', count=10)

    assert len(points) == 10
    for point in points:
        point = Point(point)
        assert get_country_polygons('Austria')[0].contains(point)