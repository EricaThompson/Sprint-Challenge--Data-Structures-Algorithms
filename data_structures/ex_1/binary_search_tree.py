class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    new_tree = BinarySearchTree(value)
      for each in self.value:
        if self.value == self.cb:
          return True
        else:
          return False 

    # if self.value == cb:
    #   return True
    # elif cb < self.value:
    #   if self.left:
    #     return self.left.contains(cb)
    #   else:
    #     if self.right:
    #       return self.right.contains(cb)
    #   return False 

  def breadth_first_for_each(self, cb):
    new_tree = BinarySearchTree(value)
    for self.value:
      if self.left == self.cb:
        return True
      elif self.right == self.cb:
        return True
      
      else:
        return False

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
