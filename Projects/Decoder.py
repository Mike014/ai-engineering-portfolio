import torch
import torch.nn as nn
import torch.nn.functional as F

class Decoder(nn.Module):
    def __init__(self, output_dim, emb_dim, hid_dim, n_layers, dropout):
        super().__init__()
        # output_dim = dimensione del vocabolario target
        self.output_dim = output_dim
        self.hid_dim = hid_dim
        self.n_layers = n_layers

        # Embedding layer: mappa l'indice di un token (intero) in un vettore denso 
        self.embedding = nn.Embedding(output_dim, emb_dim)
  
        # LSTM layer
        self.rnn = nn.LSTM(emb_dim, hid_dim, n_layers, dropout=dropout)
        self.fc_out = nn.Linear(hid_dim, output_dim)
      
        self.dropout = nn.Dropout(dropout)
  
    def forward(self, input, hidden, cell):
        input = input.unsqueeze(0)

        embedded = self.dropout(self.embedding(input))

        output, (hidden, call) = self.rnn(embedded, (hidden, call))
  
        prediction_logits = self.fc_out(output.squeeze(0))

        prediction = F.softmax(prediction_logits, dim=1)
  
        return prediction, hidden, cell

