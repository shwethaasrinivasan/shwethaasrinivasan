def isPowerOfFour(n: int) -> bool:
    if n == 1:
        return True
    if n < 1:
        return False
    return isPowerOfFour(n / 4)


# Nitik
# Goyal
# 13: 01
# public
# boolean
# isPowerOfFour(int
# n) {
# if (n == 0)
# return false;
# if (n == 1) return true;
# if (n % 4 != 0) return false;
#
# return isPowerOfFour(n / 4);
# }
# Shreya
# Das
# 13: 01
# var
# isPowerOfFour = function(n)
# {
# if (n === 1) {
# return true;
# } else if (n <= 0 | | n % 4 !== 0) {
# return false;
# } else {
# return isPowerOfFour(n / 4);
# }
# };