from ninja import Schema


def to_camel(string: str) -> str:
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])


class BilingualSchema(Schema):
    class Config(Schema.Config):
        alias_generator = to_camel
        populate_by_name = True



class BilingualConfig(Schema.Config):
    alias_generator = to_camel
    populate_by_name = True