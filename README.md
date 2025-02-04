# Random Land Points

[![Unit](https://github.com/duncaneddy/random-land-points/actions/workflows/ci.yml/badge.svg)](https://github.com/duncaneddy/random-land-points/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/duncaneddy/random-land-points/badge.svg?branch=main)](https://coveralls.io/github/duncaneddy/random-land-points?branch=main)

This is a little package that allows you to randomly sample points on land. This can be done either for all
land masses, by continent, or by country.

![Random Points](./images/random_points.png)

## Installation

```bash
pip install random-land-points
```

## Usage

This package can be used to get random points on land in a provided polygon or in a specific country.

To sample you can use the `random_points` function. This function returns a random point on land in the provided polygon.
All points are returned as a list of numpy arrays with the first element being the longitude and the second element being the latitude.
That is `[lon, lat]`.

```python

import random_land_points as rlp

# Get a random point on land
point = rlp.random_points() # Point is [lon, lat]

# Get 10 random points on land
points = rlp.random_points(count=10)
```

You can also sample points by continent or by country. To do this, you can pass the continent or country name as an argument to the `random_points` function.

```python

import random_land_points as rlp

# Get a random point on land in Europe
point = rlp.random_points('Europe')

# Get a random point on land in Italy
point = rlp.random_points('Italy')
```

The package utilizes the [Natural Earth](https://www.naturalearthdata.com/downloads/) dataset to get the land polygons for each country.
The data set comes in 3 resolutions: 10m `high`, 50m `medium`, and 110m `low`. The default resolution is `medium`, but 
you can specify the resolution by passing the `resolution` argument to the `random_points` and `get_countries` functions.
The number of polygons and the available countries vary by resolution.

An example of this is shown below:

```python

import random_land_points as rlp

# Get all high resolution countries
countries = rlp.get_countries(resolution='high')

# Get a random point on land in a high resolution country
point = rlp.random_points('Italy', resolution='high')
```

If you need to get the list of all supported countries, you can use the `get_countries` function.

```python

import random_land_points as rlp

countries = rlp.get_countries()
```

To sample from a specific polygon, you can use the `random_point_in_polygon` function. This function takes a Shapely 
polygon as an argument and returns a random point on land in that polygon.

```python

import random_land_points as rlp
from shapely.geometry import Polygon

# Create a polygon
polygon = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])

# Get a random point on land in the polygon
point = rlp.random_point_in_polygon(polygon)
```

You can check whether a given `(x,y)` coordinate is contained within a generating polygon by using the `is_in` function.
This function returns a boolean value indicating whether the point is contained within the generating polygon.

```python

import random_land_points as rlp

# Check if a point is in the generating polygon
rlp.is_in(0.0, 0.0) # False

# Check by country
rlp.is_in_country(0.0, 0.0, 'Italy') # False

# Check by continent
rlp.is_in_continent(0.0, 0.0, 'Europe') # False
```

## Examples

There are examples found in the `examples` directory. These examples show how to use the package to get random points on land
and visualize the results.

To run the examples install the package with `[examples]` option:

```bash
pip install random-land-points[examples]
```

Then run the examples with the following command:

```bash
python ./examples/random_points.py
python ./examples/random_by_continent.py
python ./examples/random_by_country.py
```

## Development

To install the package for development, you can use the following command:

```bash
pip install -e ".[dev]"
```

To run the tests, you can use the following command:

```bash
pytest
```

## License

This package is licensed under the MIT license. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Made with Natural Earth. Free vector and raster map data @ [naturalearthdata.com](https://www.naturalearthdata.com).