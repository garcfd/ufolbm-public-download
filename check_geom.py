import struct

with open("car.stl", "rb") as f:
    header = f.read(80)
    ntri = struct.unpack("<I", f.read(4))[0]
    print(f"Number of triangles: {ntri}")

    min_x = min_y = min_z = float("inf")
    max_x = max_y = max_z = float("-inf")

    for i in range(ntri):
        normal = struct.unpack("<3f", f.read(12))
        v1 = struct.unpack("<3f", f.read(12))
        v2 = struct.unpack("<3f", f.read(12))
        v3 = struct.unpack("<3f", f.read(12))
        attr = struct.unpack("<H", f.read(2))

        for v in [v1, v2, v3]:
            min_x = min(min_x, v[0])
            min_y = min(min_y, v[1])
            min_z = min(min_z, v[2])
            max_x = max(max_x, v[0])
            max_y = max(max_y, v[1])
            max_z = max(max_z, v[2])

    print(f"Bounding box:")
    print(f"  x: [{min_x:.4f}, {max_x:.4f}]  size: {max_x-min_x:.4f}")
    print(f"  y: [{min_y:.4f}, {max_y:.4f}]  size: {max_y-min_y:.4f}")
    print(f"  z: [{min_z:.4f}, {max_z:.4f}]  size: {max_z-min_z:.4f}")
    print(f"  center: ({(min_x+max_x)/2:.4f}, {(min_y+max_y)/2:.4f}, {(min_z+max_z)/2:.4f})")
