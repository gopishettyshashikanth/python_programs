# fo = open("test.txt", "w")
# print "Name of the file: ", fo.name
# fo.close()


myText = 'hello python'
with open('test.txt', 'w') as myFile:
    myFile.write(myText)


# x=[provider_data,login_trans_data,service_count_data]
# with open('test.txt', 'w') as file:

#     #for i in x:
#      #   print i
#     file.write(json.dumps(x)) 