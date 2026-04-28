---
name: nano-banana-2
description: Use Nano Banana 2 for virtual try-on, scene image editing, ad placement, object insertion, retouching, and style-driven image creation.
metadata:
  title: Nano Banana 2
---

# Nano Banana 2

## Trigger Guidance

- Use this skill when the user wants to generate or edit images with `nano-banana-2`.
- Best-fit scenarios include e-commerce outfit replacement, in-scene compositing, image retouching, and style image creation.
- Prefer this skill when the request is centered on visual transformation from prompt plus one or more reference images.

## Supported Use Cases

- **E-commerce virtual try-on**: replace clothing on a person while preserving pose, body proportion, lighting, and product details.
- **Real-scene secondary creation**: place billboards, posters, signage, props, furniture, decorations, or new structures into an existing environment.
- **Photo retouching / compositing**: remove, replace, add, or adjust visual elements in a realistic way.
- **Style image creation**: restyle an image or create a new visual with a specific look, mood, composition direction, or brand aesthetic.

## Inputs

- A clear editing or generation prompt.
- Optional reference image URLs when the task depends on an existing person, product, scene, or source artwork.
- Optional constraints such as aspect ratio, output format, resolution, visual realism, brand tone, or how strictly to preserve the original composition.

## Expected Output

- One or more generated images aligned with the prompt and any provided references.
- For editing requests, outputs should preserve the important unchanged parts of the source image unless the user explicitly asks to alter them.
- When relevant, include a short note describing what was changed and what was intentionally preserved.

## Dependencies

- Use `oo::nano-banana-2::nano-banana2-image-generate` as the verified execution block.
- This block is a verified subflow in the `nano-banana-2` package for prompt-based image generation with automatic download to local files.

## Recommended Prompting Pattern

1. State the core task first: generate, replace, add, remove, restyle, or composite.
2. Specify the subject that must stay consistent: person, garment, scene, product, architecture, perspective, or lighting.
3. Describe the exact change.
4. Add quality constraints such as realism, clean edges, natural shadows, correct scale, readable placement, and brand-safe styling.
5. If references are provided, say how each reference should be used.

## Steps

1. Classify the request as generation, edit, virtual try-on, scene insertion, retouching, or style creation.
2. Collect the prompt and any reference image URLs.
3. Rewrite the user intent into a precise visual instruction when the original wording is too vague.
4. Run `oo::nano-banana-2::nano-banana2-image-generate` with the final prompt and relevant image references.
5. Review the result for subject consistency, realism, placement accuracy, and unwanted artifacts.
6. If needed, refine the prompt and regenerate with tighter instructions.

## Use-Case Guidance

### 1. E-commerce Virtual Try-On

- Keep the model's face, pose, body shape, and camera angle unchanged unless requested otherwise.
- Describe the target garment precisely: category, fabric, color, silhouette, pattern, logo placement, sleeve length, and fit.
- Ask for realistic wrinkles, seams, lighting, and shadows so the clothing appears naturally worn.
- If a product image is provided, instruct the model to preserve the product's key commercial details.

Example prompt:

`Replace the model's current outfit with a beige oversized trench coat layered over a white shirt and black tailored trousers. Keep the person's face, pose, body proportion, background, and studio lighting unchanged. Preserve realistic fabric folds, clean edges, accurate sleeve structure, and premium e-commerce styling.`

### 2. Real-Scene Ad Placement

- Identify the exact mounting surface or physical location for the billboard, poster, or campaign visual.
- Require correct perspective, realistic scale, surface alignment, and lighting consistency.
- State whether the inserted graphic should look printed, mounted, pasted, backlit, or freestanding.

Example prompt:

`Place a large illuminated campaign billboard on the blank wall to the right side of the street scene. Match the camera perspective and nighttime lighting. Make it look like a professionally installed outdoor advertisement with natural reflections and realistic edge integration.`

### 3. Real-Scene Object Insertion

- Describe the new object, its material, size, placement, and relationship to the environment.
- Request believable occlusion, shadows, and contact with the ground or surrounding objects.
- Mention whether the result should look architectural, temporary, decorative, or product-demo oriented.

Example prompt:

`Add a modern white information kiosk near the walkway entrance of the campus. Keep the existing buildings and trees unchanged. Match daylight, perspective, and scale. The kiosk should cast a natural shadow and look permanently installed.`

### 4. Retouching / P-Image Editing

- Be explicit about what to remove, replace, enhance, or clean up.
- Mention which areas must remain untouched.
- Ask for seamless blending and no visible editing traces when realism matters.

Example prompt:

`Remove the distracting parked cars from the background, clean the pavement, and slightly enhance the storefront lighting. Keep the people, building facade, and overall composition unchanged. Make the edit look natural and unedited.`

### 5. Style Image Creation

- Specify the desired style with enough detail: editorial, cinematic, minimalist luxury, illustrated, futuristic, or warm lifestyle.
- If based on an existing image, state what should remain structurally consistent and what may be stylized.
- Add composition and color-direction hints when the mood matters.

Example prompt:

`Transform this café street photo into a cinematic editorial style image with warm late-afternoon tones, stronger contrast, elegant storefront highlights, and refined premium-brand mood. Preserve the street layout and main objects while upgrading the atmosphere.`

## Edge Cases

- If the user asks for editing but provides no source image or image URL, ask for the required reference image first.
- If the prompt is ambiguous about what should be preserved versus changed, clarify that boundary before execution.
- If brand assets, posters, or products must remain faithful, ask for the clean source asset rather than guessing from a low-quality screenshot.
- If the result needs exact text rendering on signage, note that generated images may require iteration or a downstream manual design pass for pixel-perfect typography.
- If the request combines multiple changes, split the instructions into ordered constraints so the main subject remains stable.
