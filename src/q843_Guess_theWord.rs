pub struct Master {
	pub value: String,
	pub found: bool,
	pub calls: usize,
}

impl Master {
	fn guess(&mut self, word: String) -> i32 {
		if word == self.value {
			self.found = true;
		} else {
			self.calls += 1;
		}
		return Solution::similarity(&self.value, &word);
	}
}

pub struct Solution {}

impl Solution {

	// 靠随机（取中）来避免卡数据，能不能过全看运气，好像不是最优解。
	pub fn find_secret_word(mut words: Vec<String>, master: &Master) {
		loop {
			let word = words.swap_remove(words.len() / 2);
			let matches = master.guess(word.clone());
			if matches == 6 {
				return;
			}
			words.retain(|x| Self::similarity(&word, &x) == matches);
		}
	}

	pub fn similarity(a: &str, b: &str) -> i32 {
		return a.bytes().zip(b.bytes()).filter(|&(a, b)| a == b).count() as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	fn check(words: Vec<&str>, secret: &str) {
		let mut master = Master { value: String::from(secret), found: false, calls: 0 };
		let input = words.into_iter().map(String::from).collect();
		Solution::find_secret_word(input, &mut master);
		assert!(master.found);
		assert!(master.calls < 10);
	}

	#[test]
	fn example1() {
		check(vec!["acckzz", "ccbazz", "eiowzz", "abcczz"], "acckzz");
	}

	#[test]
	fn example2() {
		check(vec!["hamada", "khaled"], "hamada");
	}

	#[test]
	fn case1() {
		check(vec!["wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc", "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo", "awvqlr", "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad", "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn", "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa", "kqbttl", "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty", "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg", "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh", "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv", "srxuus", "pydgmq"], "ccoyyo");
	}
}
