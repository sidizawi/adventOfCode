#ifndef FT_H
# define FT_H

# include <unistd.h>
# include <fcntl.h>
# include <stdlib.h>
# include <stdio.h>

# define BUFF_SIZE 1000

char	*ft_read_file(char *file);
char	*ft_join(char *str, char *buff);
char	**ft_split(char *str, char c);
void	ft_free(char **elems);
int		ft_strlen(char *str);

#endif 
