#include "ft.h"

char	*ft_read_file(char *file)
{
	int		fd;
	int		r;
	char	*buff;
	char	*res;

	fd = open(file, O_RDONLY);
	if (fd < 1)
		return (NULL);
	buff = malloc(sizeof(char) * (BUFF_SIZE + 1));
	if (!buff)
		return (NULL);
	r = 1;
	res = NULL;
	while (r > 0)
	{
		r = read(fd, buff, BUFF_SIZE);
		if (r < 0)
		{
			if (buff)
				free(buff);
			if (res)
				free(res);
		}
		if (r == 0)
			break ;
		buff[r] = '\0';
		res = ft_join(res, buff);
	}
	close(fd);
	free(buff);
	return (res);
}

