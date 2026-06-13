#!/usr/bin/env python3
"""Build the horizontal SOCAMETT oval logo SVG.

Layout (oval, ring, text positions) is measured on photo-originale.png.
The central pictogram (two profiles + speed lines) is a Potrace trace of the
sharp emblem found in sources/img.png (same motif as the original photo).
"""
import math


P = {
    "W": 1065,
    "H": 800,
    "cx": 532.5,
    "cy": 393.5,
    "rx": 523.0,
    "ry": 387.5,
    "blue": "#0B3FA4",
    "ring_rx": 438.0,
    "ring_ry": 302.5,
    "ring_w": 4.5,
    # Baseline arc for the mottos. The band runs from the inner ring
    # (438 x 302.5) to the oval edge (523 x 387.5); its midline is 480.5 x 345.
    # Motto baselines. The band has a uniform 42.5px offset on BOTH axes
    # (ring 438/302.5, edge 523/387.5, midline 480.5/345). On the original the
    # mottos sit ~30% of the band width from the INNER ring (not centred), so the
    # glyph visual centre rides an ellipse offset inward to ring+27.5 = 465.5/330.
    # Baselines offset from that by the glyph visual half-height (uniform, both
    # axes): top grows outward (centre - 12), bottom grows inward (centre + 12).
    "text_rx_top": 453.5,
    "text_ry_top": 318.0,
    "text_rx_bottom": 477.5,
    "text_ry_bottom": 342.0,
    "motto_fs": 38,
    "motto_ls": 10,
    # Refreshed logo type: Open Sans Bold, stretched ~1.10x wide. Matched against
    # photo-originale.png by stretch-normalised RMSE over a corpus of classic
    # sans fonts; SOCAMETT lands at 742x94 vs the measured 740x94. Requires Open
    # Sans installed (see ~/Library/Fonts/OpenSans-700.ttf).
    "font_family": "Open Sans, sans-serif",
    "name_x": 536.5,
    "name_y": 520.0,
    "name_fs": 128,
    "name_scale_x": 1.10,
    # Emblem ink box measured on photo-originale.png: x 350-675, y 172-359.
    # Potrace trace ink box: 1076x571 at (163, 81) in a 1280x680 canvas.
    "emblem_x": 300.8,
    "emblem_y": 154.8,
    "emblem_scale": 0.302,
}


def point(angle, rx, ry, cx, cy):
    radians = math.radians(angle)
    return cx + rx * math.cos(radians), cy + ry * math.sin(radians)


def arc_path(start, end, rx, ry, cx, cy, sweep=1, large_override=None):
    x0, y0 = point(start, rx, ry, cx, cy)
    x1, y1 = point(end, rx, ry, cx, cy)
    delta = (end - start) % 360
    large = large_override if large_override is not None else 1 if delta > 180 else 0
    return f"M {x0:.1f} {y0:.1f} A {rx:.1f} {ry:.1f} 0 {large} {sweep} {x1:.1f} {y1:.1f}"


# Central pictogram: a Potrace 1.16 trace of the sharp emblem in the source
# artwork (two stylised profiles + speed lines), in Potrace's flipped 0.1 space.
EMBLEM_PATHS = """\
<path d="M3882 5974 c-12 -8 -29 -28 -37 -44 -37 -71 -42 -70 367 -89 108 -5
259 -16 335 -25 76 -8 219 -17 318 -21 99 -3 214 -10 255 -16 41 -5 175 -13
297 -19 122 -5 242 -14 267 -20 24 -5 158 -14 298 -20 139 -6 312 -17 383 -24
72 -8 206 -17 299 -20 93 -3 228 -13 300 -21 72 -7 228 -19 346 -25 118 -6
247 -15 285 -20 39 -5 115 -9 170 -10 55 0 152 -5 215 -11 63 -7 140 -13 170
-14 149 -8 309 -25 345 -38 22 -8 64 -17 94 -21 30 -4 64 -12 75 -18 12 -6 37
-15 56 -19 53 -12 130 -38 175 -60 22 -10 43 -19 46 -19 15 0 179 -96 229
-134 82 -62 230 -217 230 -240 0 -5 9 -20 21 -34 28 -36 139 -240 139 -255 0
-7 7 -22 15 -34 24 -35 105 -275 105 -314 0 -11 7 -33 15 -48 8 -16 19 -56 24
-89 5 -34 14 -69 19 -79 5 -10 13 -38 17 -63 4 -25 16 -76 26 -115 10 -38 19
-83 19 -100 0 -16 9 -59 20 -93 11 -35 20 -81 20 -101 0 -21 6 -59 14 -84 8
-25 19 -86 25 -134 7 -48 16 -101 21 -118 4 -16 11 -55 15 -85 3 -30 15 -106
26 -168 29 -165 16 -192 -93 -192 -63 0 -73 -3 -111 -32 -136 -108 -162 -205
-176 -663 -8 -254 -9 -261 -35 -312 -15 -31 -38 -59 -54 -67 -37 -19 -222 -25
-897 -26 l-520 -2 -54 -61 c-30 -34 -79 -90 -110 -124 -31 -34 -81 -92 -111
-129 -49 -60 -108 -128 -150 -173 -8 -9 -46 -54 -84 -99 -38 -45 -72 -82 -75
-82 -4 0 -13 -11 -21 -24 -8 -14 -38 -49 -66 -78 -28 -29 -73 -80 -99 -113
-53 -65 -214 -247 -227 -256 -4 -3 -18 -19 -31 -36 -20 -27 -52 -64 -187 -218
-113 -129 -113 -128 -84 -139 9 -3 118 -6 243 -6 l228 0 49 56 c49 56 61 69
240 269 55 60 113 125 129 145 17 19 57 64 91 100 33 36 73 81 88 100 15 19
61 71 102 115 41 44 131 144 200 223 70 79 137 148 151 153 14 5 269 9 597 9
560 0 573 0 637 22 91 30 132 59 234 162 91 92 103 113 126 216 6 25 19 83 29
130 11 51 21 149 25 245 11 264 19 278 166 288 95 6 138 24 195 83 71 73 91
180 60 326 -8 42 -18 108 -21 145 -4 37 -13 104 -22 147 -8 43 -19 111 -23
150 -17 139 -41 303 -63 419 -20 109 -20 118 -5 134 15 15 49 16 325 14 233
-1 334 2 416 13 126 18 156 35 187 109 25 58 23 105 -8 178 -16 36 -28 49 -68
67 -48 22 -58 23 -508 30 -393 6 -460 9 -467 22 -4 8 -20 60 -34 115 -14 55
-32 116 -39 135 -26 70 -48 136 -56 165 -6 26 -24 66 -52 115 -10 17 -24 49
-32 70 -8 19 -53 95 -90 151 -16 24 -49 73 -72 109 -46 70 -129 168 -225 265
-98 101 -80 119 121 117 74 -1 167 -6 207 -12 40 -5 174 -14 299 -20 294 -13
454 -41 624 -108 222 -89 455 -282 595 -494 38 -57 77 -115 87 -130 10 -15 18
-34 18 -41 0 -8 6 -20 14 -26 16 -14 106 -193 106 -212 0 -8 9 -27 20 -44 11
-16 20 -37 20 -45 0 -8 7 -28 16 -45 9 -16 20 -46 25 -65 4 -19 20 -66 34
-105 15 -38 33 -90 40 -115 7 -25 20 -58 28 -75 9 -16 26 -64 37 -105 12 -41
26 -88 32 -105 6 -16 16 -48 22 -70 6 -22 19 -60 27 -85 20 -56 51 -160 79
-265 12 -44 28 -101 36 -126 18 -59 18 -71 -2 -112 -27 -56 -64 -67 -222 -67
l-138 0 -41 -42 c-23 -24 -55 -65 -70 -93 l-28 -50 -6 -425 c-8 -515 -17 -627
-56 -683 -40 -58 -83 -88 -160 -113 -66 -22 -86 -23 -576 -30 l-507 -7 -46
-51 c-67 -75 -227 -265 -244 -290 -13 -19 -101 -122 -150 -176 -8 -9 -32 -37
-52 -61 -21 -24 -79 -93 -130 -153 -51 -61 -124 -148 -162 -195 -38 -47 -88
-107 -110 -132 -23 -25 -72 -83 -111 -129 -38 -46 -92 -108 -118 -136 -27 -29
-46 -58 -42 -63 4 -7 91 -11 255 -11 l248 0 29 36 c15 20 60 70 98 112 39 43
116 126 170 186 55 60 123 133 150 162 28 29 55 59 60 66 17 23 185 210 244
271 92 96 145 154 171 187 46 57 61 59 547 60 l441 0 54 27 c125 64 220 165
264 280 23 63 32 119 49 328 8 96 23 689 18 702 -8 20 23 60 59 79 21 11 73
20 143 24 226 16 322 66 364 192 37 109 26 209 -59 528 -6 25 -18 70 -25 100
-13 51 -30 105 -61 190 -7 19 -19 55 -27 80 -8 25 -20 61 -27 80 -6 19 -16 49
-22 65 -5 17 -21 59 -35 95 -13 36 -28 79 -34 97 -5 18 -16 45 -24 60 -8 15
-15 35 -15 43 0 8 -9 32 -20 53 -11 20 -20 43 -20 49 -1 7 -9 31 -20 53 -11
22 -19 47 -20 55 0 9 -7 25 -15 37 -8 12 -28 56 -44 100 -16 43 -36 92 -44
108 -8 17 -21 46 -30 65 -8 19 -36 79 -61 133 -25 53 -46 102 -46 109 0 6 -15
34 -34 62 -18 28 -41 67 -50 86 -67 146 -262 353 -429 455 -172 106 -210 122
-372 159 -144 33 -330 64 -430 71 -44 3 -96 10 -115 16 -25 8 -842 14 -2927
20 -1941 5 -2917 11 -2968 18 -42 6 -170 11 -283 11 -172 0 -211 -3 -230 -16z"/>
<path d="M3269 5199 c-24 -21 -49 -61 -49 -80 0 -20 108 -39 223 -39 59 0 161
-9 357 -29 8 -1 117 -6 241 -11 125 -5 286 -16 359 -25 72 -8 175 -15 228 -15
121 0 402 -17 502 -30 41 -5 165 -12 275 -15 110 -3 216 -9 235 -15 19 -6 69
-11 110 -11 115 0 499 -17 650 -29 74 -6 241 -14 370 -20 196 -7 310 -14 475
-29 22 -2 346 -14 670 -26 191 -6 201 -6 232 14 52 33 86 96 91 166 3 54 1 64
-27 101 -17 22 -49 54 -71 69 l-40 28 -2408 5 c-2014 3 -2410 2 -2423 -9z"/>
<path d="M2745 4343 c-47 -53 -67 -85 -59 -93 8 -7 127 -19 369 -37 33 -2 168
-8 300 -13 132 -5 287 -13 345 -18 58 -6 119 -11 135 -11 344 -9 644 -22 695
-30 36 -6 245 -15 465 -21 220 -6 436 -15 480 -21 44 -5 235 -14 425 -19 190
-5 388 -12 440 -16 52 -3 120 -7 150 -9 30 -2 201 -9 380 -15 179 -6 393 -15
475 -20 83 -5 305 -14 495 -19 190 -6 386 -15 435 -21 50 -6 269 -14 487 -17
l398 -6 38 27 c119 82 105 247 -27 327 l-59 36 -2043 6 c-1123 4 -2552 7
-3176 7 -1067 0 -1134 -1 -1148 -17z"/>
<path d="M2196 3454 c-10 -14 -15 -31 -13 -37 5 -15 282 -43 547 -56 102 -6
214 -13 250 -17 107 -12 118 -13 320 -23 107 -6 260 -17 340 -25 80 -8 222
-17 315 -20 94 -3 208 -10 255 -16 47 -6 185 -15 307 -20 121 -5 290 -16 375
-24 84 -8 245 -17 357 -21 113 -3 225 -10 250 -16 24 -5 155 -14 290 -19 135
-4 336 -15 446 -24 110 -9 322 -21 470 -27 149 -6 292 -15 319 -20 27 -5 86
-9 131 -9 71 0 89 4 136 29 46 25 57 36 76 82 26 64 28 107 7 157 -20 49 -60
89 -111 113 -41 19 -98 19 -2546 19 l-2505 0 -16 -26z"/>
<path d="M1647 2632 c-43 -47 2 -72 133 -72 41 0 118 -5 170 -11 137 -15 174
-18 375 -29 99 -5 227 -14 285 -20 58 -6 188 -15 290 -20 102 -5 235 -14 295
-20 61 -6 207 -15 325 -20 118 -6 247 -15 285 -20 39 -6 180 -15 315 -20 135
-6 259 -15 277 -21 17 -5 58 -10 90 -10 111 0 498 -19 583 -29 47 -5 193 -14
325 -20 132 -6 311 -17 398 -25 86 -8 202 -15 257 -15 55 0 179 -5 275 -11
227 -15 254 -10 310 47 39 42 43 50 48 112 9 108 -35 178 -132 211 -25 8 -673
11 -2461 11 -2338 0 -2428 -1 -2443 -18z"/>
"""


def load_emblem():
    """Place the traced emblem, scaled and positioned into the logo."""
    tx, ty, s = P["emblem_x"], P["emblem_y"], P["emblem_scale"]
    return (
        f'<g transform="translate({tx} {ty}) scale({s})" fill="#ffffff" stroke="none">\n'
        '<g transform="translate(0,680) scale(0.1,-0.1)">\n'
        f"{EMBLEM_PATHS}</g>\n</g>"
    )



def build_svg():
    p = P
    top_arc = arc_path(
        204, 336, p["text_rx_top"], p["text_ry_top"], p["cx"], p["cy"], sweep=1
    )
    bottom_arc = arc_path(
        154,
        26,
        p["text_rx_bottom"],
        p["text_ry_bottom"],
        p["cx"],
        p["cy"],
        sweep=0,
        large_override=0,
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {p['W']} {p['H']}" width="{p['W']}" height="{p['H']}" role="img"
     aria-label="Logo SOCAMETT - Le Garant Financier des Métiers de l'Emploi">
  <title>SOCAMETT</title>
  <defs>
    <path id="topMotto" d="{top_arc}" fill="none"/>
    <path id="bottomMotto" d="{bottom_arc}" fill="none"/>
  </defs>

  <!-- Transparent background: the master SVG carries only the logo. White/JPEG
       backgrounds are added at raster export time. -->
  <ellipse cx="{p['cx']}" cy="{p['cy']}" rx="{p['rx']}" ry="{p['ry']}" fill="{p['blue']}"/>
  <ellipse cx="{p['cx']}" cy="{p['cy']}" rx="{p['ring_rx']}" ry="{p['ring_ry']}"
           fill="none" stroke="#ffffff" stroke-width="{p['ring_w']}"/>

  <text font-family="{p['font_family']}" font-weight="700"
        font-size="{p['motto_fs']}" letter-spacing="{p['motto_ls']}" fill="#ffffff"
        text-anchor="middle">
    <textPath xlink:href="#topMotto" href="#topMotto" startOffset="50%">Le Garant Financier</textPath>
  </text>

  <text font-family="{p['font_family']}" font-weight="700"
        font-size="{p['motto_fs']}" letter-spacing="{p['motto_ls']}" fill="#ffffff"
        text-anchor="middle">
    <textPath xlink:href="#bottomMotto" href="#bottomMotto" startOffset="50%">des Métiers de l'Emploi</textPath>
  </text>

  {load_emblem()}

  <text transform="matrix({p['name_scale_x']} 0 0 1 {p['name_x']} {p['name_y']})"
        font-family="{p['font_family']}" font-weight="700"
        font-size="{p['name_fs']}" fill="#ffffff" text-anchor="middle">SOCAMETT</text>
</svg>
"""


if __name__ == "__main__":
    with open("socamett-logo.svg", "w", encoding="utf-8") as f:
        f.write(build_svg())
    print("built socamett-logo.svg")
