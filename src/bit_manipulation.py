def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
print(is_power_of_two(8))
print(is_power_of_two(10))
#Remove the Lowest Set Bit
n & (n - 1)
#Count Set Bits
def count_set_bits(n):
    count = 0

    while n:
        n = n & (n - 1)
        count += 1

    return count
"""
Goal	Expression
Check odd	n & 1
Check kth bit	n & (1 << k)
Set kth bit	n | (1 << k)
Clear kth bit	n & ~(1 << k)
Toggle kth bit	n ^ (1 << k)
Remove lowest set bit	n & (n - 1)
Power of 2	n > 0 and (n & (n - 1)) == 0
Count set bits	n.bit_count()
Left shift	n << k
Right shift	n >> k
"""
"""another one lesson was there then thats the end of python"""