import datetime

# oFile = open("/Users/matthoadley/DemoFile.txt", 'w')
# oFile.write(f"Scan started at {str(datetime.datetime.now())}")
# # oFile.close()

start_time = datetime.datetime.now()

# i = 0
# while i < 10:
#     i+= 1
num_test = [1,2,3]
for num in num_test:
    let_test = ["A", "B", "C"]
    for let in let_test:
        print(num, let)

end_time = datetime.datetime.now()

total_time = end_time - start_time

print(total_time)
