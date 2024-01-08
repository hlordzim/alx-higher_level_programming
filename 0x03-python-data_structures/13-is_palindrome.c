#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverse a linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the new head after reversal.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Check if a linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head, *fast = *head;
	listint_t *second_half;
	int is_palindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	second_half = reverse_list(slow);
	slow = *head;

	while (second_half != NULL)
	{
		if (slow->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		slow = slow->next;
		second_half = second_half->next;
	}
	reverse_list(second_half);
	return (is_palindrome);
}
