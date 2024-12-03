use crate::utils;


type Report = Vec<i32>;


pub fn part2(file_path: &str) -> i32 {
    let reports: Vec<Vec<i32>> = parse_file(file_path);
    let mut num_safe = 0;
    for report in reports {
        // let mut diff_vec = Vec::<i32>::new();
        if !is_safe(report, true) {continue;}
        // let direction = diff_vec[0].signum();
        // let mut negative_count = 0;
        // let mut positive_count = 0;
        // for &value in &diff_vec {
        //     match value.signum() {
        //         -1 => negative_count += 1,
        //         1 => positive_count +=1,
        //         _ => {},
        //     }
        // }
        // if dampener_used && !(negative_count == 0 || positive_count == 0) {
        //     continue;
        // } else if !dampener_used && (negative_count > 1 && positive_count > 1) {
        //    continue; 
        // } 
        num_safe += 1;
    }
    num_safe
}


pub fn part1(file_path: &str) -> i32 {
    let reports: Vec<Vec<i32>> = parse_file(file_path);
    let mut num_safe = 0;
    for report in reports {
        if !is_safe(report, false) {continue;}
        num_safe += 1;
    }
    num_safe
}

fn is_safe(report: Report, dampener: bool) -> bool {
    let direction = (report[0] - report[1]).signum();
    for i in 1..report.len() {
        let abs_diff = report[i-1].abs_diff(report[i]);
        let diff = report[i-1] - report[i];
        if abs_diff == 0 || abs_diff > 3 || diff.signum() != direction {
            if dampener {
                for i in 0..report.len() {
                    let mut left_level_removed = report.clone();
                    left_level_removed.remove(i);
                    if is_safe(left_level_removed, false) {
                        return true;
                    }
                }
            }
            return false;
        }
    }
    return true;
}

fn parse_file(file_path: &str) -> Vec::<Vec::<i32>> {
    let mut reports = Vec::<Vec::<i32>>::new();
    if let Ok(lines) = utils::read_lines(file_path) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            let report: Vec<i32> = line
                .split_whitespace()
                .map(|s| s.parse().expect("Parse error"))
                .collect();
            reports.push(report);
        }
    }
    reports
}
