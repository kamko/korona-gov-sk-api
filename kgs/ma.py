from flask_marshmallow import Marshmallow

from kgs.db import Observation

ma = Marshmallow()


class ObservationSchema(ma.ModelSchema):
    class Meta:
        model = Observation
