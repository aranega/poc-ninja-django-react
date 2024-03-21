from ninja import Schema


def to_camel(string: str) -> str:
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])


# This class is here to configure an auto snake2camel case translator
class BilingualSchema(Schema):
    class Config(Schema.Config):
        alias_generator = to_camel
        populate_by_name = True
