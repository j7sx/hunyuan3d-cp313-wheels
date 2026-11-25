# hunyuan3d-cp313-wheels

Prebuilt `custom_rasterizer` wheel for ComfyUI-Hunyuan3DWrapper compiled for Python 3.13 and CUDA 13.0 (related to Issue #213).

## Important Limitation

This prebuilt wheel will work **only if all parameters match**:

| Parameter | Value |
|-----------|-------|
| OS | Windows x64 |
| Python | 3.13 (cp313) |
| PyTorch | 2.14.0+cu130 |
| CUDA | 13.0 (built with CUDA 13.5 toolkit, compatible with torch cu130) |

If you have a different version of Python, PyTorch, or CUDA, this `.whl` will not work and you will need to compile it from source.

## Quick Installation (Portable ComfyUI)

1. Download the wheel file from the **[Releases](https://github.com/j7sx/hunyuan3d-cp313-wheels/releases/tag/v0.1.0)** section of this repository.
2. Place it in your portable ComfyUI root folder.
3. Run:

```powershell
python_embeded\python.exe -m pip install custom_rasterizer-0.1.0+torch2140.cuda130-cp313-cp313-win_amd64.whl
4. Restart ComfyUI.

## Building from Source (for other PyTorch / CUDA versions)

If your environment differs from the table above, you can build the wheel yourself using the modified setup script:

1. Download `setup_fixed_for_py313.py` from this repository.
2. Copy it into `ComfyUI\custom_nodes\comfyui-hunyuan3dwrapper\hy3dgen\texgen\custom_rasterizer` and rename it to `setup.py` (replacing the original file).
3. Open a terminal in that folder and run:

```powershell
E:\ComfyUI_windows_portable_nvidia\ComfyUI_windows_portable\python_embeded\python.exe setup.py bdist_wheel
```

4. Install the generated `.whl` file from the `dist` folder.

## About

Prebuilt `custom_rasterizer` wheel for ComfyUI-Hunyuan3DWrapper (Python 3.13, PyTorch 2.14.0+cu130, Windows x64).
