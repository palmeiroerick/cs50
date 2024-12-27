// Implements a dictionary's functionality

#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

const unsigned short int NC = 27; // Number of Characters (all letters + apostrophe)
const unsigned int N = 18332;     // Number of buckets in hash table

// Hash table
node *table[N];

int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *currentNode = table[hash(word)];

    while (currentNode != NULL)
    {
        if (strcasecmp(currentNode->word, word) == 0)
            return true;

        currentNode = currentNode->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int len = strlen(word);

    int l1 = len >= 1 ? toupper(word[0]) - 'A' + 1 : 0;
    int l2 = len >= 2 ? toupper(word[1]) - 'A' + 1 : 0;
    int l3 = len >= 3 ? toupper(word[2]) - 'A' + 1 : 0;

    l1 = (pow(NC - 1, 2) + NC + 1) * l1 - (pow(NC - 1, 2) + NC + 1);
    l2 = l2 != 0 ? (NC + 1) * l2 - NC : 0;

    return (l1 + l2 + l3) % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];

    // Read each word in the file
    while (fgets(buffer, sizeof(buffer), source) != NULL)
    {
        // Change character '\n' to '\0'
        buffer[strcspn(buffer, "\n")] = '\0';

        if (buffer[0] == '\0')
            continue;

        // Create space for a new hash table node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(source);
            return false;
        }

        // Copy the word into the new node
        strcpy(new_node->word, buffer);

        // Hash the word to obtain its hash value
        unsigned int hash_value = hash(buffer);

        // Insert the new node into the hash table
        new_node->next = table[hash_value];
        table[hash_value] = new_node;

        word_count++;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *currentNode = table[i];

        while (currentNode != NULL)
        {
            node *tmp = currentNode;
            currentNode = currentNode->next;
            free(tmp);
        }
    }

    word_count = 0;
    return true;
}
