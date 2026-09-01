import struct

with open('record.bin', 'rb') as file:
    record_size = struct.calcsize('i20sif')
    while True:
        data = file.read(record_size)
        if not data:
            break
        record = struct.unpack('i20sif', data)
        record_id = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
        print(f"Record ID: {record_id[0]}, Name: {record_id[1]}, Age: {record_id[2]}, GPA: {record_id[3]}")