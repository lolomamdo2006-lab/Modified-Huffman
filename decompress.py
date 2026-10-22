def decompress_modified(compressed_data,code_file,original_code_file):
 
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

