# Random Land Points

This is a little pack to help get random points on land. This can be done either for all
land masses or by country.

## Installation

```bash
pip install random-land-points
```

## Usage

This package can be used to get random points on land in a provided polygon or in a specific country.

To sample from a specific country, you can use the `random_points` function. This function takes a country name as an argument and returns a random point on land in that country.

```python
import random_land_points as rlp

# Get a random point on land
point = rlp.random_points('United States of America')

# Get 10 random points on land
points = rlp.random_points('United States of America', 10)
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

If you need to get the list of all supported courntries, you can use the `get_countries` function.

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

## Examples

There are examples found in the `examples` directory. These examples show how to use the package to get random points on land
and visualize the results.

To run the examples install the package with `[examples]` option:

```bash
pip install random-land-points[examples]
```

Then run the examples with the following command:

```bash
python ./examples/plot_random_sampling.py
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