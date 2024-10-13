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
mod q275_h_index_2;
mod q279_perfect_squares;
mod q238_product_of_array_except_self;
mod q383_ransom_note;
mod q205_isomorphic_strings;
mod q228_summary_ranges;
mod q203_remove_linked_list_elements;
mod q398_random_pick_index;
mod q130_surrounded_regions;
mod q1768_merge_strings_alternately;
mod q682_baseball_game;
mod q134_gas_station;
mod q151_reverse_words_in_a_string;
mod q135_candy;
mod q392_is_subsequence;
mod q54_spiral_matrix;
mod q137_single_number_2;
mod q290_word_pattern;

/// 检查有无做重复的题，以及题目的序号是否重了，至于序号错误就不管了。
fn check() {
	let mut answers = [false; 65536];
	check_folder(&mut answers, "src");
	check_folder(&mut answers, "python");
}

fn check_folder(answers: &mut [bool], folder: &str) {
	for path in fs::read_dir(folder).unwrap() {
		let name = path.unwrap().file_name();
		let name = name.to_str().unwrap();

		let prefix = name.bytes().next().unwrap();
		if prefix != b'Q' && prefix != b'q' {
			continue;
		}
		let id = name.find("_")
			.map(|i| &name[1..i])
			.map(|s| usize::from_str_radix(s, 10).ok())
			.flatten();

		if id != None {
			let id = id.unwrap();
			if !answers[id] {
				answers[id] = true;
			} else {
				println!("Found duplecated answers for {}", id);
			}
		}
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
