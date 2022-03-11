def arithmetic_arranger(problems, results = None):
  
  rowonenum = []
  rowtwonum = []
  rowthree = []
  rowfourans = []
  
  #Test for print results parameter
  printresults = False
  if results == True:
    printresults = True

  #Test length of list
  if len(problems) > 5:
    print("Error: Too many problems.")
    quit()

  validoperator = False
  nonumbers = False
  digittoolong = False

  #Check for errors
  for listoperator in problems:
    oplist = listoperator.rsplit(' ')
    
    if oplist[1] == '+' or oplist[1] == '-':
      validoperator = True
    else:
      validoperator = False
      break
    
    if oplist[0].isdigit() != True or oplist[2].isdigit() != True:
      nonumbers = True
      break

    if len(oplist[0]) > 4 or len(oplist[2]) > 4:
      digittoolong = True
      break
  #Print errors if any
  if validoperator == False:
    print("Error: Operator must be '+' or '-'.")
    quit()

  if nonumbers == True:
    print("Error: Numbers must only contain digits.")
    quit()

  if digittoolong == True:
    print("Error: Numbers cannot be more than four digits.")
    quit()

  #Format problems
  for listitem in problems:
    sublist = listitem.rsplit(' ')
    largestnum = max(sublist, key=len)
    maxlen = len(largestnum) + 2
    templengthdiff = maxlen - len(sublist[0])
    rowonenum.append(" "*templengthdiff + sublist[0] + " "*4);
    # print(rowonenum)

    templengthdiff = (maxlen-1) - len(sublist[2])
    rowtwonum.append(sublist[1] + " "*templengthdiff + sublist[2] + " "*4)
    # print(rowtwonum)

    rowthree.append("-"*maxlen + " "*4)
    # print(rowthree)

    if sublist[1] == '+':
      calc = int(sublist[0]) + int(sublist[2])
    else:
      calc = int(sublist[0]) - int(sublist[2])
    ans = str(calc)
    templengthdiff = maxlen - len(ans)
    rowfourans.append(" "*templengthdiff + ans + " "*4)
    # print(rowfourans)

  #Print formatted problems
  print()
  print(*rowonenum, sep="")
  print(*rowtwonum, sep="")
  print(*rowthree, sep="")
  if printresults == True:
    print(*rowfourans, sep="")
