# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n_test_case = int(input())

def Cal(n_season, n_gen):
	total_coupon, min_season, res = 12,5,0
	
	for n in range(min_season, total_coupon+1):
		by_season = n_season // n
		need_coupon = total_coupon - n
		by_gen = n_gen // need_coupon if n != total_coupon else by_season
	
		if n_season < n:
			return res
		
		n_gift = min(by_season, by_gen)
		remain_season = n_season - n_gift*n
		remain_gen = n_gen - n_gift*need_coupon
		if remain_season >= min_season and n_gift != 0:
			assert remain_gen >= 0
			n_gift += Cal(remain_season, remain_gen)
	
		if n_gift > res:
			res = n_gift
	return res

for _ in range(n_test_case):
	N, M = map(int, input().split())
	res = Cal(N,M)
	print(res)
