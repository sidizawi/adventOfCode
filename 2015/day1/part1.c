#include "ft.h"

int	main(int ac, char **av)
{
	char	*data;
	int		i;
	int		floor;

	if (ac != 2)
		return (1);
	data = ft_read_file(av[1]);
	if (!data)
		return (1);
	i = 0;
	floor = 0;
	while (data[i])
	{
		if (data[i] == ')')
			floor--;
		else if (data[i] == '(')
			floor++;
		i++;
	}
	printf("floors: %d\n", floor);
	free(data);
}
