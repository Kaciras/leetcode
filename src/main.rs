#![allow(unused)]

use std::io::Read;
use std::{env, fs};

mod linked_list;

mod q6_zigzag_conversion;
mod q9_palindrome_number;
mod q27_remove_elements;
mod q80_remove_duplicates_from_sorted_array_2;
mod q32_longest_valid_parentheses;
mod q12_integer_to_roman;
mod q11_container_with_most_water;
mod q3024_type_of_triangle;
mod q35_search_insert_position;
mod q10_regular_expression_matching;
mod q278_first_bad_version;
mod q16_3sum_closest;
mod q45_jump_game_2;
mod q224_basic_calculator;
mod q168_excel_sheet_column_title;
mod q24_swap_nodes_in_pairs;
mod q119_pascal_triangle_2;
mod q120_triangle;
mod q42_trapping_rain_water;
mod q58_length_of_last_word;
mod q202_happy_number;
mod q169_majority_element;
mod q274_h_index;

/// 检查有无做重复的题，以及 Python 里
fn check() {
	let mut answers = [false; 65536];
	for path in fs::read_dir("src").unwrap() {
		let name = path.unwrap().file_name();
		let name = name.to_str().unwrap();
		let prefix = name.bytes().next().unwrap();
		if prefix != b'Q' && prefix != b'q' {
			continue;
		}
		let sep = name.find("_");
		if sep == None {
			continue;
		}
		let num=&name[1..sep.unwrap()];
		let id = usize::from_str_radix(num,10).unwrap();
		if answers[id] {
			println!("Found duplecated answers for {}", id);
		}
		answers[id] = true;
	}
}

fn main() {
	let args: Vec<String> = env::args().skip(1).collect();
	if args.is_empty() {
		return println!("No command given");
	}
	match args[0].as_str() {
		"check" => check(),
		x => println!("Unknown command: {}", x),
	}
}
