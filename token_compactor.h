#ifndef TOKEN_COMPACTOR_H
#define TOKEN_COMPACTOR_H

typedef struct TokenStack TokenStack;
TokenStack* init_stack_buffer();
int push_and_compact(TokenStack* ts, const char* text_segment);
const char* expose_prompt(TokenStack* ts);

#endif
