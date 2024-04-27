pub struct Solution;

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let length = nums.len();
        if length == 0 {
            return 0
        }
        let mut start_index = 0;
        let mut end_index = length-1;
        while start_index < end_index {
            if nums[start_index] != val {
                start_index += 1;
            }
            if nums[end_index] == val {
                end_index -= 1;
            }
            if nums[start_index] != val && nums[end_index] == val {
                nums[start_index] = nums[end_index];
                end_index -= 1;
                start_index += 1;
            }
        }
        return end_index as i32;
    }
}