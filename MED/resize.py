import os
from PIL import Image

args={
    'image_dir': '/ssd_scratch/cvit/ajoy/data/training_equation_images/',             #directory for train images
    'output_dir': '/ssd_scratch/cvit/ajoy/data/resize_training_equation_images/',     #diirectory for saving resized images
    'image_size': 224                                                # 256 size for image after processing for training images
}

def resize_image(image, size):
    """Resize an image to the given size."""
    return image.resize(size, Image.ANTIALIAS)

def resize_images(image_dir, output_dir, size):
    """Resize the images in 'image_dir' and save into 'output_dir'."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = os.listdir(image_dir)
    num_images = len(images)
    for i, image in enumerate(images):
        with open(os.path.join(image_dir, image), 'r+b') as f:
            with Image.open(f) as img:
                img = resize_image(img, size)
                img.save(os.path.join(output_dir, image), img.format)
        if i % 1000 == 0:
            print ("[%d/%d] Resized the images and saved into '%s'."
                   %(i, num_images, output_dir))

def main():
    image_dir = args['image_dir']
    output_dir = args['output_dir']
    image_size = [args['image_size'], args['image_size']]
    resize_images(image_dir, output_dir, image_size)


if __name__ == '__main__':
    main()
