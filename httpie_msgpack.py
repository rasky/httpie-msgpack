from httpie.plugins import ConverterPlugin
import json
import msgpack

DEFAULT_INDENT = 4

class MsgpackPlugin(ConverterPlugin):

    @classmethod
    def supports(cls, mime):
      return 'x-msgpack' in mime

    def convert(self, body):
        return "application/json", \
            json.dumps(msgpack.loads(body), encoding="unicode-escape", sort_keys=True)
