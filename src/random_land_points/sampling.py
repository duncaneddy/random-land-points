"""
Functions related to sampling random points from polygons and
"""

import random
import numpy as np
from functools import lru_cache
from shapely.geometry import Point, Polygon
from shapely import centroid

from random_land_points.countries import get_country_polygons

def random_point_in_polygon(polygon: Polygon) -> np.ndarray:
    """
    Returns a random point within a polygon

    Args:
        polygon: np.ndarray
            The polygon to sample from

    Returns:
        np.ndarray
            The random point
    """
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        point = np.array([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if polygon.contains(Point(point)):
            return point

def random_points(country: str, count: int = 1, resolution:str = 'medium') -> np.ndarray:
    """
    Returns a random point within a country

    Args:
        country: str
            The name of the country
        count: int
            The number of points to return
        resolution: str
            The resolution of the data to use. Can be 'low', 'medium', or 'high'

    Returns:
        np.ndarray
            The random point
    """

    if count < 1:
        raise ValueError("Count must be greater than 0")

    polygons = get_country_polygons(country, resolution)

    # Compute area weight of each polygon
    total_area = sum([polygon.area for polygon in polygons])
    weights = [polygon.area / total_area for polygon in polygons]

    points = []
    for _ in range(count):
        polygon = random.choices(polygons, weights=weights)[0]
        points.append(random_point_in_polygon(polygon))

    return np.array(points)

@lru_cache(maxsize = 50)
def get_total_country_area(country: str, resolution: str = 'medium') -> float:
    """
    Returns the total area of a country

    Args:
        country: str
            The name of the country

    Returns:
        float
            The total area
    """

    polygons = get_country_polygons(country, resolution)
    total_area = 0
    for polygon in polygons:
        total_area += polygon.area

    return total_area

def get_num_polygons(country: str, resolution: str = 'medium') -> int:
    """
    Returns the number of polygons for a country

    Args:
        country: str
            The name of the country

    Returns:
        int
            The number of polygons
    """

    polygons = get_country_polygons(country, resolution)
    return len(polygons)

@lru_cache(maxsize = 50)
def get_center_points(country: str, resolution: str = 'medium') -> np.ndarray:
    """
    Returns the center point of a polygon

    Args:
        country: str
            The name of the country

    Returns:
        np.ndarray
            The center point
    """

    polygons = get_country_polygons(country, resolution)

    center_points = []

    for polygon in polygons:
        center_points.append(centroid(polygon).coords[0])

    return np.array(center_points)