if __name__ == '__main__':
  pass

events = []

def make_list(occurence):
  events.append(occurence)
  return events

def deleted(to_delete, list):
  list.remove(to_delete)
  return list

def edit(to_edit, edited, list):
  index = list.index(to_edit)
  list[index] = edited
  return list