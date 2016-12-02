import base64
# Sample on how to encode a file to base64 string
# and decode back.
file_data = open(r'D:\CloudbaseInitSetup_x64.msi', 'rb')
file_read = file_data.read()
file_data.close()
print(file_read)
file_64_encode = base64.encodestring(file_read)
file_64_decode = base64.decodestring(file_64_encode) 
file_result = open(r'D:\decoded2.msi', 'wb') # create a writable file and write the decoding result
file_result.write(file_64_decode)
file_result.close()