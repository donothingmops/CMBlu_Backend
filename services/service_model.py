# Nodes
# Members
# Plates
# Supports




""" from rhino3dm import * """
import rhino3dm as rhino
import requests  # pip install requests

req = requests.get("https://files.mcneel.com/TEST/Rhino Logo.3dm")
model = rhino.File3dm.FromByteArray(req.content)
for obj in model.Objects:
    geometry = obj.Geometry
    bbox = geometry.GetBoundingBox()
    print("{}, {}".format(bbox.Min, bbox.Max))


pt = rhino.Point3d(0, 1, 1)
print(pt)
pt1 = rhino.Point3d(-1, -1, 1)
line = rhino.Line(pt, pt1)

print(line.PointAt(0.5))