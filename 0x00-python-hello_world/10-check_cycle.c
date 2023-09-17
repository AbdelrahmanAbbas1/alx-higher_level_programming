#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle (loop)
 * @list: A pointer to the list
 *
 * Return: 0 if there is no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node;
	listint_t *temp;

	current_node = list;
	temp = current_node->next;
	while (current_node)
	{
		while(temp)
		{
			if (temp->next == current_node)
				return (1);

			temp = temp->next;
		}
		current_node = current_node->next;
	}
	return (0);
}
