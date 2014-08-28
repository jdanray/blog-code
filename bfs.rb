require 'thread'

def match?(t)
	"fill in with whatever match conditions you want"
	false
end

def bfs(graph, source)
	q = Queue.new
	q.push(source)
	seen = [source]
	while !q.empty?
		t = q.pop
		if match?(t)
			return t
		end
		graph[t].each do |v|
			if !seen.include?(v)
				seen.push(v)
				q.push(v)
			end
		end
	end
	nil
end
