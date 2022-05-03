#include "lists.h"
#include <stdio.h>

/**
 * *insert_node - inserts a number into a sorted singly linked list.
 * @head: list
 * @number: integer
 *
 * Return: a node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if (number >= current->n && number < current->next->n)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			else if (number <= current->n && number < current->next->n)
			{
				new->next = current;
				*head = new;
				return (new);
			}
			current = current->next;
		}
		current->next = new;
	}
	return (new);
}