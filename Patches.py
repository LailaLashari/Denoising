import os
import cv2
import numpy as np
from tqdm import tqdm

# Directories for input noisy and clean images
noisy_images_dir = '/Users/lashari/Downloads/Final_DN_Traning/DSENet/dataset/NIND/input'
clean_images_dir = '/Final_DN_Traning/DSENet/dataset/NIND/groundtruth'

# Directories to save patches
noisy_patches_dir = '/Final_DN_Traning/DSENet/dataset/NIND/NIND_patches/input'
clean_patches_dir = '/Final_DN_Traning/DSENet/dataset/NIND/NIND_patches/groundtruth'

# Patch size and stride
patch_size = 256
stride = 64

# Create directories if they don't exist
os.makedirs(noisy_patches_dir, exist_ok=True)
os.makedirs(clean_patches_dir, exist_ok=True)

def create_patches(image, patch_size, stride):
    patches = []
    h, w, _ = image.shape
    for i in range(0, h - patch_size + 1, stride):
        for j in range(0, w - patch_size + 1, stride):
            patch = image[i:i + patch_size, j:j + patch_size]
            patches.append(patch)
    return patches

# Get list of images
noisy_images = sorted([f for f in os.listdir(noisy_images_dir) if f.endswith(('.png', '.jpg'))], key=lambda x: (int(''.join(filter(str.isdigit, x)) or 0), x))
clean_images = sorted([f for f in os.listdir(clean_images_dir) if f.endswith(('.png', '.jpg'))], key=lambda x: (int(''.join(filter(str.isdigit, x)) or 0), x))

# Ensure the number of noisy and clean images match
assert len(noisy_images) == len(clean_images), "Number of noisy and clean images do not match."

# Create patches from images
for noisy_image_name, clean_image_name in tqdm(zip(noisy_images, clean_images), total=len(noisy_images)):
    # Load noisy and clean images
    noisy_image_path = os.path.join(noisy_images_dir, noisy_image_name)
    clean_image_path = os.path.join(clean_images_dir, clean_image_name)
    
    noisy_image = cv2.imread(noisy_image_path)
    clean_image = cv2.imread(clean_image_path)
    
    # Check if images are loaded correctly
    if noisy_image is None or clean_image is None:
        print(f"Failed to load image: {noisy_image_name}")
        continue
    
    # Ensure image dimensions match
    if noisy_image.shape != clean_image.shape:
        print(f"Dimension mismatch for {noisy_image_name}: Noisy image shape: {noisy_image.shape}, Clean image shape: {clean_image.shape}")
        continue
    
    # Create patches
    noisy_patches = create_patches(noisy_image, patch_size, stride)
    clean_patches = create_patches(clean_image, patch_size, stride)
    
    # Ensure the number of patches match
    if len(noisy_patches) != len(clean_patches):
        print(f"Number of patches do not match for {noisy_image_name}")
        continue
    
    # Save patches
    for idx, (noisy_patch, clean_patch) in enumerate(zip(noisy_patches, clean_patches)):
        noisy_patch_filename = f"{noisy_image_name.split('.')[0]}_patch_{idx:04d}.png"
        clean_patch_filename = f"{clean_image_name.split('.')[0]}_patch_{idx:04d}.png"
        
        cv2.imwrite(os.path.join(noisy_patches_dir, noisy_patch_filename), noisy_patch)
        cv2.imwrite(os.path.join(clean_patches_dir, clean_patch_filename), clean_patch)

print("Patches created successfully!")
