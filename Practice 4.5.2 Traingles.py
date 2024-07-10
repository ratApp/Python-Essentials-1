# 4.5.2 Sample functions: Triangles

# def is_a_triangle(a,b,c):
#   if a + b <= c:
#     return False
#   if b + c <= a:
#     return False
#   if a + c <= b:
#     return False
#   return True


# def is_a_triangle(a,b,c):
#   if a + b <= c or b + c <=a or c + a <= b:
#     return False
#   return True

def is_a_triangle(a,b,c):
  return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a,b,c):
  if c > a and c > b:
    return c ** 2 == a ** 2 + b ** 2 
  if a > b and a > c:
    return a ** 2 == b ** 2 + c ** 2
  
  def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b





print(is_a_triangle(1,1,1))
print(is_a_triangle(1,1,3))

print(is_a_right_triangle(5,3,4))
print(is_a_right_triangle(1,3,4))