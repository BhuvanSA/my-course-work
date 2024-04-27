mod remove_element;
use remove_element::Solution;

fn main() {
    let mut nums = vec![3, 2, 2, 3];
    let val = 3;
    let k = Solution::remove_element(&mut nums, val);
    println!("k = {}, nums = {:?}", k, &nums[0..k as usize]);
}
