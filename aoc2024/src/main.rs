mod utils;
mod day01;
mod day02;
mod day03;

fn main() {
    let result1a = day01::part1("../inputs/day01.txt");
    println!("{}", result1a);
    let result1b = day01::part2("../inputs/day01.txt");
    println!("{}", result1b);
    let result2a = day02::part1("../inputs/day02.txt");
    println!("{}", result2a);
    let result2b = day02::part2("../inputs/day02.txt");
    println!("{}", result2b);
    let result3a = day03::part1("../inputs/day03.txt");
    println!("{}", result3a);
    let result3b = day03::part2("../inputs/day03.txt");
    println!("{}", result3b);
}
