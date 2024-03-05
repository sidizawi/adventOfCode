#include "ft.h"

char	*ft_join(char *str, char *buff)
{
	int		i;
	int		j;
	char	*res;

	i = ft_strlen(str) + ft_strlen(buff);
	if (i < 1)
		return (NULL);
	res = malloc(sizeof(char) * (i + 1));
	if (!res)
		return (NULL);
	i = -1;
	while (str && str[++i])
		res[i] = str[i];
	j = -1;
	while (buff && buff[++j])
		res[++i] = buff[j];
	res[++i] = '\0';
	return (res);
}
