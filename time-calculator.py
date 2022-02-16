def add_time(start, duration, Day = False):
  week_days={'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}
  keys=[]
  for key in week_days:
    keys.append(key)

  r_days=0
  time= start.split()[0]
  o_hour=int(time.split(':')[0])
  o_minute=int(time.split(':')[1])
  o_period= start.split()[1]
  if o_period== 'PM':
    o_hour= o_hour+12

  d_hour=int(duration.split(':')[0])
  d_minute=int(duration.split(':')[1])

  r_minute= o_minute + d_minute
  rest_min=0
  if r_minute >= 60:
    r_minute= r_minute - 60
    rest_min=1
  if r_minute<10:
    r_minute='0'+str(r_minute)


  r_hour=o_hour + d_hour +rest_min
  
  if r_hour> 24:
    r_days= int(r_hour/24) # error
    r_hour= (r_hour-24*r_days)
    
    if r_hour > 12:
      s_hour= str(r_hour-12)+':'
      s_minute= str(r_minute)+ ' PM'
      
    else:
      s_hour= str(r_hour)+':'
      s_minute= str(r_minute)+ ' AM'
      
  elif 24>r_hour>=12:
    s_hour= str(r_hour-12)+':'
    s_minute= str(r_minute)+ ' PM'
    
  else:
    s_hour= str(r_hour)+':'
    s_minute= r_minute+ ' AM'
    
  if s_hour=='0:':
    s_hour='12:'
    

  s_time=s_hour+s_minute

  if Day:
    Day= Day.capitalize()
    week_day_value=int(week_days.get(Day))
    sum= r_days+ week_day_value
    #print(sum)
    while sum>= len(keys):
      sum=sum-len(keys)
    #print (sum)
    #if sum>7:
      #sum= int((sum/7) + ( sum%7>0))
      #print(sum)
      #if sum > int(sum):
        #sum=int(sum+1)#
        #print(sum)
    d_o_t_w=keys[sum]

    if  r_days>=2:
      s_days= d_o_t_w+' ('+str(r_days) +' days later)'
      added_time= s_time+', '+ s_days
    elif 0<r_days<2 :
      s_days='(next day)'
      added_time= s_time+', '+d_o_t_w+' '+s_days
    else:
      added_time= s_time+', '+d_o_t_w

  else:
    if  r_days>=2:
      s_days= '('+str(r_days) +' days later)'
      added_time= s_time+' '+s_days
    elif 0<r_days<2 :
      s_days='(next day)'
      added_time= s_time+' '+ s_days
    else:
      added_time= s_time
  return added_time