# Interchange pipeline

The pipeline is deliberately adapter-based.

- **OpenUSD / USDZ:** canonical collaborative scene interchange; time samples, layers, variants and composition are handled by an OpenUSD adapter.
- **glTF:** runtime/web/mobile asset interchange for meshes, materials, skins and animations.
- **Alembic:** cache interchange for baked geometry and animation.
- **MaterialX:** material graph interchange.
- **OpenColorIO/OpenImageIO:** color transforms and image I/O.
- **OpenVDB:** sparse volumetric data and simulation caches.

The core scene model never requires these libraries to compile. Production builds can enable adapters through CMake/package discovery, keeping licensing and deployment choices explicit.
