use std::fs::File;
use std::collections::HashMap;
use std::u32;
use std::io::{self, BufRead};
use std::path::Path;


pub fn part2(file_path: &str) -> u32 {
    let (l_vec, r_vec) = parse_file(file_path);
    let mut counter = HashMap::<u32, u32>::new();
    for el in r_vec {
        *counter.entry(el).or_insert(0) += 1;
    }
    let mut sim_score = 0;

    for &el in &l_vec {
        if let Some(&count) = counter.get(&el) {
            sim_score += el * count;
        }
    }

    sim_score
} 

pub fn part1(file_path: &str) -> u32 {
    let (mut l_vec, mut r_vec) = parse_file(file_path);
    let mut total = 0;
    // Sort vectors
    l_vec.sort_unstable();
    r_vec.sort_unstable();

    for i in 0..l_vec.len() {
        let distance = l_vec[i].abs_diff(r_vec[i]);
        total += distance;
    }
    total
}

fn parse_file(file_path: &str) -> (Vec::<u32>, Vec::<u32>) {
    let mut l_vec = Vec::<u32>::new();
    let mut r_vec = Vec::<u32>::new();
    if let Ok(lines) = read_lines(file_path) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            let (l_num, r_num) = line.split_once("   ").unwrap();
            l_vec.push(l_num.parse::<u32>().unwrap());
            r_vec.push(r_num.parse::<u32>().unwrap());
        }
    }
    (l_vec, r_vec)
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
