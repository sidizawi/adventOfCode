#include "ft.h"

void	ft_free(char **elems)
{
	int	i;

	i = 0;
	while (elems[i])
		free(elems[i++]);
	free(elems);
}
