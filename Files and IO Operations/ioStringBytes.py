import io

s = io.StringIO()
s.write("Hello\n")
print("This is a test line", file=s)
print(s.getvalue())
print(s.read(10))

s = io.BytesIO()
s.write(b"binary data")
print(s.getvalue())