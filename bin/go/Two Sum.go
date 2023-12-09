func twoSum(nums []int, target int) []int {
  kv_pairs := make(map[int]int)

  for index, num := range nums{
    desired := target - num
    if value, exists := kv_pairs[desired]; exists {
      return []int{index, value}
    }
    kv_pairs[num] = index
  } 
  return []int{}
}