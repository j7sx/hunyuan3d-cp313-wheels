import os
import sys
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import torch

torch_version = torch.__version__.split('+')[0].replace('.', '')
if torch.version.cuda is not None:
    cuda_version = "cuda"+torch.version.cuda.replace('.', '')
elif getattr(torch.version, 'hip', None) is not None:
    cuda_version = "rocm" + torch.version.hip.replace('.','')

version = f"0.1.0+torch{torch_version}.{cuda_version}"

nvcc_args = []
cxx_args = []
if os.name == 'nt':
    nvcc_args += ['-Xcompiler', '/Zc:preprocessor', '-Xcompiler', '/std:c++20']
    cxx_args += ['/std:c++20', '/Zc:preprocessor']

class CustomBuildExt(BuildExtension):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = dict(ext.extra_compile_args or {})
            ext.extra_compile_args['cxx'] = list(ext.extra_compile_args.get('cxx', [])) + cxx_args
            ext.extra_compile_args['nvcc'] = list(ext.extra_compile_args.get('nvcc', [])) + nvcc_args
        super().build_extensions()

custom_rasterizer_module = CUDAExtension('custom_rasterizer_kernel', [
    'lib/custom_rasterizer_kernel/rasterizer.cpp',
    'lib/custom_rasterizer_kernel/grid_neighbor.cpp',
    'lib/custom_rasterizer_kernel/rasterizer_gpu.cu',
], extra_compile_args={
    'cxx': cxx_args,
    'nvcc': nvcc_args,
})

setup(
    packages=find_packages(),
    version=version,
    name='custom_rasterizer',
    include_package_data=True,
    package_dir={'': '.'},
    ext_modules=[
        custom_rasterizer_module,
    ],
    cmdclass={
        'build_ext': CustomBuildExt
    },
)