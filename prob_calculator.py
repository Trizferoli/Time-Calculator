class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    self.kwargs = kwargs
    if self.kwargs == {}:
      raise IndexError('Cannot choose from an empty sequence')  

    
    for k,v in kwargs.items():
      for item in range(v):
        self.contents.append(k)


  def draw (self, balls=int):
    result = []
    self.balls = balls

    
    if self.balls <= len(self.contents):
      for item in range(self.balls):
        draw = random.choice(self.contents)
        self.contents.remove(draw)
        result.append(draw) 

      return result
    else:
      return ''

def experiment(hat,**kwargs):
    counter = 0
    lis=list(kwargs.values())
    expected_balls = lis[0]
    num_balls_drawn= lis[1]
    num_experiments= lis[2]

    expected=[]
    ocurrences = 0
    contents = hat.contents

    f_expected_balls= expected_balls


    for k,v in expected_balls.items():
      for item in range(v):
        expected.append(k)
  
    for times in range(num_experiments):
      usable_balls = copy.deepcopy(expected)
      dic={}
      draw = hat.draw(num_balls_drawn)
      for item in draw:
        if item in usable_balls:
          usable_balls.pop(usable_balls.index(item))

      if usable_balls==[]:
        counter+=1
      for item in draw:
        hat.contents.append(item)
    prob = counter/num_experiments

    return prob
