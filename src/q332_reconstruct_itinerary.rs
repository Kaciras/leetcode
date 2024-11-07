use std::collections::HashMap;

pub struct Solution;

// Hierholzer 算法求欧拉路径，通过后序遍历确保死胡同节点必在最后。
impl Solution {
	pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
		let mut graph: HashMap<String, Vec<String>> = HashMap::new();

		for ticket in tickets {
			let (src, dst) = (ticket[0].clone(), ticket[1].clone());
			graph.entry(src.clone()).or_default().push(dst);
		}

		for destinations in graph.values_mut() {
			destinations.sort_by(|a, b| b.cmp(a));
		}

		let mut itinerary = vec![];

		fn dfs(graph: &mut HashMap<String, Vec<String>>, airport: &str, itinerary: &mut Vec<String>) {
			while let Some(next) = graph.get_mut(airport).and_then(|dests| dests.pop()) {
				dfs(graph, &next, itinerary);
			}
			itinerary.push(airport.to_string());
		}

		dfs(&mut graph, "JFK", &mut itinerary);

		itinerary.reverse();
		return itinerary;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	fn check(input: &[[&str; 2]], expected: &[&str]) {
		let tickets = input
			.into_iter()
			.map(|e| vec![e[0].into(), e[1].into()])
			.collect();
		assert_eq!(Solution::find_itinerary(tickets), expected);
	}

	#[test]
	fn example1() {
		check(&[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], &["JFK", "MUC", "LHR", "SFO", "SJC"]);
	}

	#[test]
	fn example2() {
		check(&[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], &["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]);
	}

	#[test]
	fn test1() {
		check(&[["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], &["JFK", "ATL", "SFO", "ATL", "JFK"]);
	}
}
