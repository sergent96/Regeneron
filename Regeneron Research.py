import os

output=open(f"miseq.txt", "w") #creates text file to store data
for file_name in os.listdir("miseq_rmdup_depth"):
    text_list=open(f"miseq_rmdup_depth/{file_name}").read().split() #saves file as list of elements
    grouped_text_list=list(zip(*(iter(text_list),)*3))[1:] #group elements by 3
    for ele1, ele2, ele3 in grouped_text_list: 
        if int(ele3)  <=10:  #if less than 10, low region of read depth
            output.write(f"{file_name} {ele2} {ele3}\n")  
            
#txt file: file name, coordinate, read depth
