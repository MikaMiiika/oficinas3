from marshmallow import Schema, fields, ValidationError, validates_schema

class User(Schema):
    _id = fields.Str()
    password = fields.Str()
    email = fields.Email()
    pomoID = fields.Str()
    faces = fields.List(fields.Str())

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            raise ValidationError('Unknown field', unknown)

