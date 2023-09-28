#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: A pointer to the head of the list
 *
 * Return: 0 if not palindrome and 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *arr;
	int f, l, len = 0, i = 0;

	if (*head == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	arr = malloc(sizeof(int) * (len));
	temp = *head;
	while (temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	l = len - 1;
	if (len % 2 == 0)
	{
		for (f = 0; f < len; f++)
		{
			if (arr[f] != arr[l])
				return (0);
			l--;
		}
		return (1);
	}
	for (f = 0; f < ((len - 1) / 2); f++)
	{
		if (arr[f] != arr[l])
			return (0);
		l--;
	}
	return (1);
}
