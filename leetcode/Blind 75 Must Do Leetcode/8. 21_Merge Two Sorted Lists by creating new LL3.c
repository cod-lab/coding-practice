#include <stdlib.h>                                                               
#include <stdio.h>                                                               

struct node
{
	int data;
	struct node *next;
};

void createLL(struct node *tmp, char s[])
{
	int l;
	printf("%s",s);
	printf("enter list length: ");
	scanf("%d",&l);
	if(l)
	{
		while(1)
		{
			printf("\nenter data: ");
			scanf("%d",&(tmp->data));
			if(!(--l)) break;
			tmp->next = (struct node *) malloc(sizeof(struct node));
			tmp = tmp->next;
		}
		tmp->next = NULL;
	}
	else tmp->data = 0;
}

void displayLL(struct node *tmp, char s[])
{
	printf("%s",s);
	// if(tmp->next) printf("\n\n%d\n",tmp->next->data);
	if(tmp->data)
	{
		while(1)
		{
			printf("tmp: %d,%p",tmp->data,tmp->next);
			if(!(tmp->next)) break;
			printf(" -> ");
			tmp = tmp->next;
		}
	}
	else printf("empty list");
}

struct node *mergeLL(struct node *tmp1, struct node *tmp2, struct node *tmp3)
{
	// int m=4,n=4;			X
	// printf("\n\n%d, %d\n",tmp1->data,tmp2->data);
	struct node *head3 = tmp3;
	if(tmp1->data && tmp2->data)
	{
		while(1)
		{
			if(tmp1->data < tmp2->data)
			{
				tmp3->data = tmp1->data;
				if(tmp1->next) tmp1 = tmp1->next;
				else break;
			}
			else
			{
				tmp3->data = tmp2->data;
				if(tmp2->next) tmp2 = tmp2->next;
				else break;
			}
			// if(!(tmp1->next) && !(tmp2->next)) break;		X
			// if(!m && !n) break;			X
			// if(!(--m)) break;			X
			// if(!(tmp1->next)) break;		X
			tmp3->next = (struct node *) malloc(sizeof(struct node));
			tmp3 = tmp3->next;
		}

		// printf("\n\ntmp1: %d, tmp2: %d\n",tmp1->data,tmp2->data);

    	if(!(tmp1->next) && tmp1->data > tmp2->data) tmp3->next = tmp1;
		else if(!(tmp1->next)) tmp3->next = tmp2;
		else tmp3->next = tmp1;
		// tmp3->next = NULL;			X
		return head3;
	}
	// else if(tmp1->data || tmp2->data)		✓
	else if(!tmp1->data || !tmp2->data)
	{
		if(tmp1->data) return tmp1;
		else return tmp2;
	}
	else
	{
		printf("\n\nboth lists are empty");
		// tmp3->data = 0;		✓
		return tmp1;
	}
}

int main()
{
	struct node *head1,*head2,*head3;		// creating 'struct node' type pointer 'head' pointing L.L, pointer variable to create and traverse L.L
	head1 = (struct node *) malloc(sizeof(struct node));		// allocating heap(dynamic) memory of size 'struct node'
	head2 = (struct node *) malloc(sizeof(struct node));		// allocating heap(dynamic) memory of size 'struct node'
	head3 = (struct node *) malloc(sizeof(struct node));		// allocating heap(dynamic) memory of size 'struct node'

	// int no_of_nodes = 3;			✓
	createLL(head1,"\nL.L 1\n");
	createLL(head2,"\nL.L 2\n");
	displayLL(head1,"\nL.List 1:\n");
	displayLL(head2,"\n\nL.List 2:\n");
	head3 = mergeLL(head1,head2,head3);
	displayLL(head3,"\n\nmerged L.List:\n");

	free(head1);
	free(head2);
	free(head3);

	return 0;
}

