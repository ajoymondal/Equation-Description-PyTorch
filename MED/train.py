import argparse
import torch
import torch.nn as nn
import numpy as np
import os
import pickle
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from data_loader import get_loader 
from build_vocab import Vocabulary
from model import EncoderCNN, DecoderRNN 
from torch.autograd import Variable 
from torch.nn.utils.rnn import pack_padded_sequence
from torchvision import transforms

#for visualize attention weights
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import matplotlib.ticker as ticker

args = {
    'model_path': '/ssd_scratch/cvit/ajoy/data/ResNet50_finetune_attention_lstm_node08/',    #path for saving trained models # actual model is saved in modles but for testing purpose models1
    'crop_size':  224,                                                                 #size for randomly cropping images
    'vocab_path': '/ssd_scratch/cvit/ajoy/data/vocab.pkl',                             #path for vocabulary wrapper
    'image_dir': '/ssd_scratch/cvit/ajoy/data/resize_training_equation_images/',                       #directory for resized images
    'caption_path': '/ssd_scratch/cvit/ajoy/data/annotations/captions_train.json', #path for train annotation json file
    'log_step': 10000,                                                                   #step size for prining log info
    'save_step': 10000,                                                                 #step size for saving trained models
    # Model parameters 
    'weight_decay':0.0001,                            #optional parameter
    'momentum': 0.5,                                  #optional parameter                                          
    'embed_size': 256,                                 #dimension of word embedding vectors 256 // 512 and 1024 // 512 and 512 // 256 and 512
    'hidden_size':512,                                #dimension of lstm hidden states 512
    'num_layers': 1,                                   #number of layers in lstm 1
    'num_epochs': 1,                                  #no of epoch for learning #best parameter 30
    'batch_size': 10,                                  #no of batches 128
    'num_workers': 1,                                 #no of worker  2            
    'learning_rate': 0.0001                             #learning rate for training 0.001
}

  
def main():
    
    min_train_loss = 100.0 
    # Create model directory
    if not os.path.exists(args['model_path']):
        os.makedirs(args['model_path'])

    fp_loss = open(args['model_path']+'training_loss_resnet50_finetune_attention_lstm_node08.txt','w+')     
    

    # Image preprocessing
    transform = transforms.Compose([ 
        transforms.RandomCrop(args['crop_size']),
        transforms.RandomHorizontalFlip(), 
        transforms.ToTensor(), 
        transforms.Normalize((0.9638, 0.9638, 0.9638), 
                             (0.1861, 0.1861, 0.1861))])
    # Load vocabulary wrapper.
    with open(args['vocab_path'], 'rb') as f:
        vocab = pickle.load(f)
    
    # Build data loader
    data_loader = get_loader(args['image_dir'], args['caption_path'], vocab, 
                             transform, args['batch_size'],
                             shuffle=True, num_workers=args['num_workers']) 
    
    
    # Build the models
    encoder = EncoderCNN(args['embed_size'])
    decoder = DecoderRNN(args['embed_size'], args['hidden_size'], 
                         len(vocab), args['num_layers'], max_seq_length=50)
    
    if torch.cuda.is_available():
        encoder.cuda()
        decoder.cuda()

    # Loss and Optimizer
    criterion = nn.CrossEntropyLoss()
    params = list(decoder.parameters()) + list(encoder.linear.parameters()) + list(encoder.bn.parameters())
    optimizer = torch.optim.Adam(params, lr=args['learning_rate']) #original optimizer
     
    # Train the Models
    total_step = len(data_loader)
    total = 1
    for epoch in range(args['num_epochs']):
        for i, (images, captions, lengths) in enumerate(data_loader):
            
            # Set mini-batch dataset
            images = images.cuda()      
            captions = captions.cuda()  
            targets = pack_padded_sequence(captions, lengths, batch_first=True)[0]
            
            # Forward, Backward and Optimize
            decoder.zero_grad()
            encoder.zero_grad()
            features, cnn_features = encoder(images)
            outputs = decoder(features, cnn_features, captions, lengths)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            
            fp_loss.write(str(total))
            fp_loss.write("\t") 
            fp_loss.write(str(loss.item()))
            fp_loss.write("\n")
            
            total = total+1
            
            # Print log info
            if i % args['log_step'] == 0:
                print('Epoch [%d/%d], Step [%d/%d], training-loss: %.4f'
                      %(epoch, args['num_epochs'], i, total_step, 
                        loss.item())) 
           
            if min_train_loss > loss.item():
                min_train_loss = loss.item()
                torch.save(decoder.state_dict(),os.path.join(args['model_path'],'decoder_resnet50_finetune_attention_lstm_node08.pkl'))
                torch.save(encoder.state_dict(), os.path.join(args['model_path'],'encoder_resnet50_finetune_attention_lstm_node08.pkl'))

      
    fp_loss.close()
       
                 
if __name__ == '__main__':
      main()
