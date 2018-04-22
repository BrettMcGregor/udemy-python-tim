# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

my_list = [1, 2, 3, 4545, 667, "brett", "Devon", "889s0c"]

my_iter = iter(my_list)

for i in range(0, len(my_list)):
    print(next(my_iter))
