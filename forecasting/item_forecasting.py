import torch
import pandas as pd
import torch.nn as nn

df = pd.read_csv("A:/spark_data/train.csv")

#All functions are implemented to reduce the complexity

class BiLSTM_CNN_Model(nn.Module):
    def __init__(self, input_size, sequence_length, hidden_size=64, lstm_layers=2, kernel_size=3, cnn_out_channels=32):
        super(BiLSTM_CNN_Model, self).__init__()
        self.sequence_length = sequence_length

        self.bilstm = nn.LSTM(input_size=input_size,
                              hidden_size=hidden_size,
                              num_layers=lstm_layers,
                              batch_first=True,
                              bidirectional=True)

        self.cnn = nn.Conv1d(in_channels=2*hidden_size,
                             out_channels=cnn_out_channels,
                             kernel_size=kernel_size)

        self.relu = nn.ReLU()
        cnn_output_seq_len = sequence_length - kernel_size + 1
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(cnn_out_channels * cnn_output_seq_len, 1)

    def forward(self, x):
        lstm_out, _ = self.bilstm(x)  # [B, T, F]
        lstm_out = lstm_out.permute(0, 2, 1)  # [B, F, T]
        cnn_out = self.relu(self.cnn(lstm_out))  # [B, C, T']
        out = self.flatten(cnn_out)
        return self.fc(out)
    

def get_last_sequence(df, store, item, sequence_length):
    group = df[(df['store'] == store) & (df['item'] == item)]
    group = group.sort_values('date')
    
    sales = group['sales'].values

    if len(sales) < sequence_length:
        raise ValueError("Not enough data for prediction")

    max_val = sales.max()
    if max_val == 0:
        return None  # no prediction for zero sales, base case:)

    sales = sales / max_val  

    last_seq = sales[-sequence_length:]
    return torch.tensor(last_seq.reshape(1, sequence_length, 1), dtype=torch.float32), max_val


#model instance
model = BiLSTM_CNN_Model(input_size=1, sequence_length=14)
model.load_state_dict(torch.load('A:/spark/model/bilstm_cnn_model.pth'))
model.eval()

def predict_sales(store, item, model= model, df= df, sequence_length= 14):
    try:
        x_tensor, max_val = get_last_sequence(df, store, item, sequence_length)
        model.eval()
        with torch.no_grad():
            pred = model(x_tensor).item()
        return pred * max_val  # reverse normalization
    except ValueError as e:
        print(f"{e} for ({store}, {item})")
        return None


