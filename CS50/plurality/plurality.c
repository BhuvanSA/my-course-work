#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

typedef char *string;

// Max number of candidates
#define MAX 9


// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner();
string get_string(string s);
int get_int(string s);


int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
        free(name);
    }

    // Display winner of election
    print_winner();
    return 0;
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    bool a = false;
    for (int i = 0; i < candidate_count; i++)
    {
        if (!strcmp(candidates[i].name, name))
        {
            candidates[i].votes++;
            a = true;
        }
    }
    return a;

}

// Print the winner (or winners) of the election
void print_winner()
{
    // TODO
    int highest = candidates[0].votes;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > highest)
        {
            highest = candidates[i].votes;
        }
    }    
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == highest)
        {
            printf("%s\n", candidates[i].name);
        }
    }
}
int get_int(string s)
{
    int a = 0;
    printf("%s", s);
    scanf("%i", &a);
    return a;
}
string get_string(string s)
{
    string si = malloc(sizeof(char) * 20);
    printf("%s", s);
    scanf("%s", si);
    return si;
}
