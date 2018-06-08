from utils import timeToTimestamp, timestampToTime
from marshmallow import Schema, fields, ValidationError, validates_schema, post_load
from passlib.apps import custom_app_context as pwd_context

class User(Schema):
    _id = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email()
    pomoID = fields.Str()
    useSpeech = fields.Bool(default=True, missing=True)
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

    @post_load
    def fillFaces(self, item):
        if 'faces' not in item:
            item['faces'] = []
        while len(item['faces']) != 7:
            item['faces'].append("")
        return item

class Activity(Schema):
    _id = fields.Str()
    userID = fields.Str(required=True)
    name = fields.Str(required=True)
    timeStarted = fields.Str()
    timeEnded = fields.Str()

    timeStartedInt = fields.Int()
    timeEndedInt = fields.Int()

    timeSpent = fields.Int()

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            return ValidationError('Unknown field', unknown)

    @post_load
    def fixTimes(self, item):
        #item['timeStartedInt'] = timeToTimestamp(item['timeStarted'])
        #item['timeEndedInt'] = timeToTimestamp(item['timeEnded'])
        item['timeSpent'] = item['timeEndedInt'] - item['timeStartedInt']
        return item

class ActivityList(Schema):
    activities = fields.List(fields.Str())

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        unknown = set(original_data) - set(self.fields)
        if unknown:
            return ValidationError('Unknown field', unknown)