"""
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

An example is if our input was as follows:
[1, 2, 3, 4, 5]

The output would be:
[120, 60, 40, 30, 24]

Do this without using division.

"""


def products_of_all_other_elements(nums):

  # We will use this to store values
    prefix_products = []

  # Iterate thru array
    for num in nums:
    # Check to see if value is already in prefix array
        if prefix_products:
      # If it is, take that value and multiply it times the last element in the prefix array
            prefix_products.append(prefix_products[-1] * num)

    # If it is not in the prefix array, just append that value
        else:
            prefix_products.append(num)


  # This also will be used to store values
    suffix_products = []

  # Iterate thru the list in reversed order
    for num in reversed(nums):
    # Check to see if value is already in the new suffix array
        if suffix_products:
      # If it is, append that value times the last element in the suffix array
            suffix_products.append(suffix_products[-1] * num)

    # If it isn't, add that value to the suffix array
        else:
            suffix_products.append(num)

  # Take that suffix array and turn it into a list then reverse it.
    suffix_products = list(reversed(suffix_products))


  # This will be our results array which is a product of both Prefixes and Suffixes arrays
    result = []

  # Iterate thru our input array
    for i in range(len(nums)):

    # If the iterator, is ever equal to 0
        if i == 0:

      # Add that value plus 1
            result.append(suffix_products[i + 1])

    # Check to see if the iterator is ever equal to the length of the list minus 1.
        elif i == len(nums) - 1:

    # If not, append that value minus 1 from Prefix array and multiply it by iterator plus 1 from Suffix array
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])

  # Return the result
    return result

# Runtime for this Algorithm will be 0(N) and the Space complexity will be 0(N) due to using prefix & suffix arrays
