import sys, heapq

big_number = sys.maxsize # 9223372036854775807 # returns the maximum 64 bit value
print(type(big_number))




input_list = [7, 1, 2, 3, 4, 5]
generated_q = heapq.heapify(input_list)
print(generated_q)

print(heapq.heappop(input_list))