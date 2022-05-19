


def ft_filter(fun, iter):
	for elem in iter:
		if fun(elem):
			yield elem