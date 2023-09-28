#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted linked list
 * @head: A pointer to the head of the list
 * @number: The number to be inserted
 *
 * Return: The address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	temp = *head;
	while (temp)
	{
		if (number >= temp->n && number <= temp->next->n)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	return (NULL);
}
