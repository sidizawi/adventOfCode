#include "ft.h"

int	ft_solve(char *str)
{
	int		l;
	int		w;
	int		h;
	int		min;
	char	**elems;

	elems = ft_split(str, 'x');
	if (!elems)
		return (0);
	l = atoi(elems[0]);
	w = atoi(elems[1]);
	h = atoi(elems[2]);
	ft_free(elems);
	min = l * h;
	if (l * w < min)
		min = l * w;
	if (w * h < min)
		min = w * h;
	return (2 * (l * h + l * w + w * h) + min);
}

int	main(int ac, char **av)
{
	char	*data;
	char	**lines;
	int		i;
	int		res;

	if (ac != 2)
		return (1);
	data = ft_read_file(av[1]);
	if (!data)
		return (1);
	lines = ft_split(data, '\n');
	free(data);
	if (!lines)
		return (1);
	i = 0;
	res = 0;
	while (lines[i] != 0)
		res += ft_solve(lines[i++]);
	printf("res: %d\n", res);
	ft_free(lines);
}

