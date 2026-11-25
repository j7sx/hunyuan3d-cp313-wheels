
hunyuan3d-cp313-wheels

Prebuilt custom_rasterizer wheel for ComfyUI-Hunyuan3DWrapper compiled for Python 3.13 and CUDA 13.0 (related to Issue #213).

Important Limitation

This prebuilt wheel will work only if all parameters match:

Parameter	Value
OS	Windows x64
Python	3.13 (cp313)
PyTorch	2.14.0+cu130
CUDA	13.0 (built with CUDA 13.5 toolkit, compatible with torch cu130)

If you have a different version of Python, PyTorch, or CUDA, this .whl will not work and you will need to compile it from source.

Quick Installation (Portable ComfyUI)

1. Download the wheel file from this repository:
github.com (click View raw or Download).
2. Place it in your portable ComfyUI root folder and run:
python_embeded\python.exe -m pip install custom_rasterizer-0.1.0+torch2140.cuda130-cp313-cp313-win_amd64.whl

Building from Source (for other PyTorch / CUDA versions)

If your environment differs from the table above, you can build the wheel yourself using the modified setup script:
github.com
1. Download setup_fixed_for_py313.py from the link above.
2. Copy it into ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\hy3dgen\texgen\custom_rasterizer\ and rename it to setup.py (replacing the original file).
3. Open a terminal in that folder and run:
..\..\..\..\..\python_embeded\python.exe setup.py bdist_wheel
4. Install the generated .whl file from the dist\ folder.
