try:
    print("the 'source1.txt' is opened for writing....")
    source = open("source1.txt", "w")
    source.write("these are written into the file....")
    source.close()
except:
    print("the file is not found, retry after creating the source1.txt file in the parent directory....")


try:
    print("the souece1.txt file is opened for reading... and target1.txt is opened for writing....")
    source = open("source1.txt", "r")
    target = open("target1.txt","w")
    for i in source:
        target.write(i.upper())
    source.close()
    target.close()
    print("the target file after copying.....")
    target = open("target1.txt", "r")
    for i in target:
        print(i)
    target.close()
        
except:
    print("file not found!!")