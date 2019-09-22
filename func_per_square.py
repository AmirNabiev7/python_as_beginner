# write the function of perimeter and square
def count_perimeter(side_1, side_2):
  return(side_1 + side_2) * 2
def count_square(side_1, side_2):
  return side_1 * side_2
def show_info(side_1, side_2):
  p = count_perimeter(side_1, side_2)
  s = count_square(side_1, side_2)
  result = "The perimeter is " + str(p) + " m., "
  result += "and the square is " + str(s) + " sq. m."
  return result
def runner():
  print(show_info(5, 3))
  print(show_info(4, 3))
  print(show_info(5.3, 4))
runner()