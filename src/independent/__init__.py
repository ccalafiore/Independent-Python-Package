
import datetime
from . import sequence as seq


__all__ = ["seq"]

__version__ = "0.0.0.1"

# TODO: Get the release timestamp automatically from PyPI???
__release_day__ = 24
__release_month_num__ = 9
__release_year__ = 2026

__release_date_object__ = datetime.date(__release_year__, __release_month_num__, __release_day__)
__release_date__ = __release_date_object__.__format__('%d %B %Y')
__release_month_name__ = __release_date_object__.__format__('%B')

__author__ = 'Calafiore Carmelo'
__author_email__ = 'dr.carmelo.calafiore@gmail.com'
__maintainer_email__ = 'dr.carmelo.calafiore@gmail.com'
