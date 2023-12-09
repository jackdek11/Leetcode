/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    for( var i = 0; i <= nums.length - 1; i++ )
    {
        if( target <= nums[i] )
        {
          return i;
        }
    }
    return nums.length;
};
