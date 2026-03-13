# Nano Banana 2

## Project Overview

Nano Banana 2 is an AI-powered image generation package that creates images from text descriptions. It supports text-to-image generation and image-to-image editing with reference images. The package provides flexible output options including multiple formats, aspect ratios, and resolutions.

## Block Capabilities

### Task Block: Nano Banana2 Image Generation

Generates AI images from text prompts. Supports image-to-image editing with reference URLs. Outputs image URLs and metadata including dimensions, file size, and content type.

**Key inputs:**
- `prompt` (required): Text description of desired image
- `image_urls` (optional): Reference images for editing (1-14 URLs)
- `num_images`: Number of images to generate (1-4)
- `aspect_ratio`: Output dimensions (auto, 21:9, 16:9, etc.)
- `output_format`: JPEG, PNG, or WebP
- `resolution`: 0.5K to 4K quality

### Subflow Block: Nano Banana2 Download

Generates images and automatically downloads them to local files. Combines image generation with batch download functionality. Outputs local file paths for further processing.

## Block Combination Suggestions

- **Content Creation Pipeline**: Use Nano Banana2 Download to generate images and save locally, then connect to image processing blocks for resizing or format conversion.
- **Batch Generation**: Generate multiple images with different seeds, then use array blocks to organize and process results.
- **Reference-Based Editing**: Provide reference image URLs to create variations or style transfers of existing images.

## Basic Usage

1. Enter a descriptive text prompt (be specific about style, subject, and composition)
2. Optionally add reference image URLs for guided generation
3. Select output format, aspect ratio, and resolution
4. Run the block to generate images
5. Use returned URLs or file paths for display or further processing

## Examples

**Text-to-Image Generation:**
```
Prompt: "A serene mountain lake at sunset with reflections in the water"
Output: Array of image URLs
```

**Image Editing with Reference:**
```
Prompt: "Transform this photo into watercolor style"
Reference URLs: ["https://example.com/photo.jpg"]
Output: Styled image URLs
```

**Download Generated Images:**
```
Use Nano Banana2 Download subflow
Prompt: "A futuristic city skyline at night"
Output: Local file paths of downloaded images
```