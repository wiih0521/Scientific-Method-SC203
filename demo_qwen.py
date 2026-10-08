"""
Script demo chạy thử mô hình Qwen2.5-Math trên GPU RTX 4060 (8GB VRAM)
Model đề xuất: Qwen/Qwen2.5-Math-1.5B-Instruct (nhẹ, nhanh, chuẩn bị cho thuật toán CS-OS)
"""

import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():
    print("=" * 60)
    print("1. Kiểm tra phần cứng GPU:")
    print(f"   - GPU: {torch.cuda.get_device_name(0)}")
    print(f"   - VRAM khả dụng: {round(torch.cuda.get_device_properties(0).total_memory / (1024**3), 2)} GB")
    print("=" * 60)

    model_id = "Qwen/Qwen2.5-Math-1.5B-Instruct"
    print(f"\n2. Đang nạp mô hình [{model_id}] vào GPU...")
    start_load = time.time()
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="cuda"
    )
    print(f"   -> Nạp xong sau {round(time.time() - start_load, 2)}s!")
    print(f"   -> VRAM đang dùng: {round(torch.cuda.memory_allocated() / (1024**3), 2)} GB / 8.0 GB")

    # Câu hỏi mẫu kiểm tra suy luận toán học (chuẩn GSM8K)
    question = (
        "Janet’s ducks lay 16 eggs per day. She eats three for breakfast every morning "
        "and bakes muffins for her friends every day with four. She sells the remainder "
        "at the farmers' market daily for $2 per fresh duck egg. How much in dollars "
        "does she make every day at the farmers' market?"
    )
    
    print("\n3. Thử nghiệm sinh lời giải (Chain-of-Thought):")
    print(f"   [Câu hỏi]: {question}\n")

    messages = [
        {"role": "system", "content": "Please reason step by step, and put your final answer within \\boxed{}."},
        {"role": "user", "content": question}
    ]
    prompt_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer([prompt_text], return_tensors="pt").to("cuda")

    start_gen = time.time()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.7,
            do_sample=True,
            top_p=0.9
        )
    gen_time = time.time() - start_gen

    generated_tokens = len(outputs[0]) - len(inputs.input_ids[0])
    speed = round(generated_tokens / gen_time, 2)
    response = tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], skip_special_tokens=True)

    print("=" * 60)
    print("4. Kết quả sinh từ Qwen2.5-Math:")
    print(response)
    print("=" * 60)
    print(f"-> Thống kê hiệu năng: Sinh {generated_tokens} tokens trong {round(gen_time, 2)}s (~{speed} tokens/s).")
    print("-> Sẵn sàng để tích hợp vào vòng lặp thuật toán dừng tối ưu CS-OS!")

if __name__ == "__main__":
    main()
