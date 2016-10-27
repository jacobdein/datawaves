import os
from django.contrib.gis.utils import LayerMapping
from .models import Site

site_mapping = {
    'id' : 'ID',
    'name': 'NAME',
    'lat': 'ID',
    'lon': 'ID',
    'elevation': 'ID',
    'shape' : 'POINT',
}

site_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'sample_points_field.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Site, site_shp, site_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)