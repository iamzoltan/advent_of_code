use regex::Regex;
use crate::utils;

pub fn part2(file_path: &str) -> i32 {
    let program: Vec<String> = parse_file(file_path);
    // println!("length {}", program.len());
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)").unwrap();
    return calculate_total_from_pattern(re, program);
}

pub fn part1(file_path: &str) -> i32 {
    let program: Vec<String> = parse_file(file_path);
    // println!("length {}", program.len());
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    return calculate_total_from_pattern(re, program);
}

fn calculate_total_from_pattern(re: Regex, program: Vec<String>) -> i32 {
    let mut total = 0;
    let mut enabled = true;
    for line in program {
        for caps in re.captures_iter(&line) {
            let command =  caps.get(0).map_or("", |m| m.as_str());
            if command == "do()" {
                enabled = true;
                continue;
            } else if command == "don't()" {
                enabled = false;
                continue;
            }
            if enabled {
                let mut first_num = 0;
                let mut second_num = 0;
                // Extract and parse the first number
                if let Some(first_number_str) = caps.get(1) {
                    if let Ok(first_number) = first_number_str.as_str().parse::<i32>() {
                        // println!("First number: {}", first_number);
                        first_num = first_number;
                    }
                }
        
                // Extract and parse the second number
                if let Some(second_number_str) = caps.get(2) {
                    if let Ok(second_number) = second_number_str.as_str().parse::<i32>() {
                        // println!("Second number: {}", second_number);
                        second_num = second_number;
                    }
                }
                total += first_num * second_num;
            }
        }
    }
    total
}


fn parse_file(file_path: &str) -> Vec::<String> {
    let mut program = Vec::<String>::new();
    if let Ok(lines) = utils::read_lines(file_path) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines.flatten() {
            program.push(line);
        }
    }
    program
}
