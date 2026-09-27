# Framing illustration: rain and wet-ground correction

Date: 2026-09-27

Method: built-in image_gen image editing, followed by the existing SVG/Sharp assembly in `scripts/build_framing_illustration.cjs`. Illustrative artwork; no empirical data are represented.

Final asset: `figures/framing-three-windows.png` (currently Figure 12.1).

Original inputs are retained. The new `master-scene-wet-ground.png` contributes only ground below y=850 in the right-hand scene, with a left-edge blend. The new `imagined-surroundings-rain-aligned.png` contributes only the rightmost imagined panel. Existing water trajectories, left and middle examples, frame geometry, and opacity 0.72 are preserved by the assembly. All three upper/lower framed pairs are checked for exact pixel equality in `pixel-consistency.json`.

Verification: three 304-by-304 upper/lower framed pairs are pixel-identical. The complete left and middle area (x=0..999) is pixel-identical to the previous committed figure. The HTML and EPUB embed the exact final PNG. The final illustration was inspected at native size and in HTML at desktop and 390-pixel width; the actual EPUB XHTML was also inspected in a browser at narrow and desktop widths. Source and EPUB release checks passed.

## Wet-ground edit prompt

Use case: precise-object-edit. Edit target: the supplied 1536 by 1024 educational illustration. Change only the ground under the falling sprinkler water in the LOWER RIGHT part of the wide bottom scene. The sidewalk slabs, curb, and foreground asphalt from roughly x=1180 to the right image edge must be visibly and continuously wet, with a convincing blue-gray reflective sheen, shallow puddles, small water ripples and glints, matching a thoroughly rain-soaked street. In particular make the full ground area at x=1232..1512, y=850..930 look wet rather than dry/shadowed. Keep the curb and sidewalk geometry visible. Feather the wet area naturally into the adjacent dry ground at its left. Preserve the sprinkler, hose, vegetation, tree, building, water trajectories and every other part of the illustration. Water still comes only from the sprinkler in the sunny scene, not from general rainfall. Do not move any objects or change viewpoint, crop, composition, scene boundaries, color style or dimensions. No text, frames, labels or added objects. Return the complete edited image at the same 1536x1024 composition.

## Rain-direction edit prompt

Use case: precise-object-edit. Edit target: Image 1, the three side-by-side imagined-surroundings panels (a dry urban street, a green park, and a rainy urban street). Supporting reference: Image 2, the assembled book figure, which shows the desired water-streak direction inside the top-right wooden frame. In Image 1 change ONLY the direction of ALL falling rain streaks in the rightmost rainy street panel. Each streak must slant from its UPPER LEFT endpoint to its LOWER RIGHT endpoint, like a backslash, with its lower endpoint about one third of its vertical length to the right of its upper endpoint. Rain falling DOWN AND TO THE RIGHT, matching the dominant streaks within the wooden frame in Image 2. The existing Image 1 rain slopes the opposite way: remove those old down-left streaks and replace them, leaving no mixed opposing diagonals. Preserve the gray sky, existing buildings, trees, wet reflective road, road markings, lighting, panel boundaries, composition, style, colors, dimensions and both other panels. Do not mirror or move the city; reverse only the rain-stroke orientation. No labels, text, frames or new objects. Return only the complete edited three-panel Image 1, with its same 3:1 aspect ratio.
