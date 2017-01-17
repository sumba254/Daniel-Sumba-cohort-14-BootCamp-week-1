def data_type(data=None):
  if data is None:
    print ('no value')
  elif type(data) == bool:
    print (data)
  elif type(data) == int:
    if data < 100:
      print ('less than 100')
    elif data is 100:
      print ('equal to 100')
    elif data > 100:
      print ('more than 100')
  elif type(data) == list:
    if len(data) >= 3:
      print (data[2])
    else:
      print (None)
  elif data.isalpha() is True:
    print(len(data)