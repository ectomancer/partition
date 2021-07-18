from partition import dec, partition

#https://oeis.org/A000041
oeis = [1,1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,
 297,385,490,627,792,1002,1255,1575,1958,2436,3010,
 3718,4565,5604,6842,8349,10143,12310,14883,17977,
 21637,26015,31185,37338,44583,53174,63261,75175,
 89134,105558,124754,147273,173525]

def test_partition():
    """Test partition function with pytest."""
    result = list()
    for n in range(50):
        result += [partition(n)]

    assert result == oeis

