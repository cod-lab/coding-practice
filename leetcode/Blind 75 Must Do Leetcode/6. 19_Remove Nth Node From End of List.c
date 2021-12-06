#include <stdlib.h>                                                               
#include <stdio.h>                                                               

struct node
{
	int data;
	struct node *next;
};

void createLL(struct node *tmp, int l)
{
	int x=1;
	while(1)
	{
		// tmp->data = l-- - l;		X
		tmp->data = x++;
		tmp->next = (struct node *) malloc(sizeof(struct node));
		// if(l==-1) break;		X
		if(x==l+1) break;
		tmp = tmp->next;
	}
	// printf("%p,%p",tmp,tmp->next);
	tmp->next = NULL;
	// printf("\n%p",(void *)tmp->next);
	// printf("\nvoid ",(void *)tmp->next);
	// free(tmp);		X
}

struct node *LL_BeforeDel(struct node *head, struct node *tmp, struct node *p, int n)
{
	printf("\nbefore deletion:\n");
	while(1)
	{
		printf("tmp: %d,%p",tmp->data,tmp->next);
		printf("\t\tn: %d \n",n);
		if(tmp->next == NULL) break;
		// printf(" -> ");
		tmp = tmp->next;
		// if(n-- == 1) 		✓
		// if(--n == 0)			✓
		// if(--(!n))			X
		if(!(--n))
		{
			p=head;
			printf("\tp: %d,%p\n",p->data,p->next);
		}
        // if(--n && p) 
        if(p && n) 
        {
        	p=p->next;
			printf("\tp: %d,%p\n",p->data,p->next);
        }
	}
	// free(head);		X
	// free(tmp);		X

    return p;
}

void LL_AfterDel(struct node *tmp)
{
	printf("\n\nafter deletion:\n");
	while(1)
	{
		printf("%d,%p",tmp->data,tmp->next);
		if(tmp->next == NULL) break;
		printf(" -> ");
		tmp = tmp->next;
	}
	free(tmp);
}

int main()
{
	struct node *head;		// creating 'struct node' type pointer 'head' pointing L.L, pointer variable to create and traverse L.L
	head = (struct node *) malloc(sizeof(struct node));		// allocating heap(dynamic) memory of size 'struct node'
	struct node *p;		// for deleting node from L.L

	int no_of_nodes = 5;
	for(int i=0; i<=no_of_nodes; i++)
	{
		// creating L.L
		createLL(head,no_of_nodes);


		// traversing and printing L.L before deletion
		// int node_to_del = i;		✓
		p = LL_BeforeDel(head,head,NULL,i);
	    // printf("\np: %p",p);

	    if(head->next == NULL)
	    {
	    	printf("\n\nafter deletion:\nlist is empty\n");
	    	exit(0);
	    }
	    if(!p && i) head = head->next;
	    if(p) p->next = p->next->next;


	    // traversing and printing L.L after deletion
		LL_AfterDel(head);
		printf("\n\n");
	}
	free(head);
	free(p);
}

