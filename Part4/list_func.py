nums =  [33, 22, 11, 77, 55, 66, 99, 88]
print(nums.index(11)) # 11의 index 번호 출력

# 맨 마지막 원소를 리턴하고 삭제
print(nums.pop())  
print(nums) # 88이 삭제된 것을 확인할 수 있다.

# 정렬 (오름차순)
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort()
print(nums)

# 정렬 (내림차순)
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort(reverse=True)
print(nums)

# 역순
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
nums.reverse()
print(nums)

# remove
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
nums.remove(11) # 11이 삭제된다
print(nums)

# 병합
nums1 =  [33, 22, 11]
nums2 =  [77, 55, 66, 99, 88]
nums1.extend(nums2)
print(nums1) # 원본 데이터가 변함

nums1 =  [33, 22, 11]
nums2 =  [77, 55, 66, 99, 88]
nums3 = nums1 + nums2 # 변수에 담아서 합치기 
print(nums3)

# count
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
print(nums.count(77))

# sorted 
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
print(sorted(nums)) # 원본 데이터가 바뀌지 않는다 (sort함수랑 다름)

# sorted (역순)
nums =  [33, 22, 11, 77, 55, 66, 99, 88]
print(sorted(nums,reverse=True)) # 원본 데이터가 바뀌지 않는다 (sort함수랑 다름)

rainbow = ['red', 'orange', 'yellow', 'box', 'blue', 'navy', 'purple']
rainbow.remove('box')
