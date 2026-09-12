# Flutter frontend

This layer provides the cross-platform workspace shell: project navigation, modeling/sculpting/animation/VFX tool selection and shared scene-session state.

The production renderer is supplied by a native/plugin bridge rather than reimplementing a full DCC renderer in Dart. Web builds can use the browser viewport directly.
