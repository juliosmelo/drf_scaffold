from django.db import models

STRING = "string"
INTEGER = "integer"
DECIMAL = "decimal"
POSITIVE = "positive"
AUTO = "auto"
BIGAUTO = "bigauto"
BIGINT = "bigint"
BINARY = "binary"
BOOLEAN = "boolean"
DATE = "date"
DATETIME = "datetime"
DURATION = "duration"
EMAIL = "email"
FILE = "file"
FILEPATH = "filepath"
FLOAT = "float"
IMAGE = "image"
GENERICIP = "genericip"
NULLBOOLEAN = "nullboolean"
POSITIVEINT = "positiveint"
POSITIVESMALINT = "positivesmalint"
SLUG = "slug"
SMALLINT = "smallint"
TEXT = "text"
TIME = "time"
URL = "url"
UUID = "uuid"
FK = "fk"

DELETE_CONSTRAINTS = [
    models.CASCADE.__name__,
    models.PROTECT.__name__,
    models.SET_NULL.__name__,
    models.SET_DEFAULT.__name__,
    models.SET.__name__,
    models.DO_NOTHING.__name__,
]

MODEL_FIELDS = {
    STRING: "CharField(max_length=200)",
    INTEGER: "IntegerField()",
    DECIMAL: "DecimalField()",
    POSITIVE: "PositiveIntegerField()",
    AUTO: "AutoField()",
    BIGAUTO: "BigAutoField()",
    BIGINT: "BigIntegerField()",
    BINARY: "BinaryField()",
    BOOLEAN: "BooleanField()",
    DATE: "DateField()",
    DATETIME: "DateTimeField()",
    DURATION: "DurationField()",
    EMAIL: "EmailField()",
    FILE: "FileField()",
    FILEPATH: "FilePathField()",
    FLOAT: "FloatField()",
    IMAGE: "ImageField()",
    GENERICIP: "GenericIPAddressField()",
    NULLBOOLEAN: "NullBooleanField()",
    POSITIVEINT: "PositiveIntegerField()",
    POSITIVESMALINT: "PositiveSmallIntegerField()",
    SLUG: "SlugField()",
    SMALLINT: "SmallIntegerField()",
    TEXT: "TextField()",
    TIME: "TimeField()",
    URL: "URLField()",
    UUID: "UUIDField()",
    FK: "ForeignKey('{}', on_delete=models.{})",
}