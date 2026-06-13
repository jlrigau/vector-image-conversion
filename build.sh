#!/usr/bin/env bash
# Regenerate the distributed logo and all raster declinations from source.
# Requires: python3, Inkscape, ImageMagick, npx (svgo). Open Sans Bold must be
# installed so the text renders correctly before it is outlined.
set -euo pipefail
cd "$(dirname "$0")"

SVG=socamett-logo.svg
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

echo "1/5  Generate SVG from measurements (build_logo.py)"
python3 build_logo.py >/dev/null

echo "2/5  Outline text to paths (font-independent)"
inkscape "$SVG" --export-type=svg --export-text-to-path --export-plain-svg \
  --export-filename="$tmp/outlined.svg" >/dev/null 2>&1
mv "$tmp/outlined.svg" "$SVG"

echo "3/5  Optimise with svgo"
npx --yes svgo --config svgo.config.mjs -i "$SVG" -o "$SVG" >/dev/null

echo "4/5  Export PNG (transparent + white) and JPEG declinations"
mkdir -p logos
for w in 512 1065 2130 4260; do
  inkscape "$SVG" --export-type=png --export-width="$w" --export-background-opacity=0 \
    --export-filename="logos/socamett-logo_${w}_transparent.png" >/dev/null 2>&1
  magick "logos/socamett-logo_${w}_transparent.png" -background white -flatten \
    "logos/socamett-logo_${w}_white.png"
done
for w in 1065 2130 4260; do
  magick "logos/socamett-logo_${w}_white.png" -quality 92 "logos/socamett-logo_${w}.jpg"
done

echo "5/5  Export print formats (vector PDF, EPS, CMYK PDF)"
mkdir -p print
inkscape "$SVG" --export-type=pdf --export-filename=print/socamett-logo.pdf >/dev/null 2>&1
inkscape "$SVG" --export-type=eps --export-filename=print/socamett-logo.eps >/dev/null 2>&1
# Convert the RGB vector PDF to CMYK (macOS Generic CMYK profile) for printing.
# See print/COULEURS.md for the authoritative colour spec (Pantone / CMYK).
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dProcessColorModel=/DeviceCMYK \
  -sColorConversionStrategy=CMYK \
  -sOutputICCProfile="/System/Library/ColorSync/Profiles/Generic CMYK Profile.icc" \
  -sOutputFile=print/socamett-logo-cmyk.pdf print/socamett-logo.pdf >/dev/null 2>&1

echo "Done."
