first = input()
nums = first.split(" ")
num= int(nums[0])
my_list = []


maxliters= int(nums[1])
h=float(0)

for item in range(num):
   my_list.append(input())

liters= [] 
happiness=[]

for item2 in my_list:
   parts=item2.split()
   if len(parts)>1:
      liters.append(parts[1])
      happiness.append(parts[0])
ind= -1


for items in range(num):
   maxnum=float(0)
   counter=int(0)
   maxdev=float(0)
   loo=int(0)
   for index, item in enumerate(happiness):     
      maxdev= float(item)/float(liters[loo])
      if maxdev > maxnum:
         maxnum=maxdev
         ind=index
      loo = loo+1 
   if maxliters >=int(liters[ind]):
      h = h + float(happiness[ind])
      maxliters= maxliters - int(liters[ind])
      happiness.pop(ind)
      liters.pop(ind)
      counter= counter+1
      ind=0
      continue
   if maxliters <int(liters[ind]):
      devide=maxliters/int(liters[ind])
      h = h + float(happiness[ind])*devide
      maxliters= maxliters - maxliters
      happiness.pop(ind)
      liters.pop(ind)
      counter= counter+1
      break



formatted_happiness = format(h, '.1f')
print(formatted_happiness) 





