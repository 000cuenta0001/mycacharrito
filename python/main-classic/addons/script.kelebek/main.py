import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))