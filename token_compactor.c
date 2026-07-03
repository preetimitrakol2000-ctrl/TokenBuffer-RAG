#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TOKEN_LIMIT 60 // Simulated absolute prompt character token size boundary

typedef struct {
    char data_pool[1024];
    int size_tracker;
} TokenStack;

#ifdef _WIN32
    __declspec(dllexport) TokenStack* init_stack_buffer();
    __declspec(dllexport) int push_and_compact(TokenStack* ts, const char* text_segment);
    __declspec(dllexport) const char* expose_prompt(TokenStack* ts);
#endif

TokenStack* init_stack_buffer() {
    TokenStack* ts = (TokenStack*)malloc(sizeof(TokenStack));
    strcpy(ts->data_pool, "");
    ts->size_tracker = 0;
    return ts;
}

int push_and_compact(TokenStack* ts, const char* text_segment) {
    int segment_len = strlen(text_segment);
    
    // Check if the input pushes the stack over the strict token size limit
    if (ts->size_tracker + segment_len >= MAX_TOKEN_LIMIT) {
        // Run a greedy truncation step to save context space
        int remaining_allowed_space = MAX_TOKEN_LIMIT - ts->size_tracker - 5;
        if (remaining_allowed_space > 0) {
            strncat(ts->data_pool, text_segment, remaining_allowed_space);
            strcat(ts->data_pool, "[TRUNC]");
            ts->size_tracker = MAX_TOKEN_LIMIT;
            return 1; // Flag warning that truncation occurred
        }
        return -1; // Flag refusal to append due to context limit
    }
    
    strcat(ts->data_pool, text_segment);
    ts->size_tracker += segment_len;
    return 0; // Appended successfully without context issues
}

const char* expose_prompt(TokenStack* ts) { return ts->data_pool; }
