#Ex1

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Ex2

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #False