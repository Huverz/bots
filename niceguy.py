def niceguyfunc(counter, mypoints, enpoints, mylist, enlist):
  if counter < 2:
    return "c"

  mylast = mylist[counter-1]
  enlast = enlist[len(enlist)-1]
  last_found_index = -1

  for i, item in enumerate(mylist):
    if i == counter - 1:
      break
    if mylist[i] == mylast and enlist[i] == enlast:
      last_found_index = i

  if last_found_index == -1:
    return "c"
  else:
    if enlist[last_found_index + 1] == "c":
      return "c"
    else:
      return "d"
