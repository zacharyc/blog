/*---------------------------------------------------------------------------
 | function_arrays.c
 | Date: 12/13/2007
 |
 | Description: Simple program that shows how to use arrays of functions in C.
 |  This program simply uses several string fuctions in an array to process 
 |  a string.
 |
 | Suggested compile: gcc -g function_arrays.c -o function_arrays
 -----------------------------------------------------------------------------*/

#include <stdio.h>
#include <string.h>

#define SUCCESS 0
#define TEST_STRING "foo \t: is really: not so nice\t with :other \t:people"

enum error_codes {
	NULL_STRING_POINTER_ERR 	= 1
};

/* Replaces colons with underscores */
int remove_colons(char *input_string)
{
	int i;
	
	char test_char = ':';
	char replace_with = '_';
	
	if(input_string == NULL)
	{
		fprintf(stderr, "String cannot be NULL\n");
		return NULL_STRING_POINTER_ERR;
	}
	
	for(i = 0; i < strlen(input_string); i++)
	{
		if(input_string[i] == test_char)
			input_string[i] = replace_with;
	}
	
	return SUCCESS;
}

/* Replaces spaces with underscores */
int remove_spaces(char *input_string)
{
	int i;
	
	char test_char = ' ';
	char replace_with = '_';
	
	if(input_string == NULL)
	{
		fprintf(stderr, "String cannot be NULL\n");
		return NULL_STRING_POINTER_ERR;
	}
	
	for(i = 0; i < strlen(input_string); i++)
	{
		if(input_string[i] == test_char)
			input_string[i] = replace_with;
	}
	
	return SUCCESS;
}

/* Replaces colons with underscores */
int remove_tabs(char *input_string)
{
	int i;
	
	char test_char = 'o';
	char replace_with = '_';
	
	if(input_string == NULL)
	{
		fprintf(stderr, "String cannot be NULL\n");
		return NULL_STRING_POINTER_ERR;
	}
	
	for(i = 0; i < strlen(input_string); i++)
	{

		if(input_string[i] == test_char)
		{
			input_string[i] = replace_with;
		}
	}
	
	return SUCCESS;
}

int main(int argc, char **argv) 
{
	int num_of_functions = 3;
	int i;
	
	int (*function_array[3])(char *) = {NULL};
	
	function_array[0] = &remove_tabs;
	function_array[1] = &remove_spaces;
	function_array[2] = &remove_colons;
	
	/* The string needs be defined as a character array. */
	/* if you define the string as a pointer to as set of characters it will
	   put it in read-only memory and you won't be able to update it later. */
	char test_string[] = TEST_STRING;
	
	for(i = 0; i < num_of_functions; i++)
	{
		int rc = 0;
		
		if((*function_array[i])(test_string) != 0)
			printf("There was an error processing the string.\n");
	}
	
	printf("String is now: %s\n", test_string);
	
	return SUCCESS;
}
