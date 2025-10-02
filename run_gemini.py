import sys, os
import time
import warnings
from tqdm import tqdm

from google import genai

prompts_file = sys.argv[1]
try:
    with open(prompts_file, 'r', encoding='utf-8') as f:
        prompts = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    warnings.warn("file not found")
    exit()

if not prompts:
    warnings.warn("file empty")

system_prompt = ""
if len(sys.argv) > 2:
    system_prompt_file = sys.argv[2]
    with open(system_prompt_file, 'r', encoding='utf-8') as f:
        system_prompt = "Instruction:\n"
        system_prompt += f.read()
        system_prompt += "\n\nQuestion:\n"
    warnings.warn("system_prompt loaded")


client = genai.Client()

for i, prompt in enumerate(tqdm(prompts)):
    for i in range(10):
        try:
            warnings.warn("prompting: " + system_prompt+prompt)
            response = client.models.generate_content(
                 model="gemma-3-27b-it",
                 contents=system_prompt+prompt,
            )
            print(response.text)
            break
        except Exception as e:
            warnings.warn(f"<ERROR> {e}")
            time.sleep(8)
    print("=====<End of Answer>=====")

    if i < len(prompts) - 1:
        time.sleep(8)
