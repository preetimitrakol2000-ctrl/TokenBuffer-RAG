from compactor_bridge import CompactorBridge

if __name__ == "__main__":
    compactor = CompactorBridge()

    print("=== TOKENBUFFER-RAG WINDOW COMPACTOR PIPELINE ===")
    
    # Push base threat records that fit within constraints
    compactor.append_context("System Event 1: Host isolated. ")
    compactor.append_context("System Event 2: Ports closed. ")

    # Push a large text string that exceeds token limits to trigger compression routines
    status = compactor.append_context("System Event 3: Detailed diagnostic logs containing heavy infrastructure memory mappings and network route path histories.")

    if status == 1:
        print("[!] Warning: Input text exceeded token limits. Greedy context pruning triggered.")
    
    final_output = compactor.retrieve_final_prompt_string()
    print(f"\n[Final Compiled Prompt Payload Passed to AI Engine]:\n -> {final_output}")
