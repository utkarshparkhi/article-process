from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


def get_onel(text):
    model_name = 'google/pegasus-xsum'
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    try:
        print(f'using {device}')
        torch.cuda.empty_cache()
        model.to(device)
        torch.cuda.empty_cache()
        batch = tokenizer(text, truncation=True, padding='longest', return_tensors="pt").to(device)
        torch.cuda.empty_cache()
        translated = model.generate(**batch, min_length=50, max_length=100)
        torch.cuda.empty_cache()
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text
    except RuntimeError:
        device = 'cpu'
        print(f'using {device}')
        model.to(device)
        batch = tokenizer(text, truncation=True, padding='longest', return_tensors="pt").to(device)
        translated = model.generate(**batch, min_length=50, max_length=100)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text
