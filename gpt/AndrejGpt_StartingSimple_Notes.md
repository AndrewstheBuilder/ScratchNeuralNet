### Simplest model for language is a Bigram Model
```python
import torch
import torch.nn as nn
from torch.nn import functional as F
torch.manual_seed(1337) # for reproducibility

class BigramLanguageModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
        # each token directly reads off the logits for the next token from a lookup table
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx, targets):

        # idx and targets are both (B, T) tensor of integers
        logits = self.token_embedding_table(idx) # (B, T, C)
        B, T, C = logits.shape
        logits = logits,view(B*T, C)
        targets = targets.view(B*T) # Before view operation target is (B,T)
        loss = F.cross_entropy(logits, targets)

        return logits, loss
# Calling the model / running the training
m = BigramLanguageModel(vocab_size)
out = m(xb, yb)
print(out.shape)

# understanding the token_embedding_table()
# Say you printed out xb
print(xb)
[[24, 43, 58...]]
# At 24 you will get back the 24th row in the embedding table
# All of the rows are the size vocab_size which is also the channel(C)

#
# Understanding F.cross_entropy
#
# It is also known as the negative log likelihood loss
# This api expects B, C, T in its first input so we have to reshape our logits
# We can check if we are initializing the model well by checking the initial loss
# if the initial loss exceeds the probability of equal likely hood of chosing a character
# from the vocab size in our scenario it is 1/65 = 1/vocab_size you know that the init
# may have too much entropy

# Stopped at 28:54 he is about to go into the Bigram Model's generate function
```