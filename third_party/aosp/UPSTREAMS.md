# AOSP / Android Open-Source Provenance

Chimera Mobile tracks Android Open Source Project components by upstream repository rather than vendoring the entire AOSP tree into `general`.

## Core upstreams

- platform/frameworks/base — Android framework classes/services
- platform/frameworks/native — native framework, Binder, graphics-facing infrastructure
- platform/system/core — init, libcutils, logging and core userspace infrastructure
- platform/art — Android Runtime (ART)
- platform/bionic — Android C library/dynamic linker
- platform/system/libhidl — legacy HAL infrastructure
- platform/hardware/interfaces — current HAL interfaces
- platform/packages/modules — modular system components
- platform/external/perfetto — tracing/performance instrumentation
- platform/external/boringssl — cryptography used by Android components

Official source index: https://android.googlesource.com/
Framework source: https://android.googlesource.com/platform/frameworks/base/

## Import policy

The importer records an upstream revision and copies only components whose licenses and dependency closure have been reviewed. Copyright notices and license files must remain with imported material. AOSP is Apache-2.0 for much of the platform, but individual files may have different notices/licenses; every imported subtree must therefore be audited rather than assumed equivalent.

The repository intentionally avoids a fake claim of having copied every AOSP repository. `tools/import_aosp_open_source.sh` provides a reproducible source acquisition path for a full AOSP checkout and for selected compatibility components.
