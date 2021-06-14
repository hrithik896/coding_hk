/*Program to implement a Stack using Arrays in C and develop functions to perform push and pop operations*/
#include<stdio.h>
#include<stdlib.h>

struct stack{
    int value;
    struct stack*next;                   //ensures that a variable next is a pointer to the stack .
};
struct stack *top = NULL;

void push_element();
void pop_element();
void display_stack();
void display_top();

void main()
{
    int choice;
    while(1)                             //The while(1) or while(any non-zero value) is used for infinite loop. So what are present inside the loop that will be executed forever
    {
        printf("Enter 1 to Push element\n");
        printf("Enter 2 to Pop element\n");
        printf("Enter 3 to Display top element\n");
        printf("Enter 4 to Display all elements\n");
        printf("Enter 0 Exit.\n");
        printf("Enter your choice:\n");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1: 
                push_element();
                break;

            case 2:
                pop_element();
                break;

            case 3:
                display_top();
                break;

            case 4:
                display_stack();
                break;

             case 0:
                exit(0);

            default:
                printf("wrong input!...Try again!");

        }
    }
}
void push_element()
{
    int number;
    struct stack *tmp;
    tmp = (struct stack*)malloc(sizeof(struct stack)); //dynamically allocating memory
    printf("Enter value to be inserted:\n");
    scanf("%d", &number);

    tmp->value = number;                    //The -> operator in C  gives the value held by variable_name to structure or union variable pointer_name.
    tmp->next = top;                       // Assigning value to value variable of tmp using arrow operator
    top = tmp;
}
void pop_element()
{
    struct stack *tmp;
    if(&top == NULL)
    {
        printf("Stack is empty\n");
    }
    else{
        tmp = top;
        printf("value to be popped is: %d\n", tmp->value); // Printing the assigned value to the variable
        top = top->next;
        free(tmp);                                        //freeing the memory
    }
}
void display_top()
{
    if(top == NULL)
    {
        printf("Stack is empty!\n");
    }
    else{
        printf("Top of the stack is : %d\n", top->value);
    }
}
void display_stack()
{
    struct stack *tmp;
    tmp = top;
    if(top == NULL)
    {
        printf("Stack is empty!\n");
    }
    else{
        while(tmp!= NULL)
        {
            printf("%d\n", tmp->value);
            tmp = tmp->next;
        }
    }
}
