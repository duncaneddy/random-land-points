from random_land_points import get_countries, get_country_polygons

def test_countries():
    c = get_countries()

    assert 'United States of America' in c
    assert 'Antarctica' in c

def test_countries_low():
    c = get_countries('low')

    assert len(c) == 258

def test_countries_medium():
    c = get_countries('medium')

    assert len(c) == 242

def test_countries_high():
    c = get_countries('high')

    assert len(c) == 177

def test_get_country_polygon():

    for country in get_countries():
        polygon = get_country_polygons(country)
        assert len(polygon) > 0

def test_get_country_polygon_low():

    resolution = 'low'
    for country in get_countries(resolution):
        polygon = get_country_polygons(country, resolution)
        assert len(polygon) > 0

def test_get_country_polygon_medium():

    resolution = 'medium'
    for country in get_countries(resolution):
        polygon = get_country_polygons(country, resolution)
        assert len(polygon) > 0

def test_get_country_polygon_high():

    resolution = 'high'
    for country in get_countries(resolution):
        polygon = get_country_polygons(country, resolution)
        assert len(polygon) > 0
