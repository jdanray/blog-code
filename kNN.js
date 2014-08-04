var kNNClassifier = {
	k: 0,
	training_set: [],
	train: function(attr, type) {
		this.training_set.push({attributes: attr, type: type});
	},
	classify: function(datapoint) {
		function most_freq_type(set, k) {
			var types = {};
			var max = 0;
			var mostFreq;
			
			for (var i in set.slice(0, k)) {
				var type = set[i].type;
				if (!types[type]) {
					types[type] = 0;
				}
				types[type] += 1;				
				if (types[type] > max) {
					max = types[type];
					mostFreq = type;
				}
			}
			return mostFreq;
		}
		function measure(instance, base) {
			var s = 0;
			for (var i in instance) {
				s += Math.pow(instance[i] - base[i], 2);
			}
			return Math.sqrt(s);
		}
		this.training_set.sort(function(a, b) { return measure(datapoint, a.attributes) - measure(datapoint, b.attributes) });
		return most_freq_type(this.training_set, this.k);
	}
};
