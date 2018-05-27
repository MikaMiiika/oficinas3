from utils import timeToTimestamp, timestampToTime
from marshmallow import Schema, fields, ValidationError, validates_schema, post_load
from passlib.apps import custom_app_context as pwd_context

class User(Schema):
    _id = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email()
    pomoID = fields.Str()
    faces = fields.List(fields.Str())

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            raise ValidationError('Unknown field', unknown)

    @post_load
    def hashPassword(self, item):
        item['password'] = pwd_context.encrypt(item['password'])
        return item

class Activity(Schema):
    _id = fields.Str()
    userID = fields.Str(required=True)
    name = fields.Str(required=True)
    timeStarted = fields.Str(required=True)
    timeEnded = fields.Str(required=True)
    timeSpent = fields.Str()

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            return ValidationError('Unknown field', unknown)

    @post_load
    def fixTimes(self, item):
        item['timeStarted'] = timeToTimestamp(item['timeStarted'])
        item['timeEnded'] = timeToTimestamp(item['timeEnded'])
        item['timeSpent'] = str(item['timeEnded'] - item['timeStarted'])
        item['timeStarted'] = str(item['timeStarted'])
        item['timeEnded'] = str(item['timeEnded'])
        return item

