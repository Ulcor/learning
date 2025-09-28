# Lists are mutable

class Entry:
  def __init__(self, title, entries=[]):
    self.title = title
    self.entries = entries

entry = Entry("stmh")
entry.entries.append('Value_1')
entry.entries.append('Value_2')
print(entry.entries)

# list in entry_2 is the same as in entry. Because entries is a list and lists are mutable
entry_2 = Entry("sth")
entry_2.entries.append('Value_3')
print(entry_2.entries)

# Fixed version
class Entry:
  def __init__(self, title, entries=None):

    if entries is None:
        entries = []
    self.title = title
    self.entries = entries

entry = Entry("stmh")
entry.entries.append('Value_1')
entry.entries.append('Value_2')
print(entry.entries)

# list in entry_2 is isolated
entry_2 = Entry("sth")
entry_2.entries.append('Value_3')
print(entry_2.entries)



