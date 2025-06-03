from datasets import load_dataset
from trl import SFTConfig, SFTTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig

# Load dataset
dataset = load_dataset("trl-lib/Capybara", split="train")

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-125m"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Add padding token if it doesn't exist
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Preprocess the dataset to convert messages to text format
def convert_to_text(example):
    conversations = []
    for messages in example["messages"]:
        conversation = ""
        for message in messages:
            role = message["role"]
            content = message["content"]
            conversation += f"{role.capitalize()}: {content}\n"
        conversations.append(conversation.strip())
    
    return {"text": conversations}

# Convert the dataset - this removes the "messages" column that triggers chat template logic
dataset = dataset.map(convert_to_text, batched=True, remove_columns=dataset.column_names)

print(f"Dataset converted. Sample text: {dataset[0]['text'][:200]}...")

# Configure quantization properly
quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto",
)

# Resize token embeddings if needed
model.resize_token_embeddings(len(tokenizer))

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["c_attn", "c_proj"],  # GPT-Neo specific modules
)

# Training configuration
training_args = SFTConfig(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    logging_steps=10,
    save_steps=100,
    max_seq_length=512,
    packing=False,
)

# Create trainer - no custom formatting needed since we preprocessed the data
trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    args=training_args,
    peft_config=peft_config,
    processing_class=tokenizer,
)

if __name__ == "__main__":
    trainer.train()