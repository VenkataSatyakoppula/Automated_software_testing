#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node
{
    int data;
    struct node *next;

};
struct node *head=NULL;

void inserting(int data){
   struct node *link = (struct node*) malloc(sizeof(struct node));
   link->data = data;
   link->next = head;
   head = link;
}
struct node* delete(int data) {
   struct node* cur = head;
   struct node* prev = NULL;
   if(head == NULL) {
      return NULL;
   }
   while(cur->data != data) {
      if(cur->next == NULL) {
         return NULL;
      } else {
         prev = cur;
         cur = cur->next;
      }
   }
   if(cur == head) {
      head = head->next;
   } else {
      prev->next = cur->next;
   }    
   return cur;
}
void disp() {
   struct node *ptr = head;
   while(ptr != NULL) {
      printf("%d->",ptr->data);
      ptr = ptr->next;
   }
   printf("\n");
}
void count(){
    int sum=0;
    struct node *ptr = head;
   while(ptr != NULL) {
      sum += 1;
      ptr = ptr->next;
   }
   printf("no.of nodes = %d \n",sum);
}
int main(){
    int choice;
    int n;
    printf("Enter the n digit number = ");
    scanf("%d",&n);
    for (int i = 1; i < n; i++)
    {
        inserting(i);
    }
    while (1)
    {
        printf("1)Display ordered LL(Decending)\n2)Enter data to delete\n3)Count the nodes\n4)Exit\n");
        printf("Choice = \n");
        scanf("%d",&choice);
        if (choice==1)
        {
            disp();
        }else if(choice==2)
        {
            int data;
            printf("Enter the element = ");
            scanf("%d",&data);
            delete(data);
            printf("Element %d Deleted\n",data);
        }else if(choice==3){
           count();
        }else if(choice==4){
            printf("Exiting...\n");
            break;
        }else{
            printf("Enter input between[1,3]\n");
        }
        
    }
}