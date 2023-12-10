package main

func PredictTheWinner(nums []int) bool {
    return play(nums, 0, len(nums)-1) >= 0
}

func play(nums []int, left, right int) int {
    if left > right {
        return 0
    }

    scoreLeft := nums[left] - play(nums, left+1, right)
    scoreRight := nums[right] - play(nums, left, right-1)

    if scoreLeft > scoreRight {
        return scoreLeft
    }
    return scoreRight
}