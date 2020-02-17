# tutorial/tables.py
import django_tables2 as tables
from testform.models import model_testform
import itertools
from testform import views

class table_testform(tables.Table):

    id = tables.Column(visible=False)
    author = tables.Column(visible=False)
    editBy = tables.Column(visible=False)
    blockID = tables.Column(linkify=True,verbose_name='Block ID')
    # blockID = tables.Column(linkify=("view_testformUpdate", [tables.A("list__pk")]),verbose_name='Block ID')
    # blockID = tables.Column(verbose_name='Block ID')
    parkSpecialLane = tables.Column(verbose_name='Parking Lane/Special Lane')
    consistantBlock = tables.Column(verbose_name='Consistant Block')
    rodwayType = tables.Column(verbose_name='Roadway Type')
    medianType = tables.Column(verbose_name='Median Type')
    horAlignment = tables.Column(verbose_name='Horizontal Alignment')
    speedLimit = tables.Column(verbose_name='Speed Limit')
    shoulderTypeDec = tables.Column(verbose_name='Shoulder Type Dec')
    shoulderWidthDec = tables.Column(verbose_name='Shoulder Width Dec')
    gutterWidthDec = tables.Column(verbose_name='Gutter Width Dec')
    rightLWidthDec = tables.Column(verbose_name='Right Lane Width Dec')
    centerLWidthDec = tables.Column(verbose_name='Center Lane Width Dec')
    LeftLWidthDec = tables.Column(verbose_name='Left Lane Width Dec')
    shoulderTypeInc = tables.Column(verbose_name='Shoulder Type Inc')
    shoulderWidthInc = tables.Column(verbose_name='Shoulder Width Inc')
    gutterWidthInc = tables.Column(verbose_name='Gutter Width Inc')
    rightLWidthInc = tables.Column(verbose_name='Right Lane Width Inc')
    centerLWidthInc = tables.Column(verbose_name='Center Lane Width Inc')
    LeftLWidthInc = tables.Column(verbose_name='Left Lane Width Inc')
    comment = tables.Column(visible=False,verbose_name='Comments')
    state = tables.Column(verbose_name='State')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = itertools.count()

    class Meta:
        attrs = {'id': 'foo'}
        model = model_testform
        template_name = 'django_tables2/bootstrap4.html'
