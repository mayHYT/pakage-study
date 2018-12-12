#打包二进制数据 struct模块
import struct

F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, 'spam', 8)
F.write(data)
F.close()

F = open('data.bin', 'rb')
data = F.read()
value=struct.unpack('>i4sh', data)
print(value)

