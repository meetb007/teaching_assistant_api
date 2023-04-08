from marshmallow import fields, Schema, validate

SPEAKER_CHOICES = ('English speaker', 'non-English speaker')
SEMESTER_CHOICES = ('Summer', 'Regular')
SCORE_CHOICES = ('Low', 'Medium', 'High')


class TACreateSchema(Schema):
    native_english_speaker = fields.Str(
        validate=validate.OneOf(SPEAKER_CHOICES), required=True)
    course_instructor = fields.Int(
        validate=validate.Range(min=1, max=25), required=True)
    course = fields.Int(
        validate=validate.Range(min=1, max=26), required=True)
    semester = fields.Str(
        validate=validate.OneOf(SEMESTER_CHOICES), required=True)
    class_size = fields.Int(required=True)
    performance_score = fields.Str(
        validate=validate.OneOf(SCORE_CHOICES), required=True)

    class Meta:
        fields = ('id', 'native_english_speaker', 'course_instructor',
                  'course', 'semester', 'class_size', 'performance_score')


class TAUpdateSchema(Schema):
    native_english_speaker = fields.Str(
        validate=validate.OneOf(SPEAKER_CHOICES), required=False)
    course_instructor = fields.Int(
        validate=validate.Range(min=1, max=25), required=False)
    course = fields.Int(
        validate=validate.Range(min=1, max=26), required=False)
    semester = fields.Str(
        validate=validate.OneOf(SEMESTER_CHOICES), required=False)
    class_size = fields.Int(required=False)
    performance_score = fields.Str(
        validate=validate.OneOf(SCORE_CHOICES), required=False)

