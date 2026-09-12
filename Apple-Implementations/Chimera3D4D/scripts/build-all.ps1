$ErrorActionPreference='Stop'
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel
ctest --test-dir build --output-on-failure
if (Get-Command flutter -ErrorAction SilentlyContinue) { Push-Location flutter; flutter pub get; flutter build web; Pop-Location }
if (Get-Command npm -ErrorAction SilentlyContinue) { Push-Location web; npm install; npm run build; Pop-Location }
