#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Creates 5 zombie child processes
 *
 * Return: 0 (Success)
 */

int main(void)
{
	pid_t  child_prcs;
	int i;

	for (i = 0; i < 5; ++i)
	{
		child_prcs = fork(); /*create child pid*/
		if (child_prcs < 0)
			exit(1);
		else if (child_prcs == 0) /*child process that closes auto. */
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else /* In parent process, pid > 0 is returned here by fork() */
		{
			continue;
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - creates an infinte loop
 *
 * Return: 0 (Success)
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
