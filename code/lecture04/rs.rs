use itertools::Itertools;

fn performant_smallest(arr: &[u32], n: usize) -> Vec<u32> {
    arr.iter().enumerate().sorted_by(|(_, x), (_, y)| x.cmp(&y)).take(n).sorted_unstable_by(|(i, _), (j, _)| i.cmp(&j)).map(|(_,e)| *e).collect()
}