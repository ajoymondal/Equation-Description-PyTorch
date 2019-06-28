import torch
import matplotlib.pyplot as plt
import numpy as np 
import argparse
import pickle 
import os
from torch.autograd import Variable 
from torchvision import transforms 
from build_vocab import Vocabulary
from model import EncoderCNN, DecoderRNN
from PIL import Image
    
args = {
    'image_path': '/ssd_scratch/cvit/ajoy/data/resize_test_ncrt_equation_images_class5',   # input image for generating caption for validation set
    'encoder_path': '/ssd_scratch/cvit/ajoy/data/ResNet50_finetune_attention_lstm_class5_node35/encoder_resnet50_finetune_attention_lstm_class5_node35.pkl',         # path for trained encoder
    'decoder_path': '/ssd_scratch/cvit/ajoy/data/ResNet50_finetune_attention_lstm_class5_node35/decoder_resnet50_finetune_attention_lstm_class5_node35.pkl',         # path for trained decoder
    'vocab_path': '/ssd_scratch/cvit/ajoy/data/vocab.pkl',                            # path for vocabulary wrapper
    'generate_caption_path': '/ssd_scratch/cvit/ajoy/data/ResNet50_finetune_attention_lstm_class5_node35_generate_caption/',
    # Model parameters (should be same as paramters in train.py)
    'crop_size': 224,
    'embed_size': 256,                  #dimension of word embedding vectors
    'hidden_size': 512,                 #dimension of lstm hidden states
    'num_layers': 1,                    #number of layers in lstm
    'batch_size': 1,                    #no of batches 
    'num_workers': 1                    #no of worker
}

def load_image(image_path, transform=None):
    image = Image.open(image_path)
    #image = image.convert("RGB") 
    image = image.resize([args['crop_size'], args['crop_size']], Image.LANCZOS)
    if transform is not None:
        image = transform(image).unsqueeze(0)

    return image
    
def main():

    #write predicted caption
    if not os.path.exists(args['generate_caption_path']):
        os.makedirs(args['generate_caption_path'])

    caption_string = os.path.join(args['generate_caption_path'], "caption_ncrt_class5.txt")   
    #mode = "a" if os.path.exists(caption_string) else "w"
    fp =open(caption_string, "w+")
    
    # Image preprocessing
    transform = transforms.Compose([
        transforms.ToTensor(), 
        transforms.Normalize((0.9638, 0.9638, 0.9638), 
                             (0.1861, 0.1861, 0.1861))])
    
    # Load vocabulary wrapper
    with open(args['vocab_path'], 'rb') as f:
        vocab = pickle.load(f)

    # Build Models
    encoder = EncoderCNN(args['embed_size'])
    encoder.eval()  # evaluation mode (BN uses moving mean/variance)
    decoder = DecoderRNN(args['embed_size'], args['hidden_size'], 
                         len(vocab), args['num_layers'], max_seq_length=50)
    decoder.eval()
    

    # Load the trained model parameters
    encoder.load_state_dict(torch.load(args['encoder_path']))
    decoder.load_state_dict(torch.load(args['decoder_path']))
    
    # If use gpu
    if torch.cuda.is_available():
        encoder.cuda()
        decoder.cuda()
    
    # Prepare Image
    image_dir = args['image_path']
    images = os.listdir(image_dir)
    i = 1
    for image_id in images:
        #print('i->',i)
        #i = i+1  
        if not image_id.endswith('.jpg'):
            continue
        image = os.path.join(image_dir, image_id)
        image = load_image(image, transform)
        image_tensor = image.cuda()
        
        # Generate caption from image
        try:
            feature, cnn_features = encoder(image_tensor)
            sampled_ids = decoder.sample(feature, cnn_features)
            sampled_ids = sampled_ids.cpu().data.numpy()
        except:
              continue
        #print('image_ids->',image_id)      
        # Decode word_ids to words
        sampled_caption = []
        for word_id in sampled_ids:
            word = vocab.idx2word[word_id]
            sampled_caption.append(word)
            if word == '<end>':
                break
        sentence = ' '.join(sampled_caption)
        print ('i->', i, image_id + '\t' + sentence)
        fp.write(image_id)
        fp.write('\t')
        fp.write(sentence)
        if i<398:
           fp.write("\n")
        i = i+1         
        
    fp.close()

if __name__ == '__main__':
    main()
