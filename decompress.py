import pickle
import ast
with open("code.txt", "r") as code:
  code_file = ast.literal_eval(code.read())

with open("original_code.txt", "r") as original_code:
  original_code_file = ast.literal_eval(original_code.read())


with open("compresses.bin", "rb") as comprssed_file:
  compressed_data = iter(pickle.load(comprssed_file))



def decomress_modified(compressed_data,code_file,original_code_file):
 
  i = 0
  data=""
  output=""
 
  for x in compressed_data:
    data+=x
    
    if data in code_file:
      symbol=code_file[data]
      if symbol == "others":
        sub_data=""
        while sub_data not in original_code_file:
          
          sub_data+=next(compressed_data)
        output+=original_code_file[sub_data]
      else:
         output+=symbol
      data=""

  return output

print(decomress_modified(compressed_data,code_file,original_code_file))
