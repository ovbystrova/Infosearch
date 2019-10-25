def make_results(sorted_idx, sorted_metric, data, n=10):
  final = []
  for i in range(0, n):
    element = str(data[int(sorted_idx[i])])
    line = element + ' - ' + str(sorted_metric[i])
    final.append(line)
  return final