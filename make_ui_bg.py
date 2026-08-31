import json
FRAME_COUNT = 113
FPS = 19
DURATION = 1 / FPS

data = {
    "namespace": "prova_bg",

    "prova_bg_path": {
        "type": "image",
        "fill": True,
        "texture": "('textures/ui/prova_bg/' + $prova_frame)"
    },

    "prova_bg_anim": {
        "anim_type": "offset",
        "easing": "linear",
        "duration": DURATION,
        "from": "$prova_bg_offset",
        "to": "$prova_bg_offset"
    },

    "prova_bg_panel": {
        "type": "panel",
        "size": ["100%", "100%"],
        "anchor_from": "top_left",
        "anchor_to": "top_left",
        "controls": [
            {
                "prova_bg_base@prova_bg.prova_bg_base": {}
            }
        ]
    },

    "prova_bg_base": {
        "type": "panel",
        "size": ["100%", "100%"],
        "controls": [
            {
                "prova_bg_stack": {
                    "type": "stack_panel",
                    "size": ["100%", "100%"],
                    "anchor_from": "top_left",
                    "anchor_to": "top_left",
                    "offset": "@prova_bg.prova_frame_0000",
                    "controls": []
                }
            }
        ]
    }
}

stack = data["prova_bg_base"]["controls"][0]["prova_bg_stack"]["controls"]

# Add the actual 143 textures.
for i in range(FRAME_COUNT):
    frame_number = i + 1

    stack.append({
        f"{i:04}@prova_bg.prova_bg_path": {
            "$prova_frame": f"frame_{frame_number:04d}"
        }
    })

# Create frame offsets.
for i in range(FRAME_COUNT):
    next_i = i + 1

    # Don't loop yet; frame 143 stops here.
    if next_i >= FRAME_COUNT:
        next_i = FRAME_COUNT - 1

    data[f"prova_frame_{i:04d}@prova_bg.prova_bg_anim"] = {
        "$prova_bg_offset": [0, f"-{i * 100}%"],
        "next": f"@prova_bg.prova_frame_{next_i:04d}"
    }

with open("prova_bg.json", "w") as f:
    json.dump(data, f, indent=2)

print("Generated prova_bg.json")
print(f"Frames: {FRAME_COUNT}")
print(f"FPS: {FPS}")
print(f"Duration/frame: {DURATION:.6f}s")
