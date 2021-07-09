from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def get_summary(texts):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    try:
        print(f'using {device}')
        torch.cuda.empty_cache()
        model.to(device)
        torch.cuda.empty_cache()
        batch = tokenizer(texts, truncation=True, padding='longest', return_tensors="pt").to(device)
        torch.cuda.empty_cache()
        translated = model.generate(**batch, min_length=150, max_length=250)
        torch.cuda.empty_cache()
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text
    except RuntimeError:
        device = 'cpu'
        print(f'using {device}')
        model.to(device)
        batch = tokenizer(texts, truncation=True, padding='longest', return_tensors="pt").to(device)
        translated = model.generate(**batch, min_length=150, max_length=250)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text
