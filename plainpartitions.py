def partitions(p):
	# base case of recursion: zero is the sum of the empty list
	if p == 0:
		yield []
		return
		
	# modify partitions of n-1 to form partitions of n
	for k in partitions(p-1):
		yield [1] + k
		if k and (len(k) < 2 or k[1] > k[0]):
			yield [k[0] + 1] + k[1:]


def probability(x, N, p):
    import math
    partitions_list = list(partitions(p))
    probability = 0
    for i in [0, len(partitions_list)-1]:
        nums = partitions_list[i]
        quant = math.factorial(N)/(math.factorial(nums[0]) * math.factorial(N - nums[len(nums)-1]))
        if len(nums) > 2:
            for k in [0, len(nums)-2]:
                quant = quant/math.factorial(nums[k+1]-nums[k])

        prob = math.pow(x, -p) *math.pow(1-1/float(x), N - nums[0]-1)
        total = quant * prob

        probability = probability + total

        return probability

