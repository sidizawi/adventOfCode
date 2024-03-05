#include "ft.h"

int		ft_lines_count(char *str, char ch)
{
	int	i;
	int	c;

	i = -1;
	c = 0;
	while (str[++i])
		if (i > 0 && str[i] == ch && str[i - 1] != ch)
			c++;
	if (i > 0 && str[i - 1] != ch)
		c++;
	return (c);
}

char	*ft_next_line(char *str, char ch, int idx)
{
	int		i;
	int		c;
	char	*res;

	i = -1;
	c = 0;
	while (str[++i] && c < idx)
		if (i > 0 && str[i] == ch && str[i - 1] != ch)
			c++;
	while (str[i] && str[i] == ch)
		i++;
	c = i;
	while (str[i] && str[i] != ch)
		i++;
	i -= c;
	if (i < 1)
		return (NULL);
	res = malloc(sizeof(char) * (i + 1));
	if (!res)
		return (NULL);
	i = c;
	c = 0;
	while (str[i] && str[i] != ch)
		res[c++] = str[i++];
	res[c] = '\0';
	return (res);
}

char	**ft_split(char *str, char c)
{
	int		lines_count;
	int		i;
	char	**res;

	lines_count = ft_lines_count(str, c);
	if (lines_count < 1)
		return (NULL);
	res = malloc(sizeof(char*) * (lines_count + 1));
	if (!res)
		return (NULL);
	i = -1;
	while (++i < lines_count)
	{
		res[i] = ft_next_line(str, c, i);
		if (!res[i])
		{
			i = 0;
			while (res[i])
				free(res[i++]);
			free(res);
			return (NULL);
		}
	}
	res[++i] = 0;
	return (res);
}
