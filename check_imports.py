modules = ['imutils','numpy','playsound','dlib','cv2']
import importlib
for m in modules:
    try:
        mod = importlib.import_module(m)
        ver = getattr(mod, '__version__', None)
        print(f"{m}: OK, version={ver}")
    except Exception as e:
        print(f"{m}: ERROR: {e.__class__.__name__}: {e}")
