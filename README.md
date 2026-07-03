# TokenBuffer-RAG // Token-Aware Window Compactor

An active optimization utility managing string layouts via greedy stack allocators to prune contexts before sending them to high-cost LLM generation endpoints.

## Technical Execution
- **Context Compaction Stacks ($O(1)$ Allocations):** Evaluates character boundaries natively in C to avoid string processing overhead in Python.
- **Cost Minimization Middleware:** Drops low-priority trailing strings to keep API payloads lean.

## Launch Configurations
```bash
python token_aware_rag.py
