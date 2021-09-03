from Neon.Neon import *

def onFrame(window, timeDelta):
    print("timeDelta : " + str(timeDelta))

def main():
    neon = Neon()
    window = neon.CreateWindow(400, 300)
    window.SetOnFrameEventHandler(onFrame)

    scene = NScene()
    sceneLayer = NSceneLayer()
    entity = NEntity()
    camera = NCamera()

    geometry = NGeometry()
    material = NMaterial()
    shader = NShader()
    texture = NTexture()

    window.Run()

if __name__ == "__main__":
    main()
