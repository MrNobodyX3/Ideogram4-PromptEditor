# Ideogram 4.0 ComfyUI Tools

Custom nodes and workflow for [Ideogram 4.0](https://huggingface.co/Comfy-Org/Ideogram-4) in ComfyUI.

## Custom Nodes

### Aspect Ratio Calculator
Calculates width and height from an aspect ratio and max size, snapping to multiples of 8.

| Input | Type | Default |
|-------|------|---------|
| ratio_x | INT | 16 |
| ratio_y | INT | 9 |
| max_size | INT | 2048 |

**Outputs:** width (INT), height (INT)

### Seed Generator
Flexible seed node with four modes.

| Input | Type | Default |
|-------|------|---------|
| seed | INT | 0 |
| mode | [fixed, random, step, phrase] | fixed |
| phrase | STRING (optional) | "" |

**Modes:**
- **fixed** — outputs the input seed as-is
- **random** — generates a random 64-bit seed each run
- **step** — increments the input seed by 1 each run
- **phrase** — hashes the input string via SHA-256 to produce a deterministic seed

**Outputs:** seed (INT)

## Installation

### Custom Nodes
Copy or symlink the `custom_nodes/` folder into your ComfyUI installation:

```bash
# From your ComfyUI directory
cp -r /path/to/Ideogram/custom_nodes/* ./custom_nodes/
```

Or symlink for live updates:

```bash
ln -s /path/to/Ideogram/custom_nodes/* ./custom_nodes/
```

Restart ComfyUI after installing. The nodes will appear in the **utilities** category.

### Workflow
Load `workflows/ideogram4_workflow.json` in ComfyUI via **Load** or drag-and-drop onto the canvas.

## Required Models

Download these into your ComfyUI `models/` directory:

| Model | Location |
|-------|----------|
| [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) | `models/vae/` |
| [ideogram4_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_fp8_scaled.safetensors) | `models/diffusion_models/` |
| [ideogram4_unconditional_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_unconditional_fp8_scaled.safetensors) | `models/diffusion_models/` |
| [qwen3vl_8b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) | `models/text_encoders/` |
| [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) | `models/text_encoders/` |
