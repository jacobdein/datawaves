import os
from django.contrib.gis.utils import LayerMapping
from .models import LandCover

landcover_mapping = {
    'cover_type' : 'type',
    'shape' : 'MULTIPOLYGON',
}

landcover_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'landcover.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        LandCover, landcover_shp, landcover_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)