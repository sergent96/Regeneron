import os

output=open(f"miseq.txt", "w")
for file_name in os.listdir("miseq_rmdup_depth"):
    text_list=open(f"miseq_rmdup_depth/{file_name}").read().split()
    grouped_text_list=list(zip(*(iter(text_list),)*3))[1:]
    for ele1, ele2, ele3 in grouped_text_list: 
        if int(ele3)  <=10:  
            output.write(f"{file_name} {ele2} {ele3}\n")