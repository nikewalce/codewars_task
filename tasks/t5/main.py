class Converter():
    @staticmethod
    def to_ascii(h):
        return bytes.fromhex(h).decode('utf-8')

    @staticmethod
    def to_hex(s):
        return ''.join([i.encode('utf-8').hex() for i in s])

print(Converter.to_hex("Look mom, no hands"))
#=> "4c6f6f6b206d6f6d2c206e6f2068616e6473"

print(Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473"))
#=> "Look mom, no hands"